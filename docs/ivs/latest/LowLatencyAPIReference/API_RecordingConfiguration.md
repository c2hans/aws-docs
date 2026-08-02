---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RecordingConfiguration.html
---

# RecordingConfiguration
<a name="API_RecordingConfiguration"></a>

An object representing a configuration to record a channel stream.

## Contents
<a name="API_RecordingConfiguration_Contents"></a>

 ** arn **   <a name="ivs-Type-RecordingConfiguration-arn"></a>
Recording-configuration ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** destinationConfiguration **   <a name="ivs-Type-RecordingConfiguration-destinationConfiguration"></a>
A complex type that contains information about where recorded video will be stored.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object
Required: Yes

 ** state **   <a name="ivs-Type-RecordingConfiguration-state"></a>
Indicates the current state of the recording configuration. When the state is `ACTIVE`, the configuration is ready for recording a channel stream.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE`
Required: Yes

 ** name **   <a name="ivs-Type-RecordingConfiguration-name"></a>
Recording-configuration name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** recordingReconnectWindowSeconds **   <a name="ivs-Type-RecordingConfiguration-recordingReconnectWindowSeconds"></a>
If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

 ** renditionConfiguration **   <a name="ivs-Type-RecordingConfiguration-renditionConfiguration"></a>
Object that describes which renditions should be recorded for a stream.
Type: [RenditionConfiguration](API_RenditionConfiguration.md) object
Required: No

 ** tags **   <a name="ivs-Type-RecordingConfiguration-tags"></a>
Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** thumbnailConfiguration **   <a name="ivs-Type-RecordingConfiguration-thumbnailConfiguration"></a>
A complex type that allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session.
Type: [ThumbnailConfiguration](API_ThumbnailConfiguration.md) object
Required: No

## See Also
<a name="API_RecordingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/RecordingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/RecordingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/RecordingConfiguration)
