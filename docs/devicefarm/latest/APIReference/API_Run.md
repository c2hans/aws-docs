---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Run.html
---

# Run
<a name="API_Run"></a>

Represents a test run on a set of devices with a given app package, test parameters, and so on.

## Contents
<a name="API_Run_Contents"></a>

 ** appUpload **   <a name="devicefarm-Type-Run-appUpload"></a>
An app to upload or that has been uploaded.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** arn **   <a name="devicefarm-Type-Run-arn"></a>
The run's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** billingMethod **   <a name="devicefarm-Type-Run-billingMethod"></a>
Specifies the billing method for a test run: `metered` or `unmetered`. If the parameter is not specified, the default value is `metered`.
If you have unmetered device slots, you must set this to `unmetered` to use them. Otherwise, the run is counted toward metered device minutes.
Type: String
Valid Values: `METERED | UNMETERED`
Required: No

 ** completedJobs **   <a name="devicefarm-Type-Run-completedJobs"></a>
The total number of completed jobs.
Type: Integer
Required: No

 ** counters **   <a name="devicefarm-Type-Run-counters"></a>
The run's result counters.
Type: [Counters](API_Counters.md) object
Required: No

 ** created **   <a name="devicefarm-Type-Run-created"></a>
When the run was created.
Type: Timestamp
Required: No

 ** customerArtifactPaths **   <a name="devicefarm-Type-Run-customerArtifactPaths"></a>
Output `CustomerArtifactPaths` object for the test run.
Type: [CustomerArtifactPaths](API_CustomerArtifactPaths.md) object
Required: No

 ** deviceMinutes **   <a name="devicefarm-Type-Run-deviceMinutes"></a>
Represents the total (metered or unmetered) minutes used by the test run.
Type: [DeviceMinutes](API_DeviceMinutes.md) object
Required: No

 ** devicePoolArn **   <a name="devicefarm-Type-Run-devicePoolArn"></a>
The ARN of the device pool for the run.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** deviceProxy **   <a name="devicefarm-Type-Run-deviceProxy"></a>
The device proxy configured for the devices in the run.
Type: [DeviceProxy](API_DeviceProxy.md) object
Required: No

 ** deviceSelectionResult **   <a name="devicefarm-Type-Run-deviceSelectionResult"></a>
The results of a device filter used to select the devices for a test run.
Type: [DeviceSelectionResult](API_DeviceSelectionResult.md) object
Required: No

 ** environmentVariables **   <a name="devicefarm-Type-Run-environmentVariables"></a>
Environment variables associated with the run.
Type: Array of [EnvironmentVariable](API_EnvironmentVariable.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** eventCount **   <a name="devicefarm-Type-Run-eventCount"></a>
For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.
Type: Integer
Required: No

 ** executionRoleArn **   <a name="devicefarm-Type-Run-executionRoleArn"></a>
The IAM role associated with the run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.+`
Required: No

 ** insights **   <a name="devicefarm-Type-Run-insights"></a>
The insights for the run, including the report status and job-level metrics. This field contains data only if you specified `insightsTypes` when you scheduled the run.
Type: [RunInsights](API_RunInsights.md) object
Required: No

 ** insightsTypes **   <a name="devicefarm-Type-Run-insightsTypes"></a>
The types of insights requested for the run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `TEST_REPORT`
Required: No

 ** jobTimeoutMinutes **   <a name="devicefarm-Type-Run-jobTimeoutMinutes"></a>
The number of minutes the job executes before it times out.
Type: Integer
Required: No

 ** locale **   <a name="devicefarm-Type-Run-locale"></a>
Information about the locale that is used for the run.
Type: String
Required: No

 ** location **   <a name="devicefarm-Type-Run-location"></a>
Information about the location that is used for the run.
Type: [Location](API_Location.md) object
Required: No

 ** message **   <a name="devicefarm-Type-Run-message"></a>
A message about the run's result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** name **   <a name="devicefarm-Type-Run-name"></a>
The run's name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** networkProfile **   <a name="devicefarm-Type-Run-networkProfile"></a>
The network profile being used for a test run.
Type: [NetworkProfile](API_NetworkProfile.md) object
Required: No

 ** parsingResultUrl **   <a name="devicefarm-Type-Run-parsingResultUrl"></a>
Read-only URL for an object in an S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.
Type: String
Required: No

 ** platform **   <a name="devicefarm-Type-Run-platform"></a>
The run's platform.
Allowed values include:
+ ANDROID
+ IOS
Type: String
Valid Values: `ANDROID | IOS`
Required: No

 ** radios **   <a name="devicefarm-Type-Run-radios"></a>
Information about the radio states for the run.
Type: [Radios](API_Radios.md) object
Required: No

 ** result **   <a name="devicefarm-Type-Run-result"></a>
The run's result.
Allowed values include:
+ PENDING
+ PASSED
+ WARNED
+ FAILED
+ SKIPPED
+ ERRORED
+ STOPPED
Type: String
Valid Values: `PENDING | PASSED | WARNED | FAILED | SKIPPED | ERRORED | STOPPED`
Required: No

 ** resultCode **   <a name="devicefarm-Type-Run-resultCode"></a>
Supporting field for the result field. Set only if `result` is `SKIPPED`. `PARSING_FAILED` if the result is skipped because of test package parsing failure.
Type: String
Valid Values: `PARSING_FAILED | VPC_ENDPOINT_SETUP_FAILED`
Required: No

 ** seed **   <a name="devicefarm-Type-Run-seed"></a>
For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
Type: Integer
Required: No

 ** skipAppResign **   <a name="devicefarm-Type-Run-skipAppResign"></a>
When set to `true`, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see [Do you modify my app?](http://aws.amazon.com/device-farm/faqs/) in the *AWS Device Farm FAQs*.
Type: Boolean
Required: No

 ** started **   <a name="devicefarm-Type-Run-started"></a>
The run's start time.
Type: Timestamp
Required: No

 ** status **   <a name="devicefarm-Type-Run-status"></a>
The run's status.
Allowed values include:
+ PENDING
+ PENDING\_CONCURRENCY
+ PENDING\_DEVICE
+ PROCESSING
+ SCHEDULING
+ PREPARING
+ RUNNING
+ COMPLETED
+ STOPPING
Type: String
Valid Values: `PENDING | PENDING_CONCURRENCY | PENDING_DEVICE | PROCESSING | SCHEDULING | PREPARING | RUNNING | COMPLETED | STOPPING`
Required: No

 ** stopped **   <a name="devicefarm-Type-Run-stopped"></a>
The run's stop time.
Type: Timestamp
Required: No

 ** testSpecArn **   <a name="devicefarm-Type-Run-testSpecArn"></a>
The ARN of the YAML-formatted test specification for the run.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** totalJobs **   <a name="devicefarm-Type-Run-totalJobs"></a>
The total number of jobs for the run.
Type: Integer
Required: No

 ** type **   <a name="devicefarm-Type-Run-type"></a>
The run's type.
Must be one of the following values:
+ BUILTIN\_FUZZ
+ APPIUM\_JAVA\_JUNIT
+ APPIUM\_JAVA\_TESTNG
+ APPIUM\_PYTHON
+ APPIUM\_NODE
+ APPIUM\_RUBY
+ APPIUM\_WEB\_JAVA\_JUNIT
+ APPIUM\_WEB\_JAVA\_TESTNG
+ APPIUM\_WEB\_PYTHON
+ APPIUM\_WEB\_NODE
+ APPIUM\_WEB\_RUBY
+ INSTRUMENTATION
+ XCTEST
+ XCTEST\_UI
Type: String
Valid Values: `BUILTIN_FUZZ | APPIUM_JAVA_JUNIT | APPIUM_JAVA_TESTNG | APPIUM_PYTHON | APPIUM_NODE | APPIUM_RUBY | APPIUM_WEB_JAVA_JUNIT | APPIUM_WEB_JAVA_TESTNG | APPIUM_WEB_PYTHON | APPIUM_WEB_NODE | APPIUM_WEB_RUBY | INSTRUMENTATION | XCTEST | XCTEST_UI`
Required: No

 ** vpcConfig **   <a name="devicefarm-Type-Run-vpcConfig"></a>
The VPC security groups and subnets that are attached to a project.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

 ** webUrl **   <a name="devicefarm-Type-Run-webUrl"></a>
The Device Farm console URL for the recording of the run.
Type: String
Required: No

## See Also
<a name="API_Run_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Run)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Run)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Run)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
