---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartSession.html
---

# StartSession
<a name="API_StartSession"></a>

Creates and starts a new session on the specified application. The application must be in the `STARTED` state or have `AutoStart` enabled, and have interactive sessions enabled. This operation is supported for EMR release 7.13.0 and later.

## Request Syntax
<a name="API_StartSession_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/sessions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configurationOverrides": {
      "runtimeConfiguration": [
         {
            "classification": "{{string}}",
            "configurations": [
               "Configuration"
            ],
            "properties": {
               "{{string}}" : "{{string}}"
            }
         }
      ]
   },
   "executionRoleArn": "{{string}}",
   "idleTimeoutMinutes": {{number}},
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_StartSession_RequestSyntax) **   <a name="emrserverless-StartSession-request-uri-applicationId"></a>
The ID of the application on which to start the session.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_StartSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartSession_RequestSyntax) **   <a name="emrserverless-StartSession-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the successful response without performing the operation again.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._-]+`
Required: Yes

 ** [configurationOverrides](#API_StartSession_RequestSyntax) **   <a name="emrserverless-StartSession-request-configurationOverrides"></a>
The configuration overrides for the session. Only runtime configuration overrides are supported.
Type: [SessionConfigurationOverrides](API_SessionConfigurationOverrides.md) object
Required: No

 ** [executionRoleArn](#API_StartSession_RequestSyntax) **   <a name="emrserverless-StartSession-request-executionRoleArn"></a>
The execution role ARN for the session. Amazon EMR Serverless uses this role to access AWS resources on your behalf during session execution.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** [idleTimeoutMinutes](#API_StartSession_RequestSyntax) **   <a name="emrserverless-StartSession-request-idleTimeoutMinutes"></a>
The idle timeout in minutes for the session. After the session remains idle for this duration, Amazon EMR Serverless automatically terminates it.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

 ** [name](#API_StartSession_RequestSyntax) **   <a name="emrserverless-StartSession-request-name"></a>
The optional name for the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** [tags](#API_StartSession_RequestSyntax) **   <a name="emrserverless-StartSession-request-tags"></a>
The tags to assign to the session.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9 /_.:=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 /_.:=+@-]*`
Required: No

## Response Syntax
<a name="API_StartSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "arn": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_StartSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_StartSession_ResponseSyntax) **   <a name="emrserverless-StartSession-response-applicationId"></a>
The output contains the application ID on which the session was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [arn](#API_StartSession_ResponseSyntax) **   <a name="emrserverless-StartSession-response-arn"></a>
The output contains the ARN of the session.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+\/sessions\/[0-9a-zA-Z]+`

 ** [sessionId](#API_StartSession_ResponseSyntax) **   <a name="emrserverless-StartSession-response-sessionId"></a>
The output contains the ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

## Errors
<a name="API_StartSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The maximum number of resources per account has been reached.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/StartSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/StartSession)
