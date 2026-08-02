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
