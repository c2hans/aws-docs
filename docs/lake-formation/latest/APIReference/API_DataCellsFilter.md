---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DataCellsFilter.html
---

# DataCellsFilter
<a name="API_DataCellsFilter"></a>

A structure that describes certain columns on certain rows.

## Contents
<a name="API_DataCellsFilter_Contents"></a>

 ** DatabaseName **   <a name="lakeformation-Type-DataCellsFilter-DatabaseName"></a>
A database in the AWS Glue Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Name **   <a name="lakeformation-Type-DataCellsFilter-Name"></a>
The name given by the user to the data filter cell.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** TableCatalogId **   <a name="lakeformation-Type-DataCellsFilter-TableCatalogId"></a>
The ID of the catalog to which the table belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** TableName **   <a name="lakeformation-Type-DataCellsFilter-TableName"></a>
A table in the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** ColumnNames **   <a name="lakeformation-Type-DataCellsFilter-ColumnNames"></a>
A list of column names and/or nested column attributes. When specifying nested attributes, use a qualified dot (.) delimited format such as "address"."zip". Nested attributes within this list may not exceed a depth of 5.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ColumnWildcard **   <a name="lakeformation-Type-DataCellsFilter-ColumnWildcard"></a>
A wildcard with exclusions.
You must specify either a `ColumnNames` list or the `ColumnWildCard`.
Type: [ColumnWildcard](API_ColumnWildcard.md) object
Required: No

 ** RowFilter **   <a name="lakeformation-Type-DataCellsFilter-RowFilter"></a>
A PartiQL predicate.
Type: [RowFilter](API_RowFilter.md) object
Required: No

 ** VersionId **   <a name="lakeformation-Type-DataCellsFilter-VersionId"></a>
The ID of the data cells filter version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_DataCellsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DataCellsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DataCellsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DataCellsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
