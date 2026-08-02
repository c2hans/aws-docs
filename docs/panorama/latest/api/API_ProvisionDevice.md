---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ProvisionDevice.html
---

# ProvisionDevice
<a name="API_ProvisionDevice"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Creates a device and returns a configuration archive. The configuration archive is a ZIP file that contains a provisioning certificate that is valid for 5 minutes. Name the configuration archive `certificates-omni_device-name.zip` and transfer it to the device within 5 minutes. Use the included USB storage device and connect it to the USB 3.0 port next to the HDMI output.

## Request Syntax
<a name="API_ProvisionDevice_RequestSyntax"></a>

```
POST /devices HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "NetworkingConfiguration": {
      "Ethernet0": {
         "ConnectionType": "{{string}}",
         "StaticIpConnectionInfo": {
            "DefaultGateway": "{{string}}",
            "Dns": [ "{{string}}" ],
            "IpAddress": "{{string}}",
            "Mask": "{{string}}"
         }
      },
      "Ethernet1": {
         "ConnectionType": "{{string}}",
         "StaticIpConnectionInfo": {
            "DefaultGateway": "{{string}}",
            "Dns": [ "{{string}}" ],
            "IpAddress": "{{string}}",
            "Mask": "{{string}}"
         }
      },
      "Ntp": {
         "NtpServers": [ "{{string}}" ]
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ProvisionDevice_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ProvisionDevice_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_ProvisionDevice_RequestSyntax) **   <a name="panorama-ProvisionDevice-request-Description"></a>
A description for the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [Name](#API_ProvisionDevice_RequestSyntax) **   <a name="panorama-ProvisionDevice-request-Name"></a>
A name for the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [NetworkingConfiguration](#API_ProvisionDevice_RequestSyntax) **   <a name="panorama-ProvisionDevice-request-NetworkingConfiguration"></a>
A networking configuration for the device.
Type: [NetworkPayload](API_NetworkPayload.md) object
Required: No

 ** [Tags](#API_ProvisionDevice_RequestSyntax) **   <a name="panorama-ProvisionDevice-request-Tags"></a>
Tags for the device.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ProvisionDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Certificates": blob,
   "DeviceId": "string",
   "IotThingName": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_ProvisionDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_ProvisionDevice_ResponseSyntax) **   <a name="panorama-ProvisionDevice-response-Arn"></a>
The device's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Certificates](#API_ProvisionDevice_ResponseSyntax) **   <a name="panorama-ProvisionDevice-response-Certificates"></a>
The device's configuration bundle.
Type: Base64-encoded binary data object

 ** [DeviceId](#API_ProvisionDevice_ResponseSyntax) **   <a name="panorama-ProvisionDevice-response-DeviceId"></a>
The device's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [IotThingName](#API_ProvisionDevice_ResponseSyntax) **   <a name="panorama-ProvisionDevice-response-IotThingName"></a>
The device's IoT thing name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Status](#API_ProvisionDevice_ResponseSyntax) **   <a name="panorama-ProvisionDevice-response-Status"></a>
The device's status.
Type: String
Valid Values: `AWAITING_PROVISIONING | PENDING | SUCCEEDED | FAILED | ERROR | DELETING`

## Errors
<a name="API_ProvisionDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would cause a limit to be exceeded.
 ** QuotaCode **
The name of the limit.
 ** ResourceId **
The target resource's ID.
 ** ResourceType **
The target resource's type.
 ** ServiceCode **
The name of the service.
HTTP Status Code: 402

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ProvisionDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/ProvisionDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ProvisionDevice)
