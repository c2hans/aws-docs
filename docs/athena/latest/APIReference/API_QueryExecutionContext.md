---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_QueryExecutionContext.html
---

# QueryExecutionContext
<a name="API_QueryExecutionContext"></a>

The database and data catalog context in which the query execution occurs.

## Contents
<a name="API_QueryExecutionContext_Contents"></a>

 ** Catalog **   <a name="athena-Type-QueryExecutionContext-Catalog"></a>
The name of the data catalog used in the query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Database **   <a name="athena-Type-QueryExecutionContext-Database"></a>
The name of the database used in the query execution. The database must exist in the catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_QueryExecutionContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/QueryExecutionContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/QueryExecutionContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/QueryExecutionContext)
