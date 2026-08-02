---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_NamespaceProviderProperties.html
---

# NamespaceProviderProperties
<a name="API_NamespaceProviderProperties"></a>

An object containing `providerConfiguration` and `providerServiceArn`.

## Contents
<a name="API_NamespaceProviderProperties_Contents"></a>

 ** providerServiceArn **   <a name="API-Type-NamespaceProviderProperties-providerServiceArn"></a>
The Amazon Resource Name (ARN) of the provider service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})`
Required: Yes

 ** providerConfiguration **   <a name="API-Type-NamespaceProviderProperties-providerConfiguration"></a>
An object which defines any additional configurations required by the provider service.
Type: JSON value
Required: No

## See Also
<a name="API_NamespaceProviderProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/NamespaceProviderProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/NamespaceProviderProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/NamespaceProviderProperties)
