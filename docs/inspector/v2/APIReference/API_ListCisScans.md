---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScans.html
---

# ListCisScans
<a name="API_ListCisScans"></a>

Returns a CIS scan list.

## Request Syntax
<a name="API_ListCisScans_RequestSyntax"></a>

```
POST /cis/scan/list HTTP/1.1
Content-type: application/json

{
   "detailLevel": "{{string}}",
   "filterCriteria": {
      "failedChecksFilters": [
         {
            "lowerInclusive": {{number}},
            "upperInclusive": {{number}}
         }
      ],
      "scanArnFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanAtFilters": [
         {
            "earliestScanStartTime": {{number}},
            "latestScanStartTime": {{number}}
         }
      ],
      "scanConfigurationArnFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanNameFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanStatusFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scheduledByFilters": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "targetAccountIdFilters": [
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
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCisScans_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCisScans_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [detailLevel](#API_ListCisScans_RequestSyntax) **   <a name="inspector2-ListCisScans-request-detailLevel"></a>
The detail applied to the CIS scan.
Type: String
Valid Values: `ORGANIZATION | MEMBER`
Required: No

 ** [filterCriteria](#API_ListCisScans_RequestSyntax) **   <a name="inspector2-ListCisScans-request-filterCriteria"></a>
The CIS scan filter criteria.
Type: [ListCisScansFilterCriteria](API_ListCisScansFilterCriteria.md) object
Required: No

 ** [maxResults](#API_ListCisScans_RequestSyntax) **   <a name="inspector2-ListCisScans-request-maxResults"></a>
The maximum number of results to be returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListCisScans_RequestSyntax) **   <a name="inspector2-ListCisScans-request-nextToken"></a>
The pagination token from a previous request that's used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

 ** [sortBy](#API_ListCisScans_RequestSyntax) **   <a name="inspector2-ListCisScans-request-sortBy"></a>
The CIS scans sort by order.
Type: String
Valid Values: `STATUS | SCHEDULED_BY | SCAN_START_DATE | FAILED_CHECKS`
Required: No

 ** [sortOrder](#API_ListCisScans_RequestSyntax) **   <a name="inspector2-ListCisScans-request-sortOrder"></a>
The CIS scans sort order.
Type: String
Valid Values: `ASC | DESC`
Required: No

## Response Syntax
<a name="API_ListCisScans_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "scans": [
      {
         "failedChecks": number,
         "scanArn": "string",
         "scanConfigurationArn": "string",
         "scanDate": number,
         "scanName": "string",
         "scheduledBy": "string",
         "securityLevel": "string",
         "status": "string",
         "targets": {
            "accountIds": [ "string" ],
            "targetResourceTags": {
               "string" : [ "string" ]
            }
         },
         "totalChecks": number
      }
   ]
}
```

## Response Elements
<a name="API_ListCisScans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListCisScans_ResponseSyntax) **   <a name="inspector2-ListCisScans-response-nextToken"></a>
The pagination token from a previous request that's used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

 ** [scans](#API_ListCisScans_ResponseSyntax) **   <a name="inspector2-ListCisScans-response-scans"></a>
The CIS scans.
Type: Array of [CisScan](API_CisScan.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_ListCisScans_Errors"></a>

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
<a name="API_ListCisScans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListCisScans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCisScans)
