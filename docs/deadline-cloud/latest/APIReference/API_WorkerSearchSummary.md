---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_WorkerSearchSummary.html
---

# WorkerSearchSummary
<a name="API_WorkerSearchSummary"></a>

The details of a worker search.

## Contents
<a name="API_WorkerSearchSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-WorkerSearchSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="deadlinecloud-Type-WorkerSearchSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: No

 ** fleetId **   <a name="deadlinecloud-Type-WorkerSearchSummary-fleetId"></a>
The fleet ID.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: No

 ** hostProperties **   <a name="deadlinecloud-Type-WorkerSearchSummary-hostProperties"></a>
Provides the Amazon EC2 instance properties of the worker host.
Type: [HostPropertiesResponse](API_HostPropertiesResponse.md) object
Required: No

 ** status **   <a name="deadlinecloud-Type-WorkerSearchSummary-status"></a>
The status of the worker search.
Type: String
Valid Values: `CREATED | STARTED | STOPPING | STOPPED | NOT_RESPONDING | NOT_COMPATIBLE | RUNNING | IDLE`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-WorkerSearchSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-WorkerSearchSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

 ** workerId **   <a name="deadlinecloud-Type-WorkerSearchSummary-workerId"></a>
The worker ID.
Type: String
Pattern: `worker-[0-9a-f]{32}`
Required: No

## See Also
<a name="API_WorkerSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerSearchSummary)
