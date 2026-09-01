---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/architecture-options.html
---

# Architecture options
<a name="architecture-options"></a>

This solution offers two distinct deployment architectures to meet different performance and cost requirements:

 **Lambda Architecture**

A cost-optimized serverless architecture suitable for most image transformation workloads. This architecture supports transformed images up to 6 MB in size with a pay-per-request pricing model that eliminates idle costs. It provides automatic scaling with built-in high availability, making it ideal for applications with moderate image processing requirements.

 **ECS Architecture**

A high-performance container-based architecture for demanding workloads. This architecture supports images up to 100 MB in size and includes the solution’s advanced capabilities such as transformation policies, content-aware smart cropping, content moderation, multi-tier device detection, non-S3 origins, and the Admin UI. It offers configurable resource allocation with t-shirt sizing (S, M, L, XL) and is optimized for high-throughput and large image processing.

Both architectures leverage Amazon CloudFront for global content delivery and caching, ensuring optimal performance for end users regardless of their geographic location.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
