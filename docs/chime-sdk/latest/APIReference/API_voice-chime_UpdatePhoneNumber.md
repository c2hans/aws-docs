---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdatePhoneNumber.html
---

# UpdatePhoneNumber
<a name="API_voice-chime_UpdatePhoneNumber"></a>

Updates phone number details, such as product type, calling name, or phone number name for the specified phone number ID. You can update one phone number detail at a time. For example, you can update either the product type, calling name, or phone number name in one action.

For numbers outside the U.S., you must use the Amazon Chime SDK SIP Media Application Dial-In product type.

Updates to outbound calling names can take 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.

## Request Syntax
<a name="API_voice-chime_UpdatePhoneNumber_RequestSyntax"></a>

```
POST /phone-numbers/{{phoneNumberId}} HTTP/1.1
Content-type: application/json

{
   "CallingName": "{{string}}",
   "Name": "{{string}}",
   "ProductType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_voice-chime_UpdatePhoneNumber_RequestParameters"></a>

The request uses the following URI parameters.

 ** [phoneNumberId](#API_voice-chime_UpdatePhoneNumber_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdatePhoneNumber-request-uri-PhoneNumberId"></a>
The phone number ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_UpdatePhoneNumber_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CallingName](#API_voice-chime_UpdatePhoneNumber_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdatePhoneNumber-request-CallingName"></a>
The outbound calling name associated with the phone number.
Type: String
Pattern: `^$|^[a-zA-Z0-9 ]{2,15}$`
Required: No

 ** [Name](#API_voice-chime_UpdatePhoneNumber_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdatePhoneNumber-request-Name"></a>
Specifies the updated name assigned to one or more phone numbers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^$|^[a-zA-Z0-9\,\.\_\-]+(\s+[a-zA-Z0-9\,\.\_\-]+)*$`
Required: No

 ** [ProductType](#API_voice-chime_UpdatePhoneNumber_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdatePhoneNumber-request-ProductType"></a>
The product type.
Type: String
Valid Values: `VoiceConnector | SipMediaApplicationDialIn`
Required: No

## Response Syntax
<a name="API_voice-chime_UpdatePhoneNumber_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PhoneNumber": {
      "Associations": [
         {
            "AssociatedTimestamp": "string",
            "Name": "string",
            "Value": "string"
         }
      ],
      "CallingName": "string",
      "CallingNameStatus": "string",
      "Capabilities": {
         "InboundCall": boolean,
         "InboundMMS": boolean,
         "InboundSMS": boolean,
         "OutboundCall": boolean,
         "OutboundMMS": boolean,
         "OutboundSMS": boolean
      },
      "Country": "string",
      "CreatedTimestamp": "string",
      "DeletionTimestamp": "string",
      "E164PhoneNumber": "string",
      "Name": "string",
      "OrderId": "string",
      "PhoneNumberId": "string",
      "ProductType": "string",
      "Status": "string",
      "Type": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_UpdatePhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumber](#API_voice-chime_UpdatePhoneNumber_ResponseSyntax) **   <a name="chimesdk-voice-chime_UpdatePhoneNumber-response-PhoneNumber"></a>
The updated phone number details.
Type: [PhoneNumber](API_voice-chime_PhoneNumber.md) object

## Errors
<a name="API_voice-chime_UpdatePhoneNumber_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request were made simultaneously.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## See Also
<a name="API_voice-chime_UpdatePhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdatePhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
