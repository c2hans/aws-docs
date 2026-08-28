---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PublishWhatsAppFlow.html
---

# PublishWhatsAppFlow
<a name="API_PublishWhatsAppFlow"></a>

Publishes a WhatsApp Flow, making it available for use in template messages. The Flow must be in DRAFT status with valid Flow JSON that passes Meta's validation. This is an irreversible operation.

## Request Syntax
<a name="API_PublishWhatsAppFlow_RequestSyntax"></a>

```
POST /v1/whatsapp/flow/publish HTTP/1.1
Content-type: application/json

{
   "flowId": "{{string}}",
   "id": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PublishWhatsAppFlow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PublishWhatsAppFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [flowId](#API_PublishWhatsAppFlow_RequestSyntax) **   <a name="Social-PublishWhatsAppFlow-request-flowId"></a>
The unique identifier of the Flow to publish.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9]+`
Required: Yes

 ** [id](#API_PublishWhatsAppFlow_RequestSyntax) **   <a name="Social-PublishWhatsAppFlow-request-id"></a>
The ID of the WhatsApp Business Account associated with this Flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_PublishWhatsAppFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PublishWhatsAppFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PublishWhatsAppFlow_Errors"></a>

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
<a name="API_PublishWhatsAppFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/PublishWhatsAppFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/PublishWhatsAppFlow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
