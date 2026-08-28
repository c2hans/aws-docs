---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ViewDefinition.html
---

# ViewDefinition
<a name="API_ViewDefinition"></a>

A structure containing details for representations.

## Contents
<a name="API_ViewDefinition_Contents"></a>

 ** Definer **   <a name="Glue-Type-ViewDefinition-Definer"></a>
The definer of a view in SQL.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** IsProtected **   <a name="Glue-Type-ViewDefinition-IsProtected"></a>
You can set this flag as true to instruct the engine not to push user-provided operations into the logical plan of the view during query planning. However, setting this flag does not guarantee that the engine will comply. Refer to the engine's documentation to understand the guarantees provided, if any.
Type: Boolean
Required: No

 ** LastRefreshType **   <a name="Glue-Type-ViewDefinition-LastRefreshType"></a>
Sets the method used for the most recent refresh.
Type: String
Valid Values: `FULL | INCREMENTAL`
Required: No

 ** RefreshSeconds **   <a name="Glue-Type-ViewDefinition-RefreshSeconds"></a>
Auto refresh interval in seconds for the materialized view. If not specified, the view will not automatically refresh.
Type: Long
Required: No

 ** Representations **   <a name="Glue-Type-ViewDefinition-Representations"></a>
A list of representations.
Type: Array of [ViewRepresentation](API_ViewRepresentation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

 ** SubObjects **   <a name="Glue-Type-ViewDefinition-SubObjects"></a>
A list of table Amazon Resource Names (ARNs).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** SubObjectVersionIds **   <a name="Glue-Type-ViewDefinition-SubObjectVersionIds"></a>
List of the Apache Iceberg table versions referenced by the materialized view.
Type: Array of longs
Array Members: Minimum number of 0 items. Maximum number of 250 items.
Valid Range: Minimum value of -1.
Required: No

 ** ViewVersionId **   <a name="Glue-Type-ViewDefinition-ViewVersionId"></a>
The ID value that identifies this view's version. For materialized views, the version ID is the Apache Iceberg table's snapshot ID.
Type: Long
Valid Range: Minimum value of -1.
Required: No

 ** ViewVersionToken **   <a name="Glue-Type-ViewDefinition-ViewVersionToken"></a>
The version ID of the Apache Iceberg table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_ViewDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ViewDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ViewDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ViewDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
