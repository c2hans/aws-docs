---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tstk-custom-transformer.html
---

# Customizing the transformation
<a name="tstk-custom-transformer"></a>

The built-in `analyzed`-to-`text` and `not_analyzed`-to-`keyword` mapping suits most migrations. If you need different behavior — for example, forcing certain fields to `keyword` regardless of their original `index` setting, or applying type changes the built-in transformations do not cover — supply a custom metadata transformer through `metadataTransforms` in your workflow configuration. Raw descriptor configurations can also use `transformerConfig`, `transformerConfigBase64`, or `transformerConfigFile`. Custom transformers compose with the built-in transformations rather than replacing them. For step-by-step instructions on writing and applying a custom field-type transformer, see [Transform field types](transform-field-types.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
