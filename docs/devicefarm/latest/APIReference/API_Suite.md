---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Suite.html
---

# Suite
<a name="API_Suite"></a>

Represents a collection of one or more tests.

## Contents
<a name="API_Suite_Contents"></a>

 ** arn **   <a name="devicefarm-Type-Suite-arn"></a>
The suite's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** counters **   <a name="devicefarm-Type-Suite-counters"></a>
The suite's result counters.
Type: [Counters](API_Counters.md) object
Required: No

 ** created **   <a name="devicefarm-Type-Suite-created"></a>
When the suite was created.
Type: Timestamp
Required: No

 ** deviceMinutes **   <a name="devicefarm-Type-Suite-deviceMinutes"></a>
Represents the total (metered or unmetered) minutes used by the test suite.
Type: [DeviceMinutes](API_DeviceMinutes.md) object
Required: No

 ** message **   <a name="devicefarm-Type-Suite-message"></a>
A message about the suite's result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** name **   <a name="devicefarm-Type-Suite-name"></a>
The suite's name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** result **   <a name="devicefarm-Type-Suite-result"></a>
The suite's result.
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

 ** started **   <a name="devicefarm-Type-Suite-started"></a>
The suite's start time.
Type: Timestamp
Required: No

 ** status **   <a name="devicefarm-Type-Suite-status"></a>
The suite's status.
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

 ** stopped **   <a name="devicefarm-Type-Suite-stopped"></a>
The suite's stop time.
Type: Timestamp
Required: No

 ** type **   <a name="devicefarm-Type-Suite-type"></a>
The suite's type.
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
<a name="API_Suite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Suite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Suite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Suite)
