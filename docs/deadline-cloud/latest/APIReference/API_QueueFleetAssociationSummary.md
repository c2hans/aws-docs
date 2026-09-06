---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_QueueFleetAssociationSummary.html
---

# QueueFleetAssociationSummary
<a name="API_QueueFleetAssociationSummary"></a>

The details of a queue-fleet association.

## Contents
<a name="API_QueueFleetAssociationSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-QueueFleetAssociationSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-QueueFleetAssociationSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** fleetId **   <a name="deadlinecloud-Type-QueueFleetAssociationSummary-fleetId"></a>
The fleet ID.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-QueueFleetAssociationSummary-queueId"></a>
The queue ID.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** status **   <a name="deadlinecloud-Type-QueueFleetAssociationSummary-status"></a>
The status of task scheduling in the queue-fleet association.
+  `ACTIVE`–Association is active.
+  `STOP_SCHEDULING_AND_COMPLETE_TASKS`–Association has stopped scheduling new tasks and is completing current tasks.
+  `STOP_SCHEDULING_AND_CANCEL_TASKS`–Association has stopped scheduling new tasks and is canceling current tasks.
+  `STOPPED`–Association has been stopped.
Type: String
Valid Values: `ACTIVE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS | STOPPED`
Required: Yes

 ** updatedAt **   <a name="deadlinecloud-Type-QueueFleetAssociationSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-QueueFleetAssociationSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_QueueFleetAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueFleetAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueFleetAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueFleetAssociationSummary)
