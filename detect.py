import cv2
import torch
import clip
from PIL import Image


cap = cv2.VideoCapture(0)



tracker = cv2.TrackerCSRT_create()



Dev = "cuda" if torch.cuda.is_available() else "cpu"
model, prepro = clip.load("ViT-B/32", device=Dev)

labels = ["person", "phone", "tongue", "water bottle", "cup", "hand", "keyboard", "mouse"]
text = clip.tokenize(labels).to(Dev)

non = "unknown"


def cropBox(img, bowbox):
  x, y, w, h = int(bowbox[0]), int(bowbox[1]), int(bowbox[2]), int(bowbox[3])
  cv2.rectangle(img, (x,y), (x+w, y+h), (255,100,255), 3, 1)
  cv2.putText(img, "status: tracking", (25, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL ,0.7, (225,0,225), 1)


def clipsMod(frame, bowbox):
   x, y, w, h = int(bowbox[0]), int(bowbox[1]), int(bowbox[2]), int(bowbox[3])

   crop = frame[y:y + h, x:x + w]
   crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
   crop = Image.fromarray(crop)
   img2 = prepro(crop).unsqueeze(0).to(Dev)

   with torch.no_grad():
        imgf = model.encode_image(img2)
        txtf = model.encode_text(text)

        imgf = imgf / imgf.norm(dim=-1, keepdim=True)
        txtf = txtf / txtf.norm(dim=-1, keepdim=True)

        score = torch.matmul(imgf, txtf.T)
        score = score * 100.0
        rfinish = torch.softmax(score, dim=-1)

        x = rfinish[0].argmax().item()

   return labels[x]


suc, img = cap.read()
bowbox = cv2.selectROI("tracking", img, False)
tracker.init(img, bowbox)

category = clipsMod(img, bowbox)
print(category)

while True:
     timer = cv2.getTickCount()



     suc, img = cap.read()

     suc, bowbox = tracker.update(img)



     if suc:
          cropBox(img, bowbox)
          cv2.putText(img, "object: " + category, (25, 80), cv2.FONT_HERSHEY_COMPLEX_SMALL ,0.7, (225,0,225), 1)

     else:
          cv2.putText(img, "status: failed tracking :( ", (25, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL ,0.7, (0,0,225), 1)


     fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
     cv2.putText(img, "FPS: " + str(int(fps)), (25, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL ,0.7, (225,0,225), 1)
     cv2.imshow("trackin", img)

     if cv2.waitKey(1) & 0xFF == ord('g'):
          break

     #i made the break to be g because eyego