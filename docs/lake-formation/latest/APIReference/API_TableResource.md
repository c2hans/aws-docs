---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_TableResource.html
---

# TableResource
<a name="API_TableResource"></a>

A structure for the table object. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

## Contents
<a name="API_TableResource_Contents"></a>

 ** DatabaseName **   <a name="lakeformation-Type-TableResource-DatabaseName"></a>
The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CatalogId **   <a name="lakeformation-Type-TableResource-CatalogId"></a>
The identifier for the Data Catalog. By default, it is the account ID of the caller.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Name **   <a name="lakeformation-Type-TableResource-Name"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** TableWildcard **   <a name="lakeformation-Type-TableResource-TableWildcard"></a>
A wildcard object representing every table under a database.
At least one of `TableResource$Name` or `TableResource$TableWildcard` is required.
Type: [TableWildcard](API_TableWildcard.md) object
Required: No

## See Also
<a name="API_TableResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/TableResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/TableResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/TableResource)
