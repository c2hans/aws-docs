---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html
---

# GetLinkedWhatsAppBusinessAccount
<a name="API_GetLinkedWhatsAppBusinessAccount"></a>

Get the details of your linked WhatsApp Business Account.

## Request Syntax
<a name="API_GetLinkedWhatsAppBusinessAccount_RequestSyntax"></a>

```
GET /v1/whatsapp/waba/details?id={{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLinkedWhatsAppBusinessAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetLinkedWhatsAppBusinessAccount_RequestSyntax) **   <a name="Social-GetLinkedWhatsAppBusinessAccount-request-uri-id"></a>
The unique identifier, from AWS, of the linked WhatsApp Business Account. WABA identifiers are formatted as `waba-01234567890123456789012345678901`. Use [ListLinkedWhatsAppBusinessAccounts](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html) to list all WABAs and their details.
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`
Required: Yes

## Request Body
<a name="API_GetLinkedWhatsAppBusinessAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLinkedWhatsAppBusinessAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "account": {
      "arn": "string",
      "datasetId": "string",
      "eventDestinations": [
         {
            "eventDestinationArn": "string",
            "roleArn": "string"
         }
      ],
      "id": "string",
      "linkDate": number,
      "marketingMessagesOnboardingStatus": "string",
      "phoneNumbers": [
         {
            "arn": "string",
            "dataLocalizationRegion": "string",
            "displayPhoneNumber": "string",
            "displayPhoneNumberName": "string",
            "metaPhoneNumberId": "string",
            "phoneNumber": "string",
            "phoneNumberId": "string",
            "qualityRating": "string"
         }
      ],
      "registrationStatus": "string",
      "wabaId": "string",
      "wabaName": "string"
   }
}
```

## Response Elements
<a name="API_GetLinkedWhatsAppBusinessAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [account](#API_GetLinkedWhatsAppBusinessAccount_ResponseSyntax) **   <a name="Social-GetLinkedWhatsAppBusinessAccount-response-account"></a>
The details of the linked WhatsApp Business Account.
Type: [LinkedWhatsAppBusinessAccount](API_LinkedWhatsAppBusinessAccount.md) object

## Errors
<a name="API_GetLinkedWhatsAppBusinessAccount_Errors"></a>

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
<a name="API_GetLinkedWhatsAppBusinessAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)
