---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TimeoutConfig.html
---

# TimeoutConfig
<a name="API_TimeoutConfig"></a>

Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.

## Contents
<a name="API_TimeoutConfig_Contents"></a>

 ** inProgressTimeoutInMinutes **   <a name="iot-Type-TimeoutConfig-inProgressTimeoutInMinutes"></a>
Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can't be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN\_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal `TIMED_OUT` status.
Type: Long
Required: No

## See Also
<a name="API_TimeoutConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TimeoutConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TimeoutConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TimeoutConfig)
