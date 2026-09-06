---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_WorkflowDefinitionSummary.html
---

# WorkflowDefinitionSummary
<a name="API_WorkflowDefinitionSummary"></a>

Summary information about a workflow definition, used in list operations.

## Contents
<a name="API_WorkflowDefinitionSummary_Contents"></a>

 ** createdAt **   <a name="novaact-Type-WorkflowDefinitionSummary-createdAt"></a>
The timestamp when the workflow definition was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="novaact-Type-WorkflowDefinitionSummary-status"></a>
The current status of the workflow definition.
Type: String
Valid Values: `ACTIVE | DELETING`
Required: Yes

 ** workflowDefinitionArn **   <a name="novaact-Type-WorkflowDefinitionSummary-workflowDefinitionArn"></a>
The Amazon Resource Name (ARN) of the workflow definition.
Type: String
Pattern: `arn:(aws|aws-cn|aws-us-gov):nova-act:[a-z0-9-]+:[0-9]{12}:workflow-definition/[a-zA-Z0-9_-]{1,40}`
Required: Yes

 ** workflowDefinitionName **   <a name="novaact-Type-WorkflowDefinitionSummary-workflowDefinitionName"></a>
The name of the workflow definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]{1,40}`
Required: Yes

## See Also
<a name="API_WorkflowDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/WorkflowDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/WorkflowDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/WorkflowDefinitionSummary)
