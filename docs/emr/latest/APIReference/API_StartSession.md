---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_StartSession.html
---

# StartSession
<a name="API_StartSession"></a>

Creates and starts a new Spark Connect session on the specified cluster. The cluster must be in the `RUNNING` or `WAITING` state and have sessions enabled. This operation is supported in Amazon EMR Spark 8.0.0 and later.

## Request Syntax
<a name="API_StartSession_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "ClusterId": "{{string}}",
   "EngineConfigurations": [
      {
         "Classification": "{{string}}",
         "Configurations": [
            "Configuration"
         ],
         "Properties": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "ExecutionRoleArn": "{{string}}",
   "MonitoringConfiguration": {
      "CloudWatchLoggingConfiguration": {
         "Enabled": {{boolean}},
         "EncryptionKeyArn": "{{string}}",
         "LogGroup": "{{string}}",
         "LogStreamNamePrefix": "{{string}}",
         "LogTypes": {
            "{{string}}" : [ "{{string}}" ]
         }
      },
      "ManagedLoggingConfiguration": {
         "Enabled": {{boolean}},
         "EncryptionKeyArn": "{{string}}"
      },
      "S3LoggingConfiguration": {
         "Enabled": {{boolean}},
         "EncryptionKeyArn": "{{string}}",
         "LogTypes": {
            "{{string}}" : [ "{{string}}" ]
         },
         "LogUri": "{{string}}"
      }
   },
   "Name": "{{string}}",
   "SessionIdleTimeoutInMinutes": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StartSession_RequestSyntax) **   <a name="EMR-StartSession-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client request token, the service returns the original response without performing the operation again.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** [ClusterId](#API_StartSession_RequestSyntax) **   <a name="EMR-StartSession-request-ClusterId"></a>
The ID of the cluster on which to start the session.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** [EngineConfigurations](#API_StartSession_RequestSyntax) **   <a name="EMR-StartSession-request-EngineConfigurations"></a>
The configuration overrides for the session. Only runtime configuration overrides are supported.
Type: Array of [Configuration](API_Configuration.md) objects
Required: No

 ** [ExecutionRoleArn](#API_StartSession_RequestSyntax) **   <a name="EMR-StartSession-request-ExecutionRoleArn"></a>
The execution role ARN for the session. Amazon EMR uses this role to access AWS resources on your behalf during session execution.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
Required: No

 ** [MonitoringConfiguration](#API_StartSession_RequestSyntax) **   <a name="EMR-StartSession-request-MonitoringConfiguration"></a>
The monitoring configuration that controls where session logs are published, such as Amazon S3, CloudWatch, or managed logging.
Type: [SessionMonitoringConfiguration](API_SessionMonitoringConfiguration.md) object
Required: No

 ** [Name](#API_StartSession_RequestSyntax) **   <a name="EMR-StartSession-request-Name"></a>
An optional name for the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [SessionIdleTimeoutInMinutes](#API_StartSession_RequestSyntax) **   <a name="EMR-StartSession-request-SessionIdleTimeoutInMinutes"></a>
The idle timeout, in minutes. If the session is idle for this duration, Amazon EMR EC2 automatically terminates it.
Type: Long
Required: No

 ** [Tags](#API_StartSession_RequestSyntax) **   <a name="EMR-StartSession-request-Tags"></a>
The tags to assign to the session.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_StartSession_ResponseSyntax"></a>

```
{
   "AccountId": "string",
   "Arn": "string",
   "ClusterId": "string",
   "Id": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_StartSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountId](#API_StartSession_ResponseSyntax) **   <a name="EMR-StartSession-response-AccountId"></a>
The AWS account ID that owns the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [Arn](#API_StartSession_ResponseSyntax) **   <a name="EMR-StartSession-response-Arn"></a>
The output contains the ARN of the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [ClusterId](#API_StartSession_ResponseSyntax) **   <a name="EMR-StartSession-response-ClusterId"></a>
The ID of the cluster that the session was started on.
Type: String
Length Constraints: Maximum length of 256.

 ** [Id](#API_StartSession_ResponseSyntax) **   <a name="EMR-StartSession-response-Id"></a>
The output contains the ID of the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [State](#API_StartSession_ResponseSyntax) **   <a name="EMR-StartSession-response-State"></a>
The state of the session at the time the request returned. When a session is first created, it enters the `SUBMITTED` state.
Type: String
Valid Values: `SUBMITTED | STARTING | STARTED | IDLE | BUSY | TERMINATING | TERMINATED | FAILED`

## Errors
<a name="API_StartSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon EMR service.
 ** Message **
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception occurs when there is something wrong with user input.
 ** ErrorCode **
The error code associated with the exception.
 ** Message **
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_StartSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/StartSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StartSession)
