---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_IntegrationSummary.html
---

# IntegrationSummary
<a name="API_connect-outbound-campaigns-v2_IntegrationSummary"></a>

The summary of integration.

## Contents
<a name="API_connect-outbound-campaigns-v2_IntegrationSummary_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customerProfiles **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationSummary-customerProfiles"></a>
The summary of the integration with Customer Profiles.
Type: [CustomerProfilesIntegrationSummary](API_connect-outbound-campaigns-v2_CustomerProfilesIntegrationSummary.md) object
Required: No

 ** lambda **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationSummary-lambda"></a>
The summary of the integration with Lambda.
Type: [LambdaIntegrationSummary](API_connect-outbound-campaigns-v2_LambdaIntegrationSummary.md) object
Required: No

 ** qConnect **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationSummary-qConnect"></a>
The summary of integration with Amazon Q in Connect.
Type: [QConnectIntegrationSummary](API_connect-outbound-campaigns-v2_QConnectIntegrationSummary.md) object
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_IntegrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/IntegrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/IntegrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/IntegrationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
