---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdatePlaybackRestrictionPolicy.html
---

# UpdatePlaybackRestrictionPolicy
<a name="API_UpdatePlaybackRestrictionPolicy"></a>

Updates a specified playback restriction policy.

## Request Syntax
<a name="API_UpdatePlaybackRestrictionPolicy_RequestSyntax"></a>

```
POST /UpdatePlaybackRestrictionPolicy HTTP/1.1
Content-type: application/json

{
   "allowedCountries": [ "{{string}}" ],
   "allowedOrigins": [ "{{string}}" ],
   "arn": "{{string}}",
   "enableStrictOriginEnforcement": {{boolean}},
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePlaybackRestrictionPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdatePlaybackRestrictionPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedCountries](#API_UpdatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-UpdatePlaybackRestrictionPolicy-request-allowedCountries"></a>
A list of country codes that control geoblocking restriction. Allowed values are the officially assigned [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) codes. Default: All countries (an empty array).
Type: Array of strings
Length Constraints: Fixed length of 2.
Required: No

 ** [allowedOrigins](#API_UpdatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-UpdatePlaybackRestrictionPolicy-request-allowedOrigins"></a>
A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin). Default: All origins (an empty array).
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [arn](#API_UpdatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-UpdatePlaybackRestrictionPolicy-request-arn"></a>
ARN of the playback-restriction-policy to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-restriction-policy/[a-zA-Z0-9-]+`
Required: Yes

 ** [enableStrictOriginEnforcement](#API_UpdatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-UpdatePlaybackRestrictionPolicy-request-enableStrictOriginEnforcement"></a>
Whether channel playback is constrained by origin site. Default: `false`.
Type: Boolean
Required: No

 ** [name](#API_UpdatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-UpdatePlaybackRestrictionPolicy-request-name"></a>
Playback-restriction-policy name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

## Response Syntax
<a name="API_UpdatePlaybackRestrictionPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "playbackRestrictionPolicy": {
      "allowedCountries": [ "string" ],
      "allowedOrigins": [ "string" ],
      "arn": "string",
      "enableStrictOriginEnforcement": boolean,
      "name": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdatePlaybackRestrictionPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [playbackRestrictionPolicy](#API_UpdatePlaybackRestrictionPolicy_ResponseSyntax) **   <a name="ivs-UpdatePlaybackRestrictionPolicy-response-playbackRestrictionPolicy"></a>
Object specifying the updated policy.
Type: [PlaybackRestrictionPolicy](API_PlaybackRestrictionPolicy.md) object

## Errors
<a name="API_UpdatePlaybackRestrictionPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePlaybackRestrictionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/UpdatePlaybackRestrictionPolicy)
