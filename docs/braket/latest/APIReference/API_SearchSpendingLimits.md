---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchSpendingLimits.html
---

# SearchSpendingLimits
<a name="API_SearchSpendingLimits"></a>

Searches and lists spending limits based on specified filters. This operation supports pagination and allows filtering by various criteria to find specific spending limits. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_SearchSpendingLimits_RequestSyntax"></a>

```
POST /spending-limits HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "operator": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchSpendingLimits_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchSpendingLimits_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchSpendingLimits_RequestSyntax) **   <a name="braket-SearchSpendingLimits-request-filters"></a>
The filters to apply when searching for spending limits. Use filters to narrow down the results based on specific criteria.
Type: Array of [SearchSpendingLimitsFilter](API_SearchSpendingLimitsFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_SearchSpendingLimits_RequestSyntax) **   <a name="braket-SearchSpendingLimits-request-maxResults"></a>
The maximum number of results to return in a single call. Minimum value of 1, maximum value of 100. Default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_SearchSpendingLimits_RequestSyntax) **   <a name="braket-SearchSpendingLimits-request-nextToken"></a>
The token to retrieve the next page of results. This value is returned from a previous call to SearchSpendingLimits when there are more results available.
Type: String
Required: No

## Response Syntax
<a name="API_SearchSpendingLimits_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "spendingLimits": [
      {
         "createdAt": "string",
         "deviceArn": "string",
         "queuedSpend": "string",
         "spendingLimit": "string",
         "spendingLimitArn": "string",
         "tags": {
            "string" : "string"
         },
         "timePeriod": {
            "endAt": number,
            "startAt": number
         },
         "totalSpend": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchSpendingLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_SearchSpendingLimits_ResponseSyntax) **   <a name="braket-SearchSpendingLimits-response-nextToken"></a>
The token to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

 ** [spendingLimits](#API_SearchSpendingLimits_ResponseSyntax) **   <a name="braket-SearchSpendingLimits-response-spendingLimits"></a>
An array of spending limit summaries that match the specified filters.
Type: Array of [SpendingLimitSummary](API_SpendingLimitSummary.md) objects

## Errors
<a name="API_SearchSpendingLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ThrottlingException **
The API throttling rate limit is exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input request failed to satisfy constraints expected by Amazon Braket.
 ** programSetValidationFailures **
The validation failures in the program set submitted in the request.
 ** reason **
The reason for validation failure.
HTTP Status Code: 400

## See Also
<a name="API_SearchSpendingLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/SearchSpendingLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/SearchSpendingLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
