---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsStepFunctionStateMachineLoggingConfigurationDetails.html
---

# AwsStepFunctionStateMachineLoggingConfigurationDetails
<a name="API_AwsStepFunctionStateMachineLoggingConfigurationDetails"></a>

 The `LoggingConfiguration` data type is used to set CloudWatch Logs options.

## Contents
<a name="API_AwsStepFunctionStateMachineLoggingConfigurationDetails_Contents"></a>

 ** Destinations **   <a name="securityhub-Type-AwsStepFunctionStateMachineLoggingConfigurationDetails-Destinations"></a>
 An array of objects that describes where your execution history events will be logged.
Type: Array of [AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails](API_AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails.md) objects
Required: No

 ** IncludeExecutionData **   <a name="securityhub-Type-AwsStepFunctionStateMachineLoggingConfigurationDetails-IncludeExecutionData"></a>
 Determines whether execution data is included in your log. When set to false, data is excluded.
Type: Boolean
Required: No

 ** Level **   <a name="securityhub-Type-AwsStepFunctionStateMachineLoggingConfigurationDetails-Level"></a>
 Defines which category of execution history events are logged.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsStepFunctionStateMachineLoggingConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsStepFunctionStateMachineLoggingConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsStepFunctionStateMachineLoggingConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsStepFunctionStateMachineLoggingConfigurationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
