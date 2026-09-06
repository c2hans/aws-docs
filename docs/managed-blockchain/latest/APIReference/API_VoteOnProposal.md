---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_VoteOnProposal.html
---

# VoteOnProposal
<a name="API_VoteOnProposal"></a>

Casts a vote for a specified `ProposalId` on behalf of a member. The member to vote as, specified by `VoterMemberId`, must be in the same AWS account as the principal that calls the action.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_VoteOnProposal_RequestSyntax"></a>

```
POST /networks/{{networkId}}/proposals/{{proposalId}}/votes HTTP/1.1
Content-type: application/json

{
   "Vote": "{{string}}",
   "VoterMemberId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_VoteOnProposal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_VoteOnProposal_RequestSyntax) **   <a name="ManagedBlockchain-VoteOnProposal-request-uri-NetworkId"></a>
 The unique identifier of the network.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [proposalId](#API_VoteOnProposal_RequestSyntax) **   <a name="ManagedBlockchain-VoteOnProposal-request-uri-ProposalId"></a>
 The unique identifier of the proposal.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_VoteOnProposal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Vote](#API_VoteOnProposal_RequestSyntax) **   <a name="ManagedBlockchain-VoteOnProposal-request-Vote"></a>
 The value of the vote.
Type: String
Valid Values: `YES | NO`
Required: Yes

 ** [VoterMemberId](#API_VoteOnProposal_RequestSyntax) **   <a name="ManagedBlockchain-VoteOnProposal-request-VoterMemberId"></a>
The unique identifier of the member casting the vote.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Response Syntax
<a name="API_VoteOnProposal_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_VoteOnProposal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_VoteOnProposal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** IllegalActionException **

HTTP Status Code: 400

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
<a name="API_VoteOnProposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/VoteOnProposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/VoteOnProposal)
