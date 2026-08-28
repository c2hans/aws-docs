---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ListWorkflowsItem.html
---

# ListWorkflowsItem
<a name="API_connect-customer-profiles_ListWorkflowsItem"></a>

A workflow in list of workflows.

## Contents
<a name="API_connect-customer-profiles_ListWorkflowsItem_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_ListWorkflowsItem-CreatedAt"></a>
Creation timestamp for workflow.
Type: Timestamp
Required: Yes

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_ListWorkflowsItem-LastUpdatedAt"></a>
Last updated timestamp for workflow.
Type: Timestamp
Required: Yes

 ** Status **   <a name="connect-Type-connect-customer-profiles_ListWorkflowsItem-Status"></a>
Status of workflow execution.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETE | FAILED | SPLIT | RETRY | CANCELLED`
Required: Yes

 ** StatusDescription **   <a name="connect-Type-connect-customer-profiles_ListWorkflowsItem-StatusDescription"></a>
Description for workflow execution status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** WorkflowId **   <a name="connect-Type-connect-customer-profiles_ListWorkflowsItem-WorkflowId"></a>
Unique identifier for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** WorkflowType **   <a name="connect-Type-connect-customer-profiles_ListWorkflowsItem-WorkflowType"></a>
The type of workflow. The only supported value is APPFLOW\_INTEGRATION.
Type: String
Valid Values: `APPFLOW_INTEGRATION`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_ListWorkflowsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListWorkflowsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListWorkflowsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListWorkflowsItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
