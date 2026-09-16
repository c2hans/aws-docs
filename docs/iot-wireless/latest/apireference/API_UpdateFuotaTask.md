---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateFuotaTask.html
---

# UpdateFuotaTask
<a name="API_UpdateFuotaTask"></a>

Updates properties of a FUOTA task.

## Request Syntax
<a name="API_UpdateFuotaTask_RequestSyntax"></a>

```
PATCH /fuota-tasks/{{Id}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Descriptor": "{{string}}",
   "FirmwareUpdateImage": "{{string}}",
   "FirmwareUpdateRole": "{{string}}",
   "FragmentIntervalMS": {{number}},
   "FragmentSizeBytes": {{number}},
   "LoRaWAN": {
      "RfRegion": "{{string}}"
   },
   "Name": "{{string}}",
   "RedundancyPercent": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateFuotaTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-uri-Id"></a>
The ID of a FUOTA task.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateFuotaTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-Description"></a>
The description of the new resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [Descriptor](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-Descriptor"></a>
The descriptor is the metadata about the file that is transferred to the device using FUOTA, such as the software version. It is a binary field encoded in base64.
Type: String
Length Constraints: Maximum length of 332.
Pattern: `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
Required: No

 ** [FirmwareUpdateImage](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-FirmwareUpdateImage"></a>
The S3 URI points to a firmware update image that is to be used with a FUOTA task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [FirmwareUpdateRole](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-FirmwareUpdateRole"></a>
The firmware update role that is to be used with a FUOTA task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [FragmentIntervalMS](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-FragmentIntervalMS"></a>
The interval for sending fragments in milliseconds, rounded to the nearest second.
This interval only determines the timing for when the Cloud sends down the fragments to yor device. There can be a delay for when your device will receive these fragments. This delay depends on the device's class and the communication delay with the cloud.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [FragmentSizeBytes](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-FragmentSizeBytes"></a>
The size of each fragment in bytes. This parameter is supported only for FUOTA tasks with multicast groups.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [LoRaWAN](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-LoRaWAN"></a>
The LoRaWAN information used with a FUOTA task.
Type: [LoRaWANFuotaTask](API_LoRaWANFuotaTask.md) object
Required: No

 ** [Name](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-Name"></a>
The name of a FUOTA task.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [RedundancyPercent](#API_UpdateFuotaTask_RequestSyntax) **   <a name="iotwireless-UpdateFuotaTask-request-RedundancyPercent"></a>
The percentage of the added fragments that are redundant. For example, if the size of the firmware image file is 100 bytes and the fragment size is 10 bytes, with `RedundancyPercent` set to 50(%), the final number of encoded fragments is (100 / 10) \+ (100 / 10 \* 50%) = 15.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_UpdateFuotaTask_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateFuotaTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateFuotaTask_Errors"></a>

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
<a name="API_UpdateFuotaTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateFuotaTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateFuotaTask)
