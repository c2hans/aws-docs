---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateAdConfiguration.html
---

# CreateAdConfiguration
<a name="API_CreateAdConfiguration"></a>

Creates a new ad configuration to be used for server-side ad insertion.

## Request Syntax
<a name="API_CreateAdConfiguration_RequestSyntax"></a>

```
POST /CreateAdConfiguration HTTP/1.1
Content-type: application/json

{
   "mediaTailorPlaybackConfigurations": [
      {
         "playbackConfigurationArn": "{{string}}"
      }
   ],
   "name": "{{string}}",
   "postRollConfiguration": {
      "durationSeconds": {{number}},
      "enabled": {{boolean}}
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAdConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAdConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [mediaTailorPlaybackConfigurations](#API_CreateAdConfiguration_RequestSyntax) **   <a name="ivs-CreateAdConfiguration-request-mediaTailorPlaybackConfigurations"></a>
List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see [Generate and Sign IVS Playback Tokens](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html).
Type: Array of [MediaTailorPlaybackConfiguration](API_MediaTailorPlaybackConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: Yes

 ** [name](#API_CreateAdConfiguration_RequestSyntax) **   <a name="ivs-CreateAdConfiguration-request-name"></a>
Ad configuration name. Defaults to “”.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [postRollConfiguration](#API_CreateAdConfiguration_RequestSyntax) **   <a name="ivs-CreateAdConfiguration-request-postRollConfiguration"></a>
Configuration for the post-roll ad break to use for this ad configuration. Default: disabled (`enabled` set to false, `durationSeconds` set to 15).
Type: [PostRollConfiguration](API_PostRollConfiguration.md) object
Required: No

 ** [tags](#API_CreateAdConfiguration_RequestSyntax) **   <a name="ivs-CreateAdConfiguration-request-tags"></a>
Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreateAdConfiguration_ResponseSyntax"></a>

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
<a name="API_CreateAdConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adConfiguration](#API_CreateAdConfiguration_ResponseSyntax) **   <a name="ivs-CreateAdConfiguration-response-adConfiguration"></a>

Type: [AdConfiguration](API_AdConfiguration.md) object

## Errors
<a name="API_CreateAdConfiguration_Errors"></a>

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
<a name="API_CreateAdConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/CreateAdConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/CreateAdConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
