---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessDevices.html
---

# ListWirelessDevices
<a name="API_ListWirelessDevices"></a>

Lists the wireless devices registered to your AWS account.

## Request Syntax
<a name="API_ListWirelessDevices_RequestSyntax"></a>

```
GET /wireless-devices?destinationName={{DestinationName}}&deviceProfileId={{DeviceProfileId}}&fuotaTaskId={{FuotaTaskId}}&maxResults={{MaxResults}}&multicastGroupId={{MulticastGroupId}}&nextToken={{NextToken}}&serviceProfileId={{ServiceProfileId}}&wirelessDeviceType={{WirelessDeviceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWirelessDevices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DestinationName](#API_ListWirelessDevices_RequestSyntax) **   <a name="iotwireless-ListWirelessDevices-request-uri-DestinationName"></a>
A filter to list only the wireless devices that use as uplink destination.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`

 ** [DeviceProfileId](#API_ListWirelessDevices_RequestSyntax) **   <a name="iotwireless-ListWirelessDevices-request-uri-DeviceProfileId"></a>
A filter to list only the wireless devices that use this device profile.
Length Constraints: Maximum length of 256.

 ** [FuotaTaskId](#API_ListWirelessDevices_RequestSyntax) **   <a name="iotwireless-ListWirelessDevices-request-uri-FuotaTaskId"></a>
The ID of a FUOTA task.
Length Constraints: Maximum length of 256.

 ** [MaxResults](#API_ListWirelessDevices_RequestSyntax) **   <a name="iotwireless-ListWirelessDevices-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [MulticastGroupId](#API_ListWirelessDevices_RequestSyntax) **   <a name="iotwireless-ListWirelessDevices-request-uri-MulticastGroupId"></a>
The ID of the multicast group.
Length Constraints: Maximum length of 256.

 ** [NextToken](#API_ListWirelessDevices_RequestSyntax) **   <a name="iotwireless-ListWirelessDevices-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Length Constraints: Maximum length of 4096.

 ** [ServiceProfileId](#API_ListWirelessDevices_RequestSyntax) **   <a name="iotwireless-ListWirelessDevices-request-uri-ServiceProfileId"></a>
A filter to list only the wireless devices that use this service profile.
Length Constraints: Maximum length of 256.

 ** [WirelessDeviceType](#API_ListWirelessDevices_RequestSyntax) **   <a name="iotwireless-ListWirelessDevices-request-uri-WirelessDeviceType"></a>
A filter to list only the wireless devices that use this wireless device type.
Valid Values: `Sidewalk | LoRaWAN`

## Request Body
<a name="API_ListWirelessDevices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWirelessDevices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "WirelessDeviceList": [
      {
         "Arn": "string",
         "DestinationName": "string",
         "FuotaDeviceStatus": "string",
         "Id": "string",
         "LastUplinkReceivedAt": "string",
         "LoRaWAN": {
            "DevEui": "string"
         },
         "McGroupId": number,
         "MulticastDeviceStatus": "string",
         "Name": "string",
         "Positioning": "string",
         "Sidewalk": {
            "AmazonId": "string",
            "DeviceCertificates": [
               {
                  "SigningAlg": "string",
                  "Value": "string"
               }
            ],
            "DeviceProfileId": "string",
            "Positioning": {
               "DestinationName": "string"
            },
            "SidewalkId": "string",
            "SidewalkManufacturingSn": "string",
            "Status": "string"
         },
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWirelessDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWirelessDevices_ResponseSyntax) **   <a name="iotwireless-ListWirelessDevices-response-NextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String
Length Constraints: Maximum length of 4096.

 ** [WirelessDeviceList](#API_ListWirelessDevices_ResponseSyntax) **   <a name="iotwireless-ListWirelessDevices-response-WirelessDeviceList"></a>
The ID of the wireless device.
Type: Array of [WirelessDeviceStatistics](API_WirelessDeviceStatistics.md) objects

## Errors
<a name="API_ListWirelessDevices_Errors"></a>

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
<a name="API_ListWirelessDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListWirelessDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListWirelessDevices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
