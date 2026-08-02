---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportFilterPropertyAttributes.html
---

# ExportFilterPropertyAttributes
<a name="API_ExportFilterPropertyAttributes"></a>

A structure representing a property's attributes. It is a map object of outputType, sourcePropertyName and multiValueHandling.

## Contents
<a name="API_ExportFilterPropertyAttributes_Contents"></a>

 ** multiValueHandling **   <a name="neptunegraph-Type-ExportFilterPropertyAttributes-multiValueHandling"></a>
Specifies how to handle properties that have multiple values. Can be either `TO_LIST` to export all values as a list, or `PICK_FIRST` to export the first value encountered. If not specified, the default value is `PICK_FIRST`.
Type: String
Valid Values: `TO_LIST | PICK_FIRST`
Required: No

 ** outputType **   <a name="neptunegraph-Type-ExportFilterPropertyAttributes-outputType"></a>
Specifies the data type to use for the property in the exported data (e.g. "String", "Int", "Float"). If a type is not provided, the export process will determine the type. If a given property is present as multiple types (e.g. one vertex has "height" stored as a double, and another edge has it stored as a string), the type will be of Any type, otherwise, it will be the type of the property as present in vertices.
Type: String
Pattern: `(Any|Byte|Short|Int|Long|Float|Double|String|Bool|Boolean|Float\[\]|Double\[\])`
Required: No

 ** sourcePropertyName **   <a name="neptunegraph-Type-ExportFilterPropertyAttributes-sourcePropertyName"></a>
The name of the property as it exists in the original graph data. If not provided, it is assumed that the key matches the desired sourcePropertyName.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ExportFilterPropertyAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ExportFilterPropertyAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ExportFilterPropertyAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ExportFilterPropertyAttributes)
