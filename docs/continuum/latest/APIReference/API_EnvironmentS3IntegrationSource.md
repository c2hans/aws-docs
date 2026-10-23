---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_EnvironmentS3IntegrationSource.html
---

# EnvironmentS3IntegrationSource
<a name="API_EnvironmentS3IntegrationSource"></a>

An S3 source for one environment, backed by a previously-created S3 integration.

## Contents
<a name="API_EnvironmentS3IntegrationSource_Contents"></a>

 ** integrationId **   <a name="continuum-Type-EnvironmentS3IntegrationSource-integrationId"></a>
The identifier of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** codePrefix **   <a name="continuum-Type-EnvironmentS3IntegrationSource-codePrefix"></a>
The code Prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*/`
Required: No

 ** contextPrefix **   <a name="continuum-Type-EnvironmentS3IntegrationSource-contextPrefix"></a>
The context Prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*/`
Required: No

## See Also
<a name="API_EnvironmentS3IntegrationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/EnvironmentS3IntegrationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/EnvironmentS3IntegrationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/EnvironmentS3IntegrationSource)
