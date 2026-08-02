---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateConnectAttachment.html
---

# CreateConnectAttachment
<a name="API_CreateConnectAttachment"></a>

Creates a core network Connect attachment from a specified core network attachment.

A core network Connect attachment is a GRE-based tunnel attachment that you can use to establish a connection between a core network and an appliance. A core network Connect attachment uses an existing VPC attachment as the underlying transport mechanism.

## Request Syntax
<a name="API_CreateConnectAttachment_RequestSyntax"></a>

```
POST /connect-attachments HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "CoreNetworkId": "{{string}}",
   "EdgeLocation": "{{string}}",
   "Options": {
      "Protocol": "{{string}}"
   },
   "RoutingPolicyLabel": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TransportAttachmentId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateConnectAttachment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnectAttachment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateConnectAttachment_RequestSyntax) **   <a name="networkmanager-CreateConnectAttachment-request-ClientToken"></a>
The client token associated with the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [CoreNetworkId](#API_CreateConnectAttachment_RequestSyntax) **   <a name="networkmanager-CreateConnectAttachment-request-CoreNetworkId"></a>
The ID of a core network where you want to create the attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

 ** [EdgeLocation](#API_CreateConnectAttachment_RequestSyntax) **   <a name="networkmanager-CreateConnectAttachment-request-EdgeLocation"></a>
The Region where the edge is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: Yes

 ** [Options](#API_CreateConnectAttachment_RequestSyntax) **   <a name="networkmanager-CreateConnectAttachment-request-Options"></a>
Options for creating an attachment.
Type: [ConnectAttachmentOptions](API_ConnectAttachmentOptions.md) object
Required: Yes

 ** [RoutingPolicyLabel](#API_CreateConnectAttachment_RequestSyntax) **   <a name="networkmanager-CreateConnectAttachment-request-RoutingPolicyLabel"></a>
The routing policy label to apply to the Connect attachment for traffic routing decisions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Tags](#API_CreateConnectAttachment_RequestSyntax) **   <a name="networkmanager-CreateConnectAttachment-request-Tags"></a>
The list of key-value tags associated with the request.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [TransportAttachmentId](#API_CreateConnectAttachment_RequestSyntax) **   <a name="networkmanager-CreateConnectAttachment-request-TransportAttachmentId"></a>
The ID of the attachment between the two connections.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: Yes

## Response Syntax
<a name="API_CreateConnectAttachment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectAttachment": {
      "Attachment": {
         "AttachmentId": "string",
         "AttachmentPolicyRuleNumber": number,
         "AttachmentType": "string",
         "CoreNetworkArn": "string",
         "CoreNetworkId": "string",
         "CreatedAt": number,
         "EdgeLocation": "string",
         "EdgeLocations": [ "string" ],
         "LastModificationErrors": [
            {
               "Code": "string",
               "Message": "string",
               "RequestId": "string",
               "ResourceArn": "string"
            }
         ],
         "NetworkFunctionGroupName": "string",
         "OwnerAccountId": "string",
         "ProposedNetworkFunctionGroupChange": {
            "AttachmentPolicyRuleNumber": number,
            "NetworkFunctionGroupName": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "ProposedSegmentChange": {
            "AttachmentPolicyRuleNumber": number,
            "SegmentName": "string",
            "Tags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "ResourceArn": "string",
         "SegmentName": "string",
         "State": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "UpdatedAt": number
      },
      "Options": {
         "Protocol": "string"
      },
      "TransportAttachmentId": "string"
   }
}
```

## Response Elements
<a name="API_CreateConnectAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectAttachment](#API_CreateConnectAttachment_ResponseSyntax) **   <a name="networkmanager-CreateConnectAttachment-response-ConnectAttachment"></a>
The response to a Connect attachment request.
Type: [ConnectAttachment](API_ConnectAttachment.md) object

## Errors
<a name="API_CreateConnectAttachment_Errors"></a>

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
<a name="API_CreateConnectAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateConnectAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateConnectAttachment)
