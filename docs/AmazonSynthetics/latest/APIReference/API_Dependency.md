---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Dependency.html
---

# Dependency
<a name="API_Dependency"></a>

A structure that contains information about a dependency for a canary.

## Contents
<a name="API_Dependency_Contents"></a>

 ** Reference **   <a name="synthetics-Type-Dependency-Reference"></a>
The dependency reference. For Lambda layers, this is the ARN of the Lambda layer. For more information about Lambda ARN format, see [Lambda](https://docs.aws.amazon.com/lambda/latest/api/API_Layer.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Type **   <a name="synthetics-Type-Dependency-Type"></a>
The type of dependency. Valid value is `LambdaLayer`.
Type: String
Valid Values: `LambdaLayer`
Required: No

## See Also
<a name="API_Dependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/Dependency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/Dependency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/Dependency)
