---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/rotate-images-manually.html
---

# Rotate images manually
<a name="rotate-images-manually"></a>

Not all browsers support rotational EXIF data for all image formats and you may notice visual issues when viewing your images through the browser. This tends to be more common with the WebP image format. Sharp allows the passing of a null value in the rotate field to indicate that the orientation associated with the EXIF orientation tag should be manually applied (and the tag removed). You can implement this for base64 image requests through the inclusion of a `rotate: null` edit, or for Thumbor-style requests by including `filters:strip_exif()` or `filters:strip_icc()` in your request path.
