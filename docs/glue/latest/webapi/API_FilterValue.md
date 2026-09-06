---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FilterValue.html
---

# FilterValue
<a name="API_FilterValue"></a>

Represents a single entry in the list of values for a `FilterExpression`.

## Contents
<a name="API_FilterValue_Contents"></a>

 ** Type **   <a name="Glue-Type-FilterValue-Type"></a>
The type of filter value.
Type: String
Valid Values: `COLUMNEXTRACTED | CONSTANT`
Required: Yes

 ** Value **   <a name="Glue-Type-FilterValue-Value"></a>
The value to be associated.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

## See Also
<a name="API_FilterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FilterValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FilterValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FilterValue)
