

from PIL import Image

def main():
    # 画像を開く
    img = Image.open('/Users/20_sic/oshite/app/static/images/oshiteFontIncludeKana/0x304a.png')

    # 切り抜きたい領域を指定（左上のx座標、左上のy座標、右下のx座標、右下のy座標）
    crop_area = (0, 0, 60, 60)

    # 画像を切り抜く
    cropped_img = img.crop(crop_area)

    # 切り抜いた画像を保存
    cropped_img.save("/Users/20_sic/oshite/tool/img_cut/out/0x304a.png")

## 
if __name__ == '__main__':
    main()