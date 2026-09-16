---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListAvailableVoiceConnectorRegions.html
---

# ListAvailableVoiceConnectorRegions
<a name="API_voice-chime_ListAvailableVoiceConnectorRegions"></a>

Lists the available AWS Regions in which you can create an Amazon Chime SDK Voice Connector.

## Request Syntax
<a name="API_voice-chime_ListAvailableVoiceConnectorRegions_RequestSyntax"></a>

```
GET /voice-connector-regions HTTP/1.1
```

## URI Request Parameters
<a name="API_voice-chime_ListAvailableVoiceConnectorRegions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_ListAvailableVoiceConnectorRegions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_voice-chime_ListAvailableVoiceConnectorRegions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VoiceConnectorRegions": [ "string" ]
}
```

## Response Elements
<a name="API_voice-chime_ListAvailableVoiceConnectorRegions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VoiceConnectorRegions](#API_voice-chime_ListAvailableVoiceConnectorRegions_ResponseSyntax) **   <a name="chimesdk-voice-chime_ListAvailableVoiceConnectorRegions-response-VoiceConnectorRegions"></a>
The list of AWS Regions.
Type: Array of strings
Valid Values: `us-east-1 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-2 | ap-northeast-1 | ap-southeast-1 | ap-southeast-2`

## Errors
<a name="API_voice-chime_ListAvailableVoiceConnectorRegions_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

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
<a name="API_voice-chime_ListAvailableVoiceConnectorRegions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/ListAvailableVoiceConnectorRegions)
