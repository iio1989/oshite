from PIL import Image

def main():
    # 画像を開く
    img = Image.open('/Users/20_sic/oshite/app/static/images/oshiteFontIncludeKana/0x304a.png')

    # 画像をRGBAモードに変換
    img = img.convert("RGBA")

    # 背景色を定義（この値は例です。実際の背景色に置き換えてください）
    background_color = (255, 255, 255)  # 白色

    # 画像の各ピクセルを調べ、背景色と一致するピクセルのアルファ値を0に設定
    data = []
    for color in img.getdata():
        if color[:3] == background_color:
            data.append((255, 255, 255, 0))
        else:
            data.append(color)

    # 新しい画像を作成
    img_with_transparent_background = Image.new('RGBA', img.size)
    img_with_transparent_background.putdata(data)

    # 画像を保存
    img_with_transparent_background.save('/Users/20_sic/oshite/tool/clearing/out/part_0_transparent.png')

## 
if __name__ == '__main__':
    main()