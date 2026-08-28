---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeclineInvitations.html
---

# DeclineInvitations
<a name="API_DeclineInvitations"></a>

**Note**
We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see [Managing Security Hub CSPM administrator and member accounts with Organizations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html) in the * AWS Security Hub CSPM User Guide*.

Declines invitations to become a Security Hub CSPM member account.

A prospective member account uses this operation to decline an invitation to become a member.

Only member accounts that aren't part of an AWS organization should use this operation. Organization accounts don't receive invitations.

## Request Syntax
<a name="API_DeclineInvitations_RequestSyntax"></a>

```
POST /invitations/decline HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DeclineInvitations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeclineInvitations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_DeclineInvitations_RequestSyntax) **   <a name="securityhub-DeclineInvitations-request-AccountIds"></a>
The list of prospective member account IDs for which to decline an invitation.
Type: Array of strings
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_DeclineInvitations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "UnprocessedAccounts": [
      {
         "AccountId": "string",
         "ProcessingResult": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DeclineInvitations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UnprocessedAccounts](#API_DeclineInvitations_ResponseSyntax) **   <a name="securityhub-DeclineInvitations-response-UnprocessedAccounts"></a>
The list of AWS accounts that were not processed. For each account, the list includes the account ID and the email address.
Type: Array of [Result](API_Result.md) objects

## Errors
<a name="API_DeclineInvitations_Errors"></a>

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

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_DeclineInvitations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DeclineInvitations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DeclineInvitations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
