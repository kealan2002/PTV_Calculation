# PTV_Calculation
This Python program calculates the CLinical Target Volume (CTV) and Planning Target Volume (PTV) based on user inputs for the Gross Tumour Volume (GTV) and applies standard expansion margins as per the EViQ guidelines for different tumour sites. 

This helps us to understand the signifcant impact that CTV & PTV margins have on the total volume being irradiated. If a spherical tumour has a 1cm radius the GTV volume is 4.19cm-cubed. If one person uses 1.5cm isotropic expansion for CTV and another 1.5cm isotropic expansion for the PTV, the PTV radius will then be 4cm, giving a total volume of 268cm cubed. If another person uses the margins of 1cm and 1cm, the radius of 3cm will produce a PTV volume of just 113.1cm cubed (less than half of the 4cm radius).
It illustrates the importance of reducing margins if possible. 

Features: 
Calculates GTV radius from the user provided volume, assuming a spherical shape. 
Applies site-specific GTV to CTV expansion margins automatically based on EviQ guidelines.
Allows the user to input thier own PTV expansion margin.
Calculates and displays to the user  the radii and volumes for GTV, CTV and PTV.
Handles user input errors with appropriate error messages.



