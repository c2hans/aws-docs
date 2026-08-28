---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateTestSetDiscrepancyReport.html
---

# CreateTestSetDiscrepancyReport
<a name="API_CreateTestSetDiscrepancyReport"></a>

Create a report that describes the differences between the bot and the test set.

## Request Syntax
<a name="API_CreateTestSetDiscrepancyReport_RequestSyntax"></a>

```
POST /testsets/{{testSetId}}/testsetdiscrepancy HTTP/1.1
Content-type: application/json

{
   "target": {
      "botAliasTarget": {
         "botAliasId": "{{string}}",
         "botId": "{{string}}",
         "localeId": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateTestSetDiscrepancyReport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testSetId](#API_CreateTestSetDiscrepancyReport_RequestSyntax) **   <a name="lexv2-CreateTestSetDiscrepancyReport-request-uri-testSetId"></a>
The test set Id for the test set discrepancy report.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_CreateTestSetDiscrepancyReport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [target](#API_CreateTestSetDiscrepancyReport_RequestSyntax) **   <a name="lexv2-CreateTestSetDiscrepancyReport-request-target"></a>
The target bot for the test set discrepancy report.
Type: [TestSetDiscrepancyReportResourceTarget](API_TestSetDiscrepancyReportResourceTarget.md) object
Required: Yes

## Response Syntax
<a name="API_CreateTestSetDiscrepancyReport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "creationDateTime": number,
   "target": {
      "botAliasTarget": {
         "botAliasId": "string",
         "botId": "string",
         "localeId": "string"
      }
   },
   "testSetDiscrepancyReportId": "string",
   "testSetId": "string"
}
```

## Response Elements
<a name="API_CreateTestSetDiscrepancyReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_CreateTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-CreateTestSetDiscrepancyReport-response-creationDateTime"></a>
The creation date and time for the test set discrepancy report.
Type: Timestamp

 ** [target](#API_CreateTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-CreateTestSetDiscrepancyReport-response-target"></a>
The target bot for the test set discrepancy report.
Type: [TestSetDiscrepancyReportResourceTarget](API_TestSetDiscrepancyReportResourceTarget.md) object

 ** [testSetDiscrepancyReportId](#API_CreateTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-CreateTestSetDiscrepancyReport-response-testSetDiscrepancyReportId"></a>
The unique identifier of the test set discrepancy report to describe.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testSetId](#API_CreateTestSetDiscrepancyReport_ResponseSyntax) **   <a name="lexv2-CreateTestSetDiscrepancyReport-response-testSetId"></a>
The test set Id for the test set discrepancy report.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

## Errors
<a name="API_CreateTestSetDiscrepancyReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

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
<a name="API_CreateTestSetDiscrepancyReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateTestSetDiscrepancyReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
