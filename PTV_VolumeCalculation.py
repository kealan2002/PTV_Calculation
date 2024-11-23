# My program assumes the tumour is spherical to simplify the calculations. 
# all margins are isotropic, so sites such as oesophagus and lung are less suited here.
import math

def calculate_radius(volume):
    # calculate radius of sphere given its volume
    radius = ((3 * volume) / (4 * math.pi)) ** (1/3)
    return radius

def calculate_volume(radius):
    # calculate volume of sphere given its radius
    volume = (4/3) * math.pi * radius ** 3
    return volume

def main():
    # step 1: get GTV volume from user
    try:
        V_GTV = float(input("Enter the size of the GTV (in cm³): "))
        if V_GTV <= 0:
            print("GTV volume must be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a numerical value for the GTV volume.")
        return

    # step 2: get tumour site from user
    site = input("Enter the tumour site (breast, lung, prostate, cervical): ").strip().lower()

    # step 3: set GTV to CTV expansion margin based on the site
    expansion_margins = {
        'breast': 1.0,      # in cm
        'lung': 0.8,        # in cm 
        'prostate': 0.0,    # in cm
        'cervical': 1.0     # in cm
    }

    if site in expansion_margins:
        m_GTV_CTV = expansion_margins[site]
    else:
        print("Invalid tumour site entered.")
        return

    # step 4: calculate radius and volume for GTV and CTV
    r_GTV = calculate_radius(V_GTV)
    r_CTV = r_GTV + m_GTV_CTV
    V_CTV = calculate_volume(r_CTV)

    print(f"\nCalculated Results:")
    print(f"GTV Radius: {r_GTV:.2f} cm")
    print(f"CTV Radius: {r_CTV:.2f} cm")
    print(f"Total volume of the CTV: {V_CTV:.2f} cm³")

    # step 5: get PTV expansion margin from user
    try:
        m_PTV = float(input("\nEnter the PTV expansion margin (in cm): "))
        if m_PTV < 0:
            print("PTV expansion margin cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a numerical value for the PTV expansion margin.")
        return

    # step 6: calculate radius and volume for PTV
    r_PTV = r_CTV + m_PTV
    V_PTV = calculate_volume(r_PTV)

    print(f"PTV Radius: {r_PTV:.2f} cm")
    print(f"Total volume of the PTV: {V_PTV:.2f} cm³")

if __name__ == "__main__":
    main()
