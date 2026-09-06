---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartConnection.html
---

# StartConnection
<a name="API_StartConnection"></a>

**Note**
 AWS uses this action to install Outpost servers.

 Starts the connection required for Outpost server installation.

 Use CloudTrail to monitor this action or AWS managed policy for AWS Outposts to secure it. For more information, see [AWS managed policies for AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/security-iam-awsmanpol.html) and [ Logging AWS Outposts API calls with AWS CloudTrail](https://docs.aws.amazon.com/outposts/latest/userguide/logging-using-cloudtrail.html) in the * AWS Outposts User Guide*.

## Request Syntax
<a name="API_StartConnection_RequestSyntax"></a>

```
POST /connections HTTP/1.1
Content-type: application/json

{
   "AssetId": "{{string}}",
   "ClientPublicKey": "{{string}}",
   "DeviceSerialNumber": "{{string}}",
   "NetworkInterfaceDeviceIndex": {{number}}
}
```

## URI Request Parameters
<a name="API_StartConnection_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssetId](#API_StartConnection_RequestSyntax) **   <a name="outposts-StartConnection-request-AssetId"></a>
 The ID of the Outpost server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`
Required: Yes

 ** [ClientPublicKey](#API_StartConnection_RequestSyntax) **   <a name="outposts-StartConnection-request-ClientPublicKey"></a>
 The public key of the client.
Type: String
Length Constraints: Fixed length of 44.
Pattern: `^[a-zA-Z0-9/+]{43}=$`
Required: Yes

 ** [DeviceSerialNumber](#API_StartConnection_RequestSyntax) **   <a name="outposts-StartConnection-request-DeviceSerialNumber"></a>
 The serial number of the dongle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`
Required: No

 ** [NetworkInterfaceDeviceIndex](#API_StartConnection_RequestSyntax) **   <a name="outposts-StartConnection-request-NetworkInterfaceDeviceIndex"></a>
 The device index of the network interface on the Outpost server.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

## Response Syntax
<a name="API_StartConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectionId": "string",
   "UnderlayIpAddress": "string"
}
```

## Response Elements
<a name="API_StartConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionId](#API_StartConnection_ResponseSyntax) **   <a name="outposts-StartConnection-response-ConnectionId"></a>
 The ID of the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[a-zA-Z0-9+/=]{1,1024}$`

 ** [UnderlayIpAddress](#API_StartConnection_ResponseSyntax) **   <a name="outposts-StartConnection-response-UnderlayIpAddress"></a>
 The underlay IP address.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 15.
Pattern: `^([0-9]{1,3}\.){3}[0-9]{1,3}$`

## Errors
<a name="API_StartConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_StartConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/StartConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/StartConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/StartConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/StartConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/StartConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/StartConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/StartConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/StartConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/StartConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/StartConnection)
