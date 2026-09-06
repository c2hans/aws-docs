---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataIntegrationEvents.html
---

# ListDataIntegrationEvents
<a name="API_ListDataIntegrationEvents"></a>

Enables you to programmatically list all data integration events for the provided AWS Supply Chain instance. Data integration events older than 30 days are not returned in the response.

## Request Syntax
<a name="API_ListDataIntegrationEvents_RequestSyntax"></a>

```
GET /api-data/data-integration/instance/{{instanceId}}/data-integration-events?eventType={{eventType}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataIntegrationEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [eventType](#API_ListDataIntegrationEvents_RequestSyntax) **   <a name="supplychain-ListDataIntegrationEvents-request-uri-eventType"></a>
List data integration events for the specified eventType.
Valid Values: `scn.data.forecast | scn.data.inventorylevel | scn.data.inboundorder | scn.data.inboundorderline | scn.data.inboundorderlineschedule | scn.data.outboundorderline | scn.data.outboundshipment | scn.data.processheader | scn.data.processoperation | scn.data.processproduct | scn.data.reservation | scn.data.shipment | scn.data.shipmentstop | scn.data.shipmentstoporder | scn.data.supplyplan | scn.data.dataset`

 ** [instanceId](#API_ListDataIntegrationEvents_RequestSyntax) **   <a name="supplychain-ListDataIntegrationEvents-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [maxResults](#API_ListDataIntegrationEvents_RequestSyntax) **   <a name="supplychain-ListDataIntegrationEvents-request-uri-maxResults"></a>
Specify the maximum number of data integration events to fetch in one paginated request.
Valid Range: Minimum value of 1. Maximum value of 20.

 ** [nextToken](#API_ListDataIntegrationEvents_RequestSyntax) **   <a name="supplychain-ListDataIntegrationEvents-request-uri-nextToken"></a>
The pagination token to fetch the next page of the data integration events.
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Request Body
<a name="API_ListDataIntegrationEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataIntegrationEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "events": [
      {
         "datasetTargetDetails": {
            "datasetIdentifier": "string",
            "datasetLoadExecution": {
               "message": "string",
               "status": "string"
            },
            "operationType": "string"
         },
         "eventGroupId": "string",
         "eventId": "string",
         "eventTimestamp": number,
         "eventType": "string",
         "instanceId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataIntegrationEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_ListDataIntegrationEvents_ResponseSyntax) **   <a name="supplychain-ListDataIntegrationEvents-response-events"></a>
The list of data integration events.
Type: Array of [DataIntegrationEvent](API_DataIntegrationEvent.md) objects

 ** [nextToken](#API_ListDataIntegrationEvents_ResponseSyntax) **   <a name="supplychain-ListDataIntegrationEvents-response-nextToken"></a>
The pagination token to fetch the next page of the ListDataIntegrationEvents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Errors
<a name="API_ListDataIntegrationEvents_Errors"></a>

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
<a name="API_ListDataIntegrationEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/ListDataIntegrationEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/ListDataIntegrationEvents)
