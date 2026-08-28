---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetConnectPeer.html
---

# GetConnectPeer
<a name="API_GetConnectPeer"></a>

Returns information about a core network Connect peer.

## Request Syntax
<a name="API_GetConnectPeer_RequestSyntax"></a>

```
GET /connect-peers/{{connectPeerId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnectPeer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectPeerId](#API_GetConnectPeer_RequestSyntax) **   <a name="networkmanager-GetConnectPeer-request-uri-ConnectPeerId"></a>
The ID of the Connect peer.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^connect-peer-([0-9a-f]{8,17})$`
Required: Yes

## Request Body
<a name="API_GetConnectPeer_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnectPeer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectPeer": {
      "Configuration": {
         "BgpConfigurations": [
            {
               "CoreNetworkAddress": "string",
               "CoreNetworkAsn": number,
               "PeerAddress": "string",
               "PeerAsn": number
            }
         ],
         "CoreNetworkAddress": "string",
         "InsideCidrBlocks": [ "string" ],
         "PeerAddress": "string",
         "Protocol": "string"
      },
      "ConnectAttachmentId": "string",
      "ConnectPeerId": "string",
      "CoreNetworkId": "string",
      "CreatedAt": number,
      "EdgeLocation": "string",
      "LastModificationErrors": [
         {
            "Code": "string",
            "Message": "string",
            "RequestId": "string",
            "ResourceArn": "string"
         }
      ],
      "State": "string",
      "SubnetArn": "string",
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
<a name="API_GetConnectPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectPeer](#API_GetConnectPeer_ResponseSyntax) **   <a name="networkmanager-GetConnectPeer-response-ConnectPeer"></a>
Returns information about a core network Connect peer.
Type: [ConnectPeer](API_ConnectPeer.md) object

## Errors
<a name="API_GetConnectPeer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetConnectPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetConnectPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetConnectPeer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
