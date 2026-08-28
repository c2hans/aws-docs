---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetProposal.html
---

# GetProposal
<a name="API_GetProposal"></a>

Returns detailed information about a proposal.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_GetProposal_RequestSyntax"></a>

```
GET /networks/{{networkId}}/proposals/{{proposalId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProposal_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_GetProposal_RequestSyntax) **   <a name="ManagedBlockchain-GetProposal-request-uri-NetworkId"></a>
The unique identifier of the network for which the proposal is made.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** [proposalId](#API_GetProposal_RequestSyntax) **   <a name="ManagedBlockchain-GetProposal-request-uri-ProposalId"></a>
The unique identifier of the proposal.
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Request Body
<a name="API_GetProposal_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProposal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Proposal": {
      "Actions": {
         "Invitations": [
            {
               "Principal": "string"
            }
         ],
         "Removals": [
            {
               "MemberId": "string"
            }
         ]
      },
      "Arn": "string",
      "CreationDate": "string",
      "Description": "string",
      "ExpirationDate": "string",
      "NetworkId": "string",
      "NoVoteCount": number,
      "OutstandingVoteCount": number,
      "ProposalId": "string",
      "ProposedByMemberId": "string",
      "ProposedByMemberName": "string",
      "Status": "string",
      "Tags": {
         "string" : "string"
      },
      "YesVoteCount": number
   }
}
```

## Response Elements
<a name="API_GetProposal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Proposal](#API_GetProposal_ResponseSyntax) **   <a name="ManagedBlockchain-GetProposal-response-Proposal"></a>
Information about a proposal.
Type: [Proposal](API_Proposal.md) object

## Errors
<a name="API_GetProposal_Errors"></a>

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
<a name="API_GetProposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/GetProposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/GetProposal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
