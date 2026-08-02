---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdateAdConfiguration.html
---

# UpdateAdConfiguration
<a name="API_UpdateAdConfiguration"></a>

Updates a specified ad configuration.

## Request Syntax
<a name="API_UpdateAdConfiguration_RequestSyntax"></a>

```
POST /UpdateAdConfiguration HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "mediaTailorPlaybackConfigurations": [
      {
         "playbackConfigurationArn": "{{string}}"
      }
   ],
   "name": "{{string}}",
   "postRollConfiguration": {
      "durationSeconds": {{number}},
      "enabled": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateAdConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAdConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateAdConfiguration_RequestSyntax) **   <a name="ivs-UpdateAdConfiguration-request-arn"></a>
ARN of the ad configuration to be updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ad-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** [mediaTailorPlaybackConfigurations](#API_UpdateAdConfiguration_RequestSyntax) **   <a name="ivs-UpdateAdConfiguration-request-mediaTailorPlaybackConfigurations"></a>
List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see [Generate and Sign IVS Playback Tokens](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html).
Type: Array of [MediaTailorPlaybackConfiguration](API_MediaTailorPlaybackConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

 ** [name](#API_UpdateAdConfiguration_RequestSyntax) **   <a name="ivs-UpdateAdConfiguration-request-name"></a>
Ad configuration name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [postRollConfiguration](#API_UpdateAdConfiguration_RequestSyntax) **   <a name="ivs-UpdateAdConfiguration-request-postRollConfiguration"></a>
Configuration for the post-roll ad break to use for this ad configuration.
Type: [PostRollConfiguration](API_PostRollConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateAdConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adConfiguration": {
      "arn": "string",
      "mediaTailorPlaybackConfigurations": [
         {
            "playbackConfigurationArn": "string"
         }
      ],
      "name": "string",
      "postRollConfiguration": {
         "durationSeconds": number,
         "enabled": boolean
      },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateAdConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adConfiguration](#API_UpdateAdConfiguration_ResponseSyntax) **   <a name="ivs-UpdateAdConfiguration-response-adConfiguration"></a>
Object specifying the updated ad configuration.
Type: [AdConfiguration](API_AdConfiguration.md) object

## Errors
<a name="API_UpdateAdConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAdConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/UpdateAdConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/UpdateAdConfiguration)
