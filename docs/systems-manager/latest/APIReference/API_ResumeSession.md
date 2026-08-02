---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResumeSession.html
---

# ResumeSession
<a name="API_ResumeSession"></a>

Reconnects a session to a managed node after it has been disconnected. Connections can be resumed for disconnected sessions, but not terminated sessions.

**Note**
This command is primarily for use by client machines to automatically reconnect during intermittent network issues. It isn't intended for any other use.

## Request Syntax
<a name="API_ResumeSession_RequestSyntax"></a>

```
{
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_ResumeSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SessionId](#API_ResumeSession_RequestSyntax) **   <a name="systemsmanager-ResumeSession-request-SessionId"></a>
The ID of the disconnected session to resume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 96.
Required: Yes

## Response Syntax
<a name="API_ResumeSession_ResponseSyntax"></a>

```
{
   "SessionId": "string",
   "StreamUrl": "string",
   "TokenValue": "string"
}
```

## Response Elements
<a name="API_ResumeSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SessionId](#API_ResumeSession_ResponseSyntax) **   <a name="systemsmanager-ResumeSession-response-SessionId"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 96.

 ** [StreamUrl](#API_ResumeSession_ResponseSyntax) **   <a name="systemsmanager-ResumeSession-response-StreamUrl"></a>
A URL back to SSM Agent on the managed node that the Session Manager client uses to send commands and receive output from the managed node. Format: `wss://ssmmessages.region.amazonaws.com/v1/data-channel/session-id?stream=(input|output)`.
 **region** represents the Region identifier for an AWS Region supported by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported **region** values, see the **Region** column in [Systems Manager service endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html#ssm_region) in the *Amazon Web Services General Reference*.
 **session-id** represents the ID of a Session Manager session, such as `1a2b3c4dEXAMPLE`.
Type: String

 ** [TokenValue](#API_ResumeSession_ResponseSyntax) **   <a name="systemsmanager-ResumeSession-response-TokenValue"></a>
An encrypted token value containing session and caller information. Used to authenticate the connection to the managed node.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.

## Errors
<a name="API_ResumeSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_ResumeSession_Examples"></a>

### Example
<a name="API_ResumeSession_Example_1"></a>

This example illustrates one usage of ResumeSession.

#### Sample Request
<a name="API_ResumeSession_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ResumeSession
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T181144Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 50

{
    "SessionId": "John-Doe-0402960697EXAMPLE"
}
```

#### Sample Response
<a name="API_ResumeSession_Example_1_Response"></a>

```
{{
    "SessionId": "John-Doe-0402960697EXAMPLE",
    "StreamUrl": "wss://ssmmessages.us-east-2.amazonaws.com/v1/data-channel/John-Doe-0402960697EXAMPLE?role=publish_subscribe",
    "TokenValue": "EXAMPLENPKTm3/39c3b3042cd2aEXAMPLE/a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE"
}
```

## See Also
<a name="API_ResumeSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ResumeSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ResumeSession)
