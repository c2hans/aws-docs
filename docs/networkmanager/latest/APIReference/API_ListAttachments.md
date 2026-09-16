---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListAttachments.html
---

# ListAttachments
<a name="API_ListAttachments"></a>

Returns a list of core network attachments.

## Request Syntax
<a name="API_ListAttachments_RequestSyntax"></a>

```
GET /attachments?attachmentType={{AttachmentType}}&coreNetworkId={{CoreNetworkId}}&edgeLocation={{EdgeLocation}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&state={{State}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAttachments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttachmentType](#API_ListAttachments_RequestSyntax) **   <a name="networkmanager-ListAttachments-request-uri-AttachmentType"></a>
The type of attachment.
Valid Values: `CONNECT | SITE_TO_SITE_VPN | VPC | DIRECT_CONNECT_GATEWAY | TRANSIT_GATEWAY_ROUTE_TABLE`

 ** [CoreNetworkId](#API_ListAttachments_RequestSyntax) **   <a name="networkmanager-ListAttachments-request-uri-CoreNetworkId"></a>
The ID of a core network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`

 ** [EdgeLocation](#API_ListAttachments_RequestSyntax) **   <a name="networkmanager-ListAttachments-request-uri-EdgeLocation"></a>
The Region where the edge is located.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`

 ** [MaxResults](#API_ListAttachments_RequestSyntax) **   <a name="networkmanager-ListAttachments-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_ListAttachments_RequestSyntax) **   <a name="networkmanager-ListAttachments-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [State](#API_ListAttachments_RequestSyntax) **   <a name="networkmanager-ListAttachments-request-uri-State"></a>
The state of the attachment.
Valid Values: `REJECTED | PENDING_ATTACHMENT_ACCEPTANCE | CREATING | FAILED | AVAILABLE | UPDATING | PENDING_NETWORK_UPDATE | PENDING_TAG_ACCEPTANCE | DELETING`

## Request Body
<a name="API_ListAttachments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAttachments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attachments": [
      {
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
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAttachments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attachments](#API_ListAttachments_ResponseSyntax) **   <a name="networkmanager-ListAttachments-response-Attachments"></a>
Describes the list of attachments.
Type: Array of [Attachment](API_Attachment.md) objects

 ** [NextToken](#API_ListAttachments_ResponseSyntax) **   <a name="networkmanager-ListAttachments-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Errors
<a name="API_ListAttachments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

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
<a name="API_ListAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListAttachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListAttachments)
