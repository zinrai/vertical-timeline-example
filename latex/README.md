# LaTeX Timeline Generator

This LaTeX project provides a template for generating a vertical timeline using the TikZ package.

## Features

- Easily customizable vertical timeline
- Display of year-event pairs
- Japanese language support (using IPAPMincho font)

## Requirements

- LaTeX environment (e.g., TeXLive)
- XeLaTeX (for Japanese support)
- TikZ package
- geometry package
- xeCJK package
- IPAPMincho font

## Installation

example for Debia GNU/Linux.

```bash
# apt install texlive-pictures texlive-xetex
```

## Usage

1. Use the `\timelineentry` command to add entries to the timeline:
   ```latex
   \timelineentry{position}{year}{event description}
   ```
   - `position`: Vertical position on the timeline (numeric value)
   - `year`: Year (or date) to display
   - `event description`: Details of the event (can be multiple lines)

2. Use the `\drawtimeline` command to draw the entire timeline:
   ```latex
   \drawtimeline{height}
   ```
   - `height`: Overall height of the timeline

3. Compile using XeLaTeX:
   ```
   xelatex your_file_name.tex
   ```

## Customization

- To change font sizes or styles, edit the `\documentclass` options or the style definitions within the `tikzpicture` environment.
- To adjust page margins, modify the options of the `geometry` package.
- To change the Japanese font, edit the `\setCJKmainfont` command.

## Notes

- Use XeLaTeX to compile for proper display of Japanese text.
- Ensure that the IPAPMincho font is installed on your system.

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
