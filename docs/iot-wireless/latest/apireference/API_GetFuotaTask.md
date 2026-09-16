---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetFuotaTask.html
---

# GetFuotaTask
<a name="API_GetFuotaTask"></a>

Gets information about a FUOTA task.

## Request Syntax
<a name="API_GetFuotaTask_RequestSyntax"></a>

```
GET /fuota-tasks/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFuotaTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetFuotaTask_RequestSyntax) **   <a name="iotwireless-GetFuotaTask-request-uri-Id"></a>
The ID of a FUOTA task.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetFuotaTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFuotaTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedAt": number,
   "Description": "string",
   "Descriptor": "string",
   "FirmwareUpdateImage": "string",
   "FirmwareUpdateRole": "string",
   "FragmentIntervalMS": number,
   "FragmentSizeBytes": number,
   "Id": "string",
   "LoRaWAN": {
      "RfRegion": "string",
      "StartTime": "string"
   },
   "Name": "string",
   "RedundancyPercent": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_GetFuotaTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-Arn"></a>
The arn of a FUOTA task.
Type: String
Length Constraints: Maximum length of 128.

 ** [CreatedAt](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-CreatedAt"></a>
Created at timestamp for the resource.
Type: Timestamp

 ** [Description](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-Description"></a>
The description of the new resource.
Type: String
Length Constraints: Maximum length of 2048.

 ** [Descriptor](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-Descriptor"></a>
The descriptor is the metadata about the file that is transferred to the device using FUOTA, such as the software version. It is a binary field encoded in base64.
Type: String
Length Constraints: Maximum length of 332.
Pattern: `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`

 ** [FirmwareUpdateImage](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-FirmwareUpdateImage"></a>
The S3 URI points to a firmware update image that is to be used with a FUOTA task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [FirmwareUpdateRole](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-FirmwareUpdateRole"></a>
The firmware update role that is to be used with a FUOTA task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [FragmentIntervalMS](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-FragmentIntervalMS"></a>
The interval for sending fragments in milliseconds, rounded to the nearest second.
This interval only determines the timing for when the Cloud sends down the fragments to yor device. There can be a delay for when your device will receive these fragments. This delay depends on the device's class and the communication delay with the cloud.
Type: Integer
Valid Range: Minimum value of 1.

 ** [FragmentSizeBytes](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-FragmentSizeBytes"></a>
The size of each fragment in bytes. This parameter is supported only for FUOTA tasks with multicast groups.
Type: Integer
Valid Range: Minimum value of 1.

 ** [Id](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-Id"></a>
The ID of a FUOTA task.
Type: String
Length Constraints: Maximum length of 256.

 ** [LoRaWAN](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-LoRaWAN"></a>
The LoRaWAN information returned from getting a FUOTA task.
Type: [LoRaWANFuotaTaskGetInfo](API_LoRaWANFuotaTaskGetInfo.md) object

 ** [Name](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-Name"></a>
The name of a FUOTA task.
Type: String
Length Constraints: Maximum length of 256.

 ** [RedundancyPercent](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-RedundancyPercent"></a>
The percentage of the added fragments that are redundant. For example, if the size of the firmware image file is 100 bytes and the fragment size is 10 bytes, with `RedundancyPercent` set to 50(%), the final number of encoded fragments is (100 / 10) \+ (100 / 10 \* 50%) = 15.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [Status](#API_GetFuotaTask_ResponseSyntax) **   <a name="iotwireless-GetFuotaTask-response-Status"></a>
The status of a FUOTA task.
Type: String
Valid Values: `Pending | FuotaSession_Waiting | In_FuotaSession | FuotaDone | Delete_Waiting`

## Errors
<a name="API_GetFuotaTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

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
<a name="API_GetFuotaTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetFuotaTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetFuotaTask)
