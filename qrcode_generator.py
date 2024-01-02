import qrcode

class MyQr:
    def __init__(self, size:int, padding:int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, filename:str, fc:str, bc:str):
        user_input = input("Enter text: ")
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fc, back_color=bc)
            qr_image.save(filename)
            print(f"Successfully created ({filename})")
        except Exception as e:
            print(f"Error: {e}")

def main():
    myqr = MyQr(size=30, padding=3)
    myqr.create_qr("sample.png", "pink", "white")

if __name__ == '__main__':
    main()
