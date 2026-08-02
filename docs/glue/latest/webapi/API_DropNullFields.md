---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DropNullFields.html
---

# DropNullFields
<a name="API_DropNullFields"></a>

Specifies a transform that removes columns from the dataset if all values in the column are 'null'. By default, AWS Glue Studio will recognize null objects, but some values such as empty strings, strings that are "null", -1 integers or other placeholders such as zeros, are not automatically recognized as nulls.

## Contents
<a name="API_DropNullFields_Contents"></a>

 ** Inputs **   <a name="Glue-Type-DropNullFields-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-DropNullFields-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** NullCheckBoxList **   <a name="Glue-Type-DropNullFields-NullCheckBoxList"></a>
A structure that represents whether certain values are recognized as null values for removal.
Type: [NullCheckBoxList](API_NullCheckBoxList.md) object
Required: No

 ** NullTextList **   <a name="Glue-Type-DropNullFields-NullTextList"></a>
A structure that specifies a list of NullValueField structures that represent a custom null value such as zero or other value being used as a null placeholder unique to the dataset.
The `DropNullFields` transform removes custom null values only if both the value of the null placeholder and the datatype match the data.
Type: Array of [NullValueField](API_NullValueField.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_DropNullFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DropNullFields)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DropNullFields)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DropNullFields)
