---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListPlaybackRestrictionPolicies.html
---

# ListPlaybackRestrictionPolicies
<a name="API_ListPlaybackRestrictionPolicies"></a>

Gets summary information about playback restriction policies.

## Request Syntax
<a name="API_ListPlaybackRestrictionPolicies_RequestSyntax"></a>

```
POST /ListPlaybackRestrictionPolicies HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPlaybackRestrictionPolicies_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPlaybackRestrictionPolicies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPlaybackRestrictionPolicies_RequestSyntax) **   <a name="ivs-ListPlaybackRestrictionPolicies-request-maxResults"></a>
Maximum number of policies to return. Default: 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListPlaybackRestrictionPolicies_RequestSyntax) **   <a name="ivs-ListPlaybackRestrictionPolicies-request-nextToken"></a>
The first policy to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListPlaybackRestrictionPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "playbackRestrictionPolicies": [
      {
         "allowedCountries": [ "string" ],
         "allowedOrigins": [ "string" ],
         "arn": "string",
         "enableStrictOriginEnforcement": boolean,
         "name": "string",
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListPlaybackRestrictionPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPlaybackRestrictionPolicies_ResponseSyntax) **   <a name="ivs-ListPlaybackRestrictionPolicies-response-nextToken"></a>
If there are more channels than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [playbackRestrictionPolicies](#API_ListPlaybackRestrictionPolicies_ResponseSyntax) **   <a name="ivs-ListPlaybackRestrictionPolicies-response-playbackRestrictionPolicies"></a>
List of the matching policies.
Type: Array of [PlaybackRestrictionPolicySummary](API_PlaybackRestrictionPolicySummary.md) objects

## Errors
<a name="API_ListPlaybackRestrictionPolicies_Errors"></a>

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

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListPlaybackRestrictionPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/ListPlaybackRestrictionPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/ListPlaybackRestrictionPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
