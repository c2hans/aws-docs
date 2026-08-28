---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution. Dynamic Image Transformation for Amazon CloudFront offers two deployment architectures to meet different performance and cost requirements. The Lambda architecture provides cost-optimized serverless processing for images up to 6 MB. The ECS architecture delivers high-performance processing for images up to 100 MB and includes advanced features like transformation policies, non-S3 origin support, and an administrative interface.

This solution provides two architecture options, each optimized for different use cases and performance requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
