---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetColumnStatisticsTaskSettings.html
---

# GetColumnStatisticsTaskSettings
<a name="API_GetColumnStatisticsTaskSettings"></a>

Gets settings for a column statistics task.

## Request Syntax
<a name="API_GetColumnStatisticsTaskSettings_RequestSyntax"></a>

```
{
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetColumnStatisticsTaskSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatabaseName](#API_GetColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-GetColumnStatisticsTaskSettings-request-DatabaseName"></a>
The name of the database where the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_GetColumnStatisticsTaskSettings_RequestSyntax) **   <a name="Glue-GetColumnStatisticsTaskSettings-request-TableName"></a>
The name of the table for which to retrieve column statistics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetColumnStatisticsTaskSettings_ResponseSyntax"></a>

```
{
   "ColumnStatisticsTaskSettings": {
      "CatalogID": "string",
      "ColumnNameList": [ "string" ],
      "DatabaseName": "string",
      "LastExecutionAttempt": {
         "ColumnStatisticsTaskRunId": "string",
         "ErrorMessage": "string",
         "ExecutionTimestamp": number,
         "Status": "string"
      },
      "Role": "string",
      "SampleSize": number,
      "Schedule": {
         "ScheduleExpression": "string",
         "State": "string"
      },
      "ScheduleType": "string",
      "SecurityConfiguration": "string",
      "SettingSource": "string",
      "TableName": "string"
   }
}
```

## Response Elements
<a name="API_GetColumnStatisticsTaskSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ColumnStatisticsTaskSettings](#API_GetColumnStatisticsTaskSettings_ResponseSyntax) **   <a name="Glue-GetColumnStatisticsTaskSettings-response-ColumnStatisticsTaskSettings"></a>
A `ColumnStatisticsTaskSettings` object representing the settings for the column statistics task.
Type: [ColumnStatisticsTaskSettings](API_ColumnStatisticsTaskSettings.md) object

## Errors
<a name="API_GetColumnStatisticsTaskSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_GetColumnStatisticsTaskSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetColumnStatisticsTaskSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetColumnStatisticsTaskSettings)
