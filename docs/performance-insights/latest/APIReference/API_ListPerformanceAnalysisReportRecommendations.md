---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListPerformanceAnalysisReportRecommendations.html
---

# ListPerformanceAnalysisReportRecommendations
<a name="API_ListPerformanceAnalysisReportRecommendations"></a>

Retrieves recommendations for a performance analysis report.

## Request Syntax
<a name="API_ListPerformanceAnalysisReportRecommendations_RequestSyntax"></a>

```
{
   "AnalysisReportId": "{{string}}",
   "Identifier": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RecommendationIds": [ "{{string}}" ],
   "ServiceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPerformanceAnalysisReportRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AnalysisReportId](#API_ListPerformanceAnalysisReportRecommendations_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReportRecommendations-request-AnalysisReportId"></a>
A unique identifier of the created analysis report. For example, `report-12345678901234567`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `report-[0-9a-f]{17}`
Required: Yes

 ** [Identifier](#API_ListPerformanceAnalysisReportRecommendations_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReportRecommendations-request-Identifier"></a>
An immutable identifier for a data source that is unique for an AWS Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID*. When you call `DescribeDBInstances`, the identifier is returned as `DbiResourceId`.
To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [ServiceType](#API_ListPerformanceAnalysisReportRecommendations_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReportRecommendations-request-ServiceType"></a>
The AWS service for which Performance Insights returns metrics. Valid value is `RDS`.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [MaxResults](#API_ListPerformanceAnalysisReportRecommendations_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReportRecommendations-request-MaxResults"></a>
The maximum number of items to return in the response. If more items exist than the specified `MaxResults` value, a pagination token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No

 ** [NextToken](#API_ListPerformanceAnalysisReportRecommendations_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReportRecommendations-request-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxResults`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`
Required: No

 ** [RecommendationIds](#API_ListPerformanceAnalysisReportRecommendations_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReportRecommendations-request-RecommendationIds"></a>
A list of recommendation identifiers to filter the results.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_ListPerformanceAnalysisReportRecommendations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Recommendations": [
      {
         "RecommendationDescription": "string",
         "RecommendationDetails": "string",
         "RecommendationId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPerformanceAnalysisReportRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPerformanceAnalysisReportRecommendations_ResponseSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReportRecommendations-response-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxResults`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`

 ** [Recommendations](#API_ListPerformanceAnalysisReportRecommendations_ResponseSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReportRecommendations-response-Recommendations"></a>
The list of recommendations for the analysis report.
Type: Array of [Recommendation](API_Recommendation.md) objects

## Errors
<a name="API_ListPerformanceAnalysisReportRecommendations_Errors"></a>

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

## See Also
<a name="API_ListPerformanceAnalysisReportRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/ListPerformanceAnalysisReportRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
