---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SplitFields.html
---

# SplitFields
<a name="API_SplitFields"></a>

Specifies a transform that splits data property keys into two `DynamicFrames`. The output is a collection of `DynamicFrames`: one with selected data property keys, and one with the remaining data property keys.

## Contents
<a name="API_SplitFields_Contents"></a>

 ** Inputs **   <a name="Glue-Type-SplitFields-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-SplitFields-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Paths **   <a name="Glue-Type-SplitFields-Paths"></a>
A JSON path to a variable in the data structure.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

## See Also
<a name="API_SplitFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SplitFields)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SplitFields)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SplitFields)
