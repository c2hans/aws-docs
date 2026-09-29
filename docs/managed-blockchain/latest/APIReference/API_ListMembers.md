---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListMembers.html
---

# ListMembers
<a name="API_ListMembers"></a>

**Note**
End of support notice: Amazon Managed Blockchain will stop accepting new customers on October 29, 2026. Existing customers can continue using Amazon Managed Blockchain until September 29, 2027. After September 29, 2027 you will no longer be able to access Amazon Managed Blockchain. For more information, see [Amazon Managed Blockchain availability change](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-end-of-support.html).

Returns a list of the members in a network and properties of their configurations.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_ListMembers_RequestSyntax"></a>

```
GET /networks/{{networkId}}/members?isOwned={{IsOwned}}&maxResults={{MaxResults}}&name={{Name}}&nextToken={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMembers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IsOwned](#API_ListMembers_RequestSyntax) **   <a name="ManagedBlockchain-ListMembers-request-uri-IsOwned"></a>
An optional Boolean value. If provided, the request is limited either to members that the current AWS account owns (`true`) or that other AWS accountsn own (`false`). If omitted, all members are listed.

 ** [MaxResults](#API_ListMembers_RequestSyntax) **   <a name="ManagedBlockchain-ListMembers-request-uri-MaxResults"></a>
The maximum number of members to return in the request.
Valid Range: Minimum value of 1. Maximum value of 20.

 ** [Name](#API_ListMembers_RequestSyntax) **   <a name="ManagedBlockchain-ListMembers-request-uri-Name"></a>
The optional name of the member to list.

 ** [networkId](#API_ListMembers_RequestSyntax) **   <a name="ManagedBlockchain-ListMembers-request-uri-NetworkId"></a>
The unique identifier of the network for which to list members.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [NextToken](#API_ListMembers_RequestSyntax) **   <a name="ManagedBlockchain-ListMembers-request-uri-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Length Constraints: Maximum length of 128.

 ** [Status](#API_ListMembers_RequestSyntax) **   <a name="ManagedBlockchain-ListMembers-request-uri-Status"></a>
An optional status specifier. If provided, only members currently in this status are listed.
Valid Values: `CREATING | AVAILABLE | CREATE_FAILED | UPDATING | DELETING | DELETED | INACCESSIBLE_ENCRYPTION_KEY`

## Request Body
<a name="API_ListMembers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Members": [
      {
         "Arn": "string",
         "CreationDate": "string",
         "Description": "string",
         "Id": "string",
         "IsOwned": boolean,
         "Name": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Members](#API_ListMembers_ResponseSyntax) **   <a name="ManagedBlockchain-ListMembers-response-Members"></a>
An array of `MemberSummary` objects. Each object contains details about a network member.
Type: Array of [MemberSummary](API_MemberSummary.md) objects

 ** [NextToken](#API_ListMembers_ResponseSyntax) **   <a name="ManagedBlockchain-ListMembers-response-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Maximum length of 128.

## Errors
<a name="API_ListMembers_Errors"></a>

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
<a name="API_ListMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/ListMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ListMembers)
