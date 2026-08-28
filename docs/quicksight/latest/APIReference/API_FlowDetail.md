---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FlowDetail.html
---

# FlowDetail
<a name="API_FlowDetail"></a>

The full details of a flow, including its definition specifying the steps.

## Contents
<a name="API_FlowDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-FlowDetail-Arn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String
Required: Yes

 ** CreatedTime **   <a name="QS-Type-FlowDetail-CreatedTime"></a>
The time this flow was created.
Type: Timestamp
Required: Yes

 ** FlowDefinition **   <a name="QS-Type-FlowDetail-FlowDefinition"></a>
The definition of the flow, specifying the steps and configurations. This is the flow definition in Quick Flow's internal format. The format is subject to change.
Type: JSON value
Required: Yes

 ** FlowId **   <a name="QS-Type-FlowDetail-FlowId"></a>
The unique identifier of the flow.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** Name **   <a name="QS-Type-FlowDetail-Name"></a>
The display name of the flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** PublishState **   <a name="QS-Type-FlowDetail-PublishState"></a>
The publish state of the flow. Valid values are `DRAFT`, `PUBLISHED`, or `PENDING_APPROVAL`.
Type: String
Valid Values: `PUBLISHED | DRAFT | PENDING_APPROVAL`
Required: Yes

 ** CreatedBy **   <a name="QS-Type-FlowDetail-CreatedBy"></a>
The identifier of the principal who created the flow.
Type: String
Required: No

 ** Description **   <a name="QS-Type-FlowDetail-Description"></a>
The description of the flow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastUpdatedBy **   <a name="QS-Type-FlowDetail-LastUpdatedBy"></a>
The identifier of the last principal who updated the flow.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-FlowDetail-LastUpdatedTime"></a>
The last time this flow was modified.
Type: Timestamp
Required: No

 ** StepAliases **   <a name="QS-Type-FlowDetail-StepAliases"></a>
A list of step alias mappings for the flow.
Type: Array of [StepAliasMapping](API_StepAliasMapping.md) objects
Required: No

## See Also
<a name="API_FlowDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FlowDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FlowDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FlowDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
