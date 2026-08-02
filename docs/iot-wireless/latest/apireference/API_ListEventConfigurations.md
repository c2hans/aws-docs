---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListEventConfigurations.html
---

# ListEventConfigurations
<a name="API_ListEventConfigurations"></a>

List event configurations where at least one event topic has been enabled.

## Request Syntax
<a name="API_ListEventConfigurations_RequestSyntax"></a>

```
GET /event-configurations?maxResults={{MaxResults}}&nextToken={{NextToken}}&resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEventConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListEventConfigurations_RequestSyntax) **   <a name="iotwireless-ListEventConfigurations-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [NextToken](#API_ListEventConfigurations_RequestSyntax) **   <a name="iotwireless-ListEventConfigurations-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Length Constraints: Maximum length of 4096.

 ** [ResourceType](#API_ListEventConfigurations_RequestSyntax) **   <a name="iotwireless-ListEventConfigurations-request-uri-ResourceType"></a>
Resource type to filter event configurations.
Valid Values: `SidewalkAccount | WirelessDevice | WirelessGateway`
Required: Yes

## Request Body
<a name="API_ListEventConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEventConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EventConfigurationsList": [
      {
         "Events": {
            "ConnectionStatus": {
               "LoRaWAN": {
                  "GatewayEuiEventTopic": "string"
               },
               "WirelessGatewayIdEventTopic": "string"
            },
            "DeviceRegistrationState": {
               "Sidewalk": {
                  "AmazonIdEventTopic": "string"
               },
               "WirelessDeviceIdEventTopic": "string"
            },
            "Join": {
               "LoRaWAN": {
                  "DevEuiEventTopic": "string"
               },
               "WirelessDeviceIdEventTopic": "string"
            },
            "MessageDeliveryStatus": {
               "Sidewalk": {
                  "AmazonIdEventTopic": "string"
               },
               "WirelessDeviceIdEventTopic": "string"
            },
            "Proximity": {
               "Sidewalk": {
                  "AmazonIdEventTopic": "string"
               },
               "WirelessDeviceIdEventTopic": "string"
            }
         },
         "Identifier": "string",
         "IdentifierType": "string",
         "PartnerType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEventConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventConfigurationsList](#API_ListEventConfigurations_ResponseSyntax) **   <a name="iotwireless-ListEventConfigurations-response-EventConfigurationsList"></a>
Event configurations of all events for a single resource.
Type: Array of [EventConfigurationItem](API_EventConfigurationItem.md) objects

 ** [NextToken](#API_ListEventConfigurations_ResponseSyntax) **   <a name="iotwireless-ListEventConfigurations-response-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Type: String
Length Constraints: Maximum length of 4096.

## Errors
<a name="API_ListEventConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListEventConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListEventConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListEventConfigurations)
