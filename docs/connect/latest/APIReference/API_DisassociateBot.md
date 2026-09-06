---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateBot.html
---

# DisassociateBot
<a name="API_DisassociateBot"></a>

This API is in preview release for Connect Customer and is subject to change.

Revokes authorization from the specified instance to access the specified Amazon Lex or Amazon Lex V2 bot.

## Request Syntax
<a name="API_DisassociateBot_RequestSyntax"></a>

```
POST /instance/{{InstanceId}}/bot HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "LexBot": {
      "LexRegion": "{{string}}",
      "Name": "{{string}}"
   },
   "LexV2Bot": {
      "AliasArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_DisassociateBot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DisassociateBot_RequestSyntax) **   <a name="connect-DisassociateBot-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DisassociateBot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_DisassociateBot_RequestSyntax) **   <a name="connect-DisassociateBot-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [LexBot](#API_DisassociateBot_RequestSyntax) **   <a name="connect-DisassociateBot-request-LexBot"></a>
Configuration information of an Amazon Lex bot.
Type: [LexBot](API_LexBot.md) object
Required: No

 ** [LexV2Bot](#API_DisassociateBot_RequestSyntax) **   <a name="connect-DisassociateBot-request-LexV2Bot"></a>
The Amazon Lex V2 bot to disassociate from the instance.
Type: [LexV2Bot](API_LexV2Bot.md) object
Required: No

## Response Syntax
<a name="API_DisassociateBot_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateBot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

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
<a name="API_DisassociateBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DisassociateBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DisassociateBot)
