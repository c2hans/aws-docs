---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetPrimaryEmail.html
---

# GetPrimaryEmail
<a name="API_GetPrimaryEmail"></a>

Retrieves the primary email address for the specified account.

## Request Syntax
<a name="API_GetPrimaryEmail_RequestSyntax"></a>

```
POST /getPrimaryEmail HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetPrimaryEmail_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPrimaryEmail_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_GetPrimaryEmail_RequestSyntax) **   <a name="accounts-GetPrimaryEmail-request-AccountId"></a>
Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.
This operation can only be called from the management account or the delegated administrator account of an organization for a member account.
The management account can't specify its own `AccountId`.
Type: String
Pattern: `\d{12}`
Required: Yes

## Response Syntax
<a name="API_GetPrimaryEmail_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PrimaryEmail": "string"
}
```

## Response Elements
<a name="API_GetPrimaryEmail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PrimaryEmail](#API_GetPrimaryEmail_ResponseSyntax) **   <a name="accounts-GetPrimaryEmail-response-PrimaryEmail"></a>
Retrieves the primary email address associated with the specified account.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.

## Errors
<a name="API_GetPrimaryEmail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The operation failed because the calling identity doesn't have the minimum required permissions.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 403

 ** InternalServerException **
The operation failed because of an error internal to AWS. Try your operation again later.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation failed because it specified a resource that can't be found.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 404

 ** TooManyRequestsException **
The operation failed because it was called too frequently and exceeded a throttle limit.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 429

 ** ValidationException **
The operation failed because one of the input parameters was invalid.
 ** fieldList **
The field where the invalid entry was detected.
 ** message **
The message that informs you about what was invalid about the request.
 ** reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_GetPrimaryEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetPrimaryEmail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetPrimaryEmail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Account Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query accounts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
