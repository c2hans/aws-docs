---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_IntegrationSummary.html
---

# IntegrationSummary
<a name="API_IntegrationSummary"></a>

A summary of an integration returned in list responses.

## Contents
<a name="API_IntegrationSummary_Contents"></a>

 ** createdAt **   <a name="continuum-Type-IntegrationSummary-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** integrationArn **   <a name="continuum-Type-IntegrationSummary-integrationArn"></a>
The Amazon Resource Name (ARN) of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:integrations/[a-z0-9]+`
Required: Yes

 ** integrationId **   <a name="continuum-Type-IntegrationSummary-integrationId"></a>
The identifier of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** integrationType **   <a name="continuum-Type-IntegrationSummary-integrationType"></a>
The integration Type.
Type: String
Valid Values: `GITHUB | S3`
Required: Yes

 ** name **   <a name="continuum-Type-IntegrationSummary-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** providerDetails **   <a name="continuum-Type-IntegrationSummary-providerDetails"></a>
Provider-specific details for an integration. Only one member will be present.
Type: [ProviderDetails](API_ProviderDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** updatedAt **   <a name="continuum-Type-IntegrationSummary-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_IntegrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/IntegrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/IntegrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/IntegrationSummary)
