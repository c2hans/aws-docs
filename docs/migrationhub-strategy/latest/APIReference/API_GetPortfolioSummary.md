---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioSummary.html
---

# GetPortfolioSummary
<a name="API_GetPortfolioSummary"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves overall summary including the number of servers to rehost and the overall number of anti-patterns.

## Request Syntax
<a name="API_GetPortfolioSummary_RequestSyntax"></a>

```
GET /get-portfolio-summary HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPortfolioSummary_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPortfolioSummary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPortfolioSummary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assessmentSummary": {
      "antipatternReportS3Object": {
         "s3Bucket": "string",
         "s3key": "string"
      },
      "antipatternReportStatus": "string",
      "antipatternReportStatusMessage": "string",
      "lastAnalyzedTimestamp": number,
      "listAntipatternSeveritySummary": [
         {
            "count": number,
            "severity": "string"
         }
      ],
      "listApplicationComponentStatusSummary": [
         {
            "count": number,
            "srcCodeOrDbAnalysisStatus": "string"
         }
      ],
      "listApplicationComponentStrategySummary": [
         {
            "count": number,
            "strategy": "string"
         }
      ],
      "listApplicationComponentSummary": [
         {
            "appType": "string",
            "count": number
         }
      ],
      "listServerStatusSummary": [
         {
            "count": number,
            "runTimeAssessmentStatus": "string"
         }
      ],
      "listServerStrategySummary": [
         {
            "count": number,
            "strategy": "string"
         }
      ],
      "listServerSummary": [
         {
            "count": number,
            "ServerOsType": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetPortfolioSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentSummary](#API_GetPortfolioSummary_ResponseSyntax) **   <a name="migrationhubstrategy-GetPortfolioSummary-response-assessmentSummary"></a>
 An assessment summary for the portfolio including the number of servers to rehost and the overall number of anti-patterns.
Type: [AssessmentSummary](API_AssessmentSummary.md) object

## Errors
<a name="API_GetPortfolioSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_GetPortfolioSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetPortfolioSummary)
