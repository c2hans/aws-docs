---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_AppflowIntegrationWorkflowStep.html
---

# AppflowIntegrationWorkflowStep
<a name="API_connect-customer-profiles_AppflowIntegrationWorkflowStep"></a>

Workflow step details for `APPFLOW_INTEGRATION` workflow.

## Contents
<a name="API_connect-customer-profiles_AppflowIntegrationWorkflowStep_Contents"></a>

 ** BatchRecordsEndTime **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowStep-BatchRecordsEndTime"></a>
End datetime of records pulled in batch during execution of workflow step for `APPFLOW_INTEGRATION` workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** BatchRecordsStartTime **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowStep-BatchRecordsStartTime"></a>
Start datetime of records pulled in batch during execution of workflow step for `APPFLOW_INTEGRATION` workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowStep-CreatedAt"></a>
Creation timestamp of workflow step for `APPFLOW_INTEGRATION` workflow.
Type: Timestamp
Required: Yes

 ** ExecutionMessage **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowStep-ExecutionMessage"></a>
Message indicating execution of workflow step for `APPFLOW_INTEGRATION` workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** FlowName **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowStep-FlowName"></a>
Name of the flow created during execution of workflow step. `APPFLOW_INTEGRATION` workflow type creates an appflow flow during workflow step execution on the customers behalf.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: Yes

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowStep-LastUpdatedAt"></a>
Last updated timestamp for workflow step for `APPFLOW_INTEGRATION` workflow.
Type: Timestamp
Required: Yes

 ** RecordsProcessed **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowStep-RecordsProcessed"></a>
Total number of records processed during execution of workflow step for `APPFLOW_INTEGRATION` workflow.
Type: Long
Required: Yes

 ** Status **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowStep-Status"></a>
Workflow step status for `APPFLOW_INTEGRATION` workflow.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETE | FAILED | SPLIT | RETRY | CANCELLED`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_AppflowIntegrationWorkflowStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AppflowIntegrationWorkflowStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AppflowIntegrationWorkflowStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AppflowIntegrationWorkflowStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
