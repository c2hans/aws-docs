---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaFunctionMetadata.html
---

# LambdaFunctionMetadata
<a name="API_LambdaFunctionMetadata"></a>

The AWS Lambda function metadata.

## Contents
<a name="API_LambdaFunctionMetadata_Contents"></a>

 ** functionName **   <a name="inspector2-Type-LambdaFunctionMetadata-functionName"></a>
The name of a function.
Type: String
Required: No

 ** functionTags **   <a name="inspector2-Type-LambdaFunctionMetadata-functionTags"></a>
The resource tags on an AWS Lambda function.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** layers **   <a name="inspector2-Type-LambdaFunctionMetadata-layers"></a>
The layers for an AWS Lambda function. A Lambda function can have up to five layers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** runtime **   <a name="inspector2-Type-LambdaFunctionMetadata-runtime"></a>
An AWS Lambda function's runtime.
Type: String
Valid Values: `NODEJS | NODEJS_12_X | NODEJS_14_X | NODEJS_16_X | JAVA_8 | JAVA_8_AL2 | JAVA_11 | PYTHON_3_7 | PYTHON_3_8 | PYTHON_3_9 | UNSUPPORTED | NODEJS_18_X | GO_1_X | JAVA_17 | PYTHON_3_10 | PYTHON_3_11 | DOTNETCORE_3_1 | DOTNET_6 | DOTNET_7 | RUBY_2_7 | RUBY_3_2 | DOTNET_10 | NODEJS_24_X | NODEJS_22_X | JAVA_21 | JAVA_25`
Required: No

## See Also
<a name="API_LambdaFunctionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/LambdaFunctionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/LambdaFunctionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/LambdaFunctionMetadata)
