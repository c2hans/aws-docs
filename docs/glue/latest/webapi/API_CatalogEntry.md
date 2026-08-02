---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogEntry.html
---

# CatalogEntry
<a name="API_CatalogEntry"></a>

Specifies a table definition in the AWS Glue Data Catalog.

## Contents
<a name="API_CatalogEntry_Contents"></a>

 ** DatabaseName **   <a name="Glue-Type-CatalogEntry-DatabaseName"></a>
The database in which the table metadata resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** TableName **   <a name="Glue-Type-CatalogEntry-TableName"></a>
The name of the table in question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## See Also
<a name="API_CatalogEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogEntry)
