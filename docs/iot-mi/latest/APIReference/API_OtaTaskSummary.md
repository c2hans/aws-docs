---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_OtaTaskSummary.html
---

# OtaTaskSummary
<a name="API_OtaTaskSummary"></a>

Structure representing one over-the-air (OTA) task.

## Contents
<a name="API_OtaTaskSummary_Contents"></a>

 ** CreatedAt **   <a name="managedintegrations-Type-OtaTaskSummary-CreatedAt"></a>
The timestamp value of when the over-the-air (OTA) task was created at.
Type: Timestamp
Required: No

 ** LastUpdatedAt **   <a name="managedintegrations-Type-OtaTaskSummary-LastUpdatedAt"></a>
The timestamp value of when the over-the-air (OTA) task was last updated at.
Type: Timestamp
Required: No

 ** Status **   <a name="managedintegrations-Type-OtaTaskSummary-Status"></a>
The status of the over-the-air (OTA) task summary.
Type: String
Valid Values: `IN_PROGRESS | CANCELED | COMPLETED | DELETION_IN_PROGRESS | SCHEDULED`
Required: No

 ** TaskArn **   <a name="managedintegrations-Type-OtaTaskSummary-TaskArn"></a>
The Amazon Resource Name (ARN) of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:ota-task/[0-9a-zA-Z]+`
Required: No

 ** TaskConfigurationId **   <a name="managedintegrations-Type-OtaTaskSummary-TaskConfigurationId"></a>
The identifier for the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** TaskId **   <a name="managedintegrations-Type-OtaTaskSummary-TaskId"></a>
The id of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: No

## See Also
<a name="API_OtaTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/OtaTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/OtaTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/OtaTaskSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
