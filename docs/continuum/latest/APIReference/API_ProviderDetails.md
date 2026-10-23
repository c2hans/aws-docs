---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_ProviderDetails.html
---

# ProviderDetails
<a name="API_ProviderDetails"></a>

Provider-specific details for an integration. Only one member will be present.

## Contents
<a name="API_ProviderDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** github **   <a name="continuum-Type-ProviderDetails-github"></a>
Details for a GitHub.com integration.
Type: [GitHubDetails](API_GitHubDetails.md) object
Required: No

 ** s3 **   <a name="continuum-Type-ProviderDetails-s3"></a>
Public details for a customer-managed S3 integration. The sensitive external ID is intentionally omitted.
Type: [S3Details](API_S3Details.md) object
Required: No

## See Also
<a name="API_ProviderDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/ProviderDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/ProviderDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/ProviderDetails)
