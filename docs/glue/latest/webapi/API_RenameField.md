---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RenameField.html
---

# RenameField
<a name="API_RenameField"></a>

Specifies a transform that renames a single data property key.

## Contents
<a name="API_RenameField_Contents"></a>

 ** Inputs **   <a name="Glue-Type-RenameField-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-RenameField-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** SourcePath **   <a name="Glue-Type-RenameField-SourcePath"></a>
A JSON path to a variable in the data structure for the source data.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** TargetPath **   <a name="Glue-Type-RenameField-TargetPath"></a>
A JSON path to a variable in the data structure for the target data.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

## See Also
<a name="API_RenameField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RenameField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RenameField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RenameField)
