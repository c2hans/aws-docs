---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_WorkflowVersionSummary.html
---

# WorkflowVersionSummary
<a name="API_WorkflowVersionSummary"></a>

Summary information about a workflow version, including identification and configuration details.

## Contents
<a name="API_WorkflowVersionSummary_Contents"></a>

 ** WorkflowArn **   <a name="mwaaserverless-Type-WorkflowVersionSummary-WorkflowArn"></a>
The Amazon Resource Name (ARN) of the workflow that contains this version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(?:-(?:cn|us-gov|iso|iso-b|iso-e|iso-f))?:airflow-serverless:([a-z]{2}-[a-z]+-[0-9]{1}):([0-9]{12}):workflow/([a-zA-Z0-9][a-zA-Z0-9\.\-_]{0,254}-[a-zA-Z0-9]{10})`
Required: Yes

 ** WorkflowVersion **   <a name="mwaaserverless-Type-WorkflowVersionSummary-WorkflowVersion"></a>
The version identifier of the workflow version.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-z0-9]{32}`
Required: Yes

 ** CreatedAt **   <a name="mwaaserverless-Type-WorkflowVersionSummary-CreatedAt"></a>
The timestamp when the workflow version was created, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** DefinitionS3Location **   <a name="mwaaserverless-Type-WorkflowVersionSummary-DefinitionS3Location"></a>
The Amazon S3 location of the workflow definition file for this version.
Type: [DefinitionS3Location](API_DefinitionS3Location.md) object
Required: No

 ** IsLatestVersion **   <a name="mwaaserverless-Type-WorkflowVersionSummary-IsLatestVersion"></a>
Boolean flag that indicates whether this is the latest version of the workflow.
Type: Boolean
Required: No

 ** ModifiedAt **   <a name="mwaaserverless-Type-WorkflowVersionSummary-ModifiedAt"></a>
The timestamp when the workflow version was last modified, in ISO 8601 date-time format.
Type: Timestamp
Required: No

 ** ScheduleConfiguration **   <a name="mwaaserverless-Type-WorkflowVersionSummary-ScheduleConfiguration"></a>
The schedule configuration for this workflow version.
Type: [ScheduleConfiguration](API_ScheduleConfiguration.md) object
Required: No

 ** TriggerMode **   <a name="mwaaserverless-Type-WorkflowVersionSummary-TriggerMode"></a>
The trigger mode for the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

## See Also
<a name="API_WorkflowVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/WorkflowVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/WorkflowVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/WorkflowVersionSummary)
