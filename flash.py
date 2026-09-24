import gradio as gr
import random


flashcards = [
    {
        "question": "Open an image with Pillow",
        "answer": "Image.open()"
    },
    {
        "question": "Display a Pillow image",
        "answer": "image.show()"
    },
    {
        "question": "Find a Pillow image's size",
        "answer": "image.size"
    },
    {
        "question": "Resize an image with Pillow",
        "answer": "image.resize((width, height))"
    },
    {
        "question": "Convert a Pillow image to grayscale",
        "answer": "image.convert('L')"
    },
    {
        "question": "Rotate an image with Pillow",
        "answer": "image.rotate()"
    },
    {
        "question": "Crop an image with Pillow",
        "answer": "image.crop((left, top, left + width, top + height))"
    },
    {
        "question": "Read an image with OpenCV?",
        "answer": 'cv2.imread()'
    },
    {
        "question": "Display an OpenCV image?",
        "answer": 'cv2.imshow("Window", image)'
    },
    {
        "question": "Save an OpenCV image?",
        "answer": 'cv2.imwrite("output.jpg", image)'
    },
    {
        "question": "Convert OpenCV BGR to grayscale?",
        "answer": "cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)"
    },
    {
        "question": "What color order does OpenCV use by default?",
        "answer": "BGR — Blue, Green, Red."
    },
    {
        "question": "What color order does Pillow normally use?",
        "answer": "RGB — Red, Green, Blue."
    },
    {
        "question": "Resize an image with OpenCV?",
        "answer": "cv2.resize(image, (width, height))"
    },
    {
        "question": "Flip an image with OpenCV?",
        "answer": "cv2.flip(image, flipCode)"
    },
    {
        "question": "What does cv2.imread() return?",
        "answer": "A NumPy array containing the image pixels."
    },
    {
        "question": "What does an image's shape tell you?",
        "answer": "Its dimensions, such as height, width, and channels."
    },
    {
        "question": "What does a grayscale pixel usually contain?",
        "answer": "One intensity value, typically 0–255."
    },
    {
        "question": "What does a pixel value of 0 mean in a grayscale image?",
        "answer": "Black."
    },
    {
        "question": "How can you increase image brightness with NumPy?",
        "answer": "Add a value to pixel intensities, then clip to 0–255."
    },
    {
        "question": "What happens when image brightness increases?",
        "answer": "Pixel values become larger, making the image lighter."
    },
    {
        "question": "What does image contrast control?",
        "answer": "The difference between dark and bright pixels."
    },
    {
        "question": "How to increase contrast with NumPy?",
        "answer": "Multiply pixel values by a factor, then clip to 0–255."
    },
    {
        "question": "What are the three RGB channels?",
        "answer": "Red, Green, and Blue."
    },
    {
        "question": "How to access the red channel in an RGB array?",
        "answer": "Use image[:, :, 0]."
    },
    {
        "question": "What happens if setting the red channel to 0?",
        "answer": "The image loses its red component."
    },
    {
        "question": "What is thresholding used for?",
        "answer": "Separating pixels into groups, often foreground and background."
    },
    {
        "question": "What does binary thresholding usually produce?",
        "answer": "An image containing mainly 0 and 255."
    },
    {
        "question": "How do you apply binary thresholding in OpenCV?",
        "answer": "cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)"
    },
    {
        "question": "How do you draw a line with OpenCV?",
        "answer": "cv2.line(image, start, end, color, thickness)"
    },
    {
        "question": "How do you draw a rectangle with OpenCV?",
        "answer": "cv2.rectangle(image, start, end, color, thickness)"
    },
    {
        "question": "How do you draw a circle with OpenCV?",
        "answer": "cv2.circle(image, center, radius, color, thickness)"
    },
    {
        "question": "Why do we blur an image?",
        "answer": "To reduce noise and smooth details."
    },
    {
        "question": "How do you apply Gaussian blur in OpenCV?",
        "answer": "cv2.GaussianBlur(image, (5, 5), 0)"
    },
    {
        "question": "What does edge detection find?",
        "answer": "Strong changes in brightness, often object boundaries."
    },
    {
        "question": "Which OpenCV function performs Canny edge detection?",
        "answer": "cv2.Canny(image, threshold1, threshold2)"
    },
    {
        "question": "How is an image represented in NumPy?",
        "answer": "As an array of pixel values."
    },
    {
        "question": "How do you access one grayscale pixel?",
        "answer": "Use image[y, x]."
    },
    {
        "question": "How do you change one grayscale pixel?",
        "answer": "Use image[y, x] = 255."
    },
    {
        "question": "How do you access one RGB pixel?",
        "answer": "Use image[y, x], which contains three channel values."
    },
    {
        "question": "What does image.shape return for a color image?",
        "answer": "Usually (height, width, channels)."
    }
]

# random.shuffle(flashcards)

current_card = 0
score = 0
known_cards = set()

def show_answer():
    return flashcards[current_card]["answer"]


def next_card():
    global current_card
    current_card +=1
    if current_card >= len(flashcards):
        current_card = 0

    return (
        f"### Question {current_card + 1}:",
        flashcards[current_card]["question"],
        "",
        "" # clear feedback
    )

def pre_card():
    global current_card
    current_card -= 1
    if current_card < 0:
        current_card = len(flashcards) - 1

    return (
        f"### Question {current_card +1 }:",
        flashcards[current_card]["question"],
        "",
        "" # clear feedback
    )

def know():
    global score

    if current_card not in known_cards:
        known_cards.add(current_card)
        score += 1
        message = "✅ Correct! Great Job!"
    else:
        message = "ℹ️ You already received a point for this question."

    return (
        f"Score: {score} / {len(flashcards)}",
        message
    )


def dont_know():
    return (
        f"Score: {score} / {len(flashcards)}"
        "❌ That's okay!"
    )


with gr.Blocks() as app:

    gr.Markdown("# 🐍 Python Pillow and OpenCV Flashcards")

    question_label = gr.Markdown("### Question 1:")
    question = gr.Textbox(
        value=flashcards[0]["question"],
        show_label=False
    )

    answer = gr.Textbox(
        label="Answer"
    )

    score_display = gr.Textbox(
        value=f"Score: 0 / {len(flashcards)}",
        label="Score"
    )

    feedback = gr.Markdown("")

    with gr.Column():
        pre_button = gr.Button("← Previous")
        next_button = gr.Button("Next →")

    with gr.Column():
        know_button = gr.Button("✓ I Know")
        # dont_know_button = gr.Button("✗ Don't Know")


    show_button = gr.Button("Show Answer")


    show_button.click(
        show_answer,
        outputs=answer
    )

    next_button.click(
        next_card,
        outputs=[question_label, question, answer, feedback]
    )

    pre_button.click(
        pre_card,
        outputs=[question_label, question, answer, feedback]
    )

    know_button.click(
        know,
        outputs=[score_display, feedback]
    )

    # dont_know_button.click(
    #     dont_know,
    #     outputs=[score_display, feedback]
    # )


app.launch(share=True)