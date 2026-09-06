---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsTrendsV2.html
---

# GetFindingsTrendsV2
<a name="API_GetFindingsTrendsV2"></a>

Returns findings trend data based on the specified criteria. This operation helps you analyze patterns and changes in findings over time.

## Request Syntax
<a name="API_GetFindingsTrendsV2_RequestSyntax"></a>

```
POST /findingsTrendsv2 HTTP/1.1
Content-type: application/json

{
   "EndTime": "{{string}}",
   "Filters": {
      "CompositeFilters": [
         {
            "NestedCompositeFilters": [
               "FindingsTrendsCompositeFilter"
            ],
            "Operator": "{{string}}",
            "StringFilters": [
               {
                  "FieldName": "{{string}}",
                  "Filter": {
                     "Comparison": "{{string}}",
                     "Value": "{{string}}"
                  }
               }
            ]
         }
      ],
      "CompositeOperator": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTime": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetFindingsTrendsV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetFindingsTrendsV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetFindingsTrendsV2_RequestSyntax) **   <a name="securityhub-GetFindingsTrendsV2-request-EndTime"></a>
The ending timestamp for the time period to analyze findings trends, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** [Filters](#API_GetFindingsTrendsV2_RequestSyntax) **   <a name="securityhub-GetFindingsTrendsV2-request-Filters"></a>
The filters to apply to the findings trend data.
Type: [FindingsTrendsFilters](API_FindingsTrendsFilters.md) object
Required: No

 ** [MaxResults](#API_GetFindingsTrendsV2_RequestSyntax) **   <a name="securityhub-GetFindingsTrendsV2-request-MaxResults"></a>
The maximum number of trend data points to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetFindingsTrendsV2_RequestSyntax) **   <a name="securityhub-GetFindingsTrendsV2-request-NextToken"></a>
The token to use for paginating results. This value is returned in the response if more results are available.
Type: String
Required: No

 ** [StartTime](#API_GetFindingsTrendsV2_RequestSyntax) **   <a name="securityhub-GetFindingsTrendsV2-request-StartTime"></a>
The starting timestamp for the time period to analyze findings trends, in ISO 8601 format.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetFindingsTrendsV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Granularity": "string",
   "NextToken": "string",
   "TrendsMetrics": [
      {
         "Timestamp": "string",
         "TrendsValues": {
            "SeverityTrends": {
               "Critical": number,
               "Fatal": number,
               "High": number,
               "Informational": number,
               "Low": number,
               "Medium": number,
               "Other": number,
               "Unknown": number
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetFindingsTrendsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Granularity](#API_GetFindingsTrendsV2_ResponseSyntax) **   <a name="securityhub-GetFindingsTrendsV2-response-Granularity"></a>
The time interval granularity for the returned trend data.
Type: String
Valid Values: `Daily | Weekly | Monthly`

 ** [NextToken](#API_GetFindingsTrendsV2_ResponseSyntax) **   <a name="securityhub-GetFindingsTrendsV2-response-NextToken"></a>
The token to use for retrieving the next page of results, if more trend data is available.
Type: String

 ** [TrendsMetrics](#API_GetFindingsTrendsV2_ResponseSyntax) **   <a name="securityhub-GetFindingsTrendsV2-response-TrendsMetrics"></a>
The collection of time-series trend metrics, including counts of findings by severity across the specified time period.
Type: Array of [TrendsMetricsResult](API_TrendsMetricsResult.md) objects

## Errors
<a name="API_GetFindingsTrendsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_GetFindingsTrendsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetFindingsTrendsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetFindingsTrendsV2)
