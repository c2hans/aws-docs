---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessDeviceImportTask.html
---

# UpdateWirelessDeviceImportTask
<a name="API_UpdateWirelessDeviceImportTask"></a>

Update an import task to add more devices to the task.

## Request Syntax
<a name="API_UpdateWirelessDeviceImportTask_RequestSyntax"></a>

```
PATCH /wireless_device_import_task/{{Id}} HTTP/1.1
Content-type: application/json

{
   "Sidewalk": {
      "DeviceCreationFile": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateWirelessDeviceImportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDeviceImportTask-request-uri-Id"></a>
The identifier of the import task to be updated.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateWirelessDeviceImportTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Sidewalk](#API_UpdateWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-UpdateWirelessDeviceImportTask-request-Sidewalk"></a>
The Sidewalk-related parameters of the import task to be updated.
Type: [SidewalkUpdateImportInfo](API_SidewalkUpdateImportInfo.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateWirelessDeviceImportTask_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateWirelessDeviceImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateWirelessDeviceImportTask_Errors"></a>

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
<a name="API_UpdateWirelessDeviceImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateWirelessDeviceImportTask)
