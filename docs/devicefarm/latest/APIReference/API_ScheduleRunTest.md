---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRunTest.html
---

# ScheduleRunTest
<a name="API_ScheduleRunTest"></a>

Represents test settings. This data structure is passed in as the test parameter to ScheduleRun. For an example of the JSON request syntax, see [ScheduleRun](API_ScheduleRun.md).

## Contents
<a name="API_ScheduleRunTest_Contents"></a>

 ** type **   <a name="devicefarm-Type-ScheduleRunTest-type"></a>
The test's type.
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
Required: Yes

 ** filter **   <a name="devicefarm-Type-ScheduleRunTest-filter"></a>
The test's filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** parameters **   <a name="devicefarm-Type-ScheduleRunTest-parameters"></a>
The test's parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.
For all tests:
+  `app_performance_monitoring`: Performance monitoring is enabled by default. Set this parameter to false to disable it.
For Appium tests (all types):
+ appium\_version: The Appium version. Currently supported values are 1.6.5 (and later), latest, and default.
  + latest runs the latest Appium version supported by Device Farm (1.9.1).
  + For default, Device Farm selects a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier and 1.7.2 for iOS 10 and later.
  + This behavior is subject to change.
For fuzz tests (Android only):
+ event\_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.
+ throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.
+ seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
For Instrumentation:
+ filter: A test filter string. Examples:
  + Running a single test case: `com.android.abc.Test1`
  + Running a single test: `com.android.abc.Test1#smoke`
  + Running multiple tests: `com.android.abc.Test1,com.android.abc.Test2`
For XCTest and XCTestUI:
+ filter: A test filter string. Examples:
  + Running a single test class: `LoginTests`
  + Running a multiple test classes: `LoginTests,SmokeTests`
  + Running a single test: `LoginTests/testValid`
  + Running multiple tests: `LoginTests/testValid,LoginTests/testInvalid`
Type: String to string map
Required: No

 ** testPackageArn **   <a name="devicefarm-Type-ScheduleRunTest-testPackageArn"></a>
The ARN of the uploaded test to be run.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** testSpecArn **   <a name="devicefarm-Type-ScheduleRunTest-testSpecArn"></a>
The ARN of the YAML-formatted test specification.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

## See Also
<a name="API_ScheduleRunTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ScheduleRunTest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ScheduleRunTest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ScheduleRunTest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
