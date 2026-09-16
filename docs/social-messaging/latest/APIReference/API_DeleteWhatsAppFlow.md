---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeleteWhatsAppFlow.html
---

# DeleteWhatsAppFlow
<a name="API_DeleteWhatsAppFlow"></a>

Deletes a WhatsApp Flow permanently. Only Flows in DRAFT status can be deleted. Published or deprecated Flows cannot be deleted.

## Request Syntax
<a name="API_DeleteWhatsAppFlow_RequestSyntax"></a>

```
DELETE /v1/whatsapp/flow?flowId={{flowId}}&id={{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteWhatsAppFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowId](#API_DeleteWhatsAppFlow_RequestSyntax) **   <a name="Social-DeleteWhatsAppFlow-request-uri-flowId"></a>
The unique identifier of the Flow to delete.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: Yes

 ** [id](#API_DeleteWhatsAppFlow_RequestSyntax) **   <a name="Social-DeleteWhatsAppFlow-request-uri-id"></a>
The ID of the WhatsApp Business Account associated with this Flow.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Request Body
<a name="API_DeleteWhatsAppFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteWhatsAppFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteWhatsAppFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWhatsAppFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedByMetaException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** DependencyException **
Thrown when performing an action because a dependency would be broken.
HTTP Status Code: 502

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found.
HTTP Status Code: 404

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWhatsAppFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/DeleteWhatsAppFlow)
