---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackRestrictionPolicySummary.html
---

# PlaybackRestrictionPolicySummary
<a name="API_PlaybackRestrictionPolicySummary"></a>

Summary information about a PlaybackRestrictionPolicy.

## Contents
<a name="API_PlaybackRestrictionPolicySummary_Contents"></a>

 ** allowedCountries **   <a name="ivs-Type-PlaybackRestrictionPolicySummary-allowedCountries"></a>
A list of country codes that control geoblocking restriction. Allowed values are the officially assigned [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) codes. Default: All countries (an empty array).
Type: Array of strings
Length Constraints: Fixed length of 2.
Required: Yes

 ** allowedOrigins **   <a name="ivs-Type-PlaybackRestrictionPolicySummary-allowedOrigins"></a>
A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin). Default: All origins (an empty array).
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** arn **   <a name="ivs-Type-PlaybackRestrictionPolicySummary-arn"></a>
Playback-restriction-policy ARN
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-restriction-policy/[a-zA-Z0-9-]+`
Required: Yes

 ** enableStrictOriginEnforcement **   <a name="ivs-Type-PlaybackRestrictionPolicySummary-enableStrictOriginEnforcement"></a>
Whether channel playback is constrained by origin site. Default: `false`.
Type: Boolean
Required: No

 ** name **   <a name="ivs-Type-PlaybackRestrictionPolicySummary-name"></a>
Playback-restriction-policy name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** tags **   <a name="ivs-Type-PlaybackRestrictionPolicySummary-tags"></a>
Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## See Also
<a name="API_PlaybackRestrictionPolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/PlaybackRestrictionPolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/PlaybackRestrictionPolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/PlaybackRestrictionPolicySummary)
