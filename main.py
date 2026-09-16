"""Smart Quote Request Assistant.

This program collects the main details needed for a quote request,
checks that the information is valid, classifies the job,
and saves the request in a text file.
"""

from datetime import datetime


def get_required_text(prompt):
    """Ask the user for information and prevent an empty answer."""
    value = input(prompt).strip()

    while value == "":
        print("This field cannot be empty.")
        value = input(prompt).strip()

    return value


def get_text_only(prompt):
    """Ask the user for text and reject empty or numeric-only answers."""
    value = input(prompt).strip()

    while value == "" or value.isdigit():
        print("Please enter a valid text value.")
        value = input(prompt).strip()

    return value


# Display the application title
print("Smart Quote Request Assistant")

# Collect and validate customer information
customer_name = get_required_text("Enter the customer name: ")

email = input("Enter the customer email: ").strip()

while "@" not in email or "." not in email:
    print("Please enter a valid email address.")
    email = input("Enter the customer email: ").strip()

phone = input("Enter the customer phone number: ").strip()

while not phone.isdigit() or len(phone) < 8:
    print("Please enter a valid phone number using digits only.")
    phone = input("Enter the customer phone number: ").strip()

# Collect and validate job information
job_location = get_required_text("Enter the job location: ")

service_type = get_text_only("Enter the service type: ")

surface_type = get_text_only("Enter the surface type: ")

current_condition = get_text_only(
    "Describe the current condition of the surface: "
)

requested_finish = get_text_only(
    "Enter the requested finish: "
)

damage_present = input(
    "Are there scratches, stains, chips or other damage? (yes/no): "
).strip().lower()

while damage_present not in ["yes", "no"]:
    print("Please enter yes or no.")
    damage_present = input(
        "Are there scratches, stains, chips or other damage? (yes/no): "
    ).strip().lower()

photos_available = input(
    "Are photos available? (yes/no): "
).strip().lower()

while photos_available not in ["yes", "no"]:
    print("Please enter yes or no.")
    photos_available = input(
        "Are photos available? (yes/no): "
    ).strip().lower()

# Collect optional job notes
additional_notes = input("Enter any additional notes: ").strip()

if additional_notes == "":
    additional_notes = "No additional notes provided."

# Collect and assess the area
while True:
    try:
        area = float(input("Enter the area in square metres: "))

        if area > 0:
            break

        print("Area must be greater than zero.")

    except ValueError:
        print("Please enter a valid number.")

# Calculate an approximate price range
base_rate = 150
estimated_price = area * base_rate

if damage_present == "yes":
    estimated_price = estimated_price * 1.25

minimum_estimate = estimated_price * 0.90
maximum_estimate = estimated_price * 1.10

# Classify the job based on the information provided
job_complexity = "Low"
inspection_recommended = "No"

condition_lower = current_condition.lower()
finish_lower = requested_finish.lower()

if damage_present == "yes":
    job_complexity = "High"
    inspection_recommended = "Yes"

elif photos_available == "no":
    job_complexity = "Medium"
    inspection_recommended = "Yes"

elif (
    "poor" in condition_lower
    or "damaged" in condition_lower
    or "scratched" in condition_lower
    or "grinding" in finish_lower
):
    job_complexity = "High"
    inspection_recommended = "Yes"

elif (
    "polish" in finish_lower
    or "sealer" in finish_lower
    or "honed" in finish_lower
):
    job_complexity = "Medium"

# Generate a unique quote request reference number
quote_id = datetime.now().strftime("QR-%Y%m%d-%H%M%S")

# Display the completed quote request
print("\n--- Quote Request Summary ---")
print("Quote ID:", quote_id)
print("Customer name:", customer_name)
print("Email:", email)
print("Phone:", phone)
print("Job location:", job_location)
print("Service type:", service_type)
print("Surface type:", surface_type)
print("Current condition:", current_condition)
print("Requested finish:", requested_finish)
print("Damage present:", damage_present)
print("Photos available:", photos_available)
print("Area:", area, "m²")
print("Additional notes:", additional_notes)
print("Job complexity:", job_complexity)
print("Site inspection recommended:", inspection_recommended)
print(
    f"Approximate price range: "
    f"${minimum_estimate:,.2f} - ${maximum_estimate:,.2f}"
)

print("\nThis estimate is based on the information provided.")
print("The final quote may change after reviewing photos or inspecting the job.")

# Save the quote request without deleting previous records
with open("quote_requests.txt", "a", encoding="utf-8") as file:
    file.write("\n--- New Quote Request ---\n")
    file.write("Quote ID: " + quote_id + "\n")
    file.write("Date: " + str(datetime.now()) + "\n")
    file.write("Customer name: " + customer_name + "\n")
    file.write("Email: " + email + "\n")
    file.write("Phone: " + phone + "\n")
    file.write("Job location: " + job_location + "\n")
    file.write("Service type: " + service_type + "\n")
    file.write("Surface type: " + surface_type + "\n")
    file.write("Current condition: " + current_condition + "\n")
    file.write("Requested finish: " + requested_finish + "\n")
    file.write("Damage present: " + damage_present + "\n")
    file.write("Photos available: " + photos_available + "\n")
    file.write("Area: " + str(area) + " m²\n")
    file.write("Additional notes: " + additional_notes + "\n")
    file.write("Job complexity: " + job_complexity + "\n")
    file.write(
        "Site inspection recommended: "
        + inspection_recommended
        + "\n"
    )
    file.write(
        f"Approximate price range: "
        f"${minimum_estimate:,.2f} - ${maximum_estimate:,.2f}\n"
    )
    file.write("Status: Submitted for professional review.\n")

print("\nQuote request saved successfully.")