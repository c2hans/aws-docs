---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateNode.html
---

# CreateNode
<a name="API_CreateNode"></a>

**Note**
End of support notice: Amazon Managed Blockchain will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain. For more information, see [Amazon Managed Blockchain availability change](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

Creates a node on the specified blockchain network.

Applies to Hyperledger Fabric and Ethereum.

## Request Syntax
<a name="API_CreateNode_RequestSyntax"></a>

```
POST /networks/{{networkId}}/nodes HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "MemberId": "{{string}}",
   "NodeConfiguration": {
      "AvailabilityZone": "{{string}}",
      "InstanceType": "{{string}}",
      "LogPublishingConfiguration": {
         "Fabric": {
            "ChaincodeLogs": {
               "Cloudwatch": {
                  "Enabled": {{boolean}}
               }
            },
            "PeerLogs": {
               "Cloudwatch": {
                  "Enabled": {{boolean}}
               }
            }
         }
      },
      "StateDB": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateNode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_CreateNode_RequestSyntax) **   <a name="ManagedBlockchain-CreateNode-request-uri-NetworkId"></a>
The unique identifier of the network for the node.
Ethereum public networks have the following `NetworkId`s:
+  `n-ethereum-mainnet`
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_CreateNode_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateNode_RequestSyntax) **   <a name="ManagedBlockchain-CreateNode-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an AWS SDK or the AWS CLI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [MemberId](#API_CreateNode_RequestSyntax) **   <a name="ManagedBlockchain-CreateNode-request-MemberId"></a>
The unique identifier of the member that owns this node.
Applies only to Hyperledger Fabric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** [NodeConfiguration](#API_CreateNode_RequestSyntax) **   <a name="ManagedBlockchain-CreateNode-request-NodeConfiguration"></a>
The properties of a node configuration.
Type: [NodeConfiguration](API_NodeConfiguration.md) object
Required: Yes

 ** [Tags](#API_CreateNode_RequestSyntax) **   <a name="ManagedBlockchain-CreateNode-request-Tags"></a>
Tags to assign to the node.
 Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateNode_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NodeId": "string"
}
```

## Response Elements
<a name="API_CreateNode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NodeId](#API_CreateNode_ResponseSyntax) **   <a name="ManagedBlockchain-CreateNode-response-NodeId"></a>
The unique identifier of the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

## Errors
<a name="API_CreateNode_Errors"></a>

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

 ** ResourceAlreadyExistsException **
A resource request is issued for a resource that already exists.
HTTP Status Code: 409

 ** ResourceLimitExceededException **
The maximum number of resources of that type already exist. Ensure the resources requested are within the boundaries of the service edition and your account limits.
HTTP Status Code: 429

 ** ResourceNotFoundException **
A requested resource doesn't exist. It may have been deleted or referenced incorrectly.
 ** ResourceName **
A requested resource doesn't exist. It may have been deleted or referenced inaccurately.
HTTP Status Code: 404

 ** ResourceNotReadyException **
The requested resource exists but isn't in a status that can complete the operation.
HTTP Status Code: 409

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

 ** TooManyTagsException **

 ** ResourceName **

HTTP Status Code: 400

## See Also
<a name="API_CreateNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/CreateNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/CreateNode)
