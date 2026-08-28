---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_IntegrationConfig.html
---

# IntegrationConfig
<a name="API_connect-outbound-campaigns-v2_IntegrationConfig"></a>

Contains the integration configuration with an Connect Customer instance.

## Contents
<a name="API_connect-outbound-campaigns-v2_IntegrationConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customerProfiles **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationConfig-customerProfiles"></a>
The integration configuration to integrate Customer Profiles with an Connect Customer instance.
Type: [CustomerProfilesIntegrationConfig](API_connect-outbound-campaigns-v2_CustomerProfilesIntegrationConfig.md) object
Required: No

 ** lambda **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationConfig-lambda"></a>
The integration configuration to integrate Lambda with an Connect Customer instance.
Type: [LambdaIntegrationConfig](API_connect-outbound-campaigns-v2_LambdaIntegrationConfig.md) object
Required: No

 ** qConnect **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationConfig-qConnect"></a>
The integration configuration to integrate Amazon Q in Connect with an Connect Customer instance.
Type: [QConnectIntegrationConfig](API_connect-outbound-campaigns-v2_QConnectIntegrationConfig.md) object
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_IntegrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/IntegrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/IntegrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/IntegrationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
