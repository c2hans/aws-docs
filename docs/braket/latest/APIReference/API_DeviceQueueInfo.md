---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_DeviceQueueInfo.html
---

# DeviceQueueInfo
<a name="API_DeviceQueueInfo"></a>

Information about quantum tasks and hybrid jobs queued on a device.

## Contents
<a name="API_DeviceQueueInfo_Contents"></a>

 ** queue **   <a name="braket-Type-DeviceQueueInfo-queue"></a>
The name of the queue.
Type: String
Valid Values: `QUANTUM_TASKS_QUEUE | JOBS_QUEUE`
Required: Yes

 ** queueSize **   <a name="braket-Type-DeviceQueueInfo-queueSize"></a>
The number of hybrid jobs or quantum tasks in the queue for a given device.
Type: String
Required: Yes

 ** queuePriority **   <a name="braket-Type-DeviceQueueInfo-queuePriority"></a>
Optional. Specifies the priority of the queue. Quantum tasks in a priority queue are processed before the quantum tasks in a normal queue.
Type: String
Valid Values: `Normal | Priority`
Required: No

## See Also
<a name="API_DeviceQueueInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/DeviceQueueInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/DeviceQueueInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/DeviceQueueInfo)
