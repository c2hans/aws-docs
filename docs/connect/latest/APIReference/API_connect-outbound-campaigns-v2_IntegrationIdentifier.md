---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_IntegrationIdentifier.html
---

# IntegrationIdentifier
<a name="API_connect-outbound-campaigns-v2_IntegrationIdentifier"></a>

The identifier for the integration.

## Contents
<a name="API_connect-outbound-campaigns-v2_IntegrationIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customerProfiles **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationIdentifier-customerProfiles"></a>
The identifier for the integration with Customer Profiles.
Type: [CustomerProfilesIntegrationIdentifier](API_connect-outbound-campaigns-v2_CustomerProfilesIntegrationIdentifier.md) object
Required: No

 ** lambda **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationIdentifier-lambda"></a>
The identifier for the integration with Lambda.
Type: [LambdaIntegrationIdentifier](API_connect-outbound-campaigns-v2_LambdaIntegrationIdentifier.md) object
Required: No

 ** qConnect **   <a name="connect-Type-connect-outbound-campaigns-v2_IntegrationIdentifier-qConnect"></a>
The identifier for the integration with Amazon Q in Connect.
Type: [QConnectIntegrationIdentifier](API_connect-outbound-campaigns-v2_QConnectIntegrationIdentifier.md) object
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_IntegrationIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/IntegrationIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/IntegrationIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/IntegrationIdentifier)
