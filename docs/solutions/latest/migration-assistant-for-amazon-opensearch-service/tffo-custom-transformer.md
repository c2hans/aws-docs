---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tffo-custom-transformer.html
---

# Customizing the transformation
<a name="tffo-custom-transformer"></a>

The built-in conversion covers the common case. If you need behavior beyond it — for example, additional property cleanup or a target that does not support `flat_object` — supply a custom JavaScript metadata transformer instead of relying on the built-in. For the steps to author and apply a custom field type transformer through `metadataTransforms`, see [Transform field types](transform-field-types.md).
