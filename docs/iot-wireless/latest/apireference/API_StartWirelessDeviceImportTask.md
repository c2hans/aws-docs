---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartWirelessDeviceImportTask.html
---

# StartWirelessDeviceImportTask
<a name="API_StartWirelessDeviceImportTask"></a>

Start import task for provisioning Sidewalk devices in bulk using an S3 CSV file.

## Request Syntax
<a name="API_StartWirelessDeviceImportTask_RequestSyntax"></a>

```
POST /wireless_device_import_task HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "DestinationName": "{{string}}",
   "Positioning": "{{string}}",
   "Sidewalk": {
      "DeviceCreationFile": "{{string}}",
      "Positioning": {
         "DestinationName": "{{string}}"
      },
      "Role": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_StartWirelessDeviceImportTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartWirelessDeviceImportTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StartWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-StartWirelessDeviceImportTask-request-ClientRequestToken"></a>
Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [DestinationName](#API_StartWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-StartWirelessDeviceImportTask-request-DestinationName"></a>
The name of the Sidewalk destination that describes the IoT rule to route messages from the devices in the import task that are onboarded to AWS IoT Wireless.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** [Positioning](#API_StartWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-StartWirelessDeviceImportTask-request-Positioning"></a>
The integration status of the Device Location feature for Sidewalk devices.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [Sidewalk](#API_StartWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-StartWirelessDeviceImportTask-request-Sidewalk"></a>
The Sidewalk-related parameters for importing wireless devices that need to be provisioned in bulk.
Type: [SidewalkStartImportInfo](API_SidewalkStartImportInfo.md) object
Required: Yes

 ** [Tags](#API_StartWirelessDeviceImportTask_RequestSyntax) **   <a name="iotwireless-StartWirelessDeviceImportTask-request-Tags"></a>
The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_StartWirelessDeviceImportTask_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_StartWirelessDeviceImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_StartWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-StartWirelessDeviceImportTask-response-Arn"></a>
The ARN (Amazon Resource Name) of the import task.
Type: String
Length Constraints: Maximum length of 128.

 ** [Id](#API_StartWirelessDeviceImportTask_ResponseSyntax) **   <a name="iotwireless-StartWirelessDeviceImportTask-response-Id"></a>
The import task ID.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_StartWirelessDeviceImportTask_Errors"></a>

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
<a name="API_StartWirelessDeviceImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/StartWirelessDeviceImportTask)
