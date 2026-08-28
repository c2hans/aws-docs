---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartColumnStatisticsTaskRun.html
---

# StartColumnStatisticsTaskRun
<a name="API_StartColumnStatisticsTaskRun"></a>

Starts a column statistics task run, for a specified table and columns.

## Request Syntax
<a name="API_StartColumnStatisticsTaskRun_RequestSyntax"></a>

```
{
   "CatalogID": "{{string}}",
   "ColumnNameList": [ "{{string}}" ],
   "DatabaseName": "{{string}}",
   "Role": "{{string}}",
   "SampleSize": {{number}},
   "SecurityConfiguration": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartColumnStatisticsTaskRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogID](#API_StartColumnStatisticsTaskRun_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRun-request-CatalogID"></a>
The ID of the Data Catalog where the table reside. If none is supplied, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ColumnNameList](#API_StartColumnStatisticsTaskRun_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRun-request-ColumnNameList"></a>
A list of the column names to generate statistics. If none is supplied, all column names for the table will be used by default.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_StartColumnStatisticsTaskRun_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRun-request-DatabaseName"></a>
The name of the database where the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Role](#API_StartColumnStatisticsTaskRun_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRun-request-Role"></a>
The IAM role that the service assumes to generate statistics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [SampleSize](#API_StartColumnStatisticsTaskRun_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRun-request-SampleSize"></a>
The percentage of rows used to generate statistics. If none is supplied, the entire table will be used to generate stats.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [SecurityConfiguration](#API_StartColumnStatisticsTaskRun_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRun-request-SecurityConfiguration"></a>
Name of the security configuration that is used to encrypt CloudWatch logs for the column stats task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [TableName](#API_StartColumnStatisticsTaskRun_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRun-request-TableName"></a>
The name of the table to generate statistics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_StartColumnStatisticsTaskRun_ResponseSyntax"></a>

```
{
   "ColumnStatisticsTaskRunId": "string"
}
```

## Response Elements
<a name="API_StartColumnStatisticsTaskRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ColumnStatisticsTaskRunId](#API_StartColumnStatisticsTaskRun_ResponseSyntax) **   <a name="Glue-StartColumnStatisticsTaskRun-response-ColumnStatisticsTaskRunId"></a>
The identifier for the column statistics task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_StartColumnStatisticsTaskRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ColumnStatisticsTaskRunningException **
An exception thrown when you try to start another job while running a column stats generation job.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartColumnStatisticsTaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartColumnStatisticsTaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartColumnStatisticsTaskRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
