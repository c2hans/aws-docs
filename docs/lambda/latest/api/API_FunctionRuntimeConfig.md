---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_FunctionRuntimeConfig.html
---

# FunctionRuntimeConfig

The customer-managed runtime configuration for your function. Specifies the customer-managed runtime and the runtime alias that your function uses.

## Contents
<a name="API_FunctionRuntimeConfig_Contents"></a>

 ** RuntimeAlias **   <a name="lambda-Type-FunctionRuntimeConfig-RuntimeAlias"></a>
The name of the customer-managed runtime alias that your function uses. A runtime alias is a name that points to a runtime version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** RuntimeArn **   <a name="lambda-Type-FunctionRuntimeConfig-RuntimeArn"></a>
The Amazon Resource Name (ARN) of the customer-managed runtime that your function uses.
Type: String
Length Constraints: Minimum length of 48. Maximum length of 2048.
Pattern: `arn:[a-z-]+:lambda:[a-z0-9-]+:\d{12}:runtime/.+`
Required: Yes

## See Also
<a name="API_FunctionRuntimeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/FunctionRuntimeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/FunctionRuntimeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/FunctionRuntimeConfig)
