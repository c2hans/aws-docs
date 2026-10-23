---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_EnvironmentSourceConfiguration.html
---

# EnvironmentSourceConfiguration
<a name="API_EnvironmentSourceConfiguration"></a>

GA source configuration for code and customer-authored context.

## Contents
<a name="API_EnvironmentSourceConfiguration_Contents"></a>

 ** repositorySources **   <a name="continuum-Type-EnvironmentSourceConfiguration-repositorySources"></a>
The repository Sources.
Type: Array of [EnvironmentRepositorySource](API_EnvironmentRepositorySource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** s3Sources **   <a name="continuum-Type-EnvironmentSourceConfiguration-s3Sources"></a>
The s3 Sources.
Type: Array of [EnvironmentS3IntegrationSource](API_EnvironmentS3IntegrationSource.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_EnvironmentSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/EnvironmentSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/EnvironmentSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/EnvironmentSourceConfiguration)
