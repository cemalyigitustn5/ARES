import cv2


def kamera_baslat():
    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("ARES: Kamera bulunamadı.")
        return

    print("ARES: Görüş sistemi aktif.")

    while True:
        ret, goruntu = kamera.read()

        if not ret:
            break

        cv2.imshow("ARES Vision", goruntu)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    kamera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    kamera_baslat()
