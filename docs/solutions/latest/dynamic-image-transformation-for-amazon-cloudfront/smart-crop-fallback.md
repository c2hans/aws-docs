---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/smart-crop-fallback.html
---

# Smart crop returns an uncropped or full-frame image
<a name="smart-crop-fallback"></a>

 **Symptoms:**
+ A smart crop request returns the configured fallback (for example, a centered `cover` crop) instead of cropping around the detected content.
+ Crops vary between identical-looking images.

 **Cause:**

Smart cropping applies its fallback strategy when Amazon Rekognition detects no targets above the confidence threshold, or when the detection calls fail. The most common causes are a `minConfidence` set too high for the image, a `labels` value that doesn’t match what’s in the image, or Amazon Rekognition throttling under sustained traffic (only cache misses reach Amazon Rekognition, so this appears during traffic spikes on uncached images).

 **Solutions:**
+ Lower `smartCrop.minConfidence` or broaden the `labels` you request, then retry against an uncached image (append a unique query string to bypass the CloudFront cache).
+ Confirm the source image is a format Amazon Rekognition can analyze. The solution converts other formats automatically, but corrupt or unsupported source files yield no detections.
+ If the issue coincides with traffic spikes, you may be hitting the Amazon Rekognition per-API TPS limit. Review the smart crop log fields for the request and, if needed, request a Service Quotas increase. For limits and how to plan around them, see the Amazon Rekognition quotas guidance in the planning section.
