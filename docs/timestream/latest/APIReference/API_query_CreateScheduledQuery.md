---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_CreateScheduledQuery.html
---

# CreateScheduledQuery
<a name="API_query_CreateScheduledQuery"></a>

 Create a scheduled query that will be run on your behalf at the configured schedule. Timestream assumes the execution role provided as part of the `ScheduledQueryExecutionRoleArn` parameter to run the query. You can use the `NotificationConfiguration` parameter to configure notification for your scheduled query operations.

## Request Syntax
<a name="API_query_CreateScheduledQuery_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ErrorReportConfiguration": {
      "S3Configuration": {
         "BucketName": "{{string}}",
         "EncryptionOption": "{{string}}",
         "ObjectKeyPrefix": "{{string}}"
      }
   },
   "KmsKeyId": "{{string}}",
   "Name": "{{string}}",
   "NotificationConfiguration": {
      "SnsConfiguration": {
         "TopicArn": "{{string}}"
      }
   },
   "QueryString": "{{string}}",
   "ScheduleConfiguration": {
      "ScheduleExpression": "{{string}}"
   },
   "ScheduledQueryExecutionRoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetConfiguration": {
      "TimestreamConfiguration": {
         "DatabaseName": "{{string}}",
         "DimensionMappings": [
            {
               "DimensionValueType": "{{string}}",
               "Name": "{{string}}"
            }
         ],
         "MeasureNameColumn": "{{string}}",
         "MixedMeasureMappings": [
            {
               "MeasureName": "{{string}}",
               "MeasureValueType": "{{string}}",
               "MultiMeasureAttributeMappings": [
                  {
                     "MeasureValueType": "{{string}}",
                     "SourceColumn": "{{string}}",
                     "TargetMultiMeasureAttributeName": "{{string}}"
                  }
               ],
               "SourceColumn": "{{string}}",
               "TargetMeasureName": "{{string}}"
            }
         ],
         "MultiMeasureMappings": {
            "MultiMeasureAttributeMappings": [
               {
                  "MeasureValueType": "{{string}}",
                  "SourceColumn": "{{string}}",
                  "TargetMultiMeasureAttributeName": "{{string}}"
               }
            ],
            "TargetMultiMeasureName": "{{string}}"
         },
         "TableName": "{{string}}",
         "TimeColumn": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_query_CreateScheduledQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-ClientToken"></a>
Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request.
+  If CreateScheduledQuery is called without a `ClientToken`, the Query SDK generates a `ClientToken` on your behalf.
+  After 8 hours, any request with the same `ClientToken` is treated as a new request.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: No

 ** [ErrorReportConfiguration](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-ErrorReportConfiguration"></a>
Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.
Type: [ErrorReportConfiguration](API_query_ErrorReportConfiguration.md) object
Required: Yes

 ** [KmsKeyId](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-KmsKeyId"></a>
The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with *alias/*
If ErrorReportConfiguration uses `SSE_KMS` as encryption type, the same KmsKeyId is used to encrypt the error report at rest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Name](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-Name"></a>
Name of the scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`
Required: Yes

 ** [NotificationConfiguration](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-NotificationConfiguration"></a>
Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.
Type: [NotificationConfiguration](API_query_NotificationConfiguration.md) object
Required: Yes

 ** [QueryString](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-QueryString"></a>
The query string to run. Parameter names can be specified in the query string `@` character followed by an identifier. The named Parameter `@scheduled_runtime` is reserved and can be used in the query to get the time at which the query is scheduled to run.
The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of `@scheduled_runtime` paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the `@scheduled_runtime` parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** [ScheduleConfiguration](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-ScheduleConfiguration"></a>
The schedule configuration for the query.
Type: [ScheduleConfiguration](API_query_ScheduleConfiguration.md) object
Required: Yes

 ** [ScheduledQueryExecutionRoleArn](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-ScheduledQueryExecutionRoleArn"></a>
The ARN for the IAM role that Timestream will assume when running the scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Tags](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-Tags"></a>
A list of key-value pairs to label the scheduled query.
Type: Array of [Tag](API_query_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [TargetConfiguration](#API_query_CreateScheduledQuery_RequestSyntax) **   <a name="timestream-query_CreateScheduledQuery-request-TargetConfiguration"></a>
Configuration used for writing the result of a query.
Type: [TargetConfiguration](API_query_TargetConfiguration.md) object
Required: No

## Response Syntax
<a name="API_query_CreateScheduledQuery_ResponseSyntax"></a>

```
{
   "Arn": "string"
}
```

## Response Elements
<a name="API_query_CreateScheduledQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_query_CreateScheduledQuery_ResponseSyntax) **   <a name="timestream-query_CreateScheduledQuery-response-Arn"></a>
ARN for the created scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_query_CreateScheduledQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the necessary permissions to access the account settings.
HTTP Status Code: 400

 ** ConflictException **
 Unable to poll results for a cancelled query.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
HTTP Status Code: 400

 ** InvalidEndpointException **
The requested endpoint is invalid.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
You have exceeded the service quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to excessive requests.
HTTP Status Code: 400

 ** ValidationException **
 Invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_query_CreateScheduledQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/CreateScheduledQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/CreateScheduledQuery)
