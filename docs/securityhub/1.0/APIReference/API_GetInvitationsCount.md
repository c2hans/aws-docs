---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetInvitationsCount.html
---

# GetInvitationsCount
<a name="API_GetInvitationsCount"></a>

**Note**
We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see [Managing Security Hub CSPM administrator and member accounts with Organizations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html) in the * AWS Security Hub CSPM User Guide*.

Returns the count of all Security Hub CSPM membership invitations that were sent to the calling member account, not including the currently accepted invitation.

## Request Syntax
<a name="API_GetInvitationsCount_RequestSyntax"></a>

```
GET /invitations/count HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInvitationsCount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInvitationsCount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInvitationsCount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InvitationsCount": number
}
```

## Response Elements
<a name="API_GetInvitationsCount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvitationsCount](#API_GetInvitationsCount_ResponseSyntax) **   <a name="securityhub-GetInvitationsCount-response-InvitationsCount"></a>
The number of all membership invitations sent to this Security Hub CSPM member account, not including the currently accepted invitation.
Type: Integer

## Errors
<a name="API_GetInvitationsCount_Errors"></a>

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
<a name="API_GetInvitationsCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetInvitationsCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetInvitationsCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
