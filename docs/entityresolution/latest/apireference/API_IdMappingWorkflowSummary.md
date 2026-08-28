---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingWorkflowSummary.html
---

# IdMappingWorkflowSummary
<a name="API_IdMappingWorkflowSummary"></a>

A list of `IdMappingWorkflowSummary` objects, each of which contain the fields `WorkflowName`, `WorkflowArn`, `CreatedAt`, and `UpdatedAt`.

## Contents
<a name="API_IdMappingWorkflowSummary_Contents"></a>

 ** createdAt **   <a name="API-Type-IdMappingWorkflowSummary-createdAt"></a>
The timestamp of when the workflow was created.
Type: Timestamp
Required: Yes

 ** updatedAt **   <a name="API-Type-IdMappingWorkflowSummary-updatedAt"></a>
The timestamp of when the workflow was last updated.
Type: Timestamp
Required: Yes

 ** workflowArn **   <a name="API-Type-IdMappingWorkflowSummary-workflowArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `IdMappingWorkflow`.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})`
Required: Yes

 ** workflowName **   <a name="API-Type-IdMappingWorkflowSummary-workflowName"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## See Also
<a name="API_IdMappingWorkflowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdMappingWorkflowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdMappingWorkflowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdMappingWorkflowSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
