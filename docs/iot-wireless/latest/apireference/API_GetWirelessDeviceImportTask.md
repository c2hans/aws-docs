---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDeviceImportTask.html
---

# GetWirelessDeviceImportTask
<a name="API_GetWirelessDeviceImportTask"></a>

Get information about an import task and count of device onboarding summary information for the import task.

## Request Syntax
<a name="API_GetWirelessDeviceImportTask_RequestSyntax"></a>

```
GET /wireless_device_import_task/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWirelessDeviceImportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-request-uri-Id"></a>
The identifier of the import task for which information is requested.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetWirelessDeviceImportTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWirelessDeviceImportTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreationTime": "string",
   "DestinationName": "string",
   "FailedImportedDeviceCount": number,
   "Id": "string",
   "InitializedImportedDeviceCount": number,
   "OnboardedImportedDeviceCount": number,
   "PendingImportedDeviceCount": number,
   "Positioning": "string",
   "Sidewalk": {
      "DeviceCreationFileList": [ "string" ],
      "Positioning": {
         "DestinationName": "string"
      },
      "Role": "string"
   },
   "Status": "string",
   "StatusReason": "string"
}
```

## Response Elements
<a name="API_GetWirelessDeviceImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-Arn"></a>
The ARN (Amazon Resource Name) of the import task.
Type: String
Length Constraints: Maximum length of 128.

 ** [CreationTime](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-CreationTime"></a>
The time at which the import task was created.
Type: Timestamp

 ** [DestinationName](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-DestinationName"></a>
The name of the destination that's assigned to the wireless devices in the import task.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`

 ** [FailedImportedDeviceCount](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-FailedImportedDeviceCount"></a>
The number of devices in the import task that failed to onboard to the import task.
Type: Long

 ** [Id](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-Id"></a>
The identifier of the import task for which information is retrieved.
Type: String
Length Constraints: Maximum length of 256.

 ** [InitializedImportedDeviceCount](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-InitializedImportedDeviceCount"></a>
The number of devices in the import task that are waiting for the control log to start processing.
Type: Long

 ** [OnboardedImportedDeviceCount](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-OnboardedImportedDeviceCount"></a>
The number of devices in the import task that have been onboarded to the import task.
Type: Long

 ** [PendingImportedDeviceCount](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-PendingImportedDeviceCount"></a>
The number of devices in the import task that are waiting in the import task queue to be onboarded.
Type: Long

 ** [Positioning](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-Positioning"></a>
The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.
Type: String
Valid Values: `Enabled | Disabled`

 ** [Sidewalk](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-Sidewalk"></a>
The Sidewalk-related information about an import task.
Type: [SidewalkGetStartImportInfo](API_SidewalkGetStartImportInfo.md) object

 ** [Status](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-Status"></a>
The import task status.
Type: String
Valid Values: `INITIALIZING | INITIALIZED | PENDING | COMPLETE | FAILED | DELETING`

 ** [StatusReason](#API_GetWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-GetWirelessDeviceImportTask-response-StatusReason"></a>
The reason for the provided status information, such as a validation error that causes the import task to fail.
Type: String

## Errors
<a name="API_GetWirelessDeviceImportTask_Errors"></a>

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
<a name="API_GetWirelessDeviceImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetWirelessDeviceImportTask)
