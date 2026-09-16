---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceProfiles.html
---

# ListVoiceProfiles
<a name="API_voice-chime_ListVoiceProfiles"></a>

Lists the voice profiles in a voice profile domain.

## Request Syntax
<a name="API_voice-chime_ListVoiceProfiles_RequestSyntax"></a>

```
GET /voice-profiles?max-results={{MaxResults}}&next-token={{NextToken}}&voice-profile-domain-id={{VoiceProfileDomainId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_voice-chime_ListVoiceProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_voice-chime_ListVoiceProfiles_RequestSyntax) **   <a name="chimesdk-voice-chime_ListVoiceProfiles-request-uri-MaxResults"></a>
The maximum number of results in the request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_voice-chime_ListVoiceProfiles_RequestSyntax) **   <a name="chimesdk-voice-chime_ListVoiceProfiles-request-uri-NextToken"></a>
The token used to retrieve the next page of results.

 ** [VoiceProfileDomainId](#API_voice-chime_ListVoiceProfiles_RequestSyntax) **   <a name="chimesdk-voice-chime_ListVoiceProfiles-request-uri-VoiceProfileDomainId"></a>
The ID of the voice profile domain.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_ListVoiceProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_voice-chime_ListVoiceProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "VoiceProfiles": [
      {
         "CreatedTimestamp": "string",
         "ExpirationTimestamp": "string",
         "UpdatedTimestamp": "string",
         "VoiceProfileArn": "string",
         "VoiceProfileDomainId": "string",
         "VoiceProfileId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_voice-chime_ListVoiceProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_voice-chime_ListVoiceProfiles_ResponseSyntax) **   <a name="chimesdk-voice-chime_ListVoiceProfiles-response-NextToken"></a>
The token used to retrieve the next page of results.
Type: String

 ** [VoiceProfiles](#API_voice-chime_ListVoiceProfiles_ResponseSyntax) **   <a name="chimesdk-voice-chime_ListVoiceProfiles-response-VoiceProfiles"></a>
The list of voice profiles.
Type: Array of [VoiceProfileSummary](API_voice-chime_VoiceProfileSummary.md) objects

## Errors
<a name="API_voice-chime_ListVoiceProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

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
<a name="API_voice-chime_ListVoiceProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/ListVoiceProfiles)
