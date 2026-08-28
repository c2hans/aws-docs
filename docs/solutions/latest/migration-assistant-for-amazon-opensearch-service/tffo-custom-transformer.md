---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tffo-custom-transformer.html
---

# Customizing the transformation
<a name="tffo-custom-transformer"></a>

The built-in conversion covers the common case. If you need behavior beyond it — for example, additional property cleanup or a target that does not support `flat_object` — supply a custom JavaScript metadata transformer instead of relying on the built-in. For the steps to author and apply a custom field type transformer through `metadataTransforms`, see [Transform field types](transform-field-types.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
