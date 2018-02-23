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

for color in colors:
    for shape in shapes:
        for count in counts:
            with open('deck216/{}_{}_{}.svg'.format(color, shape, count), 'w') as f:
                f.write('''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="57mm" height="89mm" viewBox="-28.5 -44.5 57 89">
    <defs>
        <circle id="circle" cx="0" cy="0" r="16.9"/>
        <rect id="square" x="-15" y="-15" height="30" width="30"/>
        <g id="cross" transform="scale(6.71)" stroke-width="0.14">
            <polygon points="
                 3, 1  1, 1  1, 3
                -1, 3 -1, 1 -3, 1
                -3,-1 -1,-1 -1,-3
                 1,-3  1,-1  3,-1
            "/>
        </g>
        <g id="triangle" transform="scale(26.3)" stroke-width="0.038">
            <polygon points="
                 -0.866,0.5  0.866,0.5  0,-1
            "/>
        </g>
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
        <g id="clover" transform="scale(10.1)" stroke-width="0.10">
            <path d="
                M 0,1
                A 1,1 0 1,1 -0.866,-0.5
                A 1,1 0 1,1  0.866,-0.5
                A 1,1 0 1,1  0    , 1  
                z
            "/>
        </g>
        <use id="shape" xlink:href="#{shape}" transform="scale(0.878)"/>
        <g id="layout1">
            <use xlink:href="#shape"/>
        </g>
        <g id="layout2">
            <use xlink:href="#shape" transform="translate(0,-17.9) scale(0.707)"/>
            <use xlink:href="#shape" transform="translate(0, 17.9) scale(0.707)"/>
        </g>
        <g id="layout3">
            <use xlink:href="#shape" transform="translate(0,-29.2) scale(0.577)"/>
            <use xlink:href="#shape" transform="translate(0,  0  ) scale(0.577)"/>
            <use xlink:href="#shape" transform="translate(0, 29.2) scale(0.577)"/>
        </g>
        <g id="layout4">
            <use xlink:href="#shape" transform="translate(-12.7,-12.7) scale(0.5)"/>
            <use xlink:href="#shape" transform="translate(-12.7, 12.7) scale(0.5)"/>
            <use xlink:href="#shape" transform="translate( 12.7,-12.7) scale(0.5)"/>
            <use xlink:href="#shape" transform="translate( 12.7, 12.7) scale(0.5)"/>
        </g>
        <g id="layout5">
            <use xlink:href="#shape" transform="translate(-11.4,-19.7) scale(0.447)"/>
            <use xlink:href="#shape" transform="translate(-11.4, 19.7) scale(0.447)"/>
            <use xlink:href="#shape" transform="translate(  0  , 0   ) scale(0.447)"/>
            <use xlink:href="#shape" transform="translate( 11.4,-19.7) scale(0.447)"/>
            <use xlink:href="#shape" transform="translate( 11.4, 19.7) scale(0.447)"/>
        </g>
        <g id="layout6">
            <use xlink:href="#shape" transform="translate(-10.4,-20.8) scale(0.408)"/>
            <use xlink:href="#shape" transform="translate(-10.4,  0  ) scale(0.408)"/>
            <use xlink:href="#shape" transform="translate(-10.4, 20.8) scale(0.408)"/>
            <use xlink:href="#shape" transform="translate( 10.4,-20.8) scale(0.408)"/>
            <use xlink:href="#shape" transform="translate( 10.4,  0  ) scale(0.408)"/>
            <use xlink:href="#shape" transform="translate( 10.4, 20.8) scale(0.408)"/>
        </g>
    </defs>
    <g fill="{color}" stroke="black" stroke-width="1">
        <g id="labels">
            <g id="label" transform="translate(-23.5, -34.5) scale(0.167)">
                <text x="0" y="0" font-size="60" text-anchor="middle" font-family="arial">{count}</text>
                <use xlink:href="#shape" transform="translate(0, 30)"/>
            </g>
            <use xlink:href="#label" transform="translate(47)"/>
        </g>
        <use xlink:href="#labels" transform="rotate(180,0,0)"/>
        <use xlink:href="#layout{count}" transform="scale(0.878)"/>
    </g>
</svg>
'''.format(color = rgb[color], shape = shape, count = count)
                )