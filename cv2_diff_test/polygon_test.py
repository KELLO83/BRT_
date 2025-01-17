import cv2
import numpy as np
import re
import os

polygon = [(1151, 335), (1147, 342), (1147, 353), (1147, 364), (1147, 375), (1147, 381), (1144, 384), (1140, 382), (1138, 374), (1136, 371), (1132, 368), (1123, 373), (1125, 386), (1124, 399), (1122, 411), (1123, 420), (1125, 434), (1128, 444), (1131, 450), (1132, 463), (1136, 469), (1139, 460), (1145, 449), (1151, 430), (1158, 409), (1167, 398), (1176, 392), (1179, 388), (1187, 384), (1193, 375), (1187, 349), (1178, 336), (1168, 331), (1155, 330)]
#polygon = [(1289, 494), (1283, 513), (1281, 535), (1277, 553), (1255, 558), (1227, 572), (1216, 586), (1215, 601), (1216, 617), (1211, 646), (1211, 677), (1219, 686), (1232, 694), (1258, 690), (1275, 684), (1284, 688), (1294, 702), (1305, 714), (1317, 690), (1341, 679), (1348, 671), (1340, 647), (1345, 628), (1348, 603), (1347, 588), (1345, 574), (1350, 559), (1351, 539), (1338, 513), (1328, 500), (1313, 496), (1303, 494), (1295, 492)]
polygon = [(719, 256), (708, 260), (701, 264), (695, 273), (696, 287), (703, 297), (709, 305), (724, 303), (738, 302), (746, 302), (752, 293), (757, 287), (758, 271), (751, 260), (744, 255), (733, 251), (725, 253)] # 11번좌석
polygon = [(627, 267), (622, 274), (609, 284), (605, 298), (602, 310), (596, 320), (590, 326), (625, 328), (636, 331), (655, 323), (659, 313), (661, 293), (660, 280), (657, 267), (652, 259), (637, 259), (633, 263)]  # 12번좌석
polygon = [(652, 378), (643, 396), (635, 429), (627, 455), (638, 494), (665, 531), (696, 562), (734, 590), (770, 601), (835, 623), (864, 649), (886, 659), (899, 647), (865, 618), (855, 577), (857, 542), (809, 517), (773, 488), (746, 467), (726, 435), (718, 394), (704, 365), (668, 358)] #  22번좌석
#polygon = [(1032, 279), (1025, 290), (1018, 304), (1013, 306), (1004, 311), (990, 333), (987, 356), (983, 373), (988, 386), (1009, 385), (1015, 378), (1025, 367), (1034, 359), (1044, 346), (1051, 340), (1052, 330), (1062, 326), (1074, 326), (1085, 326), (1090, 316), (1087, 298), (1080, 285), (1068, 273), (1046, 267), (1038, 270)] # 23번좌석
#polygon = [(1157, 274), (1144, 278), (1129, 278), (1118, 283), (1108, 296), (1098, 309), (1098, 324), (1104, 335), (1114, 346), (1116, 356), (1121, 365), (1126, 372), (1135, 376), (1139, 361), (1144, 348), (1161, 343), (1175, 341), (1189, 343), (1184, 333), (1178, 323), (1186, 314), (1189, 297), (1179, 284), (1172, 279), (1165, 276)] # 24번좌석
NAME = 'cv2_diff_test/IMAGE_3RGB_MASK/22_MERGE.jpg'
img = cv2.imread(f"{NAME}")
number = ''.join(re.findall(r'\d',os.path.basename(NAME)))
mask = np.zeros(img.shape[:2] , dtype=np.uint8)


polygon_np = np.array(polygon, np.int32)
polygon_np = polygon_np.reshape((-1, 1, 2))  # OpenCV에서 요구하는 형태로 변환


cv2.fillPoly(mask , [polygon_np] , color=(255,255,255))
#cv2.polylines(img, [polygon_np], isClosed=True, color=(255, 0, 0), thickness=2)
print(f"Mask shape: {mask.shape}, Image shape: {img.shape}")
print(f"Mask dtype: {mask.dtype}, ImGimg dtype: {img.dtype}")
synthesis = cv2.bitwise_and(img , img , mask=mask)

cv2.imwrite(f"cv2_diff_test/IMAGE_3RGB_MASK_CROP/{number}.jpg" , synthesis)
# 결과 보여주기
cv2.namedWindow("polyline" , cv2.WINDOW_NORMAL)
cv2.namedWindow("mask" , cv2.WINDOW_NORMAL)
cv2.namedWindow("synthesis",cv2.WINDOW_NORMAL)
cv2.imshow("polyline", img)
cv2.imshow("mask",mask)
cv2.imshow("synthesis",synthesis)
cv2.waitKey(0)
cv2.destroyAllWindows()