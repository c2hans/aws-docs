---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_StartQueryExecution.html
---

# StartQueryExecution
<a name="API_StartQueryExecution"></a>

Runs the SQL query statements contained in the `Query`. Requires you to have access to the workgroup in which the query ran. Running queries against an external catalog requires [GetDataCatalog](API_GetDataCatalog.md) permission to the catalog. For code samples using the AWS SDK for Java, see [Examples and Code Samples](http://docs.aws.amazon.com/athena/latest/ug/code-samples.html) in the *Amazon Athena User Guide*.

## Request Syntax
<a name="API_StartQueryExecution_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "EngineConfiguration": {
      "AdditionalConfigs": {
         "{{string}}" : "{{string}}"
      },
      "Classifications": [
         {
            "Name": "{{string}}",
            "Properties": {
               "{{string}}" : "{{string}}"
            }
         }
      ],
      "CoordinatorDpuSize": {{number}},
      "DefaultExecutorDpuSize": {{number}},
      "MaxConcurrentDpus": {{number}},
      "SparkProperties": {
         "{{string}}" : "{{string}}"
      }
   },
   "ExecutionParameters": [ "{{string}}" ],
   "QueryExecutionContext": {
      "Catalog": "{{string}}",
      "Database": "{{string}}"
   },
   "QueryString": "{{string}}",
   "ResultConfiguration": {
      "AclConfiguration": {
         "S3AclOption": "{{string}}"
      },
      "EncryptionConfiguration": {
         "EncryptionOption": "{{string}}",
         "KmsKey": "{{string}}"
      },
      "ExpectedBucketOwner": "{{string}}",
      "OutputLocation": "{{string}}"
   },
   "ResultReuseConfiguration": {
      "ResultReuseByAgeConfiguration": {
         "Enabled": {{boolean}},
         "MaxAgeInMinutes": {{number}}
      }
   },
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_StartQueryExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StartQueryExecution_RequestSyntax) **   <a name="athena-StartQueryExecution-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another `StartQueryExecution` request is received, the same response is returned and another query is not created. An error is returned if a parameter, such as `QueryString`, has changed. A call to `StartQueryExecution` that uses a previous client request token returns the same `QueryExecutionId` even if the requester doesn't have permission on the tables specified in `QueryString`.
This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: No

 ** [EngineConfiguration](#API_StartQueryExecution_RequestSyntax) **   <a name="athena-StartQueryExecution-request-EngineConfiguration"></a>
The engine configuration for the workgroup, which includes the minimum/maximum number of Data Processing Units (DPU) that queries should use when running in provisioned capacity. If not specified, Athena uses default values (Default value for min is 4 and for max is Minimum of 124 and allocated DPUs).
To specify minimum and maximum DPU values for Capacity Reservations queries, the workgroup containing `EngineConfiguration` should have the following values: The name of the `Classifications` should be `athena-query-engine-properties`, with the only allowed properties as `max-dpu-count` and `min-dpu-count`.
 **Note:** When using StartQueryExecution, only the Classifications field applies. Do not specify the other fields (AdditionalConfigs, CoordinatorDpuSize, DefaultExecutorDpuSize, MaxConcurrentDpus, and SparkProperties), as these are used only with StartSession to configure Apache Spark-based sessions.
Type: [EngineConfiguration](API_EngineConfiguration.md) object
Required: No

 ** [ExecutionParameters](#API_StartQueryExecution_RequestSyntax) **   <a name="athena-StartQueryExecution-request-ExecutionParameters"></a>
A list of values for the parameters in a query. The values are applied sequentially to the parameters in the query in the order in which the parameters occur.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [QueryExecutionContext](#API_StartQueryExecution_RequestSyntax) **   <a name="athena-StartQueryExecution-request-QueryExecutionContext"></a>
The database within which the query executes.
Type: [QueryExecutionContext](API_QueryExecutionContext.md) object
Required: No

 ** [QueryString](#API_StartQueryExecution_RequestSyntax) **   <a name="athena-StartQueryExecution-request-QueryString"></a>
The SQL query statements to be executed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** [ResultConfiguration](#API_StartQueryExecution_RequestSyntax) **   <a name="athena-StartQueryExecution-request-ResultConfiguration"></a>
Specifies information about where and how to save the results of the query execution. If the query runs in a workgroup, then workgroup's settings may override query settings. This affects the query results location. The workgroup settings override is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration).
Type: [ResultConfiguration](API_ResultConfiguration.md) object
Required: No

 ** [ResultReuseConfiguration](#API_StartQueryExecution_RequestSyntax) **   <a name="athena-StartQueryExecution-request-ResultReuseConfiguration"></a>
Specifies the query result reuse behavior for the query.
Type: [ResultReuseConfiguration](API_ResultReuseConfiguration.md) object
Required: No

 ** [WorkGroup](#API_StartQueryExecution_RequestSyntax) **   <a name="athena-StartQueryExecution-request-WorkGroup"></a>
The name of the workgroup in which the query is being started.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: No

## Response Syntax
<a name="API_StartQueryExecution_ResponseSyntax"></a>

```
{
   "QueryExecutionId": "string"
}
```

## Response Elements
<a name="API_StartQueryExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QueryExecutionId](#API_StartQueryExecution_ResponseSyntax) **   <a name="athena-StartQueryExecution-response-QueryExecutionId"></a>
The unique ID of the query that ran as a result of this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`

## Errors
<a name="API_StartQueryExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** TooManyRequestsException **
Indicates that the request was throttled.
 ** Reason **
The reason for the query throttling, for example, when it exceeds the concurrent query limit.
HTTP Status Code: 400

## See Also
<a name="API_StartQueryExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/StartQueryExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/StartQueryExecution)
