@namespace
class SpriteKind:
    Object = SpriteKind.create()
# Game over when you reach the end of the
# neighborhood

def on_overlap_tile(sprite, location):
    game.over(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile3, on_overlap_tile)

def on_up_pressed():
    car.set_image(img("""
        . . . . . . . . . . . . . . . .
                . . . . . . 3 3 3 3 3 3 . . . .
                . . . . . 3 3 d d 3 3 3 3 . . .
                . . . . . c d 3 3 3 3 3 c . . .
                . . . . 3 c d 3 3 3 3 3 c 3 . .
                . . . a 3 c d 3 3 3 3 3 c 3 a .
                . . . f 3 c d 3 3 3 3 3 c 3 f .
                . . . f a c 3 3 3 3 3 3 c a f .
                . . . f 3 c 3 b b b b 3 c 3 f .
                . . . a 3 3 b c c c c b 3 3 a .
                . . . a a b c c c c c c b a a .
                . . . f a d d d d d d d d a f .
                . . . f a d 3 3 3 3 3 3 d a f .
                . . . . 3 d d 3 3 3 3 d d 3 f .
                . . . . f 3 d 3 3 3 3 d 3 f . .
                . . . . . a 3 3 3 3 3 3 a . . .
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    package1 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . e e e e e e e . .
                    . . . . . . e d d d d d e e . .
                    . . . . . e d d d d d d e e . .
                    . . . . e d d d d d d e d e . .
                    . . . . e e e e e e e d d e . .
                    . . . . e d d d d d e d d e . .
                    . . . . e d d d d d e d d e . .
                    . . . . e d d d d d e d d e . .
                    . . . . e d d d d d e d e e . .
                    . . . . e d d d d d e e e . . .
                    . . . . e e e e e e e e . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        car,
        0,
        50)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

# Deliver packages up (A) or down (B)

def on_a_pressed():
    package2 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . e e e e e e e . .
                    . . . . . . e d d d d d e e . .
                    . . . . . e d d d d d d e e . .
                    . . . . e d d d d d d e d e . .
                    . . . . e e e e e e e d d e . .
                    . . . . e d d d d d e d d e . .
                    . . . . e d d d d d e d d e . .
                    . . . . e d d d d d e d d e . .
                    . . . . e d d d d d e d e e . .
                    . . . . e d d d d d e e e . . .
                    . . . . e e e e e e e e . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        car,
        0,
        -50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    car.set_image(img("""
        . . . . . . . . . . . . . . . .
                . . . . . . 3 3 3 3 3 3 3 3 . .
                . . . . . 3 c 3 3 3 3 3 3 d 3 .
                . . . . 3 c c 3 3 3 3 3 3 d c 3
                . . d 3 d c c 3 d d d d d d c c
                . d 3 3 d c b a a a a a a a 3 c
                . 3 3 3 d b a a b b b a b b a 3
                . 3 3 3 3 3 a b b b b a b b b a
                . 3 3 3 3 a 3 3 3 3 3 a 3 3 3 a
                . 3 d d 3 a f a a a f a a a a a
                . d d 3 a a a f a a f a a a a a
                . a a a a a a a f f f a a a a a
                . a a a a f f f a a a a f f f f
                . . . a f f f f f a a f f f f f
                . . . . f f f f . . . . f f f .
                . . . . . . . . . . . . . . . .
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    car.set_image(img("""
        . . . . . . . . . . . . . . . .
                . . . . 3 3 3 3 3 3 3 3 . . . .
                . . . 3 d 3 3 3 3 3 3 c 3 . . .
                . . 3 c d 3 3 3 3 3 3 c c 3 . .
                . 3 c c d d d d d d 3 c c d 3 d
                . 3 c 3 a a a a a a a b c d 3 3
                . 3 3 a b b a b b b a a b d 3 3
                . 3 a b b b a b b b b a 3 3 3 3
                . a a 3 3 3 a 3 3 3 3 3 a 3 3 3
                . a a a a a a f a a a f a 3 d d
                . a a a a a a f a a f a a a 3 d
                . a a a a a a f f f a a a a a a
                . a f f f f a a a a f f f a a a
                . . f f f f f a a f f f f f a .
                . . . f f f . . . . f f f f . .
                . . . . . . . . . . . . . . . .
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

# Change the car image based on the direction it's
# driving

def on_down_pressed():
    car.set_image(img("""
        . . . . . . a a c c a a . . . .
                . . . . . a 3 3 3 3 3 3 a . . .
                . . . . 3 c 3 3 3 3 3 3 c 3 . .
                . . . a 3 c d 3 3 3 3 3 c 3 a .
                . . . f 3 3 d 3 3 3 3 3 c 3 f .
                . . . f 3 3 d 3 3 3 3 3 3 3 f .
                . . . f 3 3 d 3 3 3 3 3 3 3 f .
                . . . f 3 c 3 d d 3 3 3 c 3 f .
                . . . a 3 c a c c c c a c 3 a .
                . . . a 3 a c b b b b c a 3 a .
                . . . a 3 a b b b b b b a 3 a .
                . . . a a a a a a a a a a a a .
                . . . f a d a a a a a a d a f .
                . . . f a 3 d a a a a d 3 a f .
                . . . f f a a a a a a a a f f .
                . . . . f f . . . . . . f f . .
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

# Score a point for delivering packages to houses

def on_on_overlap(sprite2, otherSprite):
    music.magic_wand.play()
    sprite2.destroy(effects.confetti, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Object, on_on_overlap)

# Lose a point for driving into a house

def on_on_overlap2(sprite3, otherSprite2):
    music.play_tone(147, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(131, music.beat(BeatFraction.QUARTER))
    scene.camera_shake(2, 200)
    info.change_score_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Object, on_on_overlap2)

scene.set_background_color(7)
tiles.set_tilemap(tilemap("""
    level
"""))
car = sprites.create(img("""
        . . . . . . . . . . . . . . . .
            . . . . 3 3 3 3 3 3 3 3 . . . .
            . . . 3 d 3 3 3 3 3 3 c 3 . . .
            . . 3 c d 3 3 3 3 3 3 c c 3 . .
            . 3 c c d d d d d d 3 c c d 3 d
            . 3 c 3 a a a a a a a b c d 3 3
            . 3 3 a b b a b b b a a b d 3 3
            . 3 a b b b a b b b b a 3 3 3 3
            . a a 3 3 3 a 3 3 3 3 3 a 3 3 3
            . a a a a a a f a a a f a 3 d d
            . a a a a a a f a a f a a a 3 d
            . a a a a a a f f f a a a a a a
            . a f f f f a a a a f f f a a a
            . . f f f f f a a f f f f f a .
            . . . f f f . . . . f f f f . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
tiles.place_on_random_tile(car, myTiles.tile4)
controller.move_sprite(car)
scene.camera_follow_sprite(car)
for value in tiles.get_tiles_by_type(myTiles.tile1):
    myPurpleHouse = sprites.create(img("""
            ....................8a8aa8a8....................
                    .................aaa888aa8a8aaa.................
                    ..............aaa8aa8a8aa888aa8aaa..............
                    ...........8aa8aa8888a8aa8a8888aa8aa8...........
                    ........8888aa8aa8aa8a8aa8a8aa8aa8aa8888........
                    .....aaa8aa8aa8888aa8a8aa8a8aa8888aa8aa8aaa.....
                    ...aa8888aa8aa8aa8aa888aa888aa8aa8aa8aa8888aa...
                    dccaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aaccd
                    bcb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bcb
                    dbbaa8aa8888aa8aa8888a8aa8a8888aa8aa8888aa8aabbd
                    dbbaa8aa8aa8aa8888aa8a8aa8a8aa8888aa8aa8aa8aabbd
                    dccaa8888aa8aa8aa8aa888aa888aa8aa8aa8aa8888aaccd
                    bcbaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aabcb
                    dbb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bbd
                    dbbaa8aa8888aa8aa8aa8a8aa8a8aa8aa8aa8888aa8aabbd
                    dccaa8aa8aa8aa8aa8888a8aa8a8888aa8aa8aa8aa8aaccd
                    bcbaa8888aa8aa8888aa888aa888aa8888aa8aa8888aabcb
                    dbbaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aabbd
                    dbb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bbd
                    dccaa8aa8888aa8aa8aa8a8aa8a8aa8aa8aa8888aa8aaccd
                    bcbaa8aa8aa8aa8aa8aa888aa888aa8aa8aa8aa8aa8aabcb
                    dbbaa8888aa8aa8aa888ccbbbbcc888aa8aa8aa8888aabbd
                    dbbaa8aa8aa8aa888ccbbbbbbbbbbcc888aa8aa8aa8aabbd
                    dcc888aa8aa888ccbbbbbccccccbbbbbcc888aa8aa888ccd
                    bcbaa8aa888ccbbbbbccbddddddbccbbbbbcc888aa8aabcb
                    dbbaa8aaccbbbbbccbddddddddddddbccbbbbbccaa8aabbd
                    dbbaaccbbbbcccbddddddddddddddddddbcccbbbbccaabbd
                    dcccbbbbcccbdddbccbbbbbbbbbbbbccbdddbcccbbbbcccd
                    ccccccccbbbbbbbcbddddddddddddddbcbbbbbbbcccccccc
                    bddddddddddddbcddddddddddddddddddcbddddddddddddb
                    bbcbdddddddddcbd1111111111111111dbcdddddddddbcbb
                    bbbcccccccccccd1bbbbbbbbbbbbbbbb1dcccccccccccbbb
                    bbbbdddddddddc11beeeeeeeeeeeeeeb11cdddddddddbbbb
                    bbb8aaaaaaa8dc1be3b33b33b33b33beb1cd8aaaaaaa8bbb
                    bbb888888888dc1be3b33b33b33b33beb1cd888888888bbb
                    bbb833333338dcbbf3b3effffffe33bebbcd833333338bbb
                    bbb83ff3ff38dcbbf3bffffffffff3bebbcd83ff3ff38bbb
                    bbb83cc3cc38dcbbf3effffffffffebebbcd83cc3cc38bbb
                    bbb833333338dcbbf3eeeeeeeeeeeebebbcd833333338bbb
                    cbb83ff3ff38dcbbe3b33b33b33b33bebbcd83ff3ff38bbc
                    cbb83cc3cc38dcbbe3b33b33b33b33bebbcd83cc3cc38bbc
                    ccbbbbbbbbbbdcbbe3b33b33b33feeeebbcdbbbbbbbbbbcc
                    .cbbdddddddddcbbe3b33b33b33ffffebbcdddddddddbbc.
                    ..cbdbbbdbbbdcbbf3b33b33b33f33febbcdbbbdbbbdbc..
                    ...cdbbbdbbbdcbbf3b33b33b33bffeebbcdbbbdbbbdc...
                    ....bddddddddcbbf3b33b33b33b33bebbcddddddddb....
                    .....bdbbbdddcbbf3b33b33b33b33bebbcdddbbbdb.....
                    ......bcccbbbcbbe3b33b33b33b33bebbcbbbcccb......
        """),
        SpriteKind.Object)
    tiles.place_on_tile(myPurpleHouse, value)
for value2 in tiles.get_tiles_by_type(myTiles.tile2):
    myRedHouse = sprites.create(img("""
            ......6ccc666c66e4e44e44e44e44ee66c666ccc6......
                    .....64eee444c66f4e44e44e44e44ee66c444eee46.....
                    ....644444444c66f4e44e44e44e44ee66c444444446....
                    ...c4eee4eee4c66f4e44e44e44effee66c4eee4eee4c...
                    ..c64eee4eee4c66f4e44e44e44f44fe66c4eee4eee46c..
                    .c66444444444c66e4e44e44e44ffffe66c44444444466c.
                    cc66666666664c66e4e44e44e44feeee66c46666666666cc
                    c66edccdccde4c66e4e44e44e44e44ee66c4edccdccde66c
                    c66edffdffde4c66e4e44e44e44e44ee66c4edffdffde66c
                    666eddddddde4c66f4eeeeeeeeeeeeee66c4eddddddde666
                    666edccdccde4c66f4effffffffffeee66c4edccdccde666
                    666edffdffde4c66f4effffffffff4ee66c4edffdffde666
                    666eddddddde4c66f4e4effffffe44ee66c4eddddddde666
                    666eeeeeeeee4c16e4e44e44e44e44ee61c4eeeeeeeee666
                    666e2222222e4c16e4e44e44e44e44ee61c4e2222222e666
                    6666444444444c116eeeeeeeeeeeeee611c4444444446666
                    666cccccccccccd166666666666666661dccccccccccc666
                    66cb444444444cb411111111111111114bc444444444bc66
                    64444444444446c444444444444444444c64444444444446
                    cccccccc6666666cb44444444444444bc6666666cccccccc
                    4ccc6666ccc6444bcc666666666666ccb4446ccc6666ccc4
                    46622cc6666ccc64444444444444444446ccc6666cc22664
                    46622e22cc66666cc64444444444446cc66666cc22e22664
                    6c622e22eeecc66666cc64444446cc66666cceee22e226c6
                    4cceee22e22eeecc66666cccccc66666cceee22e22eeecc4
                    46622e22e22e22eeecc6666666666cceee22e22e22e22664
                    46622eeee22e22e22eeecc6666cceee22e22e22eeee22664
                    6c622e22e22e22e22e22eee22eee22e22e22e22e22e226c6
                    4cc22e22eeee22e22e22e2e22e2e22e22e22eeee22e22cc4
                    466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
                    46622e22e22eeee22e22e2e22e2e22e22eeee22e22e22664
                    6c622eeee22e22eeee22eee22eee22eeee22e22eeee226c6
                    4cc22e22e22e22e22eeee2e22e2eeee22e22e22e22e22cc4
                    46622e22eeee22e22e22e2e22e2e22e22e22eeee22e22664
                    466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
                    6c622e22e22eeee22e22e2e22e2e22e22eeee22e22e226c6
                    4cc22eeee22e22e22e22eee22eee22e22e22e22eeee22cc4
                    46622e22e22e22eeee22e2e22e2e22eeee22e22e22e22664
                    46622e22eeee22e22eeee2e22e2eeee22e22eeee22e22664
                    6c6eee22e22e22e22e22e2e22e2e22e22e22e22e22eee6c6
                    4cc22e22e22eeee22e22e2e22e2e22e22eeee22e22e22cc4
                    ...22eeee22e22e22e22eee22eee22e22e22e22eeee22...
                    .....222e22e22eeee22e2e22e2e22eeee22e22e222.....
                    ........eeee22e22e22e2e22e2e22e22e22eeee........
                    ...........e22e22eeee2e22e2eeee22e22e...........
                    ..............222e22e2e22eee22e222..............
                    .................222eee22e2e222.................
                    ....................e2e22e2e....................
        """),
        SpriteKind.Object)
    tiles.place_on_tile(myRedHouse, value2)