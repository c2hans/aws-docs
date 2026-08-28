---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/key-concepts.html
---

# Key concepts
<a name="key-concepts"></a>

## Origins
<a name="origins"></a>

An origin defines the source location where original images are stored. The solution supports two types of origins:

 **Amazon S3 origins** - S3 buckets containing your original images - Configured with valid S3 endpoint URL and optional path prefix - Supports all S3 features including versioning and encryption

 **External origins** - HTTP-accessible domains hosting images - Content management systems, CDNs, or web servers - Must use HTTPS with valid SSL certificates from trusted certificate authorities - Self-signed certificates are not supported

Origins are configured with the following properties:
+  **Origin name**: A descriptive identifier for management purposes
+  **Origin domain**: A valid S3 endpoint URL or external domain (e.g., `images.example.com`)
+  **Origin path** (optional): A path prefix appended to all requests (e.g., `/assets/images`)
+  **Origin headers** (optional): Custom headers sent with each origin request for authentication or routing

## Transformation policies
<a name="transformation-policies"></a>

Transformation policies are reusable configurations that define sets of image transformations, output settings, and conditional logic. They enable consistent image processing across applications without requiring transformation parameters in each request.

 **Policy structure:**
+  **Transformations**: Array of image operations (resize, crop, format conversion, etc.) with optional conditional logic based on request headers
+  **Output settings**: Quality, format, and optimization configurations
+  **Default policy**: Only one policy can be designated as default (applied when no specific policy is requested)

 **Example policy capabilities:**
+ Automatic format selection (WebP for supported browsers, JPEG for others)
+ Quality optimization based on device pixel ratio

 **Policy application precedence:**

1. Explicit transformations in request query parameters (highest)

1. Named policy specified in request

1. Policy configured in the mapping

1. Default policy (lowest)

## Mappings
<a name="mappings"></a>

Mappings define how incoming image requests are routed to specific origins. The solution supports two types of mappings with different precedence rules:

 **Host-header mappings** (highest precedence)
+ Route requests based on the `Host` header in the incoming request
+ Support exact matches (`images.mysite.com`) and wildcard patterns (`*.mysite.com`)
+ Useful for multi-tenant applications or domain-based routing
+ Example: `images.customer1.com` → Customer 1’s S3 bucket

 **Path-based mappings** (lower precedence)
+ Route requests based on URL path patterns
+ Support exact paths (`/thumbnails`) and wildcard patterns (`/customer-123/*`)
+ Enable content-based routing within a single domain
+ Example: `/product-images/*` → Product catalog origin

 **Mapping precedence rules:**

1. Host-header mappings are evaluated first

1. If no host-header mapping matches, path-based mappings are evaluated

1. Most specific pattern takes precedence over wildcards

1. If no mapping matches, the request returns a 404 error

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
