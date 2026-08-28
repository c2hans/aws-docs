---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/transform-field-types.html
---

# Transform field types
<a name="transform-field-types"></a>

When you migrate metadata to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, the Metadata Migration phase rewrites index settings, mappings, templates, and aliases into a shape the target can accept. As part of this, it applies built-in field-type transformations that resolve version-specific field types that are deprecated or unsupported on newer engines. Most migrations are fully served by these built-in transformations, so start there and only add a custom transformer if a pilot run shows a field type the built-ins do not cover.

This page summarizes the built-in transformations, shows how to supply a custom JavaScript field-type transformer when the built-ins are not enough, recommends a sequence for introducing custom logic safely, and shows how to validate the transformed metadata on the target. Field-type transformation is part of the broader metadata migration phase — see [Migrate metadata](migrate-metadata.md) for how the phase fits into the overall workflow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
