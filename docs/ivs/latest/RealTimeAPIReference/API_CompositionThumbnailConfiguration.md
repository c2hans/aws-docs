---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CompositionThumbnailConfiguration.html
---

# CompositionThumbnailConfiguration
<a name="API_CompositionThumbnailConfiguration"></a>

An object representing a configuration of thumbnails for recorded video for a [Composition](API_Composition.md).

## Contents
<a name="API_CompositionThumbnailConfiguration_Contents"></a>

 ** storage **   <a name="ivsrealtimeeapireference-Type-CompositionThumbnailConfiguration-storage"></a>
Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails/(width)x(height) directory, where (width) and (height) are the width and height of the thumbnail. `LATEST` saves the latest thumbnail in media/latest\_thumbnail/(width)x(height)/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds`. You can enable both `SEQUENTIAL` and `LATEST`. Default: `SEQUENTIAL`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `SEQUENTIAL | LATEST`
Required: No

 ** targetIntervalSeconds **   <a name="ivsrealtimeeapireference-Type-CompositionThumbnailConfiguration-targetIntervalSeconds"></a>
The targeted thumbnail-generation interval in seconds. Default: 60.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

## See Also
<a name="API_CompositionThumbnailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/CompositionThumbnailConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/CompositionThumbnailConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/CompositionThumbnailConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
