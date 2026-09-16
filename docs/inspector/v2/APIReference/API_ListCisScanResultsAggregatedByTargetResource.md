---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanResultsAggregatedByTargetResource.html
---

# ListCisScanResultsAggregatedByTargetResource
<a name="API_ListCisScanResultsAggregatedByTargetResource"></a>

Lists scan results aggregated by a target resource.

## Request Syntax
<a name="API_ListCisScanResultsAggregatedByTargetResource_RequestSyntax"></a>

```
POST /cis/scan-result/resource/list HTTP/1.1
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
      "failedChecksFilters": [
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
      "statusFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "targetResourceIdFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "targetResourceTagFilters": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "targetStatusFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "targetStatusReasonFilters": [
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
<a name="API_ListCisScanResultsAggregatedByTargetResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCisScanResultsAggregatedByTargetResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_ListCisScanResultsAggregatedByTargetResource_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByTargetResource-request-filterCriteria"></a>
The filter criteria.
Type: [CisScanResultsAggregatedByTargetResourceFilterCriteria](API_CisScanResultsAggregatedByTargetResourceFilterCriteria.md) object
Required: No

 ** [maxResults](#API_ListCisScanResultsAggregatedByTargetResource_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByTargetResource-request-maxResults"></a>
The maximum number of scan results aggregated by a target resource to be returned in a single page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCisScanResultsAggregatedByTargetResource_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByTargetResource-request-nextToken"></a>
The pagination token from a previous request that's used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

 ** [scanArn](#API_ListCisScanResultsAggregatedByTargetResource_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByTargetResource-request-scanArn"></a>
The scan ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [sortBy](#API_ListCisScanResultsAggregatedByTargetResource_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByTargetResource-request-sortBy"></a>
The sort by order.
Type: String
Valid Values: `RESOURCE_ID | FAILED_COUNTS | ACCOUNT_ID | PLATFORM | TARGET_STATUS | TARGET_STATUS_REASON`
Required: No

 ** [sortOrder](#API_ListCisScanResultsAggregatedByTargetResource_RequestSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByTargetResource-request-sortOrder"></a>
The sort order.
Type: String
Valid Values: `ASC | DESC`
Required: No

## Response Syntax
<a name="API_ListCisScanResultsAggregatedByTargetResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "targetResourceAggregations": [
      {
         "accountId": "string",
         "platform": "string",
         "scanArn": "string",
         "statusCounts": {
            "failed": number,
            "passed": number,
            "skipped": number
         },
         "targetResourceId": "string",
         "targetResourceTags": {
            "string" : [ "string" ]
         },
         "targetStatus": "string",
         "targetStatusReason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListCisScanResultsAggregatedByTargetResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListCisScanResultsAggregatedByTargetResource_ResponseSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByTargetResource-response-nextToken"></a>
The pagination token from a previous request that's used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

 ** [targetResourceAggregations](#API_ListCisScanResultsAggregatedByTargetResource_ResponseSyntax) **   <a name="inspector2-ListCisScanResultsAggregatedByTargetResource-response-targetResourceAggregations"></a>
The resource aggregations.
Type: Array of [CisTargetResourceAggregation](API_CisTargetResourceAggregation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.

## Errors
<a name="API_ListCisScanResultsAggregatedByTargetResource_Errors"></a>

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
<a name="API_ListCisScanResultsAggregatedByTargetResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCisScanResultsAggregatedByTargetResource)
