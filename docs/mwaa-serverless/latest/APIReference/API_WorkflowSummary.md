---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_WorkflowSummary.html
---

# WorkflowSummary
<a name="API_WorkflowSummary"></a>

Summary information about a workflow, including basic identification and metadata.

## Contents
<a name="API_WorkflowSummary_Contents"></a>

 ** WorkflowArn **   <a name="mwaaserverless-Type-WorkflowSummary-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: Yes

 ** CreatedAt **   <a name="mwaaserverless-Type-WorkflowSummary-CreatedAt"></a>
The timestamp when the workflow was created, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** Description **   <a name="mwaaserverless-Type-WorkflowSummary-Description"></a>
The description of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** ModifiedAt **   <a name="mwaaserverless-Type-WorkflowSummary-ModifiedAt"></a>
The timestamp when the workflow was last modified, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** Name **   <a name="mwaaserverless-Type-WorkflowSummary-Name"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*`
Required: No

 ** TriggerMode **   <a name="mwaaserverless-Type-WorkflowSummary-TriggerMode"></a>
The trigger mode for the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** WorkflowStatus **   <a name="mwaaserverless-Type-WorkflowSummary-WorkflowStatus"></a>
The current status of the workflow.
Type: String
Valid Values: `READY | DELETING`
Required: No

 ** WorkflowVersion **   <a name="mwaaserverless-Type-WorkflowSummary-WorkflowVersion"></a>
The version identifier of the workflow.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]{32}`
Required: No

## See Also
<a name="API_WorkflowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/WorkflowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/WorkflowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/WorkflowSummary)
