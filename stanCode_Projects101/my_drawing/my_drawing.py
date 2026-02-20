"""
File: my_drawing
Name: Cindy
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My Mickey
    Mickey has a brave and kind heart.
    Every time I see him, I feel like I have more courage to face all the challenges in my life.
    """

    window = GWindow(width=800, height=400)
    # face for Mickey Mouse
    face_size = 160
    face_x = (window.width - face_size)/2
    face_y = 110
    face = GOval(face_size, face_size, x=face_x, y=face_y)
    face.filled = True
    face.fill_color = (251, 228, 207)
    window.add(face)

    #left_ear
    ear_size = 90
    left_ear = GOval(ear_size, ear_size, x=face_x-ear_size*0.3, y=face_y-ear_size*0.7)
    left_ear.filled = True
    left_ear.fill_color = (0, 0, 0)
    window.add(left_ear)

    # Right_ear
    ear_size = 90
    right_ear = GOval(ear_size, ear_size, x=face_x + ear_size * 1, y=face_y - ear_size * 0.7)
    right_ear.filled = True
    right_ear.fill_color = (0, 0, 0)
    window.add(right_ear)

    # face for Mickey Mouse
    face_size = 160
    face_x = (window.width - face_size) / 2
    face_y = 110
    face = GOval(face_size-20, (face_size-1)/2, x=face_x+10, y=face_y)
    face.filled = True
    face.fill_color = (0, 0, 0)
    window.add(face)

    # m shape
    arc_width = 80
    arc_height = 150

    # Left Peak
    left_arc = GArc(arc_width, arc_height, 0, 195)
    left_arc.x = face_x
    left_arc.y = face_y + 20
    left_arc.filled = True
    left_arc.fill_color = (251, 228, 207)
    window.add(left_arc)

    left_arc = GArc(arc_width, arc_height+40, 0, 195)
    left_arc.x = face_x
    left_arc.y = face_y + 20
    left_arc.filled = True
    left_arc.fill_color = (251, 228, 207)
    left_arc.color = (251, 228, 207)
    window.add(left_arc)

    # Right Peak
    left_arc = GArc(arc_width, arc_height, 0, 195)
    left_arc.x = face_x + 80
    left_arc.y = face_y + 20
    left_arc.filled = True
    left_arc.fill_color = (251, 228, 207)
    window.add(left_arc)

    left_arc = GArc(arc_width, arc_height + 40, 0, 195)
    left_arc.x = face_x + 80
    left_arc.y = face_y + 20
    left_arc.filled = True
    left_arc.fill_color = (251, 228, 207)
    left_arc.color = (251, 228, 207)
    window.add(left_arc)

    # Center of face
    left_arc = GArc(arc_width, arc_height-80, 0, 195)
    left_arc.x = face_x + 50
    left_arc.y = face_y + 55
    left_arc.filled = True
    left_arc.fill_color = (251, 228, 207)
    left_arc.color = (251, 228, 207)
    window.add(left_arc)

    # Left_eye
    eye_size = 20
    left_eye = GOval(eye_size, eye_size * 1.5, x=face_x + eye_size * 2, y=face_y + eye_size * 3.5)
    left_eye.filled = True
    left_eye.fill_color = (0, 0, 0)
    window.add(left_eye)

    # Left_eye_dot
    eye_size_dot = 6
    left_eye_dot = GOval(eye_size_dot, eye_size_dot * 1.5, x=face_x + eye_size * 2.5, y=face_y + eye_size * 4)
    left_eye_dot.filled = True
    left_eye_dot.fill_color = (255, 255, 255)
    window.add(left_eye_dot)

    # Right_eye
    eye_size = 20
    right_eye = GOval(eye_size, eye_size * 1.5, x=face_x + eye_size * 5.2, y=face_y + eye_size * 3.5)
    right_eye.filled = True
    right_eye.fill_color = (0, 0, 0)
    window.add(right_eye)

    # Right_eye_dot
    eye_size_dot = 6
    right_eye_dot = GOval(eye_size_dot, eye_size_dot * 1.5, x=face_x + eye_size * 5.4, y=face_y + eye_size * 4)
    right_eye_dot.filled = True
    right_eye_dot.fill_color = (255, 255, 255)
    window.add(right_eye_dot)

    #nose
    nose_size = 15
    nose = GOval(nose_size*1.5, nose_size, x=face_x + eye_size * 3.5, y=face_y + eye_size * 5)
    nose.filled = True
    nose.fill_color = (0, 0, 0)
    window.add(nose)

    #mouth
    mouth_size = 10
    mouse = GOval(mouth_size*3.5, mouth_size, x=face_x + eye_size * 3.2, y=face_y + eye_size * 6.2)
    mouse.filled = True
    mouse.fill_color = (251, 228, 207)
    window.add(mouse)

    # mouth_cover
    mouth_size = 10
    mouse_cover = GOval(mouth_size * 3.5, mouth_size, x=face_x + eye_size * 3.2, y=face_y + eye_size * 6.1)
    mouse_cover.filled = True
    mouse_cover.fill_color = (251, 228, 207)
    mouse_cover.color = (251, 228, 207)
    window.add(mouse_cover)

    # nose_decoration
    nose_decoration_size = 20
    nose_decoration = GArc(nose_decoration_size, nose_decoration_size, 210, 60, x=face_x + eye_size * 3.5, y=face_y + eye_size * 5)
    nose_decoration.filled = True
    nose_decoration.fill_color = (255, 255, 255)
    nose_decoration.color = (255, 255, 255)
    window.add(nose_decoration)

    # left_mouse
    left_mouse_size = 18
    left_mouse = GArc(left_mouse_size, left_mouse_size-5, 0, 90, x=face_x+56, y=face_y+126)
    left_mouse.filled = True
    left_mouse.fill_color = (0, 0, 0)
    left_mouse.color = (0, 0, 0)
    window.add(left_mouse)

    # right_mouse
    right_mouse_size = 18
    right_mouse = GArc(right_mouse_size, right_mouse_size - 5, 0, 90, x=face_x + 94, y=face_y + 126)
    right_mouse.filled = True
    right_mouse.fill_color = (0, 0, 0)
    right_mouse.color = (0, 0, 0)
    window.add(right_mouse)

    # left_brush
    brush_size = 20
    left_brush = GOval(brush_size, brush_size-6, x=face_x + 25, y=face_y + 110)
    left_brush.filled = True
    left_brush.fill_color = (240, 211, 228)
    left_brush.color = (240, 211, 228)
    window.add(left_brush)

    # right_brush
    brush_size = 20
    right_brush = GOval(brush_size, brush_size - 6, x=face_x + 120, y=face_y + 110)
    right_brush.filled = True
    right_brush.fill_color = (240, 211, 228)
    right_brush.color = (240, 211, 228)
    window.add(right_brush)

    # word1
    word_size = 120
    word = GRect(word_size, word_size/2, x=face_x-200, y=face_y)
    word.filled = True
    word.fill_color = (255, 255, 255)
    word.color = (0, 0, 0)
    window.add(word)

    label = GLabel("SC101")
    label.font = "SansSerif-24"
    label_x = word.x + ((word.width - label.width) / 2)
    label_y = word.y + ((word.height + label.height)/2)
    window.add(label, x=label_x, y=label_y)

    # word2
    word_size = 120
    word = GRect(word_size, word_size / 2, x=face_x - 150, y=face_y+60)
    # word = GRect(word_size, word_size / 2, x=face_x - 200, y=face_y + 60)
    word.filled = True
    word.fill_color = (255, 255, 255)
    word.color = (0, 0, 0)
    window.add(word)

    label = GLabel("Amazing")
    label.font = "SansSerif-16"
    label_x = word.x + ((word.width - label.width) / 2)
    label_y = word.y + ((word.height + label.height) / 2)
    window.add(label, x=label_x, y=label_y)


if __name__ == '__main__':
    main()
