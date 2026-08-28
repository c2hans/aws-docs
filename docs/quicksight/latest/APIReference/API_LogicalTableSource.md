---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LogicalTableSource.html
---

# LogicalTableSource
<a name="API_LogicalTableSource"></a>

Information about the source of a logical table. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

## Contents
<a name="API_LogicalTableSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSetArn **   <a name="QS-Type-LogicalTableSource-DataSetArn"></a>
The Amazon Resource Number (ARN) of the parent dataset.
Type: String
Required: No

 ** JoinInstruction **   <a name="QS-Type-LogicalTableSource-JoinInstruction"></a>
Specifies the result of a join of two logical tables.
Type: [JoinInstruction](API_JoinInstruction.md) object
Required: No

 ** PhysicalTableId **   <a name="QS-Type-LogicalTableSource-PhysicalTableId"></a>
Physical table ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-]*`
Required: No

## See Also
<a name="API_LogicalTableSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LogicalTableSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LogicalTableSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LogicalTableSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
