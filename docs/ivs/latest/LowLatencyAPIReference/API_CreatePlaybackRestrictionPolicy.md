---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreatePlaybackRestrictionPolicy.html
---

# CreatePlaybackRestrictionPolicy
<a name="API_CreatePlaybackRestrictionPolicy"></a>

Creates a new playback restriction policy, for constraining playback by countries and/or origins.

## Request Syntax
<a name="API_CreatePlaybackRestrictionPolicy_RequestSyntax"></a>

```
POST /CreatePlaybackRestrictionPolicy HTTP/1.1
Content-type: application/json

{
   "allowedCountries": [ "{{string}}" ],
   "allowedOrigins": [ "{{string}}" ],
   "enableStrictOriginEnforcement": {{boolean}},
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePlaybackRestrictionPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePlaybackRestrictionPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowedCountries](#API_CreatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-CreatePlaybackRestrictionPolicy-request-allowedCountries"></a>
A list of country codes that control geoblocking restriction. Allowed values are the officially assigned [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) codes. Default: All countries (an empty array).
Type: Array of strings
Length Constraints: Fixed length of 2.
Required: No

 ** [allowedOrigins](#API_CreatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-CreatePlaybackRestrictionPolicy-request-allowedOrigins"></a>
A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin). Default: All origins (an empty array).
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [enableStrictOriginEnforcement](#API_CreatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-CreatePlaybackRestrictionPolicy-request-enableStrictOriginEnforcement"></a>
Whether channel playback is constrained by origin site. Default: `false`.
Type: Boolean
Required: No

 ** [name](#API_CreatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-CreatePlaybackRestrictionPolicy-request-name"></a>
Playback-restriction-policy name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [tags](#API_CreatePlaybackRestrictionPolicy_RequestSyntax) **   <a name="ivs-CreatePlaybackRestrictionPolicy-request-tags"></a>
Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreatePlaybackRestrictionPolicy_ResponseSyntax"></a>

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
<a name="API_CreatePlaybackRestrictionPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [playbackRestrictionPolicy](#API_CreatePlaybackRestrictionPolicy_ResponseSyntax) **   <a name="ivs-CreatePlaybackRestrictionPolicy-response-playbackRestrictionPolicy"></a>

Type: [PlaybackRestrictionPolicy](API_PlaybackRestrictionPolicy.md) object

## Errors
<a name="API_CreatePlaybackRestrictionPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

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
<a name="API_CreatePlaybackRestrictionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/CreatePlaybackRestrictionPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
