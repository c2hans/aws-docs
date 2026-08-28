---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SemanticTable.html
---

# SemanticTable
<a name="API_SemanticTable"></a>

A semantic table that represents the final analytical structure of the data.

## Contents
<a name="API_SemanticTable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-SemanticTable-Alias"></a>
Alias for the semantic table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** DestinationTableId **   <a name="QS-Type-SemanticTable-DestinationTableId"></a>
The identifier of the destination table from data preparation that provides data to this semantic table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-]*`
Required: Yes

 ** RowLevelPermissionConfiguration **   <a name="QS-Type-SemanticTable-RowLevelPermissionConfiguration"></a>
Configuration for row level security that control data access for this semantic table.
Type: [RowLevelPermissionConfiguration](API_RowLevelPermissionConfiguration.md) object
Required: No

 ** SemanticMetadata **   <a name="QS-Type-SemanticTable-SemanticMetadata"></a>
The column-level semantic metadata for this semantic table.
Type: [TableSemanticMetadata](API_TableSemanticMetadata.md) object
Required: No

## See Also
<a name="API_SemanticTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SemanticTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SemanticTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SemanticTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
