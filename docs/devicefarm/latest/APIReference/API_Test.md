---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Test.html
---

# Test
<a name="API_Test"></a>

Represents a condition that is evaluated.

## Contents
<a name="API_Test_Contents"></a>

 ** arn **   <a name="devicefarm-Type-Test-arn"></a>
The test's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** counters **   <a name="devicefarm-Type-Test-counters"></a>
The test's result counters.
Type: [Counters](API_Counters.md) object
Required: No

 ** created **   <a name="devicefarm-Type-Test-created"></a>
When the test was created.
Type: Timestamp
Required: No

 ** deviceMinutes **   <a name="devicefarm-Type-Test-deviceMinutes"></a>
Represents the total (metered or unmetered) minutes used by the test.
Type: [DeviceMinutes](API_DeviceMinutes.md) object
Required: No

 ** message **   <a name="devicefarm-Type-Test-message"></a>
A message about the test's result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** name **   <a name="devicefarm-Type-Test-name"></a>
The test's name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** result **   <a name="devicefarm-Type-Test-result"></a>
The test's result.
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

 ** started **   <a name="devicefarm-Type-Test-started"></a>
The test's start time.
Type: Timestamp
Required: No

 ** status **   <a name="devicefarm-Type-Test-status"></a>
The test's status.
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

 ** stopped **   <a name="devicefarm-Type-Test-stopped"></a>
The test's stop time.
Type: Timestamp
Required: No

 ** type **   <a name="devicefarm-Type-Test-type"></a>
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
Required: No

## See Also
<a name="API_Test_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Test)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Test)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Test)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
