---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CspmProviderSummary.html
---

# CspmProviderSummary
<a name="API_CspmProviderSummary"></a>

A summary of the cloud provider configuration for a connector.

## Contents
<a name="API_CspmProviderSummary_Contents"></a>

 ** ConnectorStatus **   <a name="securityhub-Type-CspmProviderSummary-ConnectorStatus"></a>
The connectivity status of the connector.
Type: String
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | UNKNOWN`
Required: No

 ** ProviderConfiguration **   <a name="securityhub-Type-CspmProviderSummary-ProviderConfiguration"></a>
The provider configuration details.
Type: [CspmProviderDetail](API_CspmProviderDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** ProviderName **   <a name="securityhub-Type-CspmProviderSummary-ProviderName"></a>
The name of the cloud provider.
Type: String
Valid Values: `AZURE`
Required: No

## See Also
<a name="API_CspmProviderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CspmProviderSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CspmProviderSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CspmProviderSummary)
