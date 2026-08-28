---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DescribeDevice.html
---

# DescribeDevice
<a name="API_DescribeDevice"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns information about a device.

## Request Syntax
<a name="API_DescribeDevice_RequestSyntax"></a>

```
GET /devices/{{DeviceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceId](#API_DescribeDevice_RequestSyntax) **   <a name="panorama-DescribeDevice-request-uri-DeviceId"></a>
The device's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

## Request Body
<a name="API_DescribeDevice_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AlternateSoftwares": [
      {
         "Version": "string"
      }
   ],
   "Arn": "string",
   "Brand": "string",
   "CreatedTime": number,
   "CurrentNetworkingStatus": {
      "Ethernet0Status": {
         "ConnectionStatus": "string",
         "HwAddress": "string",
         "IpAddress": "string"
      },
      "Ethernet1Status": {
         "ConnectionStatus": "string",
         "HwAddress": "string",
         "IpAddress": "string"
      },
      "LastUpdatedTime": number,
      "NtpStatus": {
         "ConnectionStatus": "string",
         "IpAddress": "string",
         "NtpServerName": "string"
      }
   },
   "CurrentSoftware": "string",
   "Description": "string",
   "DeviceAggregatedStatus": "string",
   "DeviceConnectionStatus": "string",
   "DeviceId": "string",
   "LatestAlternateSoftware": "string",
   "LatestDeviceJob": {
      "ImageVersion": "string",
      "JobType": "string",
      "Status": "string"
   },
   "LatestSoftware": "string",
   "LeaseExpirationTime": number,
   "Name": "string",
   "NetworkingConfiguration": {
      "Ethernet0": {
         "ConnectionType": "string",
         "StaticIpConnectionInfo": {
            "DefaultGateway": "string",
            "Dns": [ "string" ],
            "IpAddress": "string",
            "Mask": "string"
         }
      },
      "Ethernet1": {
         "ConnectionType": "string",
         "StaticIpConnectionInfo": {
            "DefaultGateway": "string",
            "Dns": [ "string" ],
            "IpAddress": "string",
            "Mask": "string"
         }
      },
      "Ntp": {
         "NtpServers": [ "string" ]
      }
   },
   "ProvisioningStatus": "string",
   "SerialNumber": "string",
   "Tags": {
      "string" : "string"
   },
   "Type": "string"
}
```

## Response Elements
<a name="API_DescribeDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AlternateSoftwares](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-AlternateSoftwares"></a>
Beta software releases available for the device.
Type: Array of [AlternateSoftwareMetadata](API_AlternateSoftwareMetadata.md) objects

 ** [Arn](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-Arn"></a>
The device's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Brand](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-Brand"></a>
The device's maker.
Type: String
Valid Values: `AWS_PANORAMA | LENOVO`

 ** [CreatedTime](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-CreatedTime"></a>
When the device was created.
Type: Timestamp

 ** [CurrentNetworkingStatus](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-CurrentNetworkingStatus"></a>
The device's networking status.
Type: [NetworkStatus](API_NetworkStatus.md) object

 ** [CurrentSoftware](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-CurrentSoftware"></a>
The device's current software version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Description](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-Description"></a>
The device's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [DeviceAggregatedStatus](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-DeviceAggregatedStatus"></a>
A device's aggregated status. Including the device's connection status, provisioning status, and lease status.
Type: String
Valid Values: `ERROR | AWAITING_PROVISIONING | PENDING | FAILED | DELETING | ONLINE | OFFLINE | LEASE_EXPIRED | UPDATE_NEEDED | REBOOTING`

 ** [DeviceConnectionStatus](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-DeviceConnectionStatus"></a>
The device's connection status.
Type: String
Valid Values: `ONLINE | OFFLINE | AWAITING_CREDENTIALS | NOT_AVAILABLE | ERROR`

 ** [DeviceId](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-DeviceId"></a>
The device's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [LatestAlternateSoftware](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-LatestAlternateSoftware"></a>
The most recent beta software release.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [LatestDeviceJob](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-LatestDeviceJob"></a>
A device's latest job. Includes the target image version, and the job status.
Type: [LatestDeviceJob](API_LatestDeviceJob.md) object

 ** [LatestSoftware](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-LatestSoftware"></a>
The latest software version available for the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [LeaseExpirationTime](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-LeaseExpirationTime"></a>
The device's lease expiration time.
Type: Timestamp

 ** [Name](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-Name"></a>
The device's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [NetworkingConfiguration](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-NetworkingConfiguration"></a>
The device's networking configuration.
Type: [NetworkPayload](API_NetworkPayload.md) object

 ** [ProvisioningStatus](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-ProvisioningStatus"></a>
The device's provisioning status.
Type: String
Valid Values: `AWAITING_PROVISIONING | PENDING | SUCCEEDED | FAILED | ERROR | DELETING`

 ** [SerialNumber](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-SerialNumber"></a>
The device's serial number.
Type: String
Pattern: `[0-9]{1,20}`

 ** [Tags](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-Tags"></a>
The device's tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`

 ** [Type](#API_DescribeDevice_ResponseSyntax) **   <a name="panorama-DescribeDevice-response-Type"></a>
The device's type.
Type: String
Valid Values: `PANORAMA_APPLIANCE_DEVELOPER_KIT | PANORAMA_APPLIANCE`

## Errors
<a name="API_DescribeDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 404

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
<a name="API_DescribeDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/DescribeDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DescribeDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
