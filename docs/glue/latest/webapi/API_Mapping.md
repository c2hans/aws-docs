---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Mapping.html
---

# Mapping
<a name="API_Mapping"></a>

Specifies the mapping of data property keys.

## Contents
<a name="API_Mapping_Contents"></a>

 ** Children **   <a name="Glue-Type-Mapping-Children"></a>
Only applicable to nested data structures. If you want to change the parent structure, but also one of its children, you can fill out this data strucutre. It is also `Mapping`, but its `FromPath` will be the parent's `FromPath` plus the `FromPath` from this structure.
For the children part, suppose you have the structure:
 `{ "FromPath": "OuterStructure", "ToKey": "OuterStructure", "ToType": "Struct", "Dropped": false, "Chidlren": [{ "FromPath": "inner", "ToKey": "inner", "ToType": "Double", "Dropped": false, }] }`
You can specify a `Mapping` that looks like:
 `{ "FromPath": "OuterStructure", "ToKey": "OuterStructure", "ToType": "Struct", "Dropped": false, "Chidlren": [{ "FromPath": "inner", "ToKey": "inner", "ToType": "Double", "Dropped": false, }] }`
Type: Array of [Mapping](#API_Mapping) objects
Required: No

 ** Dropped **   <a name="Glue-Type-Mapping-Dropped"></a>
If true, then the column is removed.
Type: Boolean
Required: No

 ** FromPath **   <a name="Glue-Type-Mapping-FromPath"></a>
The table or column to be modified.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** FromType **   <a name="Glue-Type-Mapping-FromType"></a>
The type of the data to be modified.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** ToKey **   <a name="Glue-Type-Mapping-ToKey"></a>
After the apply mapping, what the name of the column should be. Can be the same as `FromPath`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** ToType **   <a name="Glue-Type-Mapping-ToType"></a>
The data type that the data is to be modified to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_Mapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Mapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Mapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Mapping)
