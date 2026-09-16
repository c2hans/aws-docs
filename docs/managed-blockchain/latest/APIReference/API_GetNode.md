---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetNode.html
---

# GetNode
<a name="API_GetNode"></a>

Returns detailed information about a node.

Applies to Hyperledger Fabric and Ethereum.

## Request Syntax
<a name="API_GetNode_RequestSyntax"></a>

```
GET /networks/{{networkId}}/nodes/{{nodeId}}?memberId={{MemberId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MemberId](#API_GetNode_RequestSyntax) **   <a name="ManagedBlockchain-GetNode-request-uri-MemberId"></a>
The unique identifier of the member that owns the node.
Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.
Length Constraints: Minimum length of 1. Maximum length of 32.

 ** [networkId](#API_GetNode_RequestSyntax) **   <a name="ManagedBlockchain-GetNode-request-uri-NetworkId"></a>
The unique identifier of the network that the node is on.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [nodeId](#API_GetNode_RequestSyntax) **   <a name="ManagedBlockchain-GetNode-request-uri-NodeId"></a>
The unique identifier of the node.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_GetNode_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNode_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Node": {
      "Arn": "string",
      "AvailabilityZone": "string",
      "CreationDate": "string",
      "FrameworkAttributes": {
         "Ethereum": {
            "HttpEndpoint": "string",
            "WebSocketEndpoint": "string"
         },
         "Fabric": {
            "PeerEndpoint": "string",
            "PeerEventEndpoint": "string"
         }
      },
      "Id": "string",
      "InstanceType": "string",
      "KmsKeyArn": "string",
      "LogPublishingConfiguration": {
         "Fabric": {
            "ChaincodeLogs": {
               "Cloudwatch": {
                  "Enabled": boolean
               }
            },
            "PeerLogs": {
               "Cloudwatch": {
                  "Enabled": boolean
               }
            }
         }
      },
      "MemberId": "string",
      "NetworkId": "string",
      "StateDB": "string",
      "Status": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Node](#API_GetNode_ResponseSyntax) **   <a name="ManagedBlockchain-GetNode-response-Node"></a>
Properties of the node configuration.
Type: [Node](API_Node.md) object

## Errors
<a name="API_GetNode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceErrorException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidRequestException **
The action or operation requested is invalid. Verify that the action is typed correctly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A requested resource doesn't exist. It may have been deleted or referenced incorrectly.
 ** ResourceName **
A requested resource doesn't exist. It may have been deleted or referenced inaccurately.
HTTP Status Code: 404

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

## See Also
<a name="API_GetNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/GetNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/GetNode)
