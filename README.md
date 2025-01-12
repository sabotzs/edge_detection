# Edge detection

## Table of contents (TODO)

## Introduction
What are edges, what are they useful for and how can we find them?
Edges are boundaries between objects. Inside images edges also represent sharp changes in brightness like changes in surface orientation and illumination changes like shadow cast boundaries. Further down we will find ways methods for detecting edges.

After we detect edges, we can use the results to find objects inside an image, analyse it. We can also use edge detection for shape recognition.

## Mathematical modeling
For simplicity, we'll analyse a single row of an image. As we said edges are sharp changes in the brightness inside an image, thus the algorithms we'll present will work with grayscaled images.

A perfect edge would be a step function:
![](images/step_function.jpeg)

But unfortunately this is not always the case. The real case is usually a slighly blurred step:
![](images/gradient_function.jpeg)

How can we find them then? Well, we can take the first derivative of the intensity:
![](images/first_derivative.jpeg)

We can go even further, taking the second derivative:
![](images/second_derivative.jpeg)

As we can see, the first derivative has a peak at the edge and the second derivative has a zero crossing at the edge. The question is how do we find the derivative? To approximate it we'll use the [Taylor series](https://en.wikipedia.org/wiki/Taylor_series):
$$f(x + \Delta x) = f(x) + \frac{\Delta x}{1!}f'(x) + \frac{(\Delta x)^2}{2!}f''(x) + \ldots$$

In our case the step is $\Delta x = \plusmn 1$.
* For $\Delta x = 1$ we get the forward difference: $f'(x) = f(x + 1) - f(x)$
* For $\Delta x = -1$ we get the backward difference: $f'(x) = f(x) - f(x - 1)$

Adding theese equations we get the cental difference:
$$f'(x) = \frac{f(x + 1) - f(x - 1)}{2}$$

For the second order derivative $f''(x)$ we get:
* Forward difference: $f''(x) = 2(f(x + 1) - f(x) - f'(x))$
* Backward difference: $f''(x) = 2(f(x - 1) - f(x) + f'(x))$

Adding theese we get:
$$ \begin{split} f''(x) & = f(x + 1) - f(x) - f'(x) + f(x - 1) - f(x) + f'(x) \\ & = f(x + 1) - 2f(x) + f(x - 1) \end{split} $$

---
Similarly we can calculate the first and second order partial derivatives of the function $f(x, y)$:
* $f'_x(x, y) = \frac{f(x + 1, y) - f(x - 1, y)}{2}$
* $f'_y(x, y) = \frac{f(x, y + 1) - f(x, y - 1)}{2}$
* $f''_{xx}(x, y) = f(x + 1, y) - 2f(x, y) +f(x - 1, y)$
* $f''_{yy}(x, y) = f(x, y + 1) - 2f(x, y) +f(x, y - 1)$

Now that we've calculated the second order partial derivatives, we can use them to calculate the [Laplacian](https://en.wikipedia.org/wiki/Laplace_operator): $\nabla^2f(x, y) = f''_{xx}(x, y) + f''_{yy}(x, y) = f(x + 1, y) + f(x - 1, y) + f(x, y + 1) + f(x, y - 1) - 4f(x, y)$

[Gradient](https://en.wikipedia.org/wiki/Gradient) of function $f(x, y)$ at point $(x_0, y_0)$ is vector:
$$
\nabla f(x_0, y_0) =
\begin{bmatrix}
    f'_x(x_0, y_0)\\
    f'_y(x_0, y_0)
\end{bmatrix}
$$ 
Its magnitude $M(x_0, y_0) = \|\nabla f(x_0, y_0)\| = \sqrt{(f'_x(x_0, y_0))^2+(f'_y(x_0, y_0))^2}$ gives the rate of fastest increase at that point.
Its direction $d(x_0, y_0) = \arctan(\frac{f'_y(x_0, y_0)}{f'_x(x_0, y_0)})$ gives the direction of fastest increase at that point.

## Methods based on first order derivative

### Sobel operator

## References
* [1] [Digital Image Processing (4th edition), Rafael C. Gonzalez, Richard E. Woods](https://dl.icdst.org/pdfs/files4/01c56e081202b62bd7d3b4f8545775fb.pdf)
* [2] [OpenCV](https://docs.opencv.org/4.x/d7/da8/tutorial_table_of_content_imgproc.html)
