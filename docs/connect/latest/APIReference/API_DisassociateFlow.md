---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateFlow.html
---

# DisassociateFlow
<a name="API_DisassociateFlow"></a>

Disassociates a connect resource from a flow.

## Request Syntax
<a name="API_DisassociateFlow_RequestSyntax"></a>

```
DELETE /flow-associations/{{InstanceId}}/{{ResourceId}}/{{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DisassociateFlow_RequestSyntax) **   <a name="connect-DisassociateFlow-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ResourceId](#API_DisassociateFlow_RequestSyntax) **   <a name="connect-DisassociateFlow-request-uri-ResourceId"></a>
The identifier of the resource.
+  AWS End User Messaging SMS phone number ARN when using `SMS_PHONE_NUMBER`
+  AWS End User Messaging Social phone number ARN when using `WHATSAPP_MESSAGING_PHONE_NUMBER`
Required: Yes

 ** [ResourceType](#API_DisassociateFlow_RequestSyntax) **   <a name="connect-DisassociateFlow-request-uri-ResourceType"></a>
A valid resource type.
Valid Values: `SMS_PHONE_NUMBER | INBOUND_EMAIL | OUTBOUND_EMAIL | ANALYTICS_CONNECTOR | WHATSAPP_MESSAGING_PHONE_NUMBER`
Required: Yes

## Request Body
<a name="API_DisassociateFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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
<a name="API_DisassociateFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DisassociateFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DisassociateFlow)
