---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_IntegrationFilter.html
---

# IntegrationFilter
<a name="API_IntegrationFilter"></a>

A filter for listing integrations. This is a union type where you can filter by provider or provider type.

## Contents
<a name="API_IntegrationFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** provider **   <a name="securityagent-Type-IntegrationFilter-provider"></a>
Filter integrations by provider.
Type: String
Valid Values: `GITHUB | GITLAB | BITBUCKET | CONFLUENCE`
Required: No

 ** providerType **   <a name="securityagent-Type-IntegrationFilter-providerType"></a>
Filter integrations by provider type.
Type: String
Valid Values: `SOURCE_CODE | DOCUMENTATION`
Required: No

## See Also
<a name="API_IntegrationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/IntegrationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/IntegrationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/IntegrationFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
