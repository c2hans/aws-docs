---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDevicesForWirelessDeviceImportTask.html
---

# ListDevicesForWirelessDeviceImportTask
<a name="API_ListDevicesForWirelessDeviceImportTask"></a>

List the Sidewalk devices in an import task and their onboarding status.

## Request Syntax
<a name="API_ListDevicesForWirelessDeviceImportTask_RequestSyntax"></a>

```
GET /wireless_device_import_task?id={{Id}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDevicesForWirelessDeviceImportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListDevicesForWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-request-uri-Id"></a>
The identifier of the import task for which wireless devices are listed.
Length Constraints: Maximum length of 256.
Required: Yes

 ** [MaxResults](#API_ListDevicesForWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [NextToken](#API_ListDevicesForWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise `null` to receive the first set of results.
Length Constraints: Maximum length of 4096.

 ** [Status](#API_ListDevicesForWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-request-uri-Status"></a>
The status of the devices in the import task.
Valid Values: `INITIALIZED | PENDING | ONBOARDED | FAILED`

## Request Body
<a name="API_ListDevicesForWirelessDeviceImportTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDevicesForWirelessDeviceImportTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DestinationName": "string",
   "ImportedWirelessDeviceList": [
      {
         "Sidewalk": {
            "LastUpdateTime": "string",
            "OnboardingStatus": "string",
            "OnboardingStatusReason": "string",
            "SidewalkManufacturingSn": "string"
         }
      }
   ],
   "NextToken": "string",
   "Positioning": "string",
   "Sidewalk": {
      "Positioning": {
         "DestinationName": "string"
      }
   }
}
```

## Response Elements
<a name="API_ListDevicesForWirelessDeviceImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DestinationName](#API_ListDevicesForWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-response-DestinationName"></a>
The name of the Sidewalk destination that describes the IoT rule to route messages received from devices in an import task that are onboarded to AWS IoT Wireless.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`

 ** [ImportedWirelessDeviceList](#API_ListDevicesForWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-response-ImportedWirelessDeviceList"></a>
List of wireless devices in an import task and their onboarding status.
Type: Array of [ImportedWirelessDevice](API_ImportedWirelessDevice.md) objects

 ** [NextToken](#API_ListDevicesForWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-response-NextToken"></a>
The token to use to get the next set of results, or `null` if there are no additional results.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Positioning](#API_ListDevicesForWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-response-Positioning"></a>
The integration status of the Device Location feature for Sidewalk devices.
Type: String
Valid Values: `Enabled | Disabled`

 ** [Sidewalk](#API_ListDevicesForWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-ListDevicesForWirelessDeviceImportTask-response-Sidewalk"></a>
The Sidewalk object containing Sidewalk-related device information.
Type: [SidewalkListDevicesForImportInfo](API_SidewalkListDevicesForImportInfo.md) object

## Errors
<a name="API_ListDevicesForWirelessDeviceImportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Adding, updating, or deleting the resource can cause an inconsistent state.
 ** ResourceId **
Id of the resource in the conflicting operation.
 ** ResourceType **
Type of the resource in the conflicting operation.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListDevicesForWirelessDeviceImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListDevicesForWirelessDeviceImportTask)
