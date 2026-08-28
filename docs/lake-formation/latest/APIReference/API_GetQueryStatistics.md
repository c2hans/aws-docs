---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetQueryStatistics.html
---

# GetQueryStatistics
<a name="API_GetQueryStatistics"></a>

Retrieves statistics on the planning and execution of a query.

## Request Syntax
<a name="API_GetQueryStatistics_RequestSyntax"></a>

```
POST /GetQueryStatistics HTTP/1.1
Content-type: application/json

{
   "QueryId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetQueryStatistics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetQueryStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [QueryId](#API_GetQueryStatistics_RequestSyntax) **   <a name="lakeformation-GetQueryStatistics-request-QueryId"></a>
The ID of the plan query operation.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

## Response Syntax
<a name="API_GetQueryStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExecutionStatistics": {
      "AverageExecutionTimeMillis": number,
      "DataScannedBytes": number,
      "WorkUnitsExecutedCount": number
   },
   "PlanningStatistics": {
      "EstimatedDataToScanBytes": number,
      "PlanningTimeMillis": number,
      "QueueTimeMillis": number,
      "WorkUnitsGeneratedCount": number
   },
   "QuerySubmissionTime": "string"
}
```

## Response Elements
<a name="API_GetQueryStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExecutionStatistics](#API_GetQueryStatistics_ResponseSyntax) **   <a name="lakeformation-GetQueryStatistics-response-ExecutionStatistics"></a>
An `ExecutionStatistics` structure containing execution statistics.
Type: [ExecutionStatistics](API_ExecutionStatistics.md) object

 ** [PlanningStatistics](#API_GetQueryStatistics_ResponseSyntax) **   <a name="lakeformation-GetQueryStatistics-response-PlanningStatistics"></a>
A `PlanningStatistics` structure containing query planning statistics.
Type: [PlanningStatistics](API_PlanningStatistics.md) object

 ** [QuerySubmissionTime](#API_GetQueryStatistics_ResponseSyntax) **   <a name="lakeformation-GetQueryStatistics-response-QuerySubmissionTime"></a>
The time that the query was submitted.
Type: Timestamp

## Errors
<a name="API_GetQueryStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** ExpiredException **
Contains details about an error where the query request expired.
 ** Message **
A message describing the error.
HTTP Status Code: 410

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** StatisticsNotReadyYetException **
Contains details about an error related to statistics not being ready.
 ** Message **
A message describing the error.
HTTP Status Code: 420

 ** ThrottledException **
Contains details about an error where the query request was throttled.
 ** Message **
A message describing the error.
HTTP Status Code: 429

## See Also
<a name="API_GetQueryStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetQueryStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetQueryStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
