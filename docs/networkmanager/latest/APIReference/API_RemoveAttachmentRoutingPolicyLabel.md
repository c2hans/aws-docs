---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RemoveAttachmentRoutingPolicyLabel.html
---

# RemoveAttachmentRoutingPolicyLabel
<a name="API_RemoveAttachmentRoutingPolicyLabel"></a>

Removes a routing policy label from an attachment.

## Request Syntax
<a name="API_RemoveAttachmentRoutingPolicyLabel_RequestSyntax"></a>

```
DELETE /routing-policy-label/core-network/{{coreNetworkId}}/attachment/{{attachmentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RemoveAttachmentRoutingPolicyLabel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attachmentId](#API_RemoveAttachmentRoutingPolicyLabel_RequestSyntax) **   <a name="networkmanager-RemoveAttachmentRoutingPolicyLabel-request-uri-AttachmentId"></a>
The ID of the attachment to remove the routing policy label from.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: Yes

 ** [coreNetworkId](#API_RemoveAttachmentRoutingPolicyLabel_RequestSyntax) **   <a name="networkmanager-RemoveAttachmentRoutingPolicyLabel-request-uri-CoreNetworkId"></a>
The ID of the core network containing the attachment.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

## Request Body
<a name="API_RemoveAttachmentRoutingPolicyLabel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RemoveAttachmentRoutingPolicyLabel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachmentId": "string",
   "CoreNetworkId": "string",
   "RoutingPolicyLabel": "string"
}
```

## Response Elements
<a name="API_RemoveAttachmentRoutingPolicyLabel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentId](#API_RemoveAttachmentRoutingPolicyLabel_ResponseSyntax) **   <a name="networkmanager-RemoveAttachmentRoutingPolicyLabel-response-AttachmentId"></a>
The ID of the attachment from which the routing policy label was removed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`

 ** [CoreNetworkId](#API_RemoveAttachmentRoutingPolicyLabel_ResponseSyntax) **   <a name="networkmanager-RemoveAttachmentRoutingPolicyLabel-response-CoreNetworkId"></a>
The ID of the core network containing the attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`

 ** [RoutingPolicyLabel](#API_RemoveAttachmentRoutingPolicyLabel_ResponseSyntax) **   <a name="networkmanager-RemoveAttachmentRoutingPolicyLabel-response-RoutingPolicyLabel"></a>
The routing policy label that was removed from the attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`

## Errors
<a name="API_RemoveAttachmentRoutingPolicyLabel_Errors"></a>

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
<a name="API_RemoveAttachmentRoutingPolicyLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RemoveAttachmentRoutingPolicyLabel)
