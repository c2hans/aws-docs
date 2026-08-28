---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/provider-integration.html
---

# Integrate with AWS Entity Resolution as a provider
<a name="provider-integration"></a>

AWS Entity Resolution third-party provider integrations help customers protect consumer privacy and maintain compliance with data sovereignty laws. Third-party providers, such as LiveRamp and TransUnion, translate consumer identifiers into advertising IDs, such as Ramp IDs and Fabrick IDs. These advertising identifiers are commonly used in advertising and marketing tools, to prevent consumer data from being exported to non-AWS managed systems. This section provides guidance for providers to integrate with AWS Entity Resolution to encode or transcode consumer identifiers into advertising IDs for use in a [provider service-based matching workflow](create-matching-workflow-provider.md).

For more information about the provider services that are currently integrated with AWS Entity Resolution, see [Creating a provider service-based matching workflow](create-matching-workflow-provider.md).

**Topics**
+ [Requirements](requirements.md)
+ [Using the AWS Entity Resolution OpenAPI specification](entity-resolution-open-api.md)
+ [Testing a provider integration](testing-provider-integration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
