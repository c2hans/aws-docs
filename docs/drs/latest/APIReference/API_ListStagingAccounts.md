---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ListStagingAccounts.html
---

# ListStagingAccounts
<a name="API_ListStagingAccounts"></a>

Returns an array of staging accounts for existing extended source servers.

## Request Syntax
<a name="API_ListStagingAccounts_RequestSyntax"></a>

```
GET /ListStagingAccounts?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListStagingAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListStagingAccounts_RequestSyntax) **   <a name="drs-ListStagingAccounts-request-uri-maxResults"></a>
The maximum number of staging Accounts to retrieve.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListStagingAccounts_RequestSyntax) **   <a name="drs-ListStagingAccounts-request-uri-nextToken"></a>
The token of the next staging Account to retrieve.
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Request Body
<a name="API_ListStagingAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListStagingAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accounts": [
      {
         "accountID": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListStagingAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accounts](#API_ListStagingAccounts_ResponseSyntax) **   <a name="drs-ListStagingAccounts-response-accounts"></a>
An array of staging AWS Accounts.
Type: Array of [Account](API_Account.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [nextToken](#API_ListStagingAccounts_ResponseSyntax) **   <a name="drs-ListStagingAccounts-response-nextToken"></a>
The token of the next staging Account to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListStagingAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_ListStagingAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/ListStagingAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ListStagingAccounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
