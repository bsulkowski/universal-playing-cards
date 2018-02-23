from math import *
from functools import reduce

colors = ['black', 'white', 'red', 'green', 'blue', 'yellow']
shapes = ['circle', 'square', 'triangle', 'cross', 'star', 'clover']
counts = range(1, 7)

card_width = 57
card_height = 89

card_area = card_width * card_height
shape_area = card_area / 6

label_width = 10
label_height = label_width * 2

scale_factor = 0.878

def merge(list, separator):
    return reduce(lambda x, y: x + separator + y, list)

def coords(range, angle):
    return f"{range * cos(2 * pi * angle) : >7.3f}, {range * sin(-2 * pi * angle) : >7.3f}"

color_rgb = {
    'black':    '#222',
    'white':    '#fff',
    'red':      '#f33',
    'green':    '#0c0',
    'blue':     '#36f',
    'yellow':   '#ff0'
}

s = shape_area

circle_r = sqrt(s / pi)

square_a = sqrt(s)
square_r = square_a / sqrt(2)

triangle_a = sqrt(s / (sqrt(3) / 4))
triangle_r = triangle_a / sqrt(3)

cross_a = sqrt(s / 5)
cross_r = cross_a / sqrt(2)

star_a = 2 * sqrt(s / 5 / (1 / tan(pi * 0.2) - 1 / tan(pi * 0.3)))
star_r2 = (star_a / 2) / sin(pi * 0.2)
star_r1 = s / 5 / (star_a / 2)

clover_r = sqrt(s / (2 * pi + 6 * sqrt(3) / 4))
   
shape_def = {
    'circle': f'<circle cx="0" cy="0" r="{circle_r :.3f}"/>',
    'square': '''<polygon points="
                ''' + merge([coords(square_r, (i + 0.5) / 4) for i in range(4)], '''
                ''') + '''
            "/>''',
    'triangle': '''<polygon points="
                ''' + merge([coords(triangle_r, i / 3 + 0.25) for i in range(3)], '''
                ''') + '''
            "/>''',
    'cross': '''<polygon points="
                ''' + merge([
                    f'{cross_r * cos(pi * (a + 0.5) / 2) * (3 if (a % 2) * 2 == b else 1) : 7.3f}, '
                    f'{cross_r * sin(-pi * (a + 0.5) / 2) * (3 if (a % 2) * 2 == 2 - b else 1) : 7.3f}'
                    for a in range(4) for b in range(3)], '''
                ''') + '''
            "/>''',
    'star': '''<polygon points="
                ''' + merge([coords(star_r2 if i % 2 == 0 else star_r1, i / 10 + 0.25) for i in range(10)], '''
                ''') + '''
            "/>''',
    'clover': f'''<path d="
                M {coords(clover_r, 0 - 0.25)}
                ''' + merge([f"A {clover_r : 7.3f}, {clover_r : 7.3f} 0 1 0 " + coords(clover_r, (i + 1) / 3 - 0.25) for i in range(3)], '''
                ''') + '''
                z
            "/>'''
}
        
spacing = circle_r * 3
        
layout_grid = [
    [],
    [(0, 0)],
    [(0, y / 2) for y in [-1, 1]],
    [(0, y) for y in [-1, 0, 1]],
    [(x / 2, y / 2) for x in [-1, 1] for y in [-1, 1]],
    [(0, 0)] + [(x * cos(pi / 3), y * sin(pi / 3)) for x in [-1, 1] for y in [-1, 1]],
    [(x / 2, y) for x in [-1, 1] for y in [-1, 0, 1]]
]
            
for color in colors:
    for shape in shapes:
        for count in counts:
            with open(f'deck216/{color}_{shape}_{count}.svg', 'w') as f:
                f.write(f'''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="{card_width}mm" height="{card_height}mm" viewBox="{-card_width / 2 :.1f} {-card_height / 2 :.1f} {card_width} {card_height}">
    <defs>
        <g id="shape" transform="scale({scale_factor :.3f})">
            {shape_def[shape]}
        </g>
    </defs>
    <g fill="{color_rgb[color]}" stroke="black" stroke-width="1">
        <g id="labels">
            <g id="label" transform="translate({-(card_width - label_width) / 2 :.1f}, {-(card_height - label_height) / 2 :.1f}) scale({1 / 6 :.3f})">
                <text x="0" y="0" font-size="{6 * label_width}" text-anchor="middle" font-family="arial">{count}</text>
                <use xlink:href="#shape" transform="translate(0, {3 * label_width})"/>
            </g>
            <use xlink:href="#label" transform="translate({card_width - label_width :.1f})"/>
        </g>
        <use xlink:href="#labels" transform="rotate(180)"/>
        <g id="layout" transform="scale({scale_factor * sqrt(1 / count) :.3f})">
            ''' + merge([
                f'<use xlink:href="#shape" transform="translate({dx * spacing :.1f}, {dy * spacing :.1f})"/>'
                for (dx, dy) in layout_grid[count]
            ], '''
            ''') + '''
        </g>
    </g>
</svg>''')
