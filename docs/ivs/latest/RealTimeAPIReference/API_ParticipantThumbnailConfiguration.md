---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ParticipantThumbnailConfiguration.html
---

# ParticipantThumbnailConfiguration
<a name="API_ParticipantThumbnailConfiguration"></a>

An object representing a configuration of thumbnails for recorded video from an individual participant.

## Contents
<a name="API_ParticipantThumbnailConfiguration_Contents"></a>

 ** recordingMode **   <a name="ivsrealtimeeapireference-Type-ParticipantThumbnailConfiguration-recordingMode"></a>
Thumbnail recording mode. Default: `DISABLED`.
Type: String
Valid Values: `INTERVAL | DISABLED`
Required: No

 ** storage **   <a name="ivsrealtimeeapireference-Type-ParticipantThumbnailConfiguration-storage"></a>
Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails/high directory. `LATEST` saves the latest thumbnail in media/latest\_thumbnail/high/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds`. You can enable both `SEQUENTIAL` and `LATEST`. Default: `SEQUENTIAL`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `SEQUENTIAL | LATEST`
Required: No

 ** targetIntervalSeconds **   <a name="ivsrealtimeeapireference-Type-ParticipantThumbnailConfiguration-targetIntervalSeconds"></a>
The targeted thumbnail-generation interval in seconds. This is configurable only if `recordingMode` is `INTERVAL`. Default: 60.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

## See Also
<a name="API_ParticipantThumbnailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ParticipantThumbnailConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ParticipantThumbnailConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ParticipantThumbnailConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
