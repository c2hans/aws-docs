---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRunConfiguration.html
---

# ScheduleRunConfiguration
<a name="API_ScheduleRunConfiguration"></a>

Represents the settings for a run. Includes things like location, radio states, auxiliary apps, and network profiles.

## Contents
<a name="API_ScheduleRunConfiguration_Contents"></a>

 ** auxiliaryApps **   <a name="devicefarm-Type-ScheduleRunConfiguration-auxiliaryApps"></a>
A list of upload ARNs for app packages to be installed with your app.
Type: Array of strings
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** billingMethod **   <a name="devicefarm-Type-ScheduleRunConfiguration-billingMethod"></a>
Specifies the billing method for a test run: `metered` or `unmetered`. If the parameter is not specified, the default value is `metered`.
If you have purchased unmetered device slots, you must set this parameter to `unmetered` to make use of them. Otherwise, your run counts against your metered time.
Type: String
Valid Values: `METERED | UNMETERED`
Required: No

 ** customerArtifactPaths **   <a name="devicefarm-Type-ScheduleRunConfiguration-customerArtifactPaths"></a>
Input `CustomerArtifactPaths` object for the scheduled run configuration.
Type: [CustomerArtifactPaths](API_CustomerArtifactPaths.md) object
Required: No

 ** deviceProxy **   <a name="devicefarm-Type-ScheduleRunConfiguration-deviceProxy"></a>
The device proxy to be configured on the device for the run.
Type: [DeviceProxy](API_DeviceProxy.md) object
Required: No

 ** environmentVariables **   <a name="devicefarm-Type-ScheduleRunConfiguration-environmentVariables"></a>
Environment variables associated with the run.
Type: Array of [EnvironmentVariable](API_EnvironmentVariable.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** executionRoleArn **   <a name="devicefarm-Type-ScheduleRunConfiguration-executionRoleArn"></a>
An IAM role to be assumed by the test host for the run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.+`
Required: No

 ** extraDataPackageArn **   <a name="devicefarm-Type-ScheduleRunConfiguration-extraDataPackageArn"></a>
The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm extracts to external data for Android or the app's sandbox for iOS.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** insightsTypes **   <a name="devicefarm-Type-ScheduleRunConfiguration-insightsTypes"></a>
The types of insights to generate for a run. Specify one or more values to opt in to insights generation when scheduling a run.
Insights are currently supported for custom mode runs with Instrumentation, Appium Java TestNG, and XCTest UI test types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `TEST_REPORT`
Required: No

 ** locale **   <a name="devicefarm-Type-ScheduleRunConfiguration-locale"></a>
Information about the locale that is used for the run.
Type: String
Required: No

 ** location **   <a name="devicefarm-Type-ScheduleRunConfiguration-location"></a>
Information about the location that is used for the run.
Type: [Location](API_Location.md) object
Required: No

 ** networkProfileArn **   <a name="devicefarm-Type-ScheduleRunConfiguration-networkProfileArn"></a>
Reserved for internal use.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** radios **   <a name="devicefarm-Type-ScheduleRunConfiguration-radios"></a>
Information about the radio states for the run.
Type: [Radios](API_Radios.md) object
Required: No

 ** vpceConfigurationArns **   <a name="devicefarm-Type-ScheduleRunConfiguration-vpceConfigurationArns"></a>
An array of ARNs for your VPC endpoint configurations.
Type: Array of strings
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

## See Also
<a name="API_ScheduleRunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ScheduleRunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ScheduleRunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ScheduleRunConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
