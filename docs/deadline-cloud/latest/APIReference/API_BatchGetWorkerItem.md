---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetWorkerItem.html
---

# BatchGetWorkerItem
<a name="API_BatchGetWorkerItem"></a>

The details of a worker returned in a batch get operation.

## Contents
<a name="API_BatchGetWorkerItem_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-BatchGetWorkerItem-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-BatchGetWorkerItem-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetWorkerItem-farmId"></a>
The farm ID of the worker.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** fleetId **   <a name="deadlinecloud-Type-BatchGetWorkerItem-fleetId"></a>
The fleet ID of the worker.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** status **   <a name="deadlinecloud-Type-BatchGetWorkerItem-status"></a>
The status of the worker.
Type: String
Valid Values: `CREATED | STARTED | STOPPING | STOPPED | NOT_RESPONDING | NOT_COMPATIBLE | RUNNING | IDLE`
Required: Yes

 ** workerId **   <a name="deadlinecloud-Type-BatchGetWorkerItem-workerId"></a>
The worker ID.
Type: String
Pattern: `worker-[0-9a-f]{32}`
Required: Yes

 ** hostProperties **   <a name="deadlinecloud-Type-BatchGetWorkerItem-hostProperties"></a>
The host properties for the worker.
Type: [HostPropertiesResponse](API_HostPropertiesResponse.md) object
Required: No

 ** log **   <a name="deadlinecloud-Type-BatchGetWorkerItem-log"></a>
The log configuration for the worker.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-BatchGetWorkerItem-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-BatchGetWorkerItem-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_BatchGetWorkerItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetWorkerItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetWorkerItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetWorkerItem)
