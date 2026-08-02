---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RepositoryAuthConfig.html
---

# RepositoryAuthConfig
<a name="API_RepositoryAuthConfig"></a>

Specifies an authentication configuration for the private docker registry where your model image is hosted. Specify a value for this property only if you specified `Vpc` as the value for the `RepositoryAccessMode` field of the `ImageConfig` object that you passed to a call to `CreateModel` and the private Docker registry where the model image is hosted requires authentication.

## Contents
<a name="API_RepositoryAuthConfig_Contents"></a>

 ** RepositoryCredentialsProviderArn **   <a name="sagemaker-Type-RepositoryAuthConfig-RepositoryCredentialsProviderArn"></a>
The Amazon Resource Name (ARN) of an AWS Lambda function that provides credentials to authenticate to the private Docker registry where your model image is hosted. For information about how to create an AWS Lambda function, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) in the * AWS Lambda Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_RepositoryAuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RepositoryAuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RepositoryAuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RepositoryAuthConfig)
