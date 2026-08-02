---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_NullValueField.html
---

# NullValueField
<a name="API_NullValueField"></a>

Represents a custom null value such as a zeros or other value being used as a null placeholder unique to the dataset.

## Contents
<a name="API_NullValueField_Contents"></a>

 ** Datatype **   <a name="Glue-Type-NullValueField-Datatype"></a>
The datatype of the value.
Type: [Datatype](API_Datatype.md) object
Required: Yes

 ** Value **   <a name="Glue-Type-NullValueField-Value"></a>
The value of the null placeholder.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

## See Also
<a name="API_NullValueField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/NullValueField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/NullValueField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/NullValueField)
