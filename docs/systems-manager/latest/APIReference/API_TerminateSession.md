---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_TerminateSession.html
---

# TerminateSession
<a name="API_TerminateSession"></a>

Permanently ends a session and closes the data connection between the Session Manager client and SSM Agent on the managed node. A terminated session can't be resumed.

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

 ** [SessionId](#API_TerminateSession_RequestSyntax) **   <a name="systemsmanager-TerminateSession-request-SessionId"></a>
The ID of the session to terminate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 96.
Required: Yes

## Response Syntax
<a name="API_TerminateSession_ResponseSyntax"></a>

```
{
   "SessionId": "string"
}
```

## Response Elements
<a name="API_TerminateSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SessionId](#API_TerminateSession_ResponseSyntax) **   <a name="systemsmanager-TerminateSession-response-SessionId"></a>
The ID of the session that has been terminated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 96.

## Errors
<a name="API_TerminateSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_TerminateSession_Examples"></a>

### Example
<a name="API_TerminateSession_Example_1"></a>

This example illustrates one usage of TerminateSession.

#### Sample Request
<a name="API_TerminateSession_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.TerminateSession
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T182708Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 50

{
    "SessionId": "John-Doe-0402960697EXAMPLE"
}
```

#### Sample Response
<a name="API_TerminateSession_Example_1_Response"></a>

```
{
    "SessionId": "John-Doe-0402960697EXAMPLE"
}
```

## See Also
<a name="API_TerminateSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/TerminateSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/TerminateSession)
