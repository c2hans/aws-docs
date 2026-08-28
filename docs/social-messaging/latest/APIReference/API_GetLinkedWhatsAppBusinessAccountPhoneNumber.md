---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccountPhoneNumber.html
---

# GetLinkedWhatsAppBusinessAccountPhoneNumber
<a name="API_GetLinkedWhatsAppBusinessAccountPhoneNumber"></a>

Retrieve the WABA account id and phone number details of a WhatsApp business account phone number.

## Request Syntax
<a name="API_GetLinkedWhatsAppBusinessAccountPhoneNumber_RequestSyntax"></a>

```
GET /v1/whatsapp/waba/phone/details?id={{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLinkedWhatsAppBusinessAccountPhoneNumber_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetLinkedWhatsAppBusinessAccountPhoneNumber_RequestSyntax) **   <a name="Social-GetLinkedWhatsAppBusinessAccountPhoneNumber-request-uri-id"></a>
The unique identifier of the phone number. Phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`. Use [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html) to find a phone number's id.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

## Request Body
<a name="API_GetLinkedWhatsAppBusinessAccountPhoneNumber_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLinkedWhatsAppBusinessAccountPhoneNumber_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "linkedWhatsAppBusinessAccountId": "string",
   "phoneNumber": {
      "arn": "string",
      "dataLocalizationRegion": "string",
      "displayPhoneNumber": "string",
      "displayPhoneNumberName": "string",
      "metaPhoneNumberId": "string",
      "phoneNumber": "string",
      "phoneNumberId": "string",
      "qualityRating": "string"
   }
}
```

## Response Elements
<a name="API_GetLinkedWhatsAppBusinessAccountPhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [linkedWhatsAppBusinessAccountId](#API_GetLinkedWhatsAppBusinessAccountPhoneNumber_ResponseSyntax) **   <a name="Social-GetLinkedWhatsAppBusinessAccountPhoneNumber-response-linkedWhatsAppBusinessAccountId"></a>
The WABA identifier linked to the phone number, formatted as `waba-01234567890123456789012345678901`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`

 ** [phoneNumber](#API_GetLinkedWhatsAppBusinessAccountPhoneNumber_ResponseSyntax) **   <a name="Social-GetLinkedWhatsAppBusinessAccountPhoneNumber-response-phoneNumber"></a>
The details of your WhatsApp phone number.
Type: [WhatsAppPhoneNumberDetail](API_WhatsAppPhoneNumberDetail.md) object

## Errors
<a name="API_GetLinkedWhatsAppBusinessAccountPhoneNumber_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetLinkedWhatsAppBusinessAccountPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccountPhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
