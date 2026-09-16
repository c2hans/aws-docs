---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetUsageStatistics.html
---

# GetUsageStatistics
<a name="API_GetUsageStatistics"></a>

Lists Amazon GuardDuty usage statistics over the last 30 days for the specified detector ID. For newly enabled detectors or data sources, the cost returned will include only the usage so far under 30 days. This may differ from the cost metrics in the console, which project usage over 30 days to provide a monthly cost estimate. For more information, see [Understanding How Usage Costs are Calculated](https://docs.aws.amazon.com/guardduty/latest/ug/monitoring_costs.html#usage-calculations).

## Request Syntax
<a name="API_GetUsageStatistics_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/usage/statistics HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "unit": "{{string}}",
   "usageCriteria": {
      "accountIds": [ "{{string}}" ],
      "dataSources": [ "{{string}}" ],
      "features": [ "{{string}}" ],
      "resources": [ "{{string}}" ]
   },
   "usageStatisticsType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetUsageStatistics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_GetUsageStatistics_RequestSyntax) **   <a name="guardduty-GetUsageStatistics-request-uri-DetectorId"></a>
The ID of the detector that specifies the GuardDuty service whose usage statistics you want to retrieve.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_GetUsageStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetUsageStatistics_RequestSyntax) **   <a name="guardduty-GetUsageStatistics-request-maxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_GetUsageStatistics_RequestSyntax) **   <a name="guardduty-GetUsageStatistics-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.
Type: String
Required: No

 ** [unit](#API_GetUsageStatistics_RequestSyntax) **   <a name="guardduty-GetUsageStatistics-request-unit"></a>
The currency unit you would like to view your usage statistics in. Current valid values are USD.
Type: String
Required: No

 ** [usageCriteria](#API_GetUsageStatistics_RequestSyntax) **   <a name="guardduty-GetUsageStatistics-request-usageCriteria"></a>
Represents the criteria used for querying usage.
Type: [UsageCriteria](API_UsageCriteria.md) object
Required: Yes

 ** [usageStatisticsType](#API_GetUsageStatistics_RequestSyntax) **   <a name="guardduty-GetUsageStatistics-request-usageStatisticsType"></a>
The type of usage statistics to retrieve.
Type: String
Valid Values: `SUM_BY_ACCOUNT | SUM_BY_DATA_SOURCE | SUM_BY_RESOURCE | TOP_RESOURCES | SUM_BY_FEATURES | TOP_ACCOUNTS_BY_FEATURE`
Required: Yes

## Response Syntax
<a name="API_GetUsageStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "usageStatistics": {
      "sumByAccount": [
         {
            "accountId": "string",
            "total": {
               "amount": "string",
               "unit": "string"
            }
         }
      ],
      "sumByDataSource": [
         {
            "dataSource": "string",
            "total": {
               "amount": "string",
               "unit": "string"
            }
         }
      ],
      "sumByFeature": [
         {
            "feature": "string",
            "total": {
               "amount": "string",
               "unit": "string"
            }
         }
      ],
      "sumByResource": [
         {
            "resource": "string",
            "total": {
               "amount": "string",
               "unit": "string"
            }
         }
      ],
      "topAccountsByFeature": [
         {
            "accounts": [
               {
                  "accountId": "string",
                  "total": {
                     "amount": "string",
                     "unit": "string"
                  }
               }
            ],
            "feature": "string"
         }
      ],
      "topResources": [
         {
            "resource": "string",
            "total": {
               "amount": "string",
               "unit": "string"
            }
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetUsageStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetUsageStatistics_ResponseSyntax) **   <a name="guardduty-GetUsageStatistics-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String

 ** [usageStatistics](#API_GetUsageStatistics_ResponseSyntax) **   <a name="guardduty-GetUsageStatistics-response-usageStatistics"></a>
The usage statistics object. If a UsageStatisticType was provided, the objects representing other types will be null.
Type: [UsageStatistics](API_UsageStatistics.md) object

## Errors
<a name="API_GetUsageStatistics_Errors"></a>

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
<a name="API_GetUsageStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/GetUsageStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/GetUsageStatistics)
