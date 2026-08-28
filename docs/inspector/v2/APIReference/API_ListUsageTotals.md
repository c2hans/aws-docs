---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListUsageTotals.html
---

# ListUsageTotals
<a name="API_ListUsageTotals"></a>

Lists the Amazon Inspector usage totals over the last 30 days.

## Request Syntax
<a name="API_ListUsageTotals_RequestSyntax"></a>

```
POST /usage/list HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListUsageTotals_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListUsageTotals_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_ListUsageTotals_RequestSyntax) **   <a name="inspector2-ListUsageTotals-request-accountIds"></a>
The AWS account IDs to retrieve usage totals for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 7000 items.
Pattern: `.*[0-9]{12}.*`
Required: No

 ** [maxResults](#API_ListUsageTotals_RequestSyntax) **   <a name="inspector2-ListUsageTotals-request-maxResults"></a>
The maximum number of results the response can return. If your request would return more than the maximum the response will return a `nextToken` value, use this value when you call the action again to get the remaining results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_ListUsageTotals_RequestSyntax) **   <a name="inspector2-ListUsageTotals-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the `maxResults` maximum value it will also return a `nextToken` value. For subsequent calls, use the `nextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListUsageTotals_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "totals": [
      {
         "accountId": "string",
         "usage": [
            {
               "cloudProvider": "string",
               "currency": "string",
               "estimatedMonthlyCost": number,
               "total": number,
               "type": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ListUsageTotals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListUsageTotals_ResponseSyntax) **   <a name="inspector2-ListUsageTotals-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String
Length Constraints: Minimum length of 1.

 ** [totals](#API_ListUsageTotals_ResponseSyntax) **   <a name="inspector2-ListUsageTotals-response-totals"></a>
An object with details on the total usage for the requested account.
Type: Array of [UsageTotal](API_UsageTotal.md) objects

## Errors
<a name="API_ListUsageTotals_Errors"></a>

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
<a name="API_ListUsageTotals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListUsageTotals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListUsageTotals)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
