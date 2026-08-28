---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplication.html
---

# CreateSipMediaApplication
<a name="API_voice-chime_CreateSipMediaApplication"></a>

Creates a SIP media application. For more information about SIP media applications, see [Managing SIP media applications and rules](https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html) in the *Amazon Chime SDK Administrator Guide*.

## Request Syntax
<a name="API_voice-chime_CreateSipMediaApplication_RequestSyntax"></a>

```
POST /sip-media-applications HTTP/1.1
Content-type: application/json

{
   "AwsRegion": "{{string}}",
   "Endpoints": [
      {
         "LambdaArn": "{{string}}"
      }
   ],
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_voice-chime_CreateSipMediaApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_CreateSipMediaApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AwsRegion](#API_voice-chime_CreateSipMediaApplication_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplication-request-AwsRegion"></a>
The AWS Region assigned to the SIP media application.
Type: String
Required: Yes

 ** [Endpoints](#API_voice-chime_CreateSipMediaApplication_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplication-request-Endpoints"></a>
List of endpoints (Lambda ARNs) specified for the SIP media application.
Type: Array of [SipMediaApplicationEndpoint](API_voice-chime_SipMediaApplicationEndpoint.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [Name](#API_voice-chime_CreateSipMediaApplication_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplication-request-Name"></a>
The SIP media application's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: Yes

 ** [Tags](#API_voice-chime_CreateSipMediaApplication_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplication-request-Tags"></a>
The tags assigned to the SIP media application.
Type: Array of [Tag](API_voice-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_voice-chime_CreateSipMediaApplication_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "SipMediaApplication": {
      "AwsRegion": "string",
      "CreatedTimestamp": "string",
      "Endpoints": [
         {
            "LambdaArn": "string"
         }
      ],
      "Name": "string",
      "SipMediaApplicationArn": "string",
      "SipMediaApplicationId": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_CreateSipMediaApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [SipMediaApplication](#API_voice-chime_CreateSipMediaApplication_ResponseSyntax) **   <a name="chimesdk-voice-chime_CreateSipMediaApplication-response-SipMediaApplication"></a>
The SIP media application details.
Type: [SipMediaApplication](API_voice-chime_SipMediaApplication.md) object

## Errors
<a name="API_voice-chime_CreateSipMediaApplication_Errors"></a>

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
<a name="API_voice-chime_CreateSipMediaApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CreateSipMediaApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
