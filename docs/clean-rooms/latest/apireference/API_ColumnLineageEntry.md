---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ColumnLineageEntry.html
---

# ColumnLineageEntry
<a name="API_ColumnLineageEntry"></a>

Contains column lineage information that traces a disallowed output column back to its source in a base table.

## Contents
<a name="API_ColumnLineageEntry_Contents"></a>

 ** column **   <a name="API-Type-ColumnLineageEntry-column"></a>
The name of the column in the intermediate table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** sourceAccountId **   <a name="API-Type-ColumnLineageEntry-sourceAccountId"></a>
The AWS account ID of the owner of the source table.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** sourceColumn **   <a name="API-Type-ColumnLineageEntry-sourceColumn"></a>
The name of the column in the source table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** sourceId **   <a name="API-Type-ColumnLineageEntry-sourceId"></a>
The unique identifier of the source table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** sourceName **   <a name="API-Type-ColumnLineageEntry-sourceName"></a>
The name of the source table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** sourceType **   <a name="API-Type-ColumnLineageEntry-sourceType"></a>
The type of the source table.
Type: String
Valid Values: `TABLE | INTERMEDIATE_TABLE | ID_MAPPING_TABLE`
Required: Yes

## See Also
<a name="API_ColumnLineageEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ColumnLineageEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ColumnLineageEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ColumnLineageEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
