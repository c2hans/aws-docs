---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ColumnSchema.html
---

# ColumnSchema
<a name="API_ColumnSchema"></a>

Metadata for a column.

## Contents
<a name="API_ColumnSchema_Contents"></a>

 ** columnName **   <a name="API-Type-ColumnSchema-columnName"></a>
The name of a column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** columnTypes **   <a name="API-Type-ColumnSchema-columnTypes"></a>
The data type of column.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `USER_ID | ITEM_ID | TIMESTAMP | CATEGORICAL_FEATURE | NUMERICAL_FEATURE`
Required: Yes

## See Also
<a name="API_ColumnSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ColumnSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ColumnSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ColumnSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
