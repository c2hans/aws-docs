---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SkewedInfo.html
---

# SkewedInfo
<a name="API_SkewedInfo"></a>

Specifies skewed values in a table. Skewed values are those that occur with very high frequency.

## Contents
<a name="API_SkewedInfo_Contents"></a>

 ** SkewedColumnNames **   <a name="Glue-Type-SkewedInfo-SkewedColumnNames"></a>
A list of names of columns that contain skewed values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** SkewedColumnValueLocationMaps **   <a name="Glue-Type-SkewedInfo-SkewedColumnValueLocationMaps"></a>
A mapping of skewed values to the columns that contain them.
Type: String to string map
Required: No

 ** SkewedColumnValues **   <a name="Glue-Type-SkewedInfo-SkewedColumnValues"></a>
A list of values that appear so frequently as to be considered skewed.
Type: Array of strings
Required: No

## See Also
<a name="API_SkewedInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SkewedInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SkewedInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SkewedInfo)
