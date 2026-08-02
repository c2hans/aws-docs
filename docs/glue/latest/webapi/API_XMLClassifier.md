---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_XMLClassifier.html
---

# XMLClassifier
<a name="API_XMLClassifier"></a>

A classifier for `XML` content.

## Contents
<a name="API_XMLClassifier_Contents"></a>

 ** Classification **   <a name="Glue-Type-XMLClassifier-Classification"></a>
An identifier of the data format that the classifier matches.
Type: String
Required: Yes

 ** Name **   <a name="Glue-Type-XMLClassifier-Name"></a>
The name of the classifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CreationTime **   <a name="Glue-Type-XMLClassifier-CreationTime"></a>
The time that this classifier was registered.
Type: Timestamp
Required: No

 ** LastUpdated **   <a name="Glue-Type-XMLClassifier-LastUpdated"></a>
The time that this classifier was last updated.
Type: Timestamp
Required: No

 ** RowTag **   <a name="Glue-Type-XMLClassifier-RowTag"></a>
The XML tag designating the element that contains each record in an XML document being parsed. This can't identify a self-closing element (closed by `/>`). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A" item_b="B" />` is not).
Type: String
Required: No

 ** Version **   <a name="Glue-Type-XMLClassifier-Version"></a>
The version of this classifier.
Type: Long
Required: No

## See Also
<a name="API_XMLClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/XMLClassifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/XMLClassifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/XMLClassifier)
