---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCoverageStatistics.html
---

# GetCoverageStatistics
<a name="API_GetCoverageStatistics"></a>

Retrieves aggregated statistics for your account. If you are a GuardDuty administrator, you can retrieve the statistics for all the resources associated with the active member accounts in your organization who have enabled Runtime Monitoring and have the GuardDuty security agent running on their resources.

## Request Syntax
<a name="API_GetCoverageStatistics_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/coverage/statistics HTTP/1.1
Content-type: application/json

{
   "filterCriteria": {
      "filterCriterion": [
         {
            "criterionKey": "{{string}}",
            "filterCondition": {
               "equals": [ "{{string}}" ],
               "notEquals": [ "{{string}}" ]
            }
         }
      ]
   },
   "statisticsType": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetCoverageStatistics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetCoverageStatistics_RequestSyntax) **   <a name="guardduty-GetCoverageStatistics-request-uri-DetectorId"></a>
The unique ID of the GuardDuty detector.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_GetCoverageStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_GetCoverageStatistics_RequestSyntax) **   <a name="guardduty-GetCoverageStatistics-request-filterCriteria"></a>
Represents the criteria used to filter the coverage statistics.
Type: [CoverageFilterCriteria](API_CoverageFilterCriteria.md) object
Required: No

 ** [statisticsType](#API_GetCoverageStatistics_RequestSyntax) **   <a name="guardduty-GetCoverageStatistics-request-statisticsType"></a>
Represents the statistics type used to aggregate the coverage details.
Type: Array of strings
Valid Values: `COUNT_BY_RESOURCE_TYPE | COUNT_BY_COVERAGE_STATUS`
Required: Yes

## Response Syntax
<a name="API_GetCoverageStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "coverageStatistics": {
      "countByCoverageStatus": {
         "string" : number
      },
      "countByResourceType": {
         "string" : number
      }
   }
}
```

## Response Elements
<a name="API_GetCoverageStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [coverageStatistics](#API_GetCoverageStatistics_ResponseSyntax) **   <a name="guardduty-GetCoverageStatistics-response-coverageStatistics"></a>
Represents the count aggregated by the `statusCode` and `resourceType`.
Type: [CoverageStatistics](API_CoverageStatistics.md) object

## Errors
<a name="API_GetCoverageStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_GetCoverageStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetCoverageStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetCoverageStatistics)
