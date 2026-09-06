---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateProposal.html
---

# CreateProposal
<a name="API_CreateProposal"></a>

Creates a proposal for a change to the network that other members of the network can vote on, for example, a proposal to add a new member to the network. Any member can create a proposal.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_CreateProposal_RequestSyntax"></a>

```
POST /networks/{{networkId}}/proposals HTTP/1.1
Content-type: application/json

{
   "Actions": {
      "Invitations": [
         {
            "Principal": "{{string}}"
         }
      ],
      "Removals": [
         {
            "MemberId": "{{string}}"
         }
      ]
   },
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "MemberId": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateProposal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_CreateProposal_RequestSyntax) **   <a name="ManagedBlockchain-CreateProposal-request-uri-NetworkId"></a>
 The unique identifier of the network for which the proposal is made.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_CreateProposal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Actions](#API_CreateProposal_RequestSyntax) **   <a name="ManagedBlockchain-CreateProposal-request-Actions"></a>
The type of actions proposed, such as inviting a member or removing a member. The types of `Actions` in a proposal are mutually exclusive. For example, a proposal with `Invitations` actions cannot also contain `Removals` actions.
Type: [ProposalActions](API_ProposalActions.md) object
Required: Yes

 ** [ClientRequestToken](#API_CreateProposal_RequestSyntax) **   <a name="ManagedBlockchain-CreateProposal-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an AWS SDK or the AWS CLI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Description](#API_CreateProposal_RequestSyntax) **   <a name="ManagedBlockchain-CreateProposal-request-Description"></a>
A description for the proposal that is visible to voting members, for example, "Proposal to add Example Corp. as member."
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** [MemberId](#API_CreateProposal_RequestSyntax) **   <a name="ManagedBlockchain-CreateProposal-request-MemberId"></a>
The unique identifier of the member that is creating the proposal. This identifier is especially useful for identifying the member making the proposal when multiple members exist in a single AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [Tags](#API_CreateProposal_RequestSyntax) **   <a name="ManagedBlockchain-CreateProposal-request-Tags"></a>
Tags to assign to the proposal.
 Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.
For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateProposal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProposalId": "string"
}
```

## Response Elements
<a name="API_CreateProposal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProposalId](#API_CreateProposal_ResponseSyntax) **   <a name="ManagedBlockchain-CreateProposal-response-ProposalId"></a>
The unique identifier of the proposal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

## Errors
<a name="API_CreateProposal_Errors"></a>

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
<a name="API_CreateProposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/CreateProposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/CreateProposal)
