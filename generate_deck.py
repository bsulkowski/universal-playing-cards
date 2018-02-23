from math import *
from functools import reduce

colors = ['black', 'white', 'red', 'green', 'blue', 'yellow']
shapes = ['circle', 'square', 'triangle', 'cross', 'star', 'clover']
counts = range(1, 7)

rgb = {
    'black':    '#222',
    'white':    '#fff',
    'red':      '#f33',
    'green':    '#0c0',
    'blue':     '#36f',
    'yellow':   '#ff0'
}

card_width = 57
card_height = 89

card_area = card_width * card_height
shape_area = card_area / 6

label_width = 10
label_height = label_width * 2

scale_factor = 0.878

spacing = 16.9 * 2 * 1.5

def merge(list, separator):
	return reduce(lambda x, y: x + separator + y, list)
    
def shape_svg(shape):
    if shape == 'circle': 
        return '''
        <circle id="circle" cx="0" cy="0" r="16.9"/>
        '''
    elif shape == 'square':
        return '''
        <rect id="square" x="-15" y="-15" height="30" width="30"/>
        '''
    elif shape == 'triangle':
        return '''
        <g id="triangle" transform="scale(26.3)" stroke-width="0.038">
            <polygon points="
                 -0.866,0.5  0.866,0.5  0,-1
            "/>
        </g>
        '''
    elif shape == 'cross':
        return '''
        <g id="cross" transform="scale(6.71)" stroke-width="0.14">
            <polygon points="
                 3, 1  1, 1  1, 3
                -1, 3 -1, 1 -3, 1
                -3,-1 -1,-1 -1,-3
                 1,-3  1,-1  3,-1
            "/>
        </g>
        '''
    elif shape == 'star':
        return '''
        <g id="star" transform="scale(28.3)" stroke-width="0.035">
            <polygon points="
                 0    ,-1
                 0.226,-0.309
                 0.951,-0.309
                 0.363, 0.118
                 0.588, 0.809
                 0    , 0.382 
                -0.588, 0.809
                -0.363, 0.118
                -0.951,-0.309
                -0.226,-0.309
            "/>
        </g>
        '''
    elif shape == 'clover':
        return '''
        <g id="clover" transform="scale(10.1)" stroke-width="0.10">
            <path d="
                M 0,1
                A 1,1 0 1,1 -0.866,-0.5
                A 1,1 0 1,1  0.866,-0.5
                A 1,1 0 1,1  0    , 1  
                z
            "/>
        </g>
        '''

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
        {shape_svg(shape)}
        </g>
    </defs>
    <g fill="{rgb[color]}" stroke="black" stroke-width="1">
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
