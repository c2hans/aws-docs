---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ListNotifyCountries.html
---

# ListNotifyCountries
<a name="API_ListNotifyCountries"></a>

Lists countries that support notify messaging. You can optionally filter by channel, use case, or tier.

## Request Syntax
<a name="API_ListNotifyCountries_RequestSyntax"></a>

```
{
   "Channels": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Tier": "{{string}}",
   "UseCases": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListNotifyCountries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Channels](#API_ListNotifyCountries_RequestSyntax) **   <a name="pinpoint-ListNotifyCountries-request-Channels"></a>
An array of channels to filter the results by.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: No

 ** [MaxResults](#API_ListNotifyCountries_RequestSyntax) **   <a name="pinpoint-ListNotifyCountries-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListNotifyCountries_RequestSyntax) **   <a name="pinpoint-ListNotifyCountries-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [Tier](#API_ListNotifyCountries_RequestSyntax) **   <a name="pinpoint-ListNotifyCountries-request-Tier"></a>
The tier to filter the results by.
Type: String
Valid Values: `BASIC | ADVANCED`
Required: No

 ** [UseCases](#API_ListNotifyCountries_RequestSyntax) **   <a name="pinpoint-ListNotifyCountries-request-UseCases"></a>
An array of use cases to filter the results by.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `CODE_VERIFICATION`
Required: No

## Response Syntax
<a name="API_ListNotifyCountries_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "NotifyCountries": [
      {
         "CountryName": "string",
         "CustomerOwnedIdentityRequired": boolean,
         "IsoCountryCode": "string",
         "SupportedChannels": [ "string" ],
         "SupportedTiers": [ "string" ],
         "SupportedUseCases": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListNotifyCountries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNotifyCountries_ResponseSyntax) **   <a name="pinpoint-ListNotifyCountries-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [NotifyCountries](#API_ListNotifyCountries_ResponseSyntax) **   <a name="pinpoint-ListNotifyCountries-response-NotifyCountries"></a>
An array of NotifyCountryInformation objects that contain the results.
Type: Array of [NotifyCountryInformation](API_NotifyCountryInformation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 300 items.

## Errors
<a name="API_ListNotifyCountries_Errors"></a>

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
<a name="API_ListNotifyCountries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ListNotifyCountries)
