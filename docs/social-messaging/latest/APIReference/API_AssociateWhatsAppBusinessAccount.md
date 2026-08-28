---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_AssociateWhatsAppBusinessAccount.html
---

# AssociateWhatsAppBusinessAccount
<a name="API_AssociateWhatsAppBusinessAccount"></a>

This is only used through the AWS console during sign-up to associate your WhatsApp Business Account to your AWS account.

## Request Syntax
<a name="API_AssociateWhatsAppBusinessAccount_RequestSyntax"></a>

```
POST /v1/whatsapp/signup HTTP/1.1
Content-type: application/json

{
   "setupFinalization": {
      "associateInProgressToken": "{{string}}",
      "phoneNumberParent": "{{string}}",
      "phoneNumbers": [
         {
            "dataLocalizationRegion": "{{string}}",
            "id": "{{string}}",
            "tags": [
               {
                  "key": "{{string}}",
                  "value": "{{string}}"
               }
            ],
            "twoFactorPin": "{{string}}"
         }
      ],
      "waba": {
         "eventDestinations": [
            {
               "eventDestinationArn": "{{string}}",
               "roleArn": "{{string}}"
            }
         ],
         "id": "{{string}}",
         "tags": [
            {
               "key": "{{string}}",
               "value": "{{string}}"
            }
         ]
      }
   },
   "signupCallback": {
      "accessToken": "{{string}}",
      "callbackUrl": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_AssociateWhatsAppBusinessAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateWhatsAppBusinessAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [setupFinalization](#API_AssociateWhatsAppBusinessAccount_RequestSyntax) **   <a name="Social-AssociateWhatsAppBusinessAccount-request-setupFinalization"></a>
A JSON object that contains the phone numbers and WhatsApp Business Account to link to your account.
Type: [WhatsAppSetupFinalization](API_WhatsAppSetupFinalization.md) object
Required: No

 ** [signupCallback](#API_AssociateWhatsAppBusinessAccount_RequestSyntax) **   <a name="Social-AssociateWhatsAppBusinessAccount-request-signupCallback"></a>
Contains the callback access token.
Type: [WhatsAppSignupCallback](API_WhatsAppSignupCallback.md) object
Required: No

## Response Syntax
<a name="API_AssociateWhatsAppBusinessAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "linkedWhatsAppBusinessAccountId": "string",
   "signupCallbackResult": {
      "associateInProgressToken": "string",
      "linkedAccountsWithIncompleteSetup": {
         "string" : {
            "accountName": "string",
            "registrationStatus": "string",
            "unregisteredWhatsAppPhoneNumbers": [
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
            "wabaId": "string"
         }
      }
   },
   "statusCode": number
}
```

## Response Elements
<a name="API_AssociateWhatsAppBusinessAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [linkedWhatsAppBusinessAccountId](#API_AssociateWhatsAppBusinessAccount_ResponseSyntax) **   <a name="Social-AssociateWhatsAppBusinessAccount-response-linkedWhatsAppBusinessAccountId"></a>
The ID of the WhatsApp Business Account that was linked to your AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^waba-.*$)|(^arn:.*:waba/[0-9a-zA-Z]+$).*`

 ** [signupCallbackResult](#API_AssociateWhatsAppBusinessAccount_ResponseSyntax) **   <a name="Social-AssociateWhatsAppBusinessAccount-response-signupCallbackResult"></a>
Contains your WhatsApp registration status.
Type: [WhatsAppSignupCallbackResult](API_WhatsAppSignupCallbackResult.md) object

 ** [statusCode](#API_AssociateWhatsAppBusinessAccount_ResponseSyntax) **   <a name="Social-AssociateWhatsAppBusinessAccount-response-statusCode"></a>
The status code for the response.
Type: Integer

## Errors
<a name="API_AssociateWhatsAppBusinessAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** DependencyException **
Thrown when performing an action because a dependency would be broken.
HTTP Status Code: 502

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The request was denied because it would exceed one or more service quotas or limits.
HTTP Status Code: 400

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_AssociateWhatsAppBusinessAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/AssociateWhatsAppBusinessAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
