---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetReportGroupTrend.html
---

# GetReportGroupTrend
<a name="API_GetReportGroupTrend"></a>

Analyzes and accumulates test report values for the specified test reports.

## Request Syntax
<a name="API_GetReportGroupTrend_RequestSyntax"></a>

```
{
   "numOfReports": {{number}},
   "reportGroupArn": "{{string}}",
   "trendField": "{{string}}"
}
```

## Request Parameters
<a name="API_GetReportGroupTrend_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [reportGroupArn](#API_GetReportGroupTrend_RequestSyntax) **   <a name="CodeBuild-GetReportGroupTrend-request-reportGroupArn"></a>
The ARN of the report group that contains the reports to analyze.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [trendField](#API_GetReportGroupTrend_RequestSyntax) **   <a name="CodeBuild-GetReportGroupTrend-request-trendField"></a>
The test report value to accumulate. This must be one of the following values:
Test reports:
DURATION
Accumulate the test run times for the specified reports.
PASS\_RATE
Accumulate the percentage of tests that passed for the specified test reports.
TOTAL
Accumulate the total number of tests for the specified test reports.
Code coverage reports:
BRANCH\_COVERAGE
Accumulate the branch coverage percentages for the specified test reports.
BRANCHES\_COVERED
Accumulate the branches covered values for the specified test reports.
BRANCHES\_MISSED
Accumulate the branches missed values for the specified test reports.
LINE\_COVERAGE
Accumulate the line coverage percentages for the specified test reports.
LINES\_COVERED
Accumulate the lines covered values for the specified test reports.
LINES\_MISSED
Accumulate the lines not covered values for the specified test reports.
Type: String
Valid Values: `PASS_RATE | DURATION | TOTAL | LINE_COVERAGE | LINES_COVERED | LINES_MISSED | BRANCH_COVERAGE | BRANCHES_COVERED | BRANCHES_MISSED`
Required: Yes

 ** [numOfReports](#API_GetReportGroupTrend_RequestSyntax) **   <a name="CodeBuild-GetReportGroupTrend-request-numOfReports"></a>
The number of reports to analyze. This operation always retrieves the most recent reports.
If this parameter is omitted, the most recent 100 reports are analyzed.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_GetReportGroupTrend_ResponseSyntax"></a>

```
{
   "rawData": [
      {
         "data": "string",
         "reportArn": "string"
      }
   ],
   "stats": {
      "average": "string",
      "max": "string",
      "min": "string"
   }
}
```

## Response Elements
<a name="API_GetReportGroupTrend_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [rawData](#API_GetReportGroupTrend_ResponseSyntax) **   <a name="CodeBuild-GetReportGroupTrend-response-rawData"></a>
An array that contains the raw data for each report.
Type: Array of [ReportWithRawData](API_ReportWithRawData.md) objects

 ** [stats](#API_GetReportGroupTrend_ResponseSyntax) **   <a name="CodeBuild-GetReportGroupTrend-response-stats"></a>
Contains the accumulated trend data.
Type: [ReportGroupTrendStats](API_ReportGroupTrendStats.md) object

## Errors
<a name="API_GetReportGroupTrend_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_GetReportGroupTrend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/GetReportGroupTrend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/GetReportGroupTrend)
