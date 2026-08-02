---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListNodes.html
---

# ListNodes
<a name="API_ListNodes"></a>

Returns information about the nodes within a network.

Applies to Hyperledger Fabric and Ethereum.

## Request Syntax
<a name="API_ListNodes_RequestSyntax"></a>

```
GET /networks/{{networkId}}/nodes?maxResults={{MaxResults}}&memberId={{MemberId}}&nextToken={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNodes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListNodes_RequestSyntax) **   <a name="ManagedBlockchain-ListNodes-request-uri-MaxResults"></a>
The maximum number of nodes to list.
Valid Range: Minimum value of 1. Maximum value of 20.

 ** [MemberId](#API_ListNodes_RequestSyntax) **   <a name="ManagedBlockchain-ListNodes-request-uri-MemberId"></a>
The unique identifier of the member who owns the nodes to list.
Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.
Length Constraints: Minimum length of 1. Maximum length of 32.

 ** [networkId](#API_ListNodes_RequestSyntax) **   <a name="ManagedBlockchain-ListNodes-request-uri-NetworkId"></a>
The unique identifier of the network for which to list nodes.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [NextToken](#API_ListNodes_RequestSyntax) **   <a name="ManagedBlockchain-ListNodes-request-uri-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Length Constraints: Maximum length of 128.

 ** [Status](#API_ListNodes_RequestSyntax) **   <a name="ManagedBlockchain-ListNodes-request-uri-Status"></a>
An optional status specifier. If provided, only nodes currently in this status are listed.
Valid Values: `CREATING | AVAILABLE | UNHEALTHY | CREATE_FAILED | UPDATING | DELETING | DELETED | FAILED | INACCESSIBLE_ENCRYPTION_KEY`

## Request Body
<a name="API_ListNodes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNodes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Nodes": [
      {
         "Arn": "string",
         "AvailabilityZone": "string",
         "CreationDate": "string",
         "Id": "string",
         "InstanceType": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNodes_ResponseSyntax) **   <a name="ManagedBlockchain-ListNodes-response-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Maximum length of 128.

 ** [Nodes](#API_ListNodes_ResponseSyntax) **   <a name="ManagedBlockchain-ListNodes-response-Nodes"></a>
An array of `NodeSummary` objects that contain configuration properties for each node.
Type: Array of [NodeSummary](API_NodeSummary.md) objects

## Errors
<a name="API_ListNodes_Errors"></a>

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

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

## See Also
<a name="API_ListNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/ListNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ListNodes)
