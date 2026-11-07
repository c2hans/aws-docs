---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BetweenConfiguration.html
---

# BetweenConfiguration
<a name="API_BetweenConfiguration"></a>

Configuration that defines how BETWEEN range filter operations are translated into REST API request parameters.

## Contents
<a name="API_BetweenConfiguration_Contents"></a>

 ** HighBoundKey **   <a name="Glue-Type-BetweenConfiguration-HighBoundKey"></a>
The parameter name used for the upper bound value in a BETWEEN filter operation.
Type: String
Required: No

 ** LowBoundKey **   <a name="Glue-Type-BetweenConfiguration-LowBoundKey"></a>
The parameter name used for the lower bound value in a BETWEEN filter operation.
Type: String
Required: No

 ** Template **   <a name="Glue-Type-BetweenConfiguration-Template"></a>
A template string for constructing the BETWEEN filter expression.
Type: String
Required: No

## See Also
<a name="API_BetweenConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BetweenConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BetweenConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BetweenConfiguration)
