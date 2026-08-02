---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryExecution.html
---

# GetQueryExecution
<a name="API_GetQueryExecution"></a>

Returns information about a single execution of a query if you have access to the workgroup in which the query ran. Each time a query executes, information about the query execution is saved with a unique ID.

## Request Syntax
<a name="API_GetQueryExecution_RequestSyntax"></a>

```
{
   "QueryExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetQueryExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [QueryExecutionId](#API_GetQueryExecution_RequestSyntax) **   <a name="athena-GetQueryExecution-request-QueryExecutionId"></a>
The unique ID of the query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`
Required: Yes

## Response Syntax
<a name="API_GetQueryExecution_ResponseSyntax"></a>

```
{
   "QueryExecution": {
      "EngineVersion": {
         "EffectiveEngineVersion": "string",
         "SelectedEngineVersion": "string"
      },
      "ExecutionParameters": [ "string" ],
      "ManagedQueryResultsConfiguration": {
         "Enabled": boolean,
         "EncryptionConfiguration": {
            "KmsKey": "string"
         }
      },
      "Query": "string",
      "QueryExecutionContext": {
         "Catalog": "string",
         "Database": "string"
      },
      "QueryExecutionId": "string",
      "QueryResultsS3AccessGrantsConfiguration": {
         "AuthenticationType": "string",
         "CreateUserLevelPrefix": boolean,
         "EnableS3AccessGrants": boolean
      },
      "ResultConfiguration": {
         "AclConfiguration": {
            "S3AclOption": "string"
         },
         "EncryptionConfiguration": {
            "EncryptionOption": "string",
            "KmsKey": "string"
         },
         "ExpectedBucketOwner": "string",
         "OutputLocation": "string"
      },
      "ResultReuseConfiguration": {
         "ResultReuseByAgeConfiguration": {
            "Enabled": boolean,
            "MaxAgeInMinutes": number
         }
      },
      "StatementType": "string",
      "Statistics": {
         "DataManifestLocation": "string",
         "DataScannedInBytes": number,
         "DpuCount": number,
         "EngineExecutionTimeInMillis": number,
         "QueryPlanningTimeInMillis": number,
         "QueryQueueTimeInMillis": number,
         "ResultReuseInformation": {
            "ReusedPreviousResult": boolean
         },
         "ServicePreProcessingTimeInMillis": number,
         "ServiceProcessingTimeInMillis": number,
         "TotalExecutionTimeInMillis": number
      },
      "Status": {
         "AthenaError": {
            "ErrorCategory": number,
            "ErrorMessage": "string",
            "ErrorType": number,
            "Retryable": boolean
         },
         "CompletionDateTime": number,
         "State": "string",
         "StateChangeReason": "string",
         "SubmissionDateTime": number
      },
      "SubstatementType": "string",
      "WorkGroup": "string"
   }
}
```

## Response Elements
<a name="API_GetQueryExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueryExecution](#API_GetQueryExecution_ResponseSyntax) **   <a name="athena-GetQueryExecution-response-QueryExecution"></a>
Information about the query execution.
Type: [QueryExecution](API_QueryExecution.md) object

## Errors
<a name="API_GetQueryExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

## See Also
<a name="API_GetQueryExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetQueryExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetQueryExecution)
