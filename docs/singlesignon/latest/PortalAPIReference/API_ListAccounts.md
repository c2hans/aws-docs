---
source_url: https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_ListAccounts.html
---

# ListAccounts
<a name="API_ListAccounts"></a>

Lists all AWS accounts assigned to the user. These AWS accounts are assigned by the administrator of the account. For more information, see [Assign User Access](https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html#assignusers) in the *IAM Identity Center User Guide*. This operation returns a paginated response.

## Request Syntax
<a name="API_ListAccounts_RequestSyntax"></a>

```
GET /assignment/accounts?max_result={{maxResults}}&next_token={{nextToken}} HTTP/1.1
x-amz-sso_bearer_token: {{accessToken}}
```

## URI Request Parameters
<a name="API_ListAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessToken](#API_ListAccounts_RequestSyntax) **   <a name="singlesignon-ListAccounts-request-accessToken"></a>
The token issued by the `CreateToken` API call. For more information, see [CreateToken](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html) in the *IAM Identity Center OIDC API Reference Guide*.
Required: Yes

 ** [maxResults](#API_ListAccounts_RequestSyntax) **   <a name="singlesignon-ListAccounts-request-uri-maxResults"></a>
This is the number of items clients can request per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAccounts_RequestSyntax) **   <a name="singlesignon-ListAccounts-request-uri-nextToken"></a>
(Optional) When requesting subsequent pages, this is the page token from the previous response output.

## Request Body
<a name="API_ListAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountList": [
      {
         "accountId": "string",
         "accountName": "string",
         "emailAddress": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountList](#API_ListAccounts_ResponseSyntax) **   <a name="singlesignon-ListAccounts-response-accountList"></a>
A paginated response with the list of account information and the next token if more results are available.
Type: Array of [AccountInfo](API_AccountInfo.md) objects

 ** [nextToken](#API_ListAccounts_ResponseSyntax) **   <a name="singlesignon-ListAccounts-response-nextToken"></a>
The page token client that is used to retrieve the list of accounts.
Type: String

## Errors
<a name="API_ListAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
Indicates that a problem occurred with the input to the request. For example, a required parameter might be missing or out of range.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Indicates that the request is being made too frequently and is more than what the server can handle.
HTTP Status Code: 429

 ** UnauthorizedException **
Indicates that the request is not authorized. This can happen due to an invalid access token in the request.
HTTP Status Code: 401

## See Also
<a name="API_ListAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-2019-06-10/ListAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-2019-06-10/ListAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/ListAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-2019-06-10/ListAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/ListAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-2019-06-10/ListAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-2019-06-10/ListAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-2019-06-10/ListAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-2019-06-10/ListAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/ListAccounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
