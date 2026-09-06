---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetColumnStatisticsTaskRuns.html
---

# GetColumnStatisticsTaskRuns
<a name="API_GetColumnStatisticsTaskRuns"></a>

Retrieves information about all runs associated with the specified table.

## Request Syntax
<a name="API_GetColumnStatisticsTaskRuns_RequestSyntax"></a>

```
{
   "DatabaseName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetColumnStatisticsTaskRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatabaseName](#API_GetColumnStatisticsTaskRuns_RequestSyntax) **   <a name="Glue-GetColumnStatisticsTaskRuns-request-DatabaseName"></a>
The name of the database where the table resides.
Type: String
Required: Yes

 ** [MaxResults](#API_GetColumnStatisticsTaskRuns_RequestSyntax) **   <a name="Glue-GetColumnStatisticsTaskRuns-request-MaxResults"></a>
The maximum size of the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetColumnStatisticsTaskRuns_RequestSyntax) **   <a name="Glue-GetColumnStatisticsTaskRuns-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [TableName](#API_GetColumnStatisticsTaskRuns_RequestSyntax) **   <a name="Glue-GetColumnStatisticsTaskRuns-request-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetColumnStatisticsTaskRuns_ResponseSyntax"></a>

```
{
   "ColumnStatisticsTaskRuns": [
      {
         "CatalogID": "string",
         "ColumnNameList": [ "string" ],
         "ColumnStatisticsTaskRunId": "string",
         "ComputationType": "string",
         "CreationTime": number,
         "CustomerId": "string",
         "DatabaseName": "string",
         "DPUSeconds": number,
         "EndTime": number,
         "ErrorMessage": "string",
         "LastUpdated": number,
         "NumberOfWorkers": number,
         "Role": "string",
         "SampleSize": number,
         "SecurityConfiguration": "string",
         "StartTime": number,
         "Status": "string",
         "TableName": "string",
         "WorkerType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetColumnStatisticsTaskRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ColumnStatisticsTaskRuns](#API_GetColumnStatisticsTaskRuns_ResponseSyntax) **   <a name="Glue-GetColumnStatisticsTaskRuns-response-ColumnStatisticsTaskRuns"></a>
A list of column statistics task runs.
Type: Array of [ColumnStatisticsTaskRun](API_ColumnStatisticsTaskRun.md) objects

 ** [NextToken](#API_GetColumnStatisticsTaskRuns_ResponseSyntax) **   <a name="Glue-GetColumnStatisticsTaskRuns-response-NextToken"></a>
A continuation token, if not all task runs have yet been returned.
Type: String

## Errors
<a name="API_GetColumnStatisticsTaskRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetColumnStatisticsTaskRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetColumnStatisticsTaskRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetColumnStatisticsTaskRuns)
