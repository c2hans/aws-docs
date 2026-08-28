---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/create-mappings.html
---

# Create mappings
<a name="create-mappings"></a>

Mappings connect URL patterns to specific origins and transformation policies.

1. In the Admin UI, navigate to the Mappings section.

1. Click **Create Mapping** and provide:
   +  **Mapping Name**: Descriptive name for the mapping
   +  **Mapping Type**: Choose `PATH_MAPPING` or `HOST_HEADER_MAPPING`
   +  **Pattern**: URL pattern (e.g., `/mobile/*` or `example.com`)
   +  **Origin**: Select the origin created earlier
   +  **Policy**: Select the transformation policy (optional)
   +  **Priority**: Numeric priority for mapping evaluation

1. Click **Save** to create the mapping.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
