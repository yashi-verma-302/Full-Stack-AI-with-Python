masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamon_ratio = 2,1
print(f"Ratio is G:{ginger_ratio} and C:{cardamon_ratio}")
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"Ratio is G:{ginger_ratio} and C:{cardamon_ratio}")

#membership testing

print(f"Is ginger in masala_spices ? {'ginger' in masala_spices}")
