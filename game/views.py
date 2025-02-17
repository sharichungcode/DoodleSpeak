from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from google.cloud import vision
from io import BytesIO
from PIL import Image
import base64
import json
import os

# Create your views here.
def game(request):
    return render(request, 'game/game.html')

def game_index(request):
    return render(request, 'index.html')

@login_required
def add_word(request):
    from dashboard.models import Dashboard 
    if request.method == 'POST':
        word = request.POST.get('word') 
        if word:
            dashboard, created = Dashboard.objects.get_or_create(user=request.user)
            word_count = len(dashboard.words_history)
            word_with_count = f"{word}_{word_count + 1}"
            dashboard.words_history.append(word_with_count)
            dashboard.save()
            return redirect('dashboard_index')
    return render(request, 'game/game.html')

def index(request):
    return render(request, 'game/index.html')

@login_required
def analyze_image(request):
    print("Analyzing image")
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data['image'].split(",")[1]
        target_word = data['target_word']
        print(f"Image data length: {target_word}")
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        buffered = BytesIO()
        image.save(buffered, format="PNG")

        client = vision.ImageAnnotatorClient()
        content = buffered.getvalue()
        print(f"Image content length: {len(content)}")
        image = vision.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations
        print(f"API Response: {response}")

        # Comparar as labels retornadas com a palavra alvo
        target_words = target_word.lower().split()
        matched_labels = [label.description for label in labels if any(word in label.description.lower().split() for word in target_words)]

        return JsonResponse({'labels': matched_labels})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# @login_required
# def analyze_image(request):
#     print("Analyzing image")
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         image_data = data['image'].split(",")[1]
#         print(f"Image data length: {len(image_data)}")
#         image = Image.open(BytesIO(base64.b64decode(image_data)))
#         buffered = BytesIO()
#         image.save(buffered, format="PNG")


#         # Save the image to a temporary file
#         # temp_image_path = os.path.join(os.path.dirname(__file__), 'temp_image.png')
#         # with open(temp_image_path, 'wb') as f:
#         #     f.write(buffered.getvalue())
#         # image.show() 


#         client = vision.ImageAnnotatorClient()
#         content = buffered.getvalue()
#         print(f"Image content length: {len(content)}")
#         image = vision.Image(content=content)
#         response = client.label_detection(image=image)
#         labels = response.label_annotations
#         print(f"API Response: {response}")
#         return JsonResponse({'labels': [label.description for label in labels]})
#     return JsonResponse({'error': 'Invalid request'}, status=400)