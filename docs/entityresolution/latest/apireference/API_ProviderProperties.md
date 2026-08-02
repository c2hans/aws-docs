---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderProperties.html
---

# ProviderProperties
<a name="API_ProviderProperties"></a>

An object containing the `providerServiceARN`, `intermediateSourceConfiguration`, and `providerConfiguration`.

## Contents
<a name="API_ProviderProperties_Contents"></a>

 ** providerServiceArn **   <a name="API-Type-ProviderProperties-providerServiceArn"></a>
The ARN of the provider service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})`
Required: Yes

 ** intermediateSourceConfiguration **   <a name="API-Type-ProviderProperties-intermediateSourceConfiguration"></a>
The Amazon S3 location that temporarily stores your data while it processes. Your information won't be saved permanently.
Type: [IntermediateSourceConfiguration](API_IntermediateSourceConfiguration.md) object
Required: No

 ** providerConfiguration **   <a name="API-Type-ProviderProperties-providerConfiguration"></a>
The required configuration fields to use with the provider service.
Type: JSON value
Required: No

## See Also
<a name="API_ProviderProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ProviderProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ProviderProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ProviderProperties)
