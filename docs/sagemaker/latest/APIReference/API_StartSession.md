---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartSession.html
---

# StartSession
<a name="API_StartSession"></a>

Initiates a remote connection session between a local integrated development environments (IDEs) and a remote SageMaker space.

## Request Syntax
<a name="API_StartSession_RequestSyntax"></a>

```
{
   "ResourceIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_StartSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceIdentifier](#API_StartSession_RequestSyntax) **   <a name="sagemaker-StartSession-request-ResourceIdentifier"></a>
The Amazon Resource Name (ARN) of the resource to which the remote connection will be established. For example, this identifies the specific ARN space application you want to connect to from your local IDE.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:.*\/.*`
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

 ** [SessionId](#API_StartSession_ResponseSyntax) **   <a name="sagemaker-StartSession-response-SessionId"></a>
A unique identifier for the established remote connection session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [StreamUrl](#API_StartSession_ResponseSyntax) **   <a name="sagemaker-StartSession-response-StreamUrl"></a>
A WebSocket URL used to establish a SSH connection between the local IDE and remote SageMaker space.
Type: String

 ** [TokenValue](#API_StartSession_ResponseSyntax) **   <a name="sagemaker-StartSession-response-TokenValue"></a>
An encrypted token value containing session and caller information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_StartSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_StartSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/StartSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StartSession)
