---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Job.html
---

# Job
<a name="API_Job"></a>

Represents a device.

## Contents
<a name="API_Job_Contents"></a>

 ** arn **   <a name="devicefarm-Type-Job-arn"></a>
The job's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** counters **   <a name="devicefarm-Type-Job-counters"></a>
The job's result counters.
Type: [Counters](API_Counters.md) object
Required: No

 ** created **   <a name="devicefarm-Type-Job-created"></a>
When the job was created.
Type: Timestamp
Required: No

 ** device **   <a name="devicefarm-Type-Job-device"></a>
The device (phone or tablet).
Type: [Device](API_Device.md) object
Required: No

 ** deviceMinutes **   <a name="devicefarm-Type-Job-deviceMinutes"></a>
Represents the total (metered or unmetered) minutes used by the job.
Type: [DeviceMinutes](API_DeviceMinutes.md) object
Required: No

 ** instanceArn **   <a name="devicefarm-Type-Job-instanceArn"></a>
The ARN of the instance.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** message **   <a name="devicefarm-Type-Job-message"></a>
A message about the job's result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** name **   <a name="devicefarm-Type-Job-name"></a>
The job's name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** result **   <a name="devicefarm-Type-Job-result"></a>
The job's result.
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

 ** started **   <a name="devicefarm-Type-Job-started"></a>
The job's start time.
Type: Timestamp
Required: No

 ** status **   <a name="devicefarm-Type-Job-status"></a>
The job's status.
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

 ** stopped **   <a name="devicefarm-Type-Job-stopped"></a>
The job's stop time.
Type: Timestamp
Required: No

 ** type **   <a name="devicefarm-Type-Job-type"></a>
The job's type.
Allowed values include the following:
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

 ** videoCapture **   <a name="devicefarm-Type-Job-videoCapture"></a>
This value is set to true if video capture is enabled. Otherwise, it is set to false.
Type: Boolean
Required: No

 ** videoEndpoint **   <a name="devicefarm-Type-Job-videoEndpoint"></a>
The endpoint for streaming device video.
Type: String
Required: No

## See Also
<a name="API_Job_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Job)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Job)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Job)
