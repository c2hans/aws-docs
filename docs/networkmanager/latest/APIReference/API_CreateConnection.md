---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateConnection.html
---

# CreateConnection
<a name="API_CreateConnection"></a>

Creates a connection between two devices. The devices can be a physical or virtual appliance that connects to a third-party appliance in a VPC, or a physical appliance that connects to another physical appliance in an on-premises network.

## Request Syntax
<a name="API_CreateConnection_RequestSyntax"></a>

```
POST /global-networks/{{globalNetworkId}}/connections HTTP/1.1
Content-type: application/json

{
   "ConnectedDeviceId": "{{string}}",
   "ConnectedLinkId": "{{string}}",
   "Description": "{{string}}",
   "DeviceId": "{{string}}",
   "LinkId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalNetworkId](#API_CreateConnection_RequestSyntax) **   <a name="networkmanager-CreateConnection-request-uri-GlobalNetworkId"></a>
The ID of the global network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

## Request Body
<a name="API_CreateConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConnectedDeviceId](#API_CreateConnection_RequestSyntax) **   <a name="networkmanager-CreateConnection-request-ConnectedDeviceId"></a>
The ID of the second device in the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** [ConnectedLinkId](#API_CreateConnection_RequestSyntax) **   <a name="networkmanager-CreateConnection-request-ConnectedLinkId"></a>
The ID of the link for the second device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** [Description](#API_CreateConnection_RequestSyntax) **   <a name="networkmanager-CreateConnection-request-Description"></a>
A description of the connection.
Length Constraints: Maximum length of 256 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [DeviceId](#API_CreateConnection_RequestSyntax) **   <a name="networkmanager-CreateConnection-request-DeviceId"></a>
The ID of the first device in the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** [LinkId](#API_CreateConnection_RequestSyntax) **   <a name="networkmanager-CreateConnection-request-LinkId"></a>
The ID of the link for the first device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** [Tags](#API_CreateConnection_RequestSyntax) **   <a name="networkmanager-CreateConnection-request-Tags"></a>
The tags to apply to the resource during creation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Connection": {
      "ConnectedDeviceId": "string",
      "ConnectedLinkId": "string",
      "ConnectionArn": "string",
      "ConnectionId": "string",
      "CreatedAt": number,
      "Description": "string",
      "DeviceId": "string",
      "GlobalNetworkId": "string",
      "LinkId": "string",
      "State": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_CreateConnection_ResponseSyntax) **   <a name="networkmanager-CreateConnection-response-Connection"></a>
Information about the connection.
Type: [Connection](API_Connection.md) object

## Errors
<a name="API_CreateConnection_Errors"></a>

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

 ** ServiceQuotaExceededException **
A service limit was exceeded.
 ** LimitCode **
The limit code.
 ** Message **
The error message.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
 ** ServiceCode **
The service code.
HTTP Status Code: 402

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
<a name="API_CreateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
