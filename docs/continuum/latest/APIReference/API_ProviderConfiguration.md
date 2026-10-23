---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_ProviderConfiguration.html
---

# ProviderConfiguration
<a name="API_ProviderConfiguration"></a>

The provider Configuration.

## Contents
<a name="API_ProviderConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** github **   <a name="continuum-Type-ProviderConfiguration-github"></a>
Configuration for a GitHub.com integration using the OAuth authorization code flow.
Type: [GitHubConfiguration](API_GitHubConfiguration.md) object
Required: No

 ** s3 **   <a name="continuum-Type-ProviderConfiguration-s3"></a>
Configuration for a customer-managed S3 integration.
Type: [S3Configuration](API_S3Configuration.md) object
Required: No

## See Also
<a name="API_ProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/ProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/ProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/ProviderConfiguration)
