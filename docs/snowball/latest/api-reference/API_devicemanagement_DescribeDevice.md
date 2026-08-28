---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_DescribeDevice.html
---

# DescribeDevice
<a name="API_devicemanagement_DescribeDevice"></a>

Checks device-specific information, such as the device type, software version, IP addresses, and lock status.

## Request Syntax
<a name="API_devicemanagement_DescribeDevice_RequestSyntax"></a>

```
POST /managed-device/{{managedDeviceId}}/describe HTTP/1.1
```

## URI Request Parameters
<a name="API_devicemanagement_DescribeDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [managedDeviceId](#API_devicemanagement_DescribeDevice_RequestSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-request-uri-managedDeviceId"></a>
The ID of the device that you are checking the information of.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_devicemanagement_DescribeDevice_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_devicemanagement_DescribeDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associatedWithJob": "string",
   "deviceCapacities": [
      {
         "available": number,
         "name": "string",
         "total": number,
         "unit": "string",
         "used": number
      }
   ],
   "deviceState": "string",
   "deviceType": "string",
   "lastReachedOutAt": number,
   "lastUpdatedAt": number,
   "managedDeviceArn": "string",
   "managedDeviceId": "string",
   "physicalNetworkInterfaces": [
      {
         "defaultGateway": "string",
         "ipAddress": "string",
         "ipAddressAssignment": "string",
         "macAddress": "string",
         "netmask": "string",
         "physicalConnectorType": "string",
         "physicalNetworkInterfaceId": "string"
      }
   ],
   "software": {
      "installedVersion": "string",
      "installingVersion": "string",
      "installState": "string"
   },
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_devicemanagement_DescribeDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedWithJob](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-associatedWithJob"></a>
The ID of the job used when ordering the device.
Type: String

 ** [deviceCapacities](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-deviceCapacities"></a>
The hardware specifications of the device.
Type: Array of [Capacity](API_devicemanagement_Capacity.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [deviceState](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-deviceState"></a>
The current state of the device.
Type: String
Valid Values: `UNLOCKED | LOCKED | UNLOCKING`

 ** [deviceType](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-deviceType"></a>
The type of AWS Snow Family device.
Type: String

 ** [lastReachedOutAt](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-lastReachedOutAt"></a>
When the device last contacted the AWS Cloud. Indicates that the device is online.
Type: Timestamp

 ** [lastUpdatedAt](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-lastUpdatedAt"></a>
When the device last pushed an update to the AWS Cloud. Indicates when the device cache was refreshed.
Type: Timestamp

 ** [managedDeviceArn](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-managedDeviceArn"></a>
The Amazon Resource Name (ARN) of the device.
Type: String

 ** [managedDeviceId](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-managedDeviceId"></a>
The ID of the device that you checked the information for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [physicalNetworkInterfaces](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-physicalNetworkInterfaces"></a>
The network interfaces available on the device.
Type: Array of [PhysicalNetworkInterface](API_devicemanagement_PhysicalNetworkInterface.md) objects

 ** [software](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-software"></a>
The software installed on the device.
Type: [SoftwareInformation](API_devicemanagement_SoftwareInformation.md) object

 ** [tags](#API_devicemanagement_DescribeDevice_ResponseSyntax) **   <a name="Snowball-devicemanagement_DescribeDevice-response-tags"></a>
Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.
Type: String to string map

## Errors
<a name="API_devicemanagement_DescribeDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_devicemanagement_DescribeDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/DescribeDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/DescribeDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
