---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartSession.html
---

# StartSession
<a name="API_StartSession"></a>

Initiates a connection to a target (for example, a managed node) for a Session Manager session. Returns a URL and token that can be used to open a WebSocket connection for sending input and receiving outputs.

**Note**
 AWS CLI usage: `start-session` is an interactive command that requires the Session Manager plugin to be installed on the client machine making the call. For information, see [Install the Session Manager plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) in the * AWS Systems Manager User Guide*.
 AWS Tools for PowerShell usage: Start-SSMSession isn't currently supported by AWS Tools for PowerShell on Windows local machines.

## Request Syntax
<a name="API_StartSession_RequestSyntax"></a>

```
{
   "DocumentName": "{{string}}",
   "Parameters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "Reason": "{{string}}",
   "Target": "{{string}}"
}
```

## Request Parameters
<a name="API_StartSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentName](#API_StartSession_RequestSyntax) **   <a name="systemsmanager-StartSession-request-DocumentName"></a>
The name of the SSM document you want to use to define the type of session, input parameters, or preferences for the session. For example, `SSM-SessionManagerRunShell`. You can call the [GetDocument](API_GetDocument.md) API to verify the document exists before attempting to start a session. If no document name is provided, a shell to the managed node is launched by default. For more information, see [Start a session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html) in the * AWS Systems Manager User Guide*.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: No

 ** [Parameters](#API_StartSession_RequestSyntax) **   <a name="systemsmanager-StartSession-request-Parameters"></a>
The values you want to specify for the parameters defined in the Session document. For more information about these parameters, see [Create a Session Manager preferences document](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-preferences-cli.html) in the * AWS Systems Manager User Guide*.
Type: String to array of strings map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** [Reason](#API_StartSession_RequestSyntax) **   <a name="systemsmanager-StartSession-request-Reason"></a>
The reason for connecting to the instance. This value is included in the details for the Amazon CloudWatch Events event created when you start the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^.{1,256}$`
Required: No

 ** [Target](#API_StartSession_RequestSyntax) **   <a name="systemsmanager-StartSession-request-Target"></a>
The managed node to connect to for the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: Yes

## Response Syntax
<a name="API_StartSession_ResponseSyntax"></a>

```
{
   "SessionId": "string",
   "StreamUrl": "string",
   "TokenValue": "string"
}
```

## Response Elements
<a name="API_StartSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SessionId](#API_StartSession_ResponseSyntax) **   <a name="systemsmanager-StartSession-response-SessionId"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 96.

 ** [StreamUrl](#API_StartSession_ResponseSyntax) **   <a name="systemsmanager-StartSession-response-StreamUrl"></a>
A URL back to SSM Agent on the managed node that the Session Manager client uses to send commands and receive output from the node. Format: `wss://ssmmessages.region.amazonaws.com/v1/data-channel/session-id?stream=(input|output)`
 **region** represents the Region identifier for an AWS Region supported by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported **region** values, see the **Region** column in [Systems Manager service endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html#ssm_region) in the *Amazon Web Services General Reference*.
 **session-id** represents the ID of a Session Manager session, such as `1a2b3c4dEXAMPLE`.
Type: String

 ** [TokenValue](#API_StartSession_ResponseSyntax) **   <a name="systemsmanager-StartSession-response-TokenValue"></a>
An encrypted token value containing session and caller information. This token is used to authenticate the connection to the managed node, and is valid only long enough to ensure the connection is successful. Never share your session's token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.

## Errors
<a name="API_StartSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** TargetNotConnected **
The specified target managed node for the session isn't fully configured for use with Session Manager. For more information, see [Setting up Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started.html) in the * AWS Systems Manager User Guide*. This error is also returned if you attempt to start a session on a managed node that is located in a different account or Region
HTTP Status Code: 400

## Examples
<a name="API_StartSession_Examples"></a>

### Example
<a name="API_StartSession_Example_1"></a>

This example illustrates one usage of StartSession.

#### Sample Request
<a name="API_StartSession_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.StartSession
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T181823Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 33

{
    "Target": "i-02573cafcfEXAMPLE"
}
```

#### Sample Response
<a name="API_StartSession_Example_1_Response"></a>

```
{
    "SessionId": "John-Doe-0dc5b7af96EXAMPLE",
    "StreamUrl": "wss://ssmmessages.us-east-2.amazonaws.com/v1/data-channel/John-Doe-0dc5b7af96EXAMPLE?role=publish_subscribe",
    "TokenValue": "a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE/39c3b3042cd2aEXAMPLE"
}
```

## See Also
<a name="API_StartSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/StartSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/StartSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/StartSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/StartSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/StartSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/StartSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/StartSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/StartSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/StartSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/StartSession)
