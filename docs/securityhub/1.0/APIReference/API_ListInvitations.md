---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListInvitations.html
---

# ListInvitations
<a name="API_ListInvitations"></a>

**Note**
We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see [Managing Security Hub CSPM administrator and member accounts with Organizations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html) in the * AWS Security Hub CSPM User Guide*.

Lists all Security Hub CSPM membership invitations that were sent to the calling account.

Only accounts that are managed by invitation can use this operation. Accounts that are managed using the integration with Organizations don't receive invitations.

## Request Syntax
<a name="API_ListInvitations_RequestSyntax"></a>

```
GET /invitations?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInvitations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListInvitations_RequestSyntax) **   <a name="securityhub-ListInvitations-request-uri-MaxResults"></a>
The maximum number of items to return in the response.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListInvitations_RequestSyntax) **   <a name="securityhub-ListInvitations-request-uri-NextToken"></a>
The token that is required for pagination. On your first call to the `ListInvitations` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.

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
         "AccountId": "string",
         "InvitationId": "string",
         "InvitedAt": "string",
         "MemberStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInvitations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Invitations](#API_ListInvitations_ResponseSyntax) **   <a name="securityhub-ListInvitations-response-Invitations"></a>
The details of the invitations returned by the operation.
Type: Array of [Invitation](API_Invitation.md) objects

 ** [NextToken](#API_ListInvitations_ResponseSyntax) **   <a name="securityhub-ListInvitations-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_ListInvitations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListInvitations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListInvitations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListInvitations)
