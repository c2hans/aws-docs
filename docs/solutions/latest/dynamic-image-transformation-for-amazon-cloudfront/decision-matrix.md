---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/decision-matrix.html
---

# Decision matrix and when to choose each
<a name="decision-matrix"></a>

| Requirement | Lambda Architecture | ECS Architecture |
| --- | --- | --- |
|  **Image size**  | ≤ 6 MB | ≤ 100 MB |
|  **Cost optimization**  | Yes - Lowest cost | Higher cost |
|  **Transformation policies**  | No | Yes |
|  **Non-S3 origins**  | No | Yes |
|  **Administrative UI**  | No | Yes |
|  **Auto-scaling**  | Yes - Built-in | Yes - Configurable |
|  **Content-aware smart cropping**  | Face detection only | Faces, labels, text, logos, and custom models |
|  **Content moderation**  | Yes | Yes |
|  **Multi-tier device detection**  | No - WebP conversion via the Accept header only | Yes - Client Hints, CloudFront device headers, and configurable fallback |

**Note**
Content-aware smart cropping (beyond face detection) and multi-tier device detection are available in the ECS architecture only (v8.1\+).
