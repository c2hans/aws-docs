---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListConnectPeers.html
---

# ListConnectPeers
<a name="API_ListConnectPeers"></a>

Returns a list of core network Connect peers.

## Request Syntax
<a name="API_ListConnectPeers_RequestSyntax"></a>

```
GET /connect-peers?connectAttachmentId={{ConnectAttachmentId}}&coreNetworkId={{CoreNetworkId}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConnectPeers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectAttachmentId](#API_ListConnectPeers_RequestSyntax) **   <a name="networkmanager-ListConnectPeers-request-uri-ConnectAttachmentId"></a>
The ID of the attachment.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`

 ** [CoreNetworkId](#API_ListConnectPeers_RequestSyntax) **   <a name="networkmanager-ListConnectPeers-request-uri-CoreNetworkId"></a>
The ID of a core network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`

 ** [MaxResults](#API_ListConnectPeers_RequestSyntax) **   <a name="networkmanager-ListConnectPeers-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_ListConnectPeers_RequestSyntax) **   <a name="networkmanager-ListConnectPeers-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Request Body
<a name="API_ListConnectPeers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConnectPeers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectPeers": [
      {
         "ConnectAttachmentId": "string",
         "ConnectPeerId": "string",
         "ConnectPeerState": "string",
         "CoreNetworkId": "string",
         "CreatedAt": number,
         "EdgeLocation": "string",
         "SubnetArn": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectPeers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectPeers](#API_ListConnectPeers_ResponseSyntax) **   <a name="networkmanager-ListConnectPeers-response-ConnectPeers"></a>
Describes the Connect peers.
Type: Array of [ConnectPeerSummary](API_ConnectPeerSummary.md) objects

 ** [NextToken](#API_ListConnectPeers_ResponseSyntax) **   <a name="networkmanager-ListConnectPeers-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

## Errors
<a name="API_ListConnectPeers_Errors"></a>

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
<a name="API_ListConnectPeers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListConnectPeers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListConnectPeers)
