# LaTeX Timeline Generator

This LaTeX project provides a template for generating a vertical timeline using the TikZ package.

## Features

- Easily customizable vertical timeline
- Display of year-event pairs

## Requirements

- LaTeX environment (e.g., TeXLive)
- TikZ package

## Installation

example for Debia GNU/Linux.

```bash
# apt install texlive-pictures
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

3. Compile using upLaTeX:
   ```
   uplatex your_file_name.tex
   ```

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
