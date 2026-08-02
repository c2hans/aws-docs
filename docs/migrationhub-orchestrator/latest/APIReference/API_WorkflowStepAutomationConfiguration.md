---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepAutomationConfiguration.html
---

# WorkflowStepAutomationConfiguration
<a name="API_WorkflowStepAutomationConfiguration"></a>

The custom script to run tests on source or target environments.

## Contents
<a name="API_WorkflowStepAutomationConfiguration_Contents"></a>

 ** command **   <a name="migrationhuborchestrator-Type-WorkflowStepAutomationConfiguration-command"></a>
The command required to run the script.
Type: [PlatformCommand](API_PlatformCommand.md) object
Required: No

 ** runEnvironment **   <a name="migrationhuborchestrator-Type-WorkflowStepAutomationConfiguration-runEnvironment"></a>
The source or target environment.
Type: String
Valid Values: `AWS | ONPREMISE`
Required: No

 ** scriptLocationS3Bucket **   <a name="migrationhuborchestrator-Type-WorkflowStepAutomationConfiguration-scriptLocationS3Bucket"></a>
The Amazon S3 bucket where the script is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+`
Required: No

 ** scriptLocationS3Key **   <a name="migrationhuborchestrator-Type-WorkflowStepAutomationConfiguration-scriptLocationS3Key"></a>
The Amazon S3 key for the script location.
Type: [PlatformScriptKey](API_PlatformScriptKey.md) object
Required: No

 ** targetType **   <a name="migrationhuborchestrator-Type-WorkflowStepAutomationConfiguration-targetType"></a>
The servers on which to run the script.
Type: String
Valid Values: `SINGLE | ALL | NONE`
Required: No

## See Also
<a name="API_WorkflowStepAutomationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/WorkflowStepAutomationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/WorkflowStepAutomationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/WorkflowStepAutomationConfiguration)
