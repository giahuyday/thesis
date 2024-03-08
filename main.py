from methods.water_mark import makeWatermark, makepdf, water_mark_use_img
import sys

water_mark_infor = sys.argv[1]
pdf_file = sys.argv[2]

print(water_mark_infor)
print(pdf_file)

makeWatermark(water_mark_infor)
water_mark_use_img('./methods/bg.jpg', 'new.pdf')
makepdf(pdf_file, '1231312312312')
