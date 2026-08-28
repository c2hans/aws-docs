---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeTestSetDiscrepancyReport.html
---

# DescribeTestSetDiscrepancyReport
<a name="API_DescribeTestSetDiscrepancyReport"></a>

Gets metadata information about the test set discrepancy report.

## Request Syntax
<a name="API_DescribeTestSetDiscrepancyReport_RequestSyntax"></a>

```
GET /testsetdiscrepancy/{{testSetDiscrepancyReportId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTestSetDiscrepancyReport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testSetDiscrepancyReportId](#API_DescribeTestSetDiscrepancyReport_RequestSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-request-uri-testSetDiscrepancyReportId"></a>
The unique identifier of the test set discrepancy report.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeTestSetDiscrepancyReport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTestSetDiscrepancyReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDateTime": number,
   "failureReasons": [ "string" ],
   "lastUpdatedDataTime": number,
   "target": {
      "botAliasTarget": {
         "botAliasId": "string",
         "botId": "string",
         "localeId": "string"
      }
   },
   "testSetDiscrepancyRawOutputUrl": "string",
   "testSetDiscrepancyReportId": "string",
   "testSetDiscrepancyReportStatus": "string",
   "testSetDiscrepancyTopErrors": {
      "intentDiscrepancies": [
         {
            "errorMessage": "string",
            "intentName": "string"
         }
      ],
      "slotDiscrepancies": [
         {
            "errorMessage": "string",
            "intentName": "string",
            "slotName": "string"
         }
      ]
   },
   "testSetId": "string"
}
```

## Response Elements
<a name="API_DescribeTestSetDiscrepancyReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-creationDateTime"></a>
The time and date of creation for the test set discrepancy report.
Type: Timestamp

 ** [failureReasons](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-failureReasons"></a>
The failure report for the test set discrepancy report generation action.
Type: Array of strings

 ** [lastUpdatedDataTime](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-lastUpdatedDataTime"></a>
The date and time of the last update for the test set discrepancy report.
Type: Timestamp

 ** [target](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-target"></a>
The target bot location for the test set discrepancy report.
Type: [TestSetDiscrepancyReportResourceTarget](API_TestSetDiscrepancyReportResourceTarget.md) object

 ** [testSetDiscrepancyRawOutputUrl](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-testSetDiscrepancyRawOutputUrl"></a>
Pre-signed Amazon S3 URL to download the test set discrepancy report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [testSetDiscrepancyReportId](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-testSetDiscrepancyReportId"></a>
The unique identifier of the test set discrepancy report to describe.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testSetDiscrepancyReportStatus](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-testSetDiscrepancyReportStatus"></a>
The status for the test set discrepancy report.
Type: String
Valid Values: `InProgress | Completed | Failed`

 ** [testSetDiscrepancyTopErrors](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-testSetDiscrepancyTopErrors"></a>
The top 200 error results from the test set discrepancy report.
Type: [TestSetDiscrepancyErrors](API_TestSetDiscrepancyErrors.md) object

 ** [testSetId](#API_DescribeTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-DescribeTestSetDiscrepancyReport-response-testSetId"></a>
The test set Id for the test set discrepancy report.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

## Errors
<a name="API_DescribeTestSetDiscrepancyReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTestSetDiscrepancyReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
