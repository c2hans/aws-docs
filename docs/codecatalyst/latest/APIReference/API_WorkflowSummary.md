---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_WorkflowSummary.html
---

# WorkflowSummary
<a name="API_WorkflowSummary"></a>

Information about a workflow.

## Contents
<a name="API_WorkflowSummary_Contents"></a>

 ** createdTime **   <a name="codecatalyst-Type-WorkflowSummary-createdTime"></a>
The date and time the workflow was created, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp
Required: Yes

 ** definition **   <a name="codecatalyst-Type-WorkflowSummary-definition"></a>
Information about the workflow definition file.
Type: [WorkflowDefinitionSummary](API_WorkflowDefinitionSummary.md) object
Required: Yes

 ** id **   <a name="codecatalyst-Type-WorkflowSummary-id"></a>
The system-generated unique ID of a workflow.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** lastUpdatedTime **   <a name="codecatalyst-Type-WorkflowSummary-lastUpdatedTime"></a>
The date and time the workflow was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
Type: Timestamp
Required: Yes

 ** name **   <a name="codecatalyst-Type-WorkflowSummary-name"></a>
The name of the workflow.
Type: String
Required: Yes

 ** runMode **   <a name="codecatalyst-Type-WorkflowSummary-runMode"></a>
The run mode of the workflow.
Type: String
Valid Values: `QUEUED | PARALLEL | SUPERSEDED`
Required: Yes

 ** sourceBranchName **   <a name="codecatalyst-Type-WorkflowSummary-sourceBranchName"></a>
The name of the branch of the source repository where the workflow definition file is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** sourceRepositoryName **   <a name="codecatalyst-Type-WorkflowSummary-sourceRepositoryName"></a>
The name of the source repository where the workflow definition file is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`
Required: Yes

 ** status **   <a name="codecatalyst-Type-WorkflowSummary-status"></a>
The status of the workflow.
Type: String
Valid Values: `INVALID | ACTIVE`
Required: Yes

## See Also
<a name="API_WorkflowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/WorkflowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/WorkflowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/WorkflowSummary)
