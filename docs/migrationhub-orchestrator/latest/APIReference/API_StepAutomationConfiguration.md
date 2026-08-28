---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StepAutomationConfiguration.html
---

# StepAutomationConfiguration
<a name="API_StepAutomationConfiguration"></a>

The custom script to run tests on source or target environments.

## Contents
<a name="API_StepAutomationConfiguration_Contents"></a>

 ** command **   <a name="migrationhuborchestrator-Type-StepAutomationConfiguration-command"></a>
The command to run the script.
Type: [PlatformCommand](API_PlatformCommand.md) object
Required: No

 ** runEnvironment **   <a name="migrationhuborchestrator-Type-StepAutomationConfiguration-runEnvironment"></a>
The source or target environment.
Type: String
Valid Values: `AWS | ONPREMISE`
Required: No

 ** scriptLocationS3Bucket **   <a name="migrationhuborchestrator-Type-StepAutomationConfiguration-scriptLocationS3Bucket"></a>
The Amazon S3 bucket where the script is located.
Type: String
Required: No

 ** scriptLocationS3Key **   <a name="migrationhuborchestrator-Type-StepAutomationConfiguration-scriptLocationS3Key"></a>
The Amazon S3 key for the script location.
Type: [PlatformScriptKey](API_PlatformScriptKey.md) object
Required: No

 ** targetType **   <a name="migrationhuborchestrator-Type-StepAutomationConfiguration-targetType"></a>
The servers on which to run the script.
Type: String
Valid Values: `SINGLE | ALL | NONE`
Required: No

## See Also
<a name="API_StepAutomationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/StepAutomationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/StepAutomationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/StepAutomationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
