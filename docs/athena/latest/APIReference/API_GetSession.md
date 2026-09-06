---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetSession.html
---

# GetSession
<a name="API_GetSession"></a>

Gets the full details of a previously created session, including the session status and configuration.

## Request Syntax
<a name="API_GetSession_RequestSyntax"></a>

```
{
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SessionId](#API_GetSession_RequestSyntax) **   <a name="athena-GetSession-request-SessionId"></a>
The session ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_GetSession_ResponseSyntax"></a>

```
{
   "Description": "string",
   "EngineConfiguration": {
      "AdditionalConfigs": {
         "string" : "string"
      },
      "Classifications": [
         {
            "Name": "string",
            "Properties": {
               "string" : "string"
            }
         }
      ],
      "CoordinatorDpuSize": number,
      "DefaultExecutorDpuSize": number,
      "MaxConcurrentDpus": number,
      "SparkProperties": {
         "string" : "string"
      }
   },
   "EngineVersion": "string",
   "MonitoringConfiguration": {
      "CloudWatchLoggingConfiguration": {
         "Enabled": boolean,
         "LogGroup": "string",
         "LogStreamNamePrefix": "string",
         "LogTypes": {
            "string" : [ "string" ]
         }
      },
      "ManagedLoggingConfiguration": {
         "Enabled": boolean,
         "KmsKey": "string"
      },
      "S3LoggingConfiguration": {
         "Enabled": boolean,
         "KmsKey": "string",
         "LogLocation": "string"
      }
   },
   "NotebookVersion": "string",
   "SessionConfiguration": {
      "EncryptionConfiguration": {
         "EncryptionOption": "string",
         "KmsKey": "string"
      },
      "ExecutionRole": "string",
      "IdleTimeoutSeconds": number,
      "SessionIdleTimeoutInMinutes": number,
      "WorkingDirectory": "string"
   },
   "SessionId": "string",
   "Statistics": {
      "DpuExecutionInMillis": number
   },
   "Status": {
      "EndDateTime": number,
      "IdleSinceDateTime": number,
      "LastModifiedDateTime": number,
      "StartDateTime": number,
      "State": "string",
      "StateChangeReason": "string"
   },
   "WorkGroup": "string"
}
```

## Response Elements
<a name="API_GetSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-Description"></a>
The session description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [EngineConfiguration](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-EngineConfiguration"></a>
Contains engine configuration information like DPU usage.
Type: [EngineConfiguration](API_EngineConfiguration.md) object

 ** [EngineVersion](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-EngineVersion"></a>
The engine version used by the session (for example, `PySpark engine version 3`). You can get a list of engine versions by calling [ListEngineVersions](API_ListEngineVersions.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [MonitoringConfiguration](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-MonitoringConfiguration"></a>
Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object

 ** [NotebookVersion](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-NotebookVersion"></a>
The notebook version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [SessionConfiguration](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-SessionConfiguration"></a>
Contains the workgroup configuration information used by the session.
Type: [SessionConfiguration](API_SessionConfiguration.md) object

 ** [SessionId](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-SessionId"></a>
The session ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [Statistics](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-Statistics"></a>
Contains the DPU execution time.
Type: [SessionStatistics](API_SessionStatistics.md) object

 ** [Status](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-Status"></a>
Contains information about the status of the session.
Type: [SessionStatus](API_SessionStatus.md) object

 ** [WorkGroup](#API_GetSession_ResponseSyntax) **   <a name="athena-GetSession-response-WorkGroup"></a>
The workgroup to which the session belongs.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`

## Errors
<a name="API_GetSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

## See Also
<a name="API_GetSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetSession)
