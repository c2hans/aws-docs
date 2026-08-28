---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceProfileDomain.html
---

# GetVoiceProfileDomain
<a name="API_voice-chime_GetVoiceProfileDomain"></a>

Retrieves the details of the specified voice profile domain.

## Request Syntax
<a name="API_voice-chime_GetVoiceProfileDomain_RequestSyntax"></a>

```
GET /voice-profile-domains/{{VoiceProfileDomainId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_voice-chime_GetVoiceProfileDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [VoiceProfileDomainId](#API_voice-chime_GetVoiceProfileDomain_RequestSyntax) **   <a name="chimesdk-voice-chime_GetVoiceProfileDomain-request-uri-VoiceProfileDomainId"></a>
The voice profile domain ID.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_GetVoiceProfileDomain_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_voice-chime_GetVoiceProfileDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VoiceProfileDomain": {
      "CreatedTimestamp": "string",
      "Description": "string",
      "Name": "string",
      "ServerSideEncryptionConfiguration": {
         "KmsKeyArn": "string"
      },
      "UpdatedTimestamp": "string",
      "VoiceProfileDomainArn": "string",
      "VoiceProfileDomainId": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_GetVoiceProfileDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VoiceProfileDomain](#API_voice-chime_GetVoiceProfileDomain_ResponseSyntax) **   <a name="chimesdk-voice-chime_GetVoiceProfileDomain-response-VoiceProfileDomain"></a>
The details of the voice profile domain.
Type: [VoiceProfileDomain](API_voice-chime_VoiceProfileDomain.md) object

## Errors
<a name="API_voice-chime_GetVoiceProfileDomain_Errors"></a>

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
<a name="API_voice-chime_GetVoiceProfileDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/GetVoiceProfileDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
