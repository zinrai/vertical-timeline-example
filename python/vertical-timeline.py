#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os
import yaml
import textwrap
import argparse

def load_timeline_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def calculate_image_size(data, event_font, max_width=800, min_width=400):
    events = data['events']
    max_desc_width = 0
    max_year_width = 0
    total_height = 60  # Initial margins

    for event in events:
        year_width = event_font.getbbox(str(event['year']))[2]
        max_year_width = max(max_year_width, year_width)
        desc_width = sum([event_font.getbbox(char)[2] for char in event['description']])
        max_desc_width = max(max_desc_width, desc_width)

        # Calculate wrapped text height
        wrapped_text = textwrap.wrap(event['description'], width=30)  # Adjust width as needed
        total_height += len(wrapped_text) * (event_font.getbbox('Ay')[3] + 5) + 40  # 40 for spacing between events

    width = min(max(min_width, max_desc_width + max_year_width + 150), max_width)
    height = total_height

    return width, height, max_year_width

def create_vertical_timeline(data, output_filename):
    font_path = '/usr/share/fonts/truetype/fonts-japanese-mincho.ttf'  # Debian GNU/Linux

    if not os.path.exists(font_path):
        print(f"警告: {font_path} が見つかりません。デフォルトフォントを使用します。")
        event_font = ImageFont.load_default()
    else:
        event_font = ImageFont.truetype(font_path, 24)

    width, height, max_year_width = calculate_image_size(data, event_font)
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    line_x = max_year_width + 50
    draw.line([(line_x, 30), (line_x, height-30)], fill='black', width=2)

    y = 30
    for event in data['events']:
        # Draw year
        year_text = str(event['year'])
        year_bbox = event_font.getbbox(year_text)
        year_width = year_bbox[2] - year_bbox[0]
        draw.text((line_x - year_width - 20, y), year_text, fill='black', font=event_font)

        # Wrap and draw event description
        wrapped_text = textwrap.wrap(event['description'], width=30)  # Adjust width as needed
        for line in wrapped_text:
            line_width = sum([event_font.getbbox(char)[2] for char in line])
            x = line_x + 30
            for char in line:
                char_bbox = event_font.getbbox(char)
                char_width, char_height = char_bbox[2] - char_bbox[0], char_bbox[3] - char_bbox[1]
                draw.text((x, y), char, fill='black', font=event_font)
                x += char_width + 5
            y += char_height + 5

        # Draw horizontal line
        draw.line([(line_x-10, y+10), (line_x+10, y+10)], fill='black', width=2)
        y += 40  # Space between events

    img.save(output_filename)
    print(f"画像が '{output_filename}' として保存されました。サイズ: {width}x{height}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a vertical timeline from YAML data.')
    parser.add_argument('yaml_file', help='Path to the YAML file containing timeline data')
    args = parser.parse_args()

    timeline_data = load_timeline_data(args.yaml_file)

    # Remove extensions from YAML filenames and generate PNG filenames
    output_filename = os.path.splitext(os.path.basename(args.yaml_file))[0] + '.png'

    create_vertical_timeline(timeline_data, output_filename)
