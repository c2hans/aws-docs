---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AcceptInvitation.html
---

# AcceptInvitation
<a name="API_AcceptInvitation"></a>

This method is deprecated. Instead, use `AcceptAdministratorInvitation`.

The Security Hub CSPM console continues to use `AcceptInvitation`. It will eventually change to use `AcceptAdministratorInvitation`. Any IAM policies that specifically control access to this function must continue to use `AcceptInvitation`. You should also add `AcceptAdministratorInvitation` to your policies to ensure that the correct permissions are in place after the console begins to use `AcceptAdministratorInvitation`.

Accepts the invitation to be a member account and be monitored by the Security Hub CSPM administrator account that the invitation was sent from.

This operation is only used by member accounts that are not added through Organizations.

When the member account accepts the invitation, permission is granted to the administrator account to view findings generated in the member account.

## Request Syntax
<a name="API_AcceptInvitation_RequestSyntax"></a>

```
POST /master HTTP/1.1
Content-type: application/json

{
   "InvitationId": "{{string}}",
   "MasterId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AcceptInvitation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AcceptInvitation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InvitationId](#API_AcceptInvitation_RequestSyntax) **   <a name="securityhub-AcceptInvitation-request-InvitationId"></a>
The identifier of the invitation sent from the Security Hub CSPM administrator account.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [MasterId](#API_AcceptInvitation_RequestSyntax) **   <a name="securityhub-AcceptInvitation-request-MasterId"></a>
The account ID of the Security Hub CSPM administrator account that sent the invitation.
Type: String
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_AcceptInvitation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AcceptInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AcceptInvitation_Errors"></a>

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

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_AcceptInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/AcceptInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AcceptInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
