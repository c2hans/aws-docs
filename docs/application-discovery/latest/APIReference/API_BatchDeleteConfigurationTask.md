---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteConfigurationTask.html
---

# BatchDeleteConfigurationTask
<a name="API_BatchDeleteConfigurationTask"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 A metadata object that represents the deletion task being executed.

## Contents
<a name="API_BatchDeleteConfigurationTask_Contents"></a>

 ** configurationType **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-configurationType"></a>
 The type of configuration item to delete. Supported types are: SERVER.
Type: String
Valid Values: `SERVER`
Required: No

 ** deletedConfigurations **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-deletedConfigurations"></a>
 The list of configuration IDs that were successfully deleted by the deletion task.
Type: Array of strings
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** deletionWarnings **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-deletionWarnings"></a>
 A list of configuration IDs that produced warnings regarding their deletion, paired with a warning message.
Type: Array of [DeletionWarning](API_DeletionWarning.md) objects
Required: No

 ** endTime **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-endTime"></a>
 An epoch seconds timestamp (UTC) of when the deletion task was completed or failed.
Type: Timestamp
Required: No

 ** failedConfigurations **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-failedConfigurations"></a>
 A list of configuration IDs that failed to delete during the deletion task, each paired with an error message.
Type: Array of [FailedConfiguration](API_FailedConfiguration.md) objects
Required: No

 ** requestedConfigurations **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-requestedConfigurations"></a>
 The list of configuration IDs that were originally requested to be deleted by the deletion task.
Type: Array of strings
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** startTime **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-startTime"></a>
 An epoch seconds timestamp (UTC) of when the deletion task was started.
Type: Timestamp
Required: No

 ** status **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-status"></a>
 The current execution status of the deletion task. Valid status are: INITIALIZING \| VALIDATING \| DELETING \| COMPLETED \| FAILED.
Type: String
Valid Values: `INITIALIZING | VALIDATING | DELETING | COMPLETED | FAILED`
Required: No

 ** taskId **   <a name="DiscServ-Type-BatchDeleteConfigurationTask-taskId"></a>
 The deletion task's unique identifier.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_BatchDeleteConfigurationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/BatchDeleteConfigurationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/BatchDeleteConfigurationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/BatchDeleteConfigurationTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
