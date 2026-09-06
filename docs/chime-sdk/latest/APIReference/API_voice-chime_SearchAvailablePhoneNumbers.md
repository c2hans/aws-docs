---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SearchAvailablePhoneNumbers.html
---

# SearchAvailablePhoneNumbers
<a name="API_voice-chime_SearchAvailablePhoneNumbers"></a>

Searches the provisioned phone numbers in an organization.

## Request Syntax
<a name="API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax"></a>

```
GET /search?type=phone-numbers&area-code={{AreaCode}}&city={{City}}&country={{Country}}&max-results={{MaxResults}}&next-token={{NextToken}}&phone-number-type={{PhoneNumberType}}&state={{State}}&toll-free-prefix={{TollFreePrefix}} HTTP/1.1
```

## URI Request Parameters
<a name="API_voice-chime_SearchAvailablePhoneNumbers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AreaCode](#API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-request-uri-AreaCode"></a>
Confines a search to just the phone numbers associated with the specified area code.

 ** [City](#API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-request-uri-City"></a>
Confines a search to just the phone numbers associated with the specified city.

 ** [Country](#API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-request-uri-Country"></a>
Confines a search to just the phone numbers associated with the specified country.
Pattern: `[A-Z]{2}`

 ** [MaxResults](#API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-request-uri-NextToken"></a>
The token used to return the next page of results.

 ** [PhoneNumberType](#API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-request-uri-PhoneNumberType"></a>
Confines a search to just the phone numbers associated with the specified phone number type, either **local** or **toll-free**.
Valid Values: `Local | TollFree`

 ** [State](#API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-request-uri-State"></a>
Confines a search to just the phone numbers associated with the specified state.

 ** [TollFreePrefix](#API_voice-chime_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-request-uri-TollFreePrefix"></a>
Confines a search to just the phone numbers associated with the specified toll-free prefix.
Length Constraints: Fixed length of 3.
Pattern: `^8(00|33|44|55|66|77|88)$`

## Request Body
<a name="API_voice-chime_SearchAvailablePhoneNumbers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_voice-chime_SearchAvailablePhoneNumbers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "E164PhoneNumbers": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_voice-chime_SearchAvailablePhoneNumbers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [E164PhoneNumbers](#API_voice-chime_SearchAvailablePhoneNumbers_ResponseSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-response-E164PhoneNumbers"></a>
Confines a search to just the phone numbers in the E.164 format.
Type: Array of strings
Pattern: `^\+?[1-9]\d{1,14}$`

 ** [NextToken](#API_voice-chime_SearchAvailablePhoneNumbers_ResponseSyntax) **   <a name="chimesdk-voice-chime_SearchAvailablePhoneNumbers-response-NextToken"></a>
The token used to return the next page of results.
Type: String

## Errors
<a name="API_voice-chime_SearchAvailablePhoneNumbers_Errors"></a>

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
<a name="API_voice-chime_SearchAvailablePhoneNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/SearchAvailablePhoneNumbers)
