---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_TerminateSession.html
---

# TerminateSession
<a name="API_TerminateSession"></a>

Terminates the specified session. After you terminate a session, it enters the `TERMINATING` state and then the `TERMINATED` state. You can still access the Spark History Server for a terminated session through the `GetResourceDashboard` operation.

## Request Syntax
<a name="API_TerminateSession_RequestSyntax"></a>

```
DELETE /applications/{{applicationId}}/sessions/{{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_TerminateSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_TerminateSession_RequestSyntax) **   <a name="emrserverless-TerminateSession-request-uri-applicationId"></a>
The ID of the application that the session belongs to.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [sessionId](#API_TerminateSession_RequestSyntax) **   <a name="emrserverless-TerminateSession-request-uri-sessionId"></a>
The ID of the session to terminate.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_TerminateSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_TerminateSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_TerminateSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_TerminateSession_ResponseSyntax) **   <a name="emrserverless-TerminateSession-response-applicationId"></a>
The output contains the application ID on which the session was terminated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [sessionId](#API_TerminateSession_ResponseSyntax) **   <a name="emrserverless-TerminateSession-response-sessionId"></a>
The output contains the ID of the terminated session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

## Errors
<a name="API_TerminateSession_Errors"></a>

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
<a name="API_TerminateSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/TerminateSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/TerminateSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
