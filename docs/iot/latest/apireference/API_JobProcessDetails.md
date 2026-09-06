---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_JobProcessDetails.html
---

# JobProcessDetails
<a name="API_JobProcessDetails"></a>

The job process details.

## Contents
<a name="API_JobProcessDetails_Contents"></a>

 ** numberOfCanceledThings **   <a name="iot-Type-JobProcessDetails-numberOfCanceledThings"></a>
The number of things that cancelled the job.
Type: Integer
Required: No

 ** numberOfFailedThings **   <a name="iot-Type-JobProcessDetails-numberOfFailedThings"></a>
The number of things that failed executing the job.
Type: Integer
Required: No

 ** numberOfInProgressThings **   <a name="iot-Type-JobProcessDetails-numberOfInProgressThings"></a>
The number of things currently executing the job.
Type: Integer
Required: No

 ** numberOfQueuedThings **   <a name="iot-Type-JobProcessDetails-numberOfQueuedThings"></a>
The number of things that are awaiting execution of the job.
Type: Integer
Required: No

 ** numberOfRejectedThings **   <a name="iot-Type-JobProcessDetails-numberOfRejectedThings"></a>
The number of things that rejected the job.
Type: Integer
Required: No

 ** numberOfRemovedThings **   <a name="iot-Type-JobProcessDetails-numberOfRemovedThings"></a>
The number of things that are no longer scheduled to execute the job because they have been deleted or have been removed from the group that was a target of the job.
Type: Integer
Required: No

 ** numberOfSucceededThings **   <a name="iot-Type-JobProcessDetails-numberOfSucceededThings"></a>
The number of things which successfully completed the job.
Type: Integer
Required: No

 ** numberOfTimedOutThings **   <a name="iot-Type-JobProcessDetails-numberOfTimedOutThings"></a>
The number of things whose job execution status is `TIMED_OUT`.
Type: Integer
Required: No

 ** processingTargets **   <a name="iot-Type-JobProcessDetails-processingTargets"></a>
The target devices to which the job execution is being rolled out. This value will be null after the job execution has finished rolling out to all the target devices.
Type: Array of strings
Required: No

## See Also
<a name="API_JobProcessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/JobProcessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/JobProcessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/JobProcessDetails)
