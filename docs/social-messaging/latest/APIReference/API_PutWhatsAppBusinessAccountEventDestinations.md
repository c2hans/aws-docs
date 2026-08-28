---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PutWhatsAppBusinessAccountEventDestinations.html
---

# PutWhatsAppBusinessAccountEventDestinations
<a name="API_PutWhatsAppBusinessAccountEventDestinations"></a>

Add an event destination to log event data from WhatsApp for a WhatsApp Business Account (WABA). A WABA can only have one event destination at a time. All resources associated with the WABA use the same event destination.

## Request Syntax
<a name="API_PutWhatsAppBusinessAccountEventDestinations_RequestSyntax"></a>

```
PUT /v1/whatsapp/waba/eventdestinations HTTP/1.1
Content-type: application/json

{
   "eventDestinations": [
      {
         "eventDestinationArn": "{{string}}",
         "roleArn": "{{string}}"
      }
   ],
   "id": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutWhatsAppBusinessAccountEventDestinations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutWhatsAppBusinessAccountEventDestinations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [eventDestinations](#API_PutWhatsAppBusinessAccountEventDestinations_RequestSyntax) **   <a name="Social-PutWhatsAppBusinessAccountEventDestinations-request-eventDestinations"></a>
An array of `WhatsAppBusinessAccountEventDestination` event destinations.
Type: Array of [WhatsAppBusinessAccountEventDestination](API_WhatsAppBusinessAccountEventDestination.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: Yes

 ** [id](#API_PutWhatsAppBusinessAccountEventDestinations_RequestSyntax) **   <a name="Social-PutWhatsAppBusinessAccountEventDestinations-request-id"></a>
The unique identifier of your WhatsApp Business Account. WABA identifiers are formatted as `waba-01234567890123456789012345678901`. Use [ListLinkedWhatsAppBusinessAccounts](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html) to list all WABAs and their details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_PutWhatsAppBusinessAccountEventDestinations_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutWhatsAppBusinessAccountEventDestinations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutWhatsAppBusinessAccountEventDestinations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_PutWhatsAppBusinessAccountEventDestinations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/PutWhatsAppBusinessAccountEventDestinations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
