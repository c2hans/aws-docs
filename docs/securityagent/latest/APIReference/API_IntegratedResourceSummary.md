---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_IntegratedResourceSummary.html
---

# IntegratedResourceSummary
<a name="API_IntegratedResourceSummary"></a>

Contains summary information about an integrated resource.

## Contents
<a name="API_IntegratedResourceSummary_Contents"></a>

 ** integrationId **   <a name="securityagent-Type-IntegratedResourceSummary-integrationId"></a>
The unique identifier of the integration that provides access to the resource.
Type: String
Required: Yes

 ** resource **   <a name="securityagent-Type-IntegratedResourceSummary-resource"></a>
The metadata for the integrated resource.
Type: [IntegratedResourceMetadata](API_IntegratedResourceMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** capabilities **   <a name="securityagent-Type-IntegratedResourceSummary-capabilities"></a>
The capabilities enabled for the integrated resource.
Type: [ProviderResourceCapabilities](API_ProviderResourceCapabilities.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_IntegratedResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/IntegratedResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/IntegratedResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/IntegratedResourceSummary)
