---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_EncoderConfiguration.html
---

# EncoderConfiguration
<a name="API_EncoderConfiguration"></a>

Settings for transcoding.

## Contents
<a name="API_EncoderConfiguration_Contents"></a>

 ** arn **   <a name="ivsrealtimeeapireference-Type-EncoderConfiguration-arn"></a>
ARN of the EncoderConfiguration resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:encoder-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** name **   <a name="ivsrealtimeeapireference-Type-EncoderConfiguration-name"></a>
Optional name to identify the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** tags **   <a name="ivsrealtimeeapireference-Type-EncoderConfiguration-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** video **   <a name="ivsrealtimeeapireference-Type-EncoderConfiguration-video"></a>
Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps
Type: [Video](API_Video.md) object
Required: No

## See Also
<a name="API_EncoderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/EncoderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/EncoderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/EncoderConfiguration)
