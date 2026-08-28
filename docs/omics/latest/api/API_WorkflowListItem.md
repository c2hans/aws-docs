---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_WorkflowListItem.html
---

# WorkflowListItem
<a name="API_WorkflowListItem"></a>

A workflow.

## Contents
<a name="API_WorkflowListItem_Contents"></a>

 ** arn **   <a name="omics-Type-WorkflowListItem-arn"></a>
The workflow's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`
Required: No

 ** creationTime **   <a name="omics-Type-WorkflowListItem-creationTime"></a>
When the workflow was created.
Type: Timestamp
Required: No

 ** digest **   <a name="omics-Type-WorkflowListItem-digest"></a>
The workflow's digest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** id **   <a name="omics-Type-WorkflowListItem-id"></a>
The workflow's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: No

 ** metadata **   <a name="omics-Type-WorkflowListItem-metadata"></a>
 Any metadata available for workflow. The information listed may vary depending on the workflow, and there may also be no metadata to return.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** name **   <a name="omics-Type-WorkflowListItem-name"></a>
The workflow's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** status **   <a name="omics-Type-WorkflowListItem-status"></a>
The workflow's status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | ACTIVE | UPDATING | DELETED | FAILED | INACTIVE`
Required: No

 ** type **   <a name="omics-Type-WorkflowListItem-type"></a>
The workflow's type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`
Required: No

## See Also
<a name="API_WorkflowListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/WorkflowListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/WorkflowListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/WorkflowListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
