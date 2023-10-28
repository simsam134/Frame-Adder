from pathlib import Path
import cv2
import numpy as np

origin_dir = Path(r'C:\Users\simsa\OneDrive\Skrivbord\konst\alkemi\solar\original')
target_dir = Path(r'C:\Users\simsa\OneDrive\Skrivbord\konst\alkemi\solar\processed')

target_res = (1080, 1920) # höjd x bredd
for img_path in origin_dir.iterdir():
    img = cv2.imread(str(img_path))
    original_res = img.shape
    scale_factor = target_res[0]/original_res[0]
    resized_image = cv2.resize(img, None, fx=scale_factor, fy=scale_factor)
    padded_img = np.zeros((target_res[0], target_res[1], 3), dtype=np.uint8)
    padding_side = (target_res[1] - resized_image.shape[1] )//2
    padded_img[:, padding_side:(padding_side + resized_image.shape[1]), : ] = resized_image
    target_name = target_dir / (img_path.stem+'.jpg')
    cv2.imwrite(str(target_name), padded_img)



