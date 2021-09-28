# a script to convert between temperature scales
# accepts temparature valure and a key specifying the original scale
# prints all the other scales

values = input("Provide a temperature for conversion and an original unit (C, K, F, Ra, Re - Celsius, Kelvin, Fahrenheit, Rankine, Reaumur respectively). Separate values by space. Example: '298.15 K'.    Input: ")


units = ['C', 'K', 'F', 'Ra', 'Re']
#dictionary containing instructions for conversion
conversions_dict = {
    'CK':  lambda temp: temp + 273.15,
    'CF':  lambda temp: temp * 1.8 + 32,
    'CRa': lambda temp: (temp + 273.15) * 1.8,
    'CRe': lambda temp: temp * 0.8,
    
    'KC':  lambda temp: temp - 273.15,
    'KF':  lambda temp: (temp - 273.15) * 1.8 + 32,
    'KRa': lambda temp: temp * 1.8,
    'KRe': lambda temp: (temp - 273.15) * 0.8,
    
    'FC':  lambda temp: (temp - 32) / 1.8,
    'FK':  lambda temp: ((temp - 32) / 1.8) + 273.15,
    'FRa': lambda temp: (((temp - 32) / 1.8) + 273.15) * 1.8,
    'FRe': lambda temp: ((temp - 32) / 1.8) * 0.8,
    
    'RaC':  lambda temp: (temp - 491.67) / 1.8,
    'RaK':  lambda temp: ((temp - 491.67) / 1.8) + 273.15,
    'RaF':  lambda temp: (temp - 491.67) + 32,
    'RaRe': lambda temp: ((temp - 491.67) / 1.8) * 0.8,
    
    'ReC':  lambda temp: temp * 1.25,
    'ReK':  lambda temp: (temp * 1.25) + 273.15,
    'ReF':  lambda temp: (temp * 1.25) * 1.8 + 32,
    'ReRa': lambda temp: (temp * 1.25 + 273.15) * 1.8,
}

temp = float(values.split(' ')[0])
original_unit = values.split(' ')[1]

for unit in units:
    if original_unit != unit:
        print("%.3f" % conversions_dict[original_unit+unit](temp), unit)
