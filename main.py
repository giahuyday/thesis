from methods.water_mark import makeWatermark, makepdf
import sys

water_mark_infor = sys.argv[1]
pdf_file = sys.argv[2]

print(water_mark_infor)
print(pdf_file)

makeWatermark(water_mark_infor)
makepdf(pdf_file)
