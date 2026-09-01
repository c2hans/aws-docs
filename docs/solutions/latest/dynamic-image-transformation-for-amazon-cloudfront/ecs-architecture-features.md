---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-architecture-features.html
---

# ECS architecture features
<a name="ecs-architecture-features"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+). These capabilities are exclusive to the ECS architecture and are not available in the Lambda architecture. Customers who need these features should deploy the ECS architecture.

 **Smart cropping**

The ECS architecture provides a layered, content-aware smart cropping system that preserves specific elements within an image while maintaining a desired aspect ratio. Smart cropping combines one or more detection methods, then resolves the final crop through a priority-based constraint solver.

 *Multi-method target detection*: Smart cropping identifies important content using detection methods that can be combined in a single request. The solution invokes the required Amazon Rekognition APIs in parallel to help reduce request latencies:
+  **Face detection**: Uses the [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html) API, with support for selecting a specific face by index.
+  **Label detection**: Identifies objects, products, or subjects (for example, `Shoe`, `Watch`, `Car`) using the [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) API.
+  **Custom Labels**: Integrates a customer-trained Amazon Rekognition Custom Labels model for domain-specific detection using the [DetectCustomLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectCustomLabels.html) API.
+  **Text retention**: When enabled, uses the [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html) API to identify text regions (overlays, price tags, signage) and include them in the crop.
+  **Logo detection**: When enabled, includes `Logo` in label detection so brand logos are preserved.

 *Constraint-prioritized crop solver*: The solution resolves smart cropping requests through a priority-based constraint solver. When constraints conflict, higher-priority constraints are fully satisfied before lower-priority ones. The solver applies four constraints:
+  **Target inclusion** (always highest priority): Is designed to keep all detected targets fully visible inside the crop. Enforced first; this priority is fixed and not customer-configurable.
+  **Aspect ratio**: Forces the crop to a specific width:height ratio (for example, 16:9, 1:1), preserving the requested orientation.
+  **Padding**: Adds breathing room around the combined target bounding box, specified per axis in pixels or as a percentage.
+  **Gravity** (always lowest priority): Controls the relative anchoring between the target area and the crop box, specified either directionally (a 3x3 grid such as `top-left` or `center`) or by a detected label name. Applied last; this priority is fixed and not customer-configurable.

Customers control the relative priority of the two middle constraints (**aspect ratio** and **padding**) through the `priorities` parameter. Target inclusion is always resolved first and gravity is always applied last, so only these two can be reordered. When the customer does not specify priorities, the default order is aspect ratio before padding.

Each constraint also carries a default value when not explicitly set: target inclusion enabled, aspect ratio preserved from the original image, padding 3% of the target bounding box per axis, and gravity centered on the union bounding box. These defaults let a minimal request (for example, detecting `Person`) produce a reasonable crop without configuring every constraint. The solver operates entirely on in-memory rectangle arithmetic, with no additional Amazon Rekognition calls, and completes in sub-millisecond time. Each constraint receives a satisfaction status (`full`, `partial`, or `none`) for observability.

 *Fallback strategies*: When target detection fails or returns no results above the confidence threshold, the solution applies a configurable fallback strategy rather than failing the request:
+  **Cover**: Crop that fills the aspect ratio (may crop edges).
+  **Contain**: Fits the entire image within the aspect ratio (may add letterboxing).
+  **Fill**: Stretches the image to fill the aspect ratio (may distort).
+  **Inside/Outside**: Resizes to fit inside or cover the target dimensions.
+  **No-crop**: Returns the original image unchanged.

**Note**
Amazon Rekognition supports only the JPEG and PNG file formats. When you use the Amazon Rekognition detection features with an image that isn’t JPEG or PNG, the solution automatically converts the image to PNG for use with Amazon Rekognition, then converts it back to the original format.

 **Content moderation**

Administrators can enable automatic content moderation to detect and blur inappropriate images using the Amazon Rekognition [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) API. When enabled, the solution analyzes image content against configurable moderation labels and a confidence threshold, applying a Gaussian blur to images that match. This allows content platforms to maintain community standards without manual review. Configuration options include:
+  **Confidence threshold**: Minimum confidence level (default: 75) for triggering moderation.
+  **Blur intensity**: Gaussian blur strength applied to flagged content (default: 50).
+  **Moderation labels**: Specific content categories to detect (all available labels by default).

 **Multi-tier device detection**

Auto-optimization features (autosize, quality optimization, format optimization) rely on device and browser signals to deliver appropriately sized images. Client Hints headers are sent only by Chromium-based browsers (Chrome, Edge, Opera), which represent roughly 70% of web traffic. To deliver optimized images to all traffic, including Safari, Firefox, and users with privacy extensions that block Client Hints, the solution uses a progressive fallback chain for device detection. The CloudFront function evaluates each tier in order and uses the first available signal:

1.  **Responsive image width (`Sec-CH-Width`)**: Uses the browser-calculated render width for images in responsive layouts (`srcset`, `picture`). More precise than viewport width for images that don’t span the full viewport.

1.  **Viewport Client Hints**: The `Sec-CH-Viewport-Width` and `Sec-CH-DPR` signals.

1.  **CloudFront device detection**: Leverages CloudFront’s native device classification headers (`CloudFront-Is-Mobile-Viewer`, `CloudFront-Is-Tablet-Viewer`, and similar) to infer appropriate viewport and DPR values. Provides universal coverage without User-Agent parsing.

1.  **Configurable fallback**: Administrators define default viewport width and DPR values at the policy level, ensuring predictable behavior when all detection methods are unavailable.

All tier evaluation and normalization run inside the CloudFront function, before CloudFront performs its cache lookup. The function normalizes the selected signals into `dit-viewport-width`, `dit-dpr`, and `dit-accept` headers and adds them to the request. The request’s original headers are still forwarded to the origin; only the normalized `dit-*` headers participate in the cache key. Every request receives normalized `dit-*` values regardless of browser, so requests are routed to the correct breakpoint-specific cached variant. Because only the `dit-*` headers are keyed, equivalent devices share a cache entry; for example, a Safari and a Chrome user on the same display normalize to the same breakpoint and resolve to the same cached image. If the function exceeds its compute limit or any tier throws, it fails open: the request passes through with no `dit-*` headers and the image is served without auto-optimization.

 **Playground and extended metrics**

The ECS architecture includes an interactive Playground hosted within the existing Admin UI; it shares the same Amazon S3 bucket, Amazon CloudFront distribution, and Amazon Cognito user pool. Users authenticate through the Admin UI’s existing Cognito login flow before accessing it. The Playground gives you a place to request images from your origins and specify or apply transformations on the fly. It displays the resulting image alongside extended metrics to help you understand the performance of your image transformations.

Extended metrics (pre- and post-optimization dimensions, file sizes, and formats; the resulting size reduction and compression ratio; and a processing-time breakdown covering origin fetch, transformation, and total server time) are gated behind a cryptographically verified Cognito access token. When the Playground issues an image transformation request, it includes the user’s Cognito access token in the `X-DIT-Authorization` header as a Bearer token. The image-processing CloudFront distribution forwards this header to the origin but excludes it from the cache key, so all users share the same cached image variants regardless of authentication status. The ECS container verifies the token using the [aws-jwt-verify](https://github.com/awslabs/aws-jwt-verify) library and returns the metrics through the `x-dit-metrics` response header only on a valid token. If the token is invalid, expired, or absent, the standard image response is returned without metrics; the image request itself is never affected.

Each Playground request includes a cache-bust parameter to bypass CloudFront’s edge cache, ensuring metrics always reflect a fresh transformation from origin.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
