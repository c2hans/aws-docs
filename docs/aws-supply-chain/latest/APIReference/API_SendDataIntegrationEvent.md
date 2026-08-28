---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_SendDataIntegrationEvent.html
---

# SendDataIntegrationEvent
<a name="API_SendDataIntegrationEvent"></a>

Send the data payload for the event with real-time data for analysis or monitoring. The real-time data events are stored in an AWS service before being processed and stored in data lake.

## Request Syntax
<a name="API_SendDataIntegrationEvent_RequestSyntax"></a>

```
POST /api-data/data-integration/instance/{{instanceId}}/data-integration-events HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "data": "{{string}}",
   "datasetTarget": {
      "datasetIdentifier": "{{string}}",
      "operationType": "{{string}}"
   },
   "eventGroupId": "{{string}}",
   "eventTimestamp": {{number}},
   "eventType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendDataIntegrationEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_SendDataIntegrationEvent_RequestSyntax) **   <a name="supplychain-SendDataIntegrationEvent-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_SendDataIntegrationEvent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_SendDataIntegrationEvent_RequestSyntax) **   <a name="supplychain-SendDataIntegrationEvent-request-clientToken"></a>
The idempotent client token. The token is active for 8 hours, and within its lifetime, it ensures the request completes only once upon retry with same client token. If omitted, the AWS SDK generates a unique value so that AWS SDK can safely retry the request upon network errors.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 126.
Required: No

 ** [data](#API_SendDataIntegrationEvent_RequestSyntax) **   <a name="supplychain-SendDataIntegrationEvent-request-data"></a>
The data payload of the event, should follow the data schema of the target dataset, or see [Data entities supported in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html). To send single data record, use JsonObject format; to send multiple data records, use JsonArray format.
Note that for AWS Supply Chain dataset under **asc** namespace, it has a connection\_id internal field that is not allowed to be provided by client directly, they will be auto populated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: Yes

 ** [datasetTarget](#API_SendDataIntegrationEvent_RequestSyntax) **   <a name="supplychain-SendDataIntegrationEvent-request-datasetTarget"></a>
The target dataset configuration for **scn.data.dataset** event type.
Type: [DataIntegrationEventDatasetTargetConfiguration](API_DataIntegrationEventDatasetTargetConfiguration.md) object
Required: No

 ** [eventGroupId](#API_SendDataIntegrationEvent_RequestSyntax) **   <a name="supplychain-SendDataIntegrationEvent-request-eventGroupId"></a>
Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning. Noted under one eventGroupId of same eventType and instanceId, events are processed sequentially in the order they are received by the server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [eventTimestamp](#API_SendDataIntegrationEvent_RequestSyntax) **   <a name="supplychain-SendDataIntegrationEvent-request-eventTimestamp"></a>
The timestamp (in epoch seconds) associated with the event. If not provided, it will be assigned with current timestamp.
Type: Timestamp
Required: No

 ** [eventType](#API_SendDataIntegrationEvent_RequestSyntax) **   <a name="supplychain-SendDataIntegrationEvent-request-eventType"></a>
The data event type.
+  **scn.data.dataset** - Send data directly to any specified dataset.
+  **scn.data.supplyplan** - Send data to [supply\_plan](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/supply-plan-entity.html) dataset.
+  **scn.data.shipmentstoporder** - Send data to [shipment\_stop\_order](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-order-entity.html) dataset.
+  **scn.data.shipmentstop** - Send data to [shipment\_stop](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-entity.html) dataset.
+  **scn.data.shipment** - Send data to [shipment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-entity.html) dataset.
+  **scn.data.reservation** - Send data to [reservation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-reservation-entity.html) dataset.
+  **scn.data.processproduct** - Send data to [process\_product](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-product-entity.html) dataset.
+  **scn.data.processoperation** - Send data to [process\_operation](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-operation-entity.html) dataset.
+  **scn.data.processheader** - Send data to [process\_header](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-header-entity.html) dataset.
+  **scn.data.forecast** - Send data to [forecast](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-forecast-entity.html) dataset.
+  **scn.data.inventorylevel** - Send data to [inv\_level](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/inventory_mgmnt-inv-level-entity.html) dataset.
+  **scn.data.inboundorder** - Send data to [inbound\_order](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-entity.html) dataset.
+  **scn.data.inboundorderline** - Send data to [inbound\_order\_line](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-entity.html) dataset.
+  **scn.data.inboundorderlineschedule** - Send data to [inbound\_order\_line\_schedule](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-schedule-entity.html) dataset.
+  **scn.data.outboundorderline** - Send data to [outbound\_order\_line](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-order-line-entity.html) dataset.
+  **scn.data.outboundshipment** - Send data to [outbound\_shipment](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-shipment-entity.html) dataset.
Type: String
Valid Values: `scn.data.forecast | scn.data.inventorylevel | scn.data.inboundorder | scn.data.inboundorderline | scn.data.inboundorderlineschedule | scn.data.outboundorderline | scn.data.outboundshipment | scn.data.processheader | scn.data.processoperation | scn.data.processproduct | scn.data.reservation | scn.data.shipment | scn.data.shipmentstop | scn.data.shipmentstoporder | scn.data.supplyplan | scn.data.dataset`
Required: Yes

## Response Syntax
<a name="API_SendDataIntegrationEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "eventId": "string"
}
```

## Response Elements
<a name="API_SendDataIntegrationEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventId](#API_SendDataIntegrationEvent_ResponseSyntax) **   <a name="supplychain-SendDataIntegrationEvent-response-eventId"></a>
The unique event identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_SendDataIntegrationEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required privileges to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_SendDataIntegrationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/SendDataIntegrationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/SendDataIntegrationEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
