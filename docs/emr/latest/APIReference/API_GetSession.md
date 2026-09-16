---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_GetSession.html
---

# GetSession
<a name="API_GetSession"></a>

Returns detailed information about a session.

## Request Syntax
<a name="API_GetSession_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_GetSession_RequestSyntax) **   <a name="EMR-GetSession-request-ClusterId"></a>
The ID of the cluster that the session belongs to.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** [SessionId](#API_GetSession_RequestSyntax) **   <a name="EMR-GetSession-request-SessionId"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_GetSession_ResponseSyntax"></a>

```
{
   "Session": {
      "AccountId": "string",
      "Arn": "string",
      "ClusterId": "string",
      "CreatedAt": number,
      "EndedAt": number,
      "EngineConfigurations": [
         {
            "Classification": "string",
            "Configurations": [
               "Configuration"
            ],
            "Properties": {
               "string" : "string"
            }
         }
      ],
      "ExecutionRoleArn": "string",
      "Id": "string",
      "IdleSince": number,
      "MonitoringConfiguration": {
         "CloudWatchLoggingConfiguration": {
            "Enabled": boolean,
            "EncryptionKeyArn": "string",
            "LogGroup": "string",
            "LogStreamNamePrefix": "string",
            "LogTypes": {
               "string" : [ "string" ]
            }
         },
         "ManagedLoggingConfiguration": {
            "Enabled": boolean,
            "EncryptionKeyArn": "string"
         },
         "S3LoggingConfiguration": {
            "Enabled": boolean,
            "EncryptionKeyArn": "string",
            "LogTypes": {
               "string" : [ "string" ]
            },
            "LogUri": "string"
         }
      },
      "Name": "string",
      "ReleaseLabel": "string",
      "ServerUrl": "string",
      "SessionIdleTimeoutInMinutes": number,
      "StartedAt": number,
      "State": "string",
      "StateChangeReason": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_GetSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Session](#API_GetSession_ResponseSyntax) **   <a name="EMR-GetSession-response-Session"></a>
The output displays information about the session.
Type: [Session](API_Session.md) object

## Errors
<a name="API_GetSession_Errors"></a>

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
<a name="API_GetSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/GetSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/GetSession)
