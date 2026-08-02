---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListProposalVotes.html
---

# ListProposalVotes
<a name="API_ListProposalVotes"></a>

Returns the list of votes for a specified proposal, including the value of each vote and the unique identifier of the member that cast the vote.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_ListProposalVotes_RequestSyntax"></a>

```
GET /networks/{{networkId}}/proposals/{{proposalId}}/votes?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProposalVotes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListProposalVotes_RequestSyntax) **   <a name="ManagedBlockchain-ListProposalVotes-request-uri-MaxResults"></a>
 The maximum number of votes to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [networkId](#API_ListProposalVotes_RequestSyntax) **   <a name="ManagedBlockchain-ListProposalVotes-request-uri-NetworkId"></a>
 The unique identifier of the network.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [NextToken](#API_ListProposalVotes_RequestSyntax) **   <a name="ManagedBlockchain-ListProposalVotes-request-uri-NextToken"></a>
 The pagination token that indicates the next set of results to retrieve.
Length Constraints: Maximum length of 128.

 ** [proposalId](#API_ListProposalVotes_RequestSyntax) **   <a name="ManagedBlockchain-ListProposalVotes-request-uri-ProposalId"></a>
 The unique identifier of the proposal.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_ListProposalVotes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProposalVotes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProposalVotes": [
      {
         "MemberId": "string",
         "MemberName": "string",
         "Vote": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProposalVotes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProposalVotes_ResponseSyntax) **   <a name="ManagedBlockchain-ListProposalVotes-response-NextToken"></a>
 The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Maximum length of 128.

 ** [ProposalVotes](#API_ListProposalVotes_ResponseSyntax) **   <a name="ManagedBlockchain-ListProposalVotes-response-ProposalVotes"></a>
 The list of votes.
Type: Array of [VoteSummary](API_VoteSummary.md) objects

## Errors
<a name="API_ListProposalVotes_Errors"></a>

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
<a name="API_ListProposalVotes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/ListProposalVotes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ListProposalVotes)
