---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CustomActionLambdaConfiguration.html
---

# CustomActionLambdaConfiguration
<a name="API_CustomActionLambdaConfiguration"></a>

Configuration for AWS Lambda functions that perform custom actions during a Region switch.

## Contents
<a name="API_CustomActionLambdaConfiguration_Contents"></a>

 ** lambdas **   <a name="regionswitch-Type-CustomActionLambdaConfiguration-lambdas"></a>
The AWS Lambda functions for the execution block.
Type: Array of [Lambdas](API_Lambdas.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** regionToRun **   <a name="regionswitch-Type-CustomActionLambdaConfiguration-regionToRun"></a>
The AWS Region for the function to run in. For recovery workflows use `activatingRegion` or `deactivatingRegion`. For post-recovery workflows, use `activeRegion` (the Region with customer traffic) or `inactiveRegion` (the Region with no customer traffic).
Type: String
Valid Values: `activatingRegion | deactivatingRegion | activeRegion | inactiveRegion`
Required: Yes

 ** retryIntervalMinutes **   <a name="regionswitch-Type-CustomActionLambdaConfiguration-retryIntervalMinutes"></a>
The retry interval specified.
Type: Float
Required: Yes

 ** timeoutMinutes **   <a name="regionswitch-Type-CustomActionLambdaConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ungraceful **   <a name="regionswitch-Type-CustomActionLambdaConfiguration-ungraceful"></a>
The settings for ungraceful execution.
Type: [LambdaUngraceful](API_LambdaUngraceful.md) object
Required: No

## See Also
<a name="API_CustomActionLambdaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/CustomActionLambdaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/CustomActionLambdaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/CustomActionLambdaConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
