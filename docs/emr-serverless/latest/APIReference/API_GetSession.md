---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetSession.html
---

# GetSession
<a name="API_GetSession"></a>

Displays detailed information about a session.

## Request Syntax
<a name="API_GetSession_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/sessions/{{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetSession_RequestSyntax) **   <a name="emrserverless-GetSession-request-uri-applicationId"></a>
The ID of the application that the session belongs to.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [sessionId](#API_GetSession_RequestSyntax) **   <a name="emrserverless-GetSession-request-uri-sessionId"></a>
The ID of the session.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_GetSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "session": {
      "applicationId": "string",
      "arn": "string",
      "billedResourceUtilization": {
         "memoryGBHour": number,
         "storageGBHour": number,
         "vCPUHour": number
      },
      "configurationOverrides": {
         "runtimeConfiguration": [
            {
               "classification": "string",
               "configurations": [
                  "Configuration"
               ],
               "properties": {
                  "string" : "string"
               }
            }
         ]
      },
      "createdAt": number,
      "createdBy": "string",
      "endedAt": number,
      "executionRoleArn": "string",
      "idleSince": number,
      "idleTimeoutMinutes": number,
      "name": "string",
      "networkConfiguration": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ]
      },
      "releaseLabel": "string",
      "sessionId": "string",
      "startedAt": number,
      "state": "string",
      "stateDetails": "string",
      "tags": {
         "string" : "string"
      },
      "totalExecutionDurationSeconds": number,
      "totalResourceUtilization": {
         "memoryGBHour": number,
         "storageGBHour": number,
         "vCPUHour": number
      },
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_GetSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [session](#API_GetSession_ResponseSyntax) **   <a name="emrserverless-GetSession-response-session"></a>
The output displays information about the session.
Type: [Session](API_Session.md) object

## Errors
<a name="API_GetSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/GetSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/GetSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
