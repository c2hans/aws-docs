---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FillMissingValues.html
---

# FillMissingValues
<a name="API_FillMissingValues"></a>

Specifies a transform that locates records in the dataset that have missing values and adds a new field with a value determined by imputation. The input data set is used to train the machine learning model that determines what the missing value should be.

## Contents
<a name="API_FillMissingValues_Contents"></a>

 ** ImputedPath **   <a name="Glue-Type-FillMissingValues-ImputedPath"></a>
A JSON path to a variable in the data structure for the dataset that is imputed.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-FillMissingValues-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-FillMissingValues-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** FilledPath **   <a name="Glue-Type-FillMissingValues-FilledPath"></a>
A JSON path to a variable in the data structure for the dataset that is filled.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_FillMissingValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FillMissingValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FillMissingValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FillMissingValues)
