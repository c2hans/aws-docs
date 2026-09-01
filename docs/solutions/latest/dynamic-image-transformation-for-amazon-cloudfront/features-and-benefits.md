---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

This solution deploys as either a Lambda architecture or an ECS architecture. The ECS architecture is the latest option and includes the solution’s full feature set; the Lambda architecture is a cost-optimized option that supports a focused subset. Each feature below notes where it is available. For a comparison of the two options, see [Architecture options](architecture-options.md).

 **On-demand image transformation**

 *Available in: Lambda and ECS architectures.*

Generate transformed images at request time and cache the results at the CloudFront edge, so you don’t pre-generate or store multiple variants of every image, which also lowers storage costs.

 **Automatic image optimization**

 *Available in: Lambda and ECS architectures. Device- and screen-aware sizing (multi-tier device detection) is available in the ECS architecture only.*

Automatically deliver an optimized image format and quality for each request, reducing load times without sacrificing visual quality. In the ECS architecture, the solution additionally sizes images to each user’s device and screen through multi-tier device detection. This detection works across all browsers: it uses the most precise signals when a browser provides them (through Client Hints) and falls back to CloudFront device classification otherwise, so every request is optimized regardless of browser. For details, see [ECS architecture features](ecs-architecture-features.md).

 **Content moderation**

 *Available in: Lambda and ECS architectures.*

Use [Amazon Rekognition](https://aws.amazon.com/rekognition/) to automatically detect and blur inappropriate user-uploaded images.

 **Smart cropping**

 *Available in: Lambda and ECS architectures. Content-aware detection is available in the ECS architecture only.*

Use [Amazon Rekognition](https://aws.amazon.com/rekognition/) to automatically crop images around their most important content while keeping a consistent aspect ratio. The Lambda architecture crops around detected faces. The ECS architecture adds content-aware cropping that recognizes a broader range of content, including objects, text, and logos.

 **Interactive Playground**

 *Available in: Lambda and ECS architectures. The Playground and its extended metrics are available in the ECS architecture only.*

Try transformations and preview their results before you use them in production. The Lambda architecture offers an optional standalone Demo UI for exercising basic transformations against images in your Amazon S3 buckets. The ECS architecture offers the Playground, an authenticated experience hosted within the Admin UI that adds extended metrics (such as pre- and post-optimization dimensions, file sizes, compression ratio, and processing time) so you can measure the impact of each transformation.

 **Multi-origin support**

 *Available in: Lambda and ECS architectures. Non-S3 origins and host-header mappings are available in the ECS architecture only.*

Source images from Amazon S3 in either architecture. In the ECS architecture, you can also source images from external domains or any HTTP-accessible image source, and configure path-based and host-header mappings to route requests to the appropriate origin without modifying application code.

 **Transformation policies**

 *Available in: ECS architecture only.*

Create reusable transformation configurations that can be applied consistently across your applications. Policies support conditional logic based on request headers and device characteristics, enabling consistent image processing across your applications.

 **Management console**

 *Available in: ECS architecture only.*

Manage origins, transformation policies, and mappings through a web-based administrative interface, simplifying configuration management.

**Note**
The ECS architecture is the latest option and includes the solution’s full feature set, including the Admin UI, transformation policies, non-S3 origins, content-aware smart cropping, and multi-tier device detection. For a detailed description of the ECS-only capabilities, see [ECS architecture features](ecs-architecture-features.md). To compare the two deployment options, see [Architecture options](architecture-options.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
