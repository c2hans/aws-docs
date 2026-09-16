---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateDevice.html
---

# UpdateDevice
<a name="API_UpdateDevice"></a>

Updates the details for an existing device. To remove information for any of the parameters, specify an empty string.

## Request Syntax
<a name="API_UpdateDevice_RequestSyntax"></a>

```
PATCH /global-networks/{{globalNetworkId}}/devices/{{deviceId}} HTTP/1.1
Content-type: application/json

{
   "AWSLocation": {
      "SubnetArn": "{{string}}",
      "Zone": "{{string}}"
   },
   "Description": "{{string}}",
   "Location": {
      "Address": "{{string}}",
      "Latitude": "{{string}}",
      "Longitude": "{{string}}"
   },
   "Model": "{{string}}",
   "SerialNumber": "{{string}}",
   "SiteId": "{{string}}",
   "Type": "{{string}}",
   "Vendor": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [deviceId](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-uri-DeviceId"></a>
The ID of the device.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** [globalNetworkId](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-uri-GlobalNetworkId"></a>
The ID of the global network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

## Request Body
<a name="API_UpdateDevice_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AWSLocation](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-AWSLocation"></a>
The AWS location of the device, if applicable. For an on-premises device, you can omit this parameter.
Type: [AWSLocation](API_AWSLocation.md) object
Required: No

 ** [Description](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-Description"></a>
A description of the device.
Constraints: Maximum length of 256 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Location](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-Location"></a>
Describes a location.
Type: [Location](API_Location.md) object
Required: No

 ** [Model](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-Model"></a>
The model of the device.
Constraints: Maximum length of 128 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [SerialNumber](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-SerialNumber"></a>
The serial number of the device.
Constraints: Maximum length of 128 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [SiteId](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-SiteId"></a>
The ID of the site.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** [Type](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-Type"></a>
The type of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Vendor](#API_UpdateDevice_RequestSyntax) **   <a name="networkmanager-UpdateDevice-request-Vendor"></a>
The vendor of the device.
Constraints: Maximum length of 128 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_UpdateDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Device": {
      "AWSLocation": {
         "SubnetArn": "string",
         "Zone": "string"
      },
      "CreatedAt": number,
      "Description": "string",
      "DeviceArn": "string",
      "DeviceId": "string",
      "GlobalNetworkId": "string",
      "Location": {
         "Address": "string",
         "Latitude": "string",
         "Longitude": "string"
      },
      "Model": "string",
      "SerialNumber": "string",
      "SiteId": "string",
      "State": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "Type": "string",
      "Vendor": "string"
   }
}
```

## Response Elements
<a name="API_UpdateDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Device](#API_UpdateDevice_ResponseSyntax) **   <a name="networkmanager-UpdateDevice-response-Device"></a>
Information about the device.
Type: [Device](API_Device.md) object

## Errors
<a name="API_UpdateDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/UpdateDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/UpdateDevice)
