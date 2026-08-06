---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateFleetPortSettings.html
---

# UpdateFleetPortSettings
<a name="API_UpdateFleetPortSettings"></a>

 **This API works with the following fleet types:** EC2

Updates permissions that allow inbound traffic to connect to game sessions in the fleet.

To update settings, specify the fleet ID to be updated and specify the changes to be made. List the permissions you want to add in `InboundPermissionAuthorizations`, and permissions you want to remove in `InboundPermissionRevocations`. Permissions to be removed must match existing fleet permissions.

If successful, the fleet identifiers for the updated fleet are returned. For fleets with remote locations, port setting updates can take time to propagate across all locations. You can check the status of updates in each location by calling `DescribeFleetPortSettings` with a location name.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_UpdateFleetPortSettings_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "InboundPermissionAuthorizations": [
      {
         "FromPort": {{number}},
         "IpRange": "{{string}}",
         "Protocol": "{{string}}",
         "ToPort": {{number}}
      }
   ],
   "InboundPermissionRevocations": [
      {
         "FromPort": {{number}},
         "IpRange": "{{string}}",
         "Protocol": "{{string}}",
         "ToPort": {{number}}
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateFleetPortSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_UpdateFleetPortSettings_RequestSyntax) **   <a name="gameliftservers-UpdateFleetPortSettings-request-FleetId"></a>
A unique identifier for the fleet to update port settings for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [InboundPermissionAuthorizations](#API_UpdateFleetPortSettings_RequestSyntax) **   <a name="gameliftservers-UpdateFleetPortSettings-request-InboundPermissionAuthorizations"></a>
A collection of port settings to be added to the fleet resource.
Type: Array of [IpPermission](API_IpPermission.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** [InboundPermissionRevocations](#API_UpdateFleetPortSettings_RequestSyntax) **   <a name="gameliftservers-UpdateFleetPortSettings-request-InboundPermissionRevocations"></a>
A collection of port settings to be removed from the fleet resource.
Type: Array of [IpPermission](API_IpPermission.md) objects
Array Members: Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_UpdateFleetPortSettings_ResponseSyntax"></a>

```
{
   "FleetArn": "string",
   "FleetId": "string"
}
```

## Response Elements
<a name="API_UpdateFleetPortSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_UpdateFleetPortSettings_ResponseSyntax) **   <a name="gameliftservers-UpdateFleetPortSettings-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_UpdateFleetPortSettings_ResponseSyntax) **   <a name="gameliftservers-UpdateFleetPortSettings-response-FleetId"></a>
A unique identifier for the fleet that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`

## Errors
<a name="API_UpdateFleetPortSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidFleetStatusException **
The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.
HTTP Status Code: 400

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_UpdateFleetPortSettings_Examples"></a>

### Update fleet to open to enable SSH access
<a name="API_UpdateFleetPortSettings_Example_1"></a>

The following example opens port 22 for SSH access:

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateFleetPortSettings_Example_1_Request"></a>

```
{
   "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
   "InboundPermissionAuthorizations": [
      {
         "FromPort": 22,
         "IpRange": "54.186.139.221/32",
         "Protocol": "TCP",
         "ToPort": 22
      }
   ]
}
```

#### Sample Response
<a name="API_UpdateFleetPortSettings_Example_1_Response"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
}
```

### Update fleet to enable Windows Remote Desktop access
<a name="API_UpdateFleetPortSettings_Example_2"></a>

The following example opens port 3389 for Windows Remote Desktop access:

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateFleetPortSettings_Example_2_Request"></a>

```
{
   "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
   "InboundPermissionAuthorizations": [
      {
         "FromPort": 3389,
         "IpRange": "54.186.139.221/32",
         "Protocol": "TCP",
         "ToPort": 3389
      }
   ]
}
```

#### Sample Response
<a name="API_UpdateFleetPortSettings_Example_2_Response"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
}
```

## See Also
<a name="API_UpdateFleetPortSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateFleetPortSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateFleetPortSettings)
