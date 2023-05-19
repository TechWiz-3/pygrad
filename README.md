# PyGrad

> Generate awesome RGB gradients for printing text using Rich


```py

from rich.console import Console

c = Console()
p = PyGrad()

c.print(
    p.get_rich_pygrad(
        txt="The quick brown fox jumped over the lazy dawggg",
        start_rgb=[0,0,200],
        end_rgb=[255, 0, 255]
    )
)
```
