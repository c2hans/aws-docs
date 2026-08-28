---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_TerminateSession.html
---

# TerminateSession
<a name="API_TerminateSession"></a>

Terminates an active session. After you call this operation, the session enters the `TERMINATING` state and then transitions to `TERMINATED`.

## Request Syntax
<a name="API_TerminateSession_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_TerminateSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_TerminateSession_RequestSyntax) **   <a name="EMR-TerminateSession-request-ClusterId"></a>
The ID of the cluster that the session belongs to.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** [SessionId](#API_TerminateSession_RequestSyntax) **   <a name="EMR-TerminateSession-request-SessionId"></a>
The ID of the session to terminate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_TerminateSession_ResponseSyntax"></a>

```
{
   "ClusterId": "string",
   "SessionId": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_TerminateSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterId](#API_TerminateSession_ResponseSyntax) **   <a name="EMR-TerminateSession-response-ClusterId"></a>
The ID of the cluster that the session belonged to.
Type: String
Length Constraints: Maximum length of 256.

 ** [SessionId](#API_TerminateSession_ResponseSyntax) **   <a name="EMR-TerminateSession-response-SessionId"></a>
The ID of the terminated session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [State](#API_TerminateSession_ResponseSyntax) **   <a name="EMR-TerminateSession-response-State"></a>
The state of the session after the terminate request has been accepted.
Type: String
Valid Values: `SUBMITTED | STARTING | STARTED | IDLE | BUSY | TERMINATING | TERMINATED | FAILED`

## Errors
<a name="API_TerminateSession_Errors"></a>

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
<a name="API_TerminateSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/TerminateSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/TerminateSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
