---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

 **Automatic image optimization**

Automatically modify images based on users' devices and screen sizes using intelligent optimization capabilities that determine optimal image quality and format based on client viewport size, device pixel ratio, and user agent information.

 **Content moderation**

Use [Amazon Rekognition](https://aws.amazon.com/rekognition/) to automatically detect and blur inappropriate user-uploaded images.

 **Smart cropping**

Use Amazon Rekognition to crop images using facial recognition and intelligent focal point detection.

 **Low-cost image storage**

Save on image storage costs by generating modified images at runtime, and caching generated images in CloudFront.

 **Version V8.0.0 introduces significant enhancements to meet enterprise requirements alongside the core solution capabilities:**

 **Multi-origin support**

Source images from Amazon S3 buckets, external domains, or any HTTP-accessible image source. Configure path-based and host-header mappings to route requests to appropriate origins without modifying application code.

 **Transformation policies**

Create reusable transformation configurations that can be applied consistently across your applications. Policies support conditional logic based on request headers and device characteristics, enabling consistent image processing across your applications.

 **Dual architecture options**

Choose between two deployment architectures based on your specific requirements:
+ Lambda architecture for cost-optimized deployments with images up to 6MB
+ ECS architecture for high-performance deployments supporting images greater than 6MB

 **Management console**

Manage origins, transformation policies, and mappings through a web-based administrative interface, simplifying configuration management.
