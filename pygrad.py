class PyGrad:
    def __init__(self):
        pass

    def get_rich_pygrad(self, txt: str, start_rgb: list, end_rgb: list) -> str:
        rich_pygrad_text = ""
        increase = []  # list of each rgb how much increased

        chars = len(txt)

        for i, (start, end) in enumerate(zip(start_rgb, end_rgb)):
            if start > end:
                increase.append(int((start_rgb[i] - end_rgb[i]) / chars))
            else:
                increase.append(int((end_rgb[i] - start_rgb[i]) / chars))
            if increase[i] == 0 and start_rgb[i] != end_rgb[i]:
                increase[i] = 1
            elif increase[i] > 254 and start_rgb[i] - end_rgb[i] not in (255, -255):
                print("255 was replaced with 100 jump")
                increase[i] = 100


   #     num0 = int((start_rgb[0] - end_rgb[0]) / chars)
  #      num1 = int((start_rgb[1] - end_rgb[1]) / chars)
 #       num2 = int((start_rgb[2] - end_rgb[2]) / chars)

#        increase = [num0, num1, num2]

        current_rgb = start_rgb

        for character in txt:
            colors = str(tuple(current_rgb)).replace(" ", "")
            # rich_pygrad_text += f"[rgb({colors})]{character}[/rgb{colors}]"
            rich_pygrad_text += f"[rgb{colors}]{character}"
            # print(colors)
            for i in range(len(current_rgb)):
                current_rgb[i] += increase[i]

            # keep numbers in 0-255 range
            for i,num in enumerate(current_rgb):
                if num > 255:
                    current_rgb[i] = current_rgb[i] - 255
                if num < 0:
                    current_rgb[i] = current_rgb[i] + 255
        return rich_pygrad_text


from rich.console import Console

c = Console()
p = PyGrad()


