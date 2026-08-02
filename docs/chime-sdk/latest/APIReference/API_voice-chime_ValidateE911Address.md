---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html
---

# ValidateE911Address
<a name="API_voice-chime_ValidateE911Address"></a>

Validates an address to be used for 911 calls made with Amazon Chime SDK Voice Connectors. You can use validated addresses in a Presence Information Data Format Location Object file that you include in SIP requests. That helps ensure that addresses are routed to the appropriate Public Safety Answering Point.

## Request Syntax
<a name="API_voice-chime_ValidateE911Address_RequestSyntax"></a>

```
POST /emergency-calling/address HTTP/1.1
Content-type: application/json

{
   "AwsAccountId": "{{string}}",
   "City": "{{string}}",
   "Country": "{{string}}",
   "PostalCode": "{{string}}",
   "State": "{{string}}",
   "StreetInfo": "{{string}}",
   "StreetNumber": "{{string}}"
}
```

## URI Request Parameters
<a name="API_voice-chime_ValidateE911Address_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_ValidateE911Address_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AwsAccountId](#API_voice-chime_ValidateE911Address_RequestSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-request-AwsAccountId"></a>
The AWS account ID.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [City](#API_voice-chime_ValidateE911Address_RequestSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-request-City"></a>
The address city, such as `Portland`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Country](#API_voice-chime_ValidateE911Address_RequestSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-request-Country"></a>
The country in the address being validated as two-letter country code in ISO 3166-1 alpha-2 format, such as `US`. For more information, see [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) in Wikipedia.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [PostalCode](#API_voice-chime_ValidateE911Address_RequestSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-request-PostalCode"></a>
The dress postal code, such `04352`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [State](#API_voice-chime_ValidateE911Address_RequestSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-request-State"></a>
The address state, such as `ME`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [StreetInfo](#API_voice-chime_ValidateE911Address_RequestSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-request-StreetInfo"></a>
The address street information, such as `8th Avenue`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [StreetNumber](#API_voice-chime_ValidateE911Address_RequestSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-request-StreetNumber"></a>
The address street number, such as `200` or `2121`.
Type: String
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_voice-chime_ValidateE911Address_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "Address": {
      "city": "string",
      "country": "string",
      "postalCode": "string",
      "postalCodePlus4": "string",
      "postDirectional": "string",
      "preDirectional": "string",
      "state": "string",
      "streetName": "string",
      "streetNumber": "string",
      "streetSuffix": "string"
   },
   "AddressExternalId": "string",
   "CandidateAddressList": [
      {
         "city": "string",
         "country": "string",
         "postalCode": "string",
         "postalCodePlus4": "string",
         "state": "string",
         "streetInfo": "string",
         "streetNumber": "string"
      }
   ],
   "ValidationResult": number
}
```

## Response Elements
<a name="API_voice-chime_ValidateE911Address_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [Address](#API_voice-chime_ValidateE911Address_ResponseSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-response-Address"></a>
The validated address.
Type: [Address](API_voice-chime_Address.md) object

 ** [AddressExternalId](#API_voice-chime_ValidateE911Address_ResponseSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-response-AddressExternalId"></a>
The ID that represents the address.
Type: String

 ** [CandidateAddressList](#API_voice-chime_ValidateE911Address_ResponseSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-response-CandidateAddressList"></a>
The list of address suggestions..
Type: Array of [CandidateAddress](API_voice-chime_CandidateAddress.md) objects

 ** [ValidationResult](#API_voice-chime_ValidateE911Address_ResponseSyntax) **   <a name="chimesdk-voice-chime_ValidateE911Address-response-ValidationResult"></a>
Number indicating the result of address validation.
Each possible result is defined as follows:
+  `0` - Address validation succeeded.
+  `1` - Address validation succeeded. The address was a close enough match and has been corrected as part of the address object.
+  `2` - Address validation failed. You should re-submit the validation request with candidates from the `CandidateAddressList` result, if it's a close match.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.

## Errors
<a name="API_voice-chime_ValidateE911Address_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

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
<a name="API_voice-chime_ValidateE911Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/ValidateE911Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/ValidateE911Address)
