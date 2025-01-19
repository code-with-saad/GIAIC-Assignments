# ================================== Simple Operator and Conditional Statements ==================================

kElectric = True
ups = False

if(kElectric):
    print("Electricity is there")
    print("UPS is off")
    ups = False
else:
    ups = True
    print("UPS is On")
    print("Electricity is not there")