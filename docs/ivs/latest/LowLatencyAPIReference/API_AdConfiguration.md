---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_AdConfiguration.html
---

# AdConfiguration
<a name="API_AdConfiguration"></a>

Object specifying a configuration for a server-side advertising insertion (which can be triggered with the [InsertAdBreak](API_InsertAdBreak.md) operation).

## Contents
<a name="API_AdConfiguration_Contents"></a>

 ** arn **   <a name="ivs-Type-AdConfiguration-arn"></a>
Ad configuration ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:ad-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** mediaTailorPlaybackConfigurations **   <a name="ivs-Type-AdConfiguration-mediaTailorPlaybackConfigurations"></a>
List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see [Generate and Sign IVS Playback Tokens](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html).
Type: Array of [MediaTailorPlaybackConfiguration](API_MediaTailorPlaybackConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: Yes

 ** name **   <a name="ivs-Type-AdConfiguration-name"></a>
Ad configuration name. Defaults to “”.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** postRollConfiguration **   <a name="ivs-Type-AdConfiguration-postRollConfiguration"></a>
Configuration for the post-roll ad break to use for this ad configuration.
Type: [PostRollConfiguration](API_PostRollConfiguration.md) object
Required: No

 ** tags **   <a name="ivs-Type-AdConfiguration-tags"></a>
Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## See Also
<a name="API_AdConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/AdConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/AdConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/AdConfiguration)
