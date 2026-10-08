---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedWorkflow.html
---

# DescribedWorkflow
<a name="API_DescribedWorkflow"></a>

Describes the properties of the specified workflow

## Contents
<a name="API_DescribedWorkflow_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-DescribedWorkflow-Arn"></a>
Specifies the unique Amazon Resource Name (ARN) for the workflow.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: Yes

 ** Description **   <a name="TransferFamily-Type-DescribedWorkflow-Description"></a>
Specifies the text description for the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\w- ]*`
Required: No

 ** OnExceptionSteps **   <a name="TransferFamily-Type-DescribedWorkflow-OnExceptionSteps"></a>
Specifies the steps (actions) to take if errors are encountered during execution of the workflow.
Type: Array of [WorkflowStep](API_WorkflowStep.md) objects
Array Members: Minimum number of 0 items. Maximum number of 8 items.
Required: No

 ** Steps **   <a name="TransferFamily-Type-DescribedWorkflow-Steps"></a>
Specifies the details for the steps that are in the specified workflow.
Type: Array of [WorkflowStep](API_WorkflowStep.md) objects
Array Members: Minimum number of 0 items. Maximum number of 8 items.
Required: No

 ** StructuredLogDestinations **   <a name="TransferFamily-Type-DescribedWorkflow-StructuredLogDestinations"></a>
Specifies the log groups to which your workflow logs are sent.
To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:
 `arn:partition:logs:region-name:amazon-account-id:log-group:log-group-name:*`
For example, `arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*`
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: No

 ** Tags **   <a name="TransferFamily-Type-DescribedWorkflow-Tags"></a>
Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** WorkflowId **   <a name="TransferFamily-Type-DescribedWorkflow-WorkflowId"></a>
A unique identifier for the workflow.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `w-([a-z0-9]{17})`
Required: No

## See Also
<a name="API_DescribedWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedWorkflow)
