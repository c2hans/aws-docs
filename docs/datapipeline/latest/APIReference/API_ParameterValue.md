---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ParameterValue.html
---

# ParameterValue
<a name="API_ParameterValue"></a>

A value or list of parameter values.

## Contents
<a name="API_ParameterValue_Contents"></a>

 ** id **   <a name="DP-Type-ParameterValue-id"></a>
The ID of the parameter value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** stringValue **   <a name="DP-Type-ParameterValue-stringValue"></a>
The field value, expressed as a String.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

## See Also
<a name="API_ParameterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/ParameterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/ParameterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/ParameterValue)
