---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfileDomain.html
---

# CreateVoiceProfileDomain
<a name="API_voice-chime_CreateVoiceProfileDomain"></a>

Creates a voice profile domain, a collection of voice profiles, their voice prints, and encrypted enrollment audio.

**Important**
Before creating any voice profiles, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the [AWS service terms](https://aws.amazon.com/service-terms/) for the Amazon Chime SDK.

For more information about voice profile domains, see [Using Amazon Chime SDK Voice Analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-voice-analytics.html) in the *Amazon Chime SDK Developer Guide*.

## Request Syntax
<a name="API_voice-chime_CreateVoiceProfileDomain_RequestSyntax"></a>

```
POST /voice-profile-domains HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "ServerSideEncryptionConfiguration": {
      "KmsKeyArn": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_voice-chime_CreateVoiceProfileDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_CreateVoiceProfileDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_voice-chime_CreateVoiceProfileDomain_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceProfileDomain-request-ClientRequestToken"></a>
The unique identifier for the client request. Use a different token for different domain creation requests.
Type: String
Pattern: `^[-_a-zA-Z0-9]*${2,64}$`
Required: No

 ** [Description](#API_voice-chime_CreateVoiceProfileDomain_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceProfileDomain-request-Description"></a>
A description of the voice profile domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_voice-chime_CreateVoiceProfileDomain_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceProfileDomain-request-Name"></a>
The name of the voice profile domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: Yes

 ** [ServerSideEncryptionConfiguration](#API_voice-chime_CreateVoiceProfileDomain_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceProfileDomain-request-ServerSideEncryptionConfiguration"></a>
The server-side encryption configuration for the request.
Type: [ServerSideEncryptionConfiguration](API_voice-chime_ServerSideEncryptionConfiguration.md) object
Required: Yes

 ** [Tags](#API_voice-chime_CreateVoiceProfileDomain_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceProfileDomain-request-Tags"></a>
The tags assigned to the domain.
Type: Array of [Tag](API_voice-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_voice-chime_CreateVoiceProfileDomain_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_voice-chime_CreateVoiceProfileDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [VoiceProfileDomain](#API_voice-chime_CreateVoiceProfileDomain_ResponseSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceProfileDomain-response-VoiceProfileDomain"></a>
The requested voice profile domain.
Type: [VoiceProfileDomain](API_voice-chime_VoiceProfileDomain.md) object

## Errors
<a name="API_voice-chime_CreateVoiceProfileDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request were made simultaneously.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

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
<a name="API_voice-chime_CreateVoiceProfileDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CreateVoiceProfileDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
