---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateLexBot.html
---

# DisassociateLexBot
<a name="API_DisassociateLexBot"></a>

This API is in preview release for Connect Customer and is subject to change.

Revokes authorization from the specified instance to access the specified Amazon Lex bot.

## Request Syntax
<a name="API_DisassociateLexBot_RequestSyntax"></a>

```
DELETE /instance/{{InstanceId}}/lex-bot?botName={{BotName}}&clientToken={{ClientToken}}&lexRegion={{LexRegion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateLexBot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [BotName](#API_DisassociateLexBot_RequestSyntax) **   <a name="connect-DisassociateLexBot-request-uri-BotName"></a>
The name of the Amazon Lex bot. Maximum character limit of 50.
Length Constraints: Maximum length of 50.
Required: Yes

 ** [ClientToken](#API_DisassociateLexBot_RequestSyntax) **   <a name="connect-DisassociateLexBot-request-uri-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Length Constraints: Maximum length of 500.

 ** [InstanceId](#API_DisassociateLexBot_RequestSyntax) **   <a name="connect-DisassociateLexBot-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [LexRegion](#API_DisassociateLexBot_RequestSyntax) **   <a name="connect-DisassociateLexBot-request-uri-LexRegion"></a>
The AWS Region in which the Amazon Lex bot has been created.
Length Constraints: Maximum length of 60.
Required: Yes

## Request Body
<a name="API_DisassociateLexBot_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateLexBot_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateLexBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateLexBot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DisassociateLexBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DisassociateLexBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DisassociateLexBot)
