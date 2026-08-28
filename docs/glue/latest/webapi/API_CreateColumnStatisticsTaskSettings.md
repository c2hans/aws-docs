---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateColumnStatisticsTaskSettings.html
---

# CreateColumnStatisticsTaskSettings
<a name="API_CreateColumnStatisticsTaskSettings"></a>

Creates settings for a column statistics task.

## Request Syntax
<a name="API_CreateColumnStatisticsTaskSettings_RequestSyntax"></a>

```
{
   "CatalogID": "{{string}}",
   "ColumnNameList": [ "{{string}}" ],
   "DatabaseName": "{{string}}",
   "Role": "{{string}}",
   "SampleSize": {{number}},
   "Schedule": "{{string}}",
   "SecurityConfiguration": "{{string}}",
   "TableName": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateColumnStatisticsTaskSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogID](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-CatalogID"></a>
The ID of the Data Catalog in which the database resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ColumnNameList](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-ColumnNameList"></a>
A list of column names for which to run statistics.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-DatabaseName"></a>
The name of the database where the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Role](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-Role"></a>
The role used for running the column statistics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [SampleSize](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-SampleSize"></a>
The percentage of data to sample.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [Schedule](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-Schedule"></a>
A schedule for running the column statistics, specified in CRON syntax.
Type: String
Required: No

 ** [SecurityConfiguration](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-SecurityConfiguration"></a>
Name of the security configuration that is used to encrypt CloudWatch logs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [TableName](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-TableName"></a>
The name of the table for which to generate column statistics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Tags](#API_CreateColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-CreateColumnStatisticsTaskSettings-request-Tags"></a>
A map of tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateColumnStatisticsTaskSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateColumnStatisticsTaskSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
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
<a name="API_CreateColumnStatisticsTaskSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateColumnStatisticsTaskSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateColumnStatisticsTaskSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
