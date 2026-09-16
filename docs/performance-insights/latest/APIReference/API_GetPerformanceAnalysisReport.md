---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetPerformanceAnalysisReport.html
---

# GetPerformanceAnalysisReport
<a name="API_GetPerformanceAnalysisReport"></a>

Retrieves the report including the report ID, status, time details, and the insights with recommendations. The report status can be `RUNNING`, `SUCCEEDED`, or `FAILED`. The insights include the `description` and `recommendation` fields.

## Request Syntax
<a name="API_GetPerformanceAnalysisReport_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "AnalysisReportId": "{{string}}",
   "Identifier": "{{string}}",
   "ServiceType": "{{string}}",
   "TextFormat": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPerformanceAnalysisReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AnalysisReportId](#API_GetPerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-GetPerformanceAnalysisReport-request-AnalysisReportId"></a>
A unique identifier of the created analysis report. For example, `report-12345678901234567`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `report-[0-9a-f]{17}`
Required: Yes

 ** [Identifier](#API_GetPerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-GetPerformanceAnalysisReport-request-Identifier"></a>
An immutable identifier for a data source that is unique for an AWS Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID*. When you call `DescribeDBInstances`, the identifier is returned as `DbiResourceId`.
To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [ServiceType](#API_GetPerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-GetPerformanceAnalysisReport-request-ServiceType"></a>
The AWS service for which Performance Insights will return metrics. Valid value is `RDS`.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [AcceptLanguage](#API_GetPerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-GetPerformanceAnalysisReport-request-AcceptLanguage"></a>
The text language in the report. The default language is `EN_US` (English).
Type: String
Valid Values: `EN_US`
Required: No

 ** [TextFormat](#API_GetPerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-GetPerformanceAnalysisReport-request-TextFormat"></a>
Indicates the text format in the report. The options are `PLAIN_TEXT` or `MARKDOWN`. The default value is `plain text`.
Type: String
Valid Values: `PLAIN_TEXT | MARKDOWN`
Required: No

## Response Syntax
<a name="API_GetPerformanceAnalysisReport_ResponseSyntax"></a>

```
{
   "AnalysisReport": {
      "AnalysisReportId": "string",
      "CreateTime": number,
      "EndTime": number,
      "Identifier": "string",
      "Insights": [
         {
            "BaselineData": [
               {
                  "PerformanceInsightsMetric": {
                     "Dimensions": {
                        "string" : "string"
                     },
                     "DisplayName": "string",
                     "Filter": {
                        "string" : "string"
                     },
                     "Metric": "string",
                     "Value": number
                  }
               }
            ],
            "Context": "string",
            "Description": "string",
            "EndTime": number,
            "InsightData": [
               {
                  "PerformanceInsightsMetric": {
                     "Dimensions": {
                        "string" : "string"
                     },
                     "DisplayName": "string",
                     "Filter": {
                        "string" : "string"
                     },
                     "Metric": "string",
                     "Value": number
                  }
               }
            ],
            "InsightId": "string",
            "InsightType": "string",
            "Recommendations": [
               {
                  "RecommendationDescription": "string",
                  "RecommendationDetails": "string",
                  "RecommendationId": "string"
               }
            ],
            "Severity": "string",
            "StartTime": number,
            "SupportingInsights": [
               "Insight"
            ]
         }
      ],
      "ServiceType": "string",
      "StartTime": number,
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_GetPerformanceAnalysisReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalysisReport](#API_GetPerformanceAnalysisReport_ResponseSyntax) **   <a name="performanceinsights-GetPerformanceAnalysisReport-response-AnalysisReport"></a>
The summary of the performance analysis report created for a time period.
Type: [AnalysisReport](API_AnalysisReport.md) object

## Errors
<a name="API_GetPerformanceAnalysisReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
The request failed due to an unknown error.
HTTP Status Code: 500

 ** InvalidArgumentException **
One of the arguments provided is invalid for this request.
HTTP Status Code: 400

 ** NotAuthorizedException **
The user is not authorized to perform this request.
HTTP Status Code: 400

## Examples
<a name="API_GetPerformanceAnalysisReport_Examples"></a>

### Retrieve a performance analysis report
<a name="API_GetPerformanceAnalysisReport_Example_1"></a>

The following example gets the report insights and other details for the report `report-01234567890abcdef`.

#### Sample Request
<a name="API_GetPerformanceAnalysisReport_Example_1_Request"></a>

```
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetPerformanceAnalysisReport
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "AnalysisReportId": "report-01234567890abcdef",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "ServiceType": "RDS"
}
```

#### Sample Response
<a name="API_GetPerformanceAnalysisReport_Example_1_Response"></a>

```
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
    "AnalysisReport": {
        "AnalysisReportId": "report-01234567890abcdef",
        "CreateTime": 1690906983.028,
        "EndTime": 1690453065,
        "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
        "Insights": [
            {
                "BaselineData": [
                    {
                        "PerformanceInsightsMetric": {
                            "Dimensions": {},
                            "Metric": "db.load.avg",
                            "Value": 0
                        }
                    }
                ],
                "Context": "CAUSAL",
                "Description": "The database is idle, with no detectable load for the time range.",
                "EndTime": 1690453065,
                "InsightData": [
                    {
                        "PerformanceInsightsMetric": {
                            "Dimensions": {},
                            "Metric": "db.load.avg",
                            "Value": 0
                        }
                    }
                ],
                "InsightId": "MURCX0xPQURfWkVSTwY8NIdQhkWEeU19Zybf8H636v470O8ID2uUn6uLWFp5MDAwMDAwMDAw",
                "InsightType": "DB_LOAD_ZERO",
                "Recommendations": [
                    {
                        "RecommendationDescription": "Try creating an analysis report for a different time range.",
                        "RecommendationId": "MVJlY29tbWVuZGF0aW9uREJfTE9BRF9aRVJPvXe8CGe_f-ZX2tY-Em61aD6v2u9wcPi58j_zY28eKEwwMDAwMDAwMDA="
                    }
                ],
                "Severity": "LOW",
                "StartTime": 1690009222,
                "SupportingInsights": []
            }
        ],
        "ServiceType": "RDS",
        "StartTime": 1690009222,
        "Status": "SUCCEEDED"
    }
}
```

## See Also
<a name="API_GetPerformanceAnalysisReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/GetPerformanceAnalysisReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/GetPerformanceAnalysisReport)
