---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_TerminateSession.html
---

# TerminateSession
<a name="API_TerminateSession"></a>

Terminates an active session. A `TerminateSession` call on a session that is already inactive (for example, in a `FAILED`, `TERMINATED` or `TERMINATING` state) succeeds but has no effect. Calculations running in the session when `TerminateSession` is called are forcefully stopped, but may display as `FAILED` instead of `STOPPED`.

## Request Syntax
<a name="API_TerminateSession_RequestSyntax"></a>

```
{
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_TerminateSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SessionId](#API_TerminateSession_RequestSyntax) **   <a name="athena-TerminateSession-request-SessionId"></a>
The session ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_TerminateSession_ResponseSyntax"></a>

```
{
   "State": "string"
}
```

## Response Elements
<a name="API_TerminateSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [State](#API_TerminateSession_ResponseSyntax) **   <a name="athena-TerminateSession-response-State"></a>
The state of the session. A description of each state follows.
 `CREATING` - The session is being started, including acquiring resources.
 `CREATED` - The session has been started.
 `IDLE` - The session is able to accept a calculation.
 `BUSY` - The session is processing another task and is unable to accept a calculation.
 `TERMINATING` - The session is in the process of shutting down.
 `TERMINATED` - The session and its resources are no longer running.
 `DEGRADED` - The session has no healthy coordinators.
 `FAILED` - Due to a failure, the session and its resources are no longer running.
Type: String
Valid Values: `CREATING | CREATED | IDLE | BUSY | TERMINATING | TERMINATED | DEGRADED | FAILED`

## Errors
<a name="API_TerminateSession_Errors"></a>

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
<a name="API_TerminateSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/TerminateSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/TerminateSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/TerminateSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/TerminateSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/TerminateSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/TerminateSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/TerminateSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/TerminateSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/TerminateSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/TerminateSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
