---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListDelegatedAdminAccounts.html
---

# ListDelegatedAdminAccounts
<a name="API_ListDelegatedAdminAccounts"></a>

Lists information about the Amazon Inspector delegated administrator of your organization.

## Request Syntax
<a name="API_ListDelegatedAdminAccounts_RequestSyntax"></a>

```
POST /delegatedadminaccounts/list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDelegatedAdminAccounts_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDelegatedAdminAccounts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListDelegatedAdminAccounts_RequestSyntax) **   <a name="inspector2-ListDelegatedAdminAccounts-request-maxResults"></a>
The maximum number of results the response can return. If your request would return more than the maximum the response will return a `nextToken` value, use this value when you call the action again to get the remaining results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [nextToken](#API_ListDelegatedAdminAccounts_RequestSyntax) **   <a name="inspector2-ListDelegatedAdminAccounts-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the `maxResults` maximum value it will also return a `nextToken` value. For subsequent calls, use the `nextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

## Response Syntax
<a name="API_ListDelegatedAdminAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "delegatedAdminAccounts": [
      {
         "accountId": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDelegatedAdminAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [delegatedAdminAccounts](#API_ListDelegatedAdminAccounts_ResponseSyntax) **   <a name="inspector2-ListDelegatedAdminAccounts-response-delegatedAdminAccounts"></a>
Details of the Amazon Inspector delegated administrator of your organization.
Type: Array of [DelegatedAdminAccount](API_DelegatedAdminAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [nextToken](#API_ListDelegatedAdminAccounts_ResponseSyntax) **   <a name="inspector2-ListDelegatedAdminAccounts-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

## Errors
<a name="API_ListDelegatedAdminAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListDelegatedAdminAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListDelegatedAdminAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListDelegatedAdminAccounts)
