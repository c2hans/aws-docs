---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_InheritedDisallowedOutputColumns.html
---

# InheritedDisallowedOutputColumns
<a name="API_InheritedDisallowedOutputColumns"></a>

Contains the inherited disallowed output columns constraint and the column lineage tracing each column to its source.

## Contents
<a name="API_InheritedDisallowedOutputColumns_Contents"></a>

 ** columnLineage **   <a name="API-Type-InheritedDisallowedOutputColumns-columnLineage"></a>
The lineage information that traces each disallowed output column back to its source in a parent table.
Type: Array of [ColumnLineageEntry](API_ColumnLineageEntry.md) objects
Required: Yes

 ** value **   <a name="API-Type-InheritedDisallowedOutputColumns-value"></a>
The list of column names that are disallowed from appearing in query output, inherited from parent tables.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

## See Also
<a name="API_InheritedDisallowedOutputColumns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/InheritedDisallowedOutputColumns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/InheritedDisallowedOutputColumns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/InheritedDisallowedOutputColumns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
