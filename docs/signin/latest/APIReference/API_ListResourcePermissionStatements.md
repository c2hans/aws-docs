---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_ListResourcePermissionStatements.html
---

# ListResourcePermissionStatements
<a name="API_ListResourcePermissionStatements"></a>

Retrieves all permission statements in the account's AWS Sign-In resource-based policy.

## Request Syntax
<a name="API_ListResourcePermissionStatements_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourcePermissionStatements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListResourcePermissionStatements_RequestSyntax) **   <a name="signin-ListResourcePermissionStatements-request-maxResults"></a>
The maximum number of permission statements to return in a single response. Valid range is 1 to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListResourcePermissionStatements_RequestSyntax) **   <a name="signin-ListResourcePermissionStatements-request-nextToken"></a>
A pagination token that you can use in a subsequent call to retrieve the next set of results. Initially the value is null. Set this parameter to the value provided by the previous call's response to request the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`
Required: No

## Response Syntax
<a name="API_ListResourcePermissionStatements_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "permissionStatements": [
      {
         "condition": {
            "string" : {
               "string" : [ "string" ]
            }
         },
         "sid": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourcePermissionStatements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListResourcePermissionStatements_ResponseSyntax) **   <a name="signin-ListResourcePermissionStatements-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `nextToken` request parameter in a subsequent call to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`

 ** [permissionStatements](#API_ListResourcePermissionStatements_ResponseSyntax) **   <a name="signin-ListResourcePermissionStatements-response-permissionStatements"></a>
A list of summaries of the permission statements in the AWS Sign-In resource-based policy.
Type: Array of [PermissionStatementSummary](API_PermissionStatementSummary.md) objects

## Errors
<a name="API_ListResourcePermissionStatements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found.
HTTP Status Code: 400

 ** TooManyRequestsError **
The request was denied due to rate limiting.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
HTTP Status Code: 400

## See Also
<a name="API_ListResourcePermissionStatements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/ListResourcePermissionStatements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/ListResourcePermissionStatements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sign-In. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
