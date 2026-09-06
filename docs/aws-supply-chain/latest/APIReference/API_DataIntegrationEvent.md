---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationEvent.html
---

# DataIntegrationEvent
<a name="API_DataIntegrationEvent"></a>

The data integration event details.

## Contents
<a name="API_DataIntegrationEvent_Contents"></a>

 ** eventGroupId **   <a name="supplychain-Type-DataIntegrationEvent-eventGroupId"></a>
Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** eventId **   <a name="supplychain-Type-DataIntegrationEvent-eventId"></a>
The unique event identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** eventTimestamp **   <a name="supplychain-Type-DataIntegrationEvent-eventTimestamp"></a>
The event timestamp (in epoch seconds).
Type: Timestamp
Required: Yes

 ** eventType **   <a name="supplychain-Type-DataIntegrationEvent-eventType"></a>
The data event type.
Type: String
Valid Values: `scn.data.forecast | scn.data.inventorylevel | scn.data.inboundorder | scn.data.inboundorderline | scn.data.inboundorderlineschedule | scn.data.outboundorderline | scn.data.outboundshipment | scn.data.processheader | scn.data.processoperation | scn.data.processproduct | scn.data.reservation | scn.data.shipment | scn.data.shipmentstop | scn.data.shipmentstoporder | scn.data.supplyplan | scn.data.dataset`
Required: Yes

 ** instanceId **   <a name="supplychain-Type-DataIntegrationEvent-instanceId"></a>
The AWS Supply Chain instance identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** datasetTargetDetails **   <a name="supplychain-Type-DataIntegrationEvent-datasetTargetDetails"></a>
The target dataset details for a DATASET event type.
Type: [DataIntegrationEventDatasetTargetDetails](API_DataIntegrationEventDatasetTargetDetails.md) object
Required: No

## See Also
<a name="API_DataIntegrationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationEvent)
