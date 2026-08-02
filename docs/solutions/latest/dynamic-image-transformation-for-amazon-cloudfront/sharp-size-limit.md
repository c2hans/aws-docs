---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/sharp-size-limit.html
---

# Sharp Size Limit
<a name="sharp-size-limit"></a>

Sharp restricts the pixel size of input images to `268402689` by default (`16383 ^ 2`). To modify the value the solution passes to sharp, in combination with the instructions in , modify the value under `SharpSizeLimit` from "", to the pixel limit you choose, based on the following rules:

1. An empty string or a non-number string will use the existing default.

1. A value of "0" will remove the limit.

1. A positive integer value will set the limit to that value, for example, a mapping value of `"2500000"` will cause the value passed to Sharp to be `2500000`.

1. Negative and decimal values are not permitted, and may cause errors with image processing.
