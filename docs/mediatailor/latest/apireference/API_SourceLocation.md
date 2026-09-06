---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SourceLocation.html
---

# SourceLocation
<a name="API_SourceLocation"></a>

A source location is a container for sources. For more information about source locations, see [Working with source locations](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html) in the *MediaTailor User Guide*.

## Contents
<a name="API_SourceLocation_Contents"></a>

 ** Arn **   <a name="mediatailor-Type-SourceLocation-Arn"></a>
The ARN of the SourceLocation.
Type: String
Required: Yes

 ** HttpConfiguration **   <a name="mediatailor-Type-SourceLocation-HttpConfiguration"></a>
The HTTP configuration for the source location.
Type: [HttpConfiguration](API_HttpConfiguration.md) object
Required: Yes

 ** SourceLocationName **   <a name="mediatailor-Type-SourceLocation-SourceLocationName"></a>
The name of the source location.
Type: String
Required: Yes

 ** AccessConfiguration **   <a name="mediatailor-Type-SourceLocation-AccessConfiguration"></a>
The access configuration for the source location.
Type: [AccessConfiguration](API_AccessConfiguration.md) object
Required: No

 ** CreationTime **   <a name="mediatailor-Type-SourceLocation-CreationTime"></a>
The timestamp that indicates when the source location was created.
Type: Timestamp
Required: No

 ** DefaultSegmentDeliveryConfiguration **   <a name="mediatailor-Type-SourceLocation-DefaultSegmentDeliveryConfiguration"></a>
The default segment delivery configuration.
Type: [DefaultSegmentDeliveryConfiguration](API_DefaultSegmentDeliveryConfiguration.md) object
Required: No

 ** LastModifiedTime **   <a name="mediatailor-Type-SourceLocation-LastModifiedTime"></a>
The timestamp that indicates when the source location was last modified.
Type: Timestamp
Required: No

 ** SegmentDeliveryConfigurations **   <a name="mediatailor-Type-SourceLocation-SegmentDeliveryConfigurations"></a>
The segment delivery configurations for the source location.
Type: Array of [SegmentDeliveryConfiguration](API_SegmentDeliveryConfiguration.md) objects
Required: No

 ** tags **   <a name="mediatailor-Type-SourceLocation-tags"></a>
The tags assigned to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## See Also
<a name="API_SourceLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/SourceLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/SourceLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/SourceLocation)
