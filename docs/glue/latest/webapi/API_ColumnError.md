---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ColumnError.html
---

# ColumnError
<a name="API_ColumnError"></a>

Encapsulates a column name that failed and the reason for failure.

## Contents
<a name="API_ColumnError_Contents"></a>

 ** ColumnName **   <a name="Glue-Type-ColumnError-ColumnName"></a>
The name of the column that failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Error **   <a name="Glue-Type-ColumnError-Error"></a>
An error message with the reason for the failure of an operation.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

## See Also
<a name="API_ColumnError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ColumnError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ColumnError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ColumnError)
