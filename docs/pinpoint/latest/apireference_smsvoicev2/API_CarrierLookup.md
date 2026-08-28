---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CarrierLookup.html
---

# CarrierLookup
<a name="API_CarrierLookup"></a>

Returns information about a destination phone number, including whether the number type and whether it is valid, the carrier, and more.

## Request Syntax
<a name="API_CarrierLookup_RequestSyntax"></a>

```
{
   "PhoneNumber": "{{string}}"
}
```

## Request Parameters
<a name="API_CarrierLookup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PhoneNumber](#API_CarrierLookup_RequestSyntax) **   <a name="pinpoint-CarrierLookup-request-PhoneNumber"></a>
The phone number that you want to retrieve information about. You can provide the phone number in various formats including special characters such as parentheses, brackets, spaces, hyphens, periods, and commas. The service automatically converts the input to E164 format for processing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `\+[({\s\[]?[1-9][0-9(){}\s\[\],.-]{1,38}`
Required: Yes

## Response Syntax
<a name="API_CarrierLookup_ResponseSyntax"></a>

```
{
   "Carrier": "string",
   "Country": "string",
   "DialingCountryCode": "string",
   "E164PhoneNumber": "string",
   "IsoCountryCode": "string",
   "MCC": "string",
   "MNC": "string",
   "PhoneNumberType": "string"
}
```

## Response Elements
<a name="API_CarrierLookup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Carrier](#API_CarrierLookup_ResponseSyntax) **   <a name="pinpoint-CarrierLookup-response-Carrier"></a>
The carrier or service provider that the phone number is currently registered with. In some countries and regions, this value may be the carrier or service provider that the phone number was originally registered with.
Type: String

 ** [Country](#API_CarrierLookup_ResponseSyntax) **   <a name="pinpoint-CarrierLookup-response-Country"></a>
The name of the country or region for the phone number.
Type: String

 ** [DialingCountryCode](#API_CarrierLookup_ResponseSyntax) **   <a name="pinpoint-CarrierLookup-response-DialingCountryCode"></a>
The country or region numeric dialing code for the phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Pattern: `[\d]+`

 ** [E164PhoneNumber](#API_CarrierLookup_ResponseSyntax) **   <a name="pinpoint-CarrierLookup-response-E164PhoneNumber"></a>
The phone number in E164 format, sanitized from the original input by removing any formatting characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+[1-9][0-9]{1,18}`

 ** [IsoCountryCode](#API_CarrierLookup_ResponseSyntax) **   <a name="pinpoint-CarrierLookup-response-IsoCountryCode"></a>
The two-character country or region code, in ISO 3166-1 alpha-2 format, for the phone number.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`

 ** [MCC](#API_CarrierLookup_ResponseSyntax) **   <a name="pinpoint-CarrierLookup-response-MCC"></a>
The phone number's mobile country code, for mobile phone number types
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[\d]+`

 ** [MNC](#API_CarrierLookup_ResponseSyntax) **   <a name="pinpoint-CarrierLookup-response-MNC"></a>
The phone number's mobile network code, for mobile phone number types.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `[\d]+`

 ** [PhoneNumberType](#API_CarrierLookup_ResponseSyntax) **   <a name="pinpoint-CarrierLookup-response-PhoneNumberType"></a>
Describes the type of phone number. Valid values are: MOBILE, LANDLINE, OTHER, and INVALID. Avoid sending SMS or voice messages to INVALID phone numbers, as these numbers are unlikely to belong to actual recipients.
Type: String
Valid Values: `MOBILE | LANDLINE | OTHER | INVALID`

## Errors
<a name="API_CarrierLookup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## Examples
<a name="API_CarrierLookup_Examples"></a>

### Example
<a name="API_CarrierLookup_Example_1"></a>

A carrier lookup response for a valid mobile number.

```
{
    "PhoneNumber": "+1 (555) 555-5333"
}
```

```
{
   "Carrier": "ExampleCorp Mobile",
   "Country": "United States",
   "IsoCountryCode": "US",
   "MCC": "111",
   "MNC": "11",
   "DialingCountryCode": "1",
   "E164PhoneNumber": "+15555555333",
   "PhoneNumberType": "MOBILE"
}
```

## See Also
<a name="API_CarrierLookup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CarrierLookup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
