---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DisassociateConnectPeer.html
---

# DisassociateConnectPeer
<a name="API_DisassociateConnectPeer"></a>

Disassociates a core network Connect peer from a device and a link.

## Request Syntax
<a name="API_DisassociateConnectPeer_RequestSyntax"></a>

```
DELETE /global-networks/{{globalNetworkId}}/connect-peer-associations/{{connectPeerId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateConnectPeer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectPeerId](#API_DisassociateConnectPeer_RequestSyntax) **   <a name="networkmanager-DisassociateConnectPeer-request-uri-ConnectPeerId"></a>
The ID of the Connect peer to disassociate from a device.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^connect-peer-([0-9a-f]{8,17})$`
Required: Yes

 ** [globalNetworkId](#API_DisassociateConnectPeer_RequestSyntax) **   <a name="networkmanager-DisassociateConnectPeer-request-uri-GlobalNetworkId"></a>
The ID of the global network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

## Request Body
<a name="API_DisassociateConnectPeer_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateConnectPeer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectPeerAssociation": {
      "ConnectPeerId": "string",
      "DeviceId": "string",
      "GlobalNetworkId": "string",
      "LinkId": "string",
      "State": "string"
   }
}
```

## Response Elements
<a name="API_DisassociateConnectPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectPeerAssociation](#API_DisassociateConnectPeer_ResponseSyntax) **   <a name="networkmanager-DisassociateConnectPeer-response-ConnectPeerAssociation"></a>
Describes the Connect peer association.
Type: [ConnectPeerAssociation](API_ConnectPeerAssociation.md) object

## Errors
<a name="API_DisassociateConnectPeer_Errors"></a>

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
<a name="API_DisassociateConnectPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/DisassociateConnectPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/DisassociateConnectPeer)
