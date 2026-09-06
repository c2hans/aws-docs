---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableError.html
---

# TableError
<a name="API_TableError"></a>

An error record for table operations.

## Contents
<a name="API_TableError_Contents"></a>

 ** ErrorDetail **   <a name="Glue-Type-TableError-ErrorDetail"></a>
The details about the error.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** TableName **   <a name="Glue-Type-TableError-TableName"></a>
The name of the table. For Hive compatibility, this must be entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_TableError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableError)
