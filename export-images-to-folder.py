import os

from PIL import Image


def save_images_as_png(source_folder, destination_folder):
    # 指定されたフォルダーが存在しない場合は作成
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 既存のファイルの最大の番号を取得
    existing_files = [f for f in os.listdir(
        destination_folder) if f.endswith('.png')]
    if existing_files:
        existing_numbers = [int(os.path.splitext(f)[0])
                            for f in existing_files]
        next_number = max(existing_numbers) + 1
    else:
        next_number = 1

    # ソースフォルダー内の画像を取得
    source_files = [f for f in os.listdir(source_folder) if f.lower().endswith(
        ('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    for file in source_files:
        # 画像を開く
        img = Image.open(os.path.join(source_folder, file))

        # 新しいファイル名を決定
        new_file_name = f"{next_number}.png"
        next_number += 1

        # 画像をPNG形式で保存
        img.save(os.path.join(destination_folder, new_file_name), 'PNG')

        print(f"Saved {file} as {new_file_name}")


# 使用例
source_folder = r''
destination_folder = r''

save_images_as_png(source_folder, destination_folder)
