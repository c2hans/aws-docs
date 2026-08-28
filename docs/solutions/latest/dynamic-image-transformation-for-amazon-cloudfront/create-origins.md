---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/create-origins.html
---

# Create origins
<a name="create-origins"></a>

Origins define the source locations for your images.

1. In the Admin UI, navigate to the Origins section.

1. Click **Create Origin** and provide:
   +  **Origin Name**: Descriptive name for the origin
   +  **Origin Domain**: Domain name (e.g., `my-bucket.s3.amazonaws.com`)
   +  **Origin Path**: Optional path prefix (e.g., `/images`)
   +  **Origin Headers**: Optional custom headers

1. Click **Save** to create the origin.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
