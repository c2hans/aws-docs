---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListInvitations.html
---

# ListInvitations
<a name="API_ListInvitations"></a>

Returns a list of all invitations for the current AWS account.

Applies only to Hyperledger Fabric.

## Request Syntax
<a name="API_ListInvitations_RequestSyntax"></a>

```
GET /invitations?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInvitations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListInvitations_RequestSyntax) **   <a name="ManagedBlockchain-ListInvitations-request-uri-MaxResults"></a>
The maximum number of invitations to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListInvitations_RequestSyntax) **   <a name="ManagedBlockchain-ListInvitations-request-uri-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Length Constraints: Maximum length of 128.

## Request Body
<a name="API_ListInvitations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInvitations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Invitations": [
      {
         "Arn": "string",
         "CreationDate": "string",
         "ExpirationDate": "string",
         "InvitationId": "string",
         "NetworkSummary": {
            "Arn": "string",
            "CreationDate": "string",
            "Description": "string",
            "Framework": "string",
            "FrameworkVersion": "string",
            "Id": "string",
            "Name": "string",
            "Status": "string"
         },
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInvitations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Invitations](#API_ListInvitations_ResponseSyntax) **   <a name="ManagedBlockchain-ListInvitations-response-Invitations"></a>
The invitations for the network.
Type: Array of [Invitation](API_Invitation.md) objects

 ** [NextToken](#API_ListInvitations_ResponseSyntax) **   <a name="ManagedBlockchain-ListInvitations-response-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Maximum length of 128.

## Errors
<a name="API_ListInvitations_Errors"></a>

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

 ** ResourceLimitExceededException **
The maximum number of resources of that type already exist. Ensure the resources requested are within the boundaries of the service edition and your account limits.
HTTP Status Code: 429

 ** ResourceNotFoundException **
A requested resource doesn't exist. It may have been deleted or referenced incorrectly.
 ** ResourceName **
A requested resource doesn't exist. It may have been deleted or referenced inaccurately.
HTTP Status Code: 404

 ** ThrottlingException **
The request or operation couldn't be performed because a service is throttling requests. The most common source of throttling errors is creating resources that exceed your service limit for this resource type. Request a limit increase or delete unused resources if possible.
HTTP Status Code: 429

## See Also
<a name="API_ListInvitations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/ListInvitations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/ListInvitations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Blockchain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-blockchain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
