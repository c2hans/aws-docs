---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ListAvailablePhoneNumbers.html
---

# ListAvailablePhoneNumbers
<a name="API_ListAvailablePhoneNumbers"></a>

Retrieves a list of phone numbers that are available to request, based on the country, capabilities, and number type that you specify. You can optionally provide a number preference to return only numbers that match a specific digit pattern.

If no numbers match your search, this operation returns an empty list rather than an error. This operation currently supports only `TEN_DLC` number types in the `US`.

## Request Syntax
<a name="API_ListAvailablePhoneNumbers_RequestSyntax"></a>

```
{
   "IsoCountryCode": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "NumberCapabilities": [ "{{string}}" ],
   "NumberPreference": [
      {
         "Filter": [ "{{string}}" ],
         "PreferenceType": [ "{{string}}" ]
      }
   ],
   "NumberType": "{{string}}",
   "RegistrationId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAvailablePhoneNumbers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IsoCountryCode](#API_ListAvailablePhoneNumbers_RequestSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-request-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region in which to search for available phone numbers. This operation currently supports only `US`.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** [MaxResults](#API_ListAvailablePhoneNumbers_RequestSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-request-MaxResults"></a>
The maximum number of results to return per page. If you don't specify a value, the default is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [NextToken](#API_ListAvailablePhoneNumbers_RequestSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-request-NextToken"></a>
The token returned from a previous request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [NumberCapabilities](#API_ListAvailablePhoneNumbers_RequestSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-request-NumberCapabilities"></a>
The capabilities to filter by, such as SMS. Only phone numbers that support all of the specified capabilities are returned.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** [NumberPreference](#API_ListAvailablePhoneNumbers_RequestSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-request-NumberPreference"></a>
An optional selection preference used to return only phone numbers that match a specific digit pattern, such as numbers that start with, end with, or contain a particular sequence. You can specify at most one preference. Number preferences apply only to `TEN_DLC` numbers in the `US`.
Type: Array of [NumberPreferenceItem](API_NumberPreferenceItem.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [NumberType](#API_ListAvailablePhoneNumbers_RequestSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-request-NumberType"></a>
The type of phone number to search for.
Type: String
Valid Values: `TEN_DLC`
Required: Yes

 ** [RegistrationId](#API_ListAvailablePhoneNumbers_RequestSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-request-RegistrationId"></a>
The registration associated with the request. A registration is required for regulated number types. You can specify either:
+ The unique identifier of the registration.
+ The Amazon Resource Name (ARN) of the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

## Response Syntax
<a name="API_ListAvailablePhoneNumbers_ResponseSyntax"></a>

```
{
   "AvailablePhoneNumbers": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAvailablePhoneNumbers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailablePhoneNumbers](#API_ListAvailablePhoneNumbers_ResponseSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-response-AvailablePhoneNumbers"></a>
An array of phone numbers, in E.164 format, that are available to request based on the specified filters.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`

 ** [NextToken](#API_ListAvailablePhoneNumbers_ResponseSyntax) **   <a name="pinpoint-ListAvailablePhoneNumbers-response-NextToken"></a>
The token to include in the next request to retrieve the next page of results. This value is null when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

## Errors
<a name="API_ListAvailablePhoneNumbers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.
 ** Reason **
The reason for the exception.
 ** ResourceId **
The unique identifier of the request.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
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

## See Also
<a name="API_ListAvailablePhoneNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ListAvailablePhoneNumbers)
