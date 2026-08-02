---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsStepFunctionStateMachineDetails.html
---

# AwsStepFunctionStateMachineDetails
<a name="API_AwsStepFunctionStateMachineDetails"></a>

 Provides details about an AWS Step Functions state machine, which is a workflow consisting of a series of event- driven steps.

## Contents
<a name="API_AwsStepFunctionStateMachineDetails_Contents"></a>

 ** Label **   <a name="securityhub-Type-AwsStepFunctionStateMachineDetails-Label"></a>
 A user-defined or an auto-generated string that identifies a `Map` state. This parameter is present only if the `stateMachineArn` specified in input is a qualified state machine ARN.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LoggingConfiguration **   <a name="securityhub-Type-AwsStepFunctionStateMachineDetails-LoggingConfiguration"></a>
 Used to set CloudWatch Logs options.
Type: [AwsStepFunctionStateMachineLoggingConfigurationDetails](API_AwsStepFunctionStateMachineLoggingConfigurationDetails.md) object
Required: No

 ** Name **   <a name="securityhub-Type-AwsStepFunctionStateMachineDetails-Name"></a>
 The name of the state machine.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleArn **   <a name="securityhub-Type-AwsStepFunctionStateMachineDetails-RoleArn"></a>
 The Amazon Resource Name (ARN) of the IAM role used when creating this state machine.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StateMachineArn **   <a name="securityhub-Type-AwsStepFunctionStateMachineDetails-StateMachineArn"></a>
 The ARN that identifies the state machine.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsStepFunctionStateMachineDetails-Status"></a>
 The current status of the state machine.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TracingConfiguration **   <a name="securityhub-Type-AwsStepFunctionStateMachineDetails-TracingConfiguration"></a>
 Specifies whether AWS X-Ray tracing is enabled.
Type: [AwsStepFunctionStateMachineTracingConfigurationDetails](API_AwsStepFunctionStateMachineTracingConfigurationDetails.md) object
Required: No

 ** Type **   <a name="securityhub-Type-AwsStepFunctionStateMachineDetails-Type"></a>
 The type of the state machine (STANDARD or EXPRESS).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsStepFunctionStateMachineDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsStepFunctionStateMachineDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsStepFunctionStateMachineDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsStepFunctionStateMachineDetails)
