---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_TableWithColumnsResource.html
---

# TableWithColumnsResource
<a name="API_TableWithColumnsResource"></a>

A structure for a table with columns object. This object is only used when granting a SELECT permission.

This object must take a value for at least one of `ColumnsNames`, `ColumnsIndexes`, or `ColumnsWildcard`.

## Contents
<a name="API_TableWithColumnsResource_Contents"></a>

 ** DatabaseName **   <a name="lakeformation-Type-TableWithColumnsResource-DatabaseName"></a>
The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Name **   <a name="lakeformation-Type-TableWithColumnsResource-Name"></a>
The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CatalogId **   <a name="lakeformation-Type-TableWithColumnsResource-CatalogId"></a>
The identifier for the Data Catalog. By default, it is the account ID of the caller.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ColumnNames **   <a name="lakeformation-Type-TableWithColumnsResource-ColumnNames"></a>
The list of column names for the table. At least one of `ColumnNames` or `ColumnWildcard` is required.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ColumnWildcard **   <a name="lakeformation-Type-TableWithColumnsResource-ColumnWildcard"></a>
A wildcard specified by a `ColumnWildcard` object. At least one of `ColumnNames` or `ColumnWildcard` is required.
Type: [ColumnWildcard](API_ColumnWildcard.md) object
Required: No

## See Also
<a name="API_TableWithColumnsResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/TableWithColumnsResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/TableWithColumnsResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/TableWithColumnsResource)
