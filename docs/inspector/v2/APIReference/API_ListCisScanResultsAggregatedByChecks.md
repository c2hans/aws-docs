---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanResultsAggregatedByChecks.html
---

# ListCisScanResultsAggregatedByChecks
<a name="API_ListCisScanResultsAggregatedByChecks"></a>

Lists scan results aggregated by checks.

## Request Syntax
<a name="API_ListCisScanResultsAggregatedByChecks_RequestSyntax"></a>

```
POST /cis/scan-result/check/list HTTP/1.1
Content-type: application/json

{
   "filterCriteria": {
      "accountIdFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "checkIdFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "failedResourcesFilters": [
         {
            "lowerInclusive": {{number}},
            "upperInclusive": {{number}}
         }
      ],
      "platformFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "securityLevelFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "titleFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "scanArn": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCisScanResultsAggregatedByChecks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCisScanResultsAggregatedByChecks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_ListCisScanResultsAggregatedByChecks_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByChecks-request-filterCriteria"></a>
The filter criteria.
Type: [CisScanResultsAggregatedByChecksFilterCriteria](API_CisScanResultsAggregatedByChecksFilterCriteria.md) object
Required: No

 ** [maxResults](#API_ListCisScanResultsAggregatedByChecks_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByChecks-request-maxResults"></a>
The maximum number of scan results aggregated by checks to be returned in a single page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCisScanResultsAggregatedByChecks_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByChecks-request-nextToken"></a>
The pagination token from a previous request that's used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

 ** [scanArn](#API_ListCisScanResultsAggregatedByChecks_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByChecks-request-scanArn"></a>
The scan ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [sortBy](#API_ListCisScanResultsAggregatedByChecks_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByChecks-request-sortBy"></a>
The sort by order.
Type: String
Valid Values: `CHECK_ID | TITLE | PLATFORM | FAILED_COUNTS | SECURITY_LEVEL`
Required: No

 ** [sortOrder](#API_ListCisScanResultsAggregatedByChecks_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByChecks-request-sortOrder"></a>
The sort order.
Type: String
Valid Values: `ASC | DESC`
Required: No

## Response Syntax
<a name="API_ListCisScanResultsAggregatedByChecks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "checkAggregations": [
      {
         "accountId": "string",
         "checkDescription": "string",
         "checkId": "string",
         "level": "string",
         "platform": "string",
         "scanArn": "string",
         "statusCounts": {
            "failed": number,
            "passed": number,
            "skipped": number
         },
         "title": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCisScanResultsAggregatedByChecks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [checkAggregations](#API_ListCisScanResultsAggregatedByChecks_ResponseSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByChecks-response-checkAggregations"></a>
The check aggregations.
Type: Array of [CisCheckAggregation](API_CisCheckAggregation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.

 ** [nextToken](#API_ListCisScanResultsAggregatedByChecks_ResponseSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByChecks-response-nextToken"></a>
The pagination token from a previous request that's used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

## Errors
<a name="API_ListCisScanResultsAggregatedByChecks_Errors"></a>

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
<a name="API_ListCisScanResultsAggregatedByChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCisScanResultsAggregatedByChecks)
