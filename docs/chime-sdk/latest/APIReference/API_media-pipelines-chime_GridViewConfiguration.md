---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GridViewConfiguration.html
---

# GridViewConfiguration
<a name="API_media-pipelines-chime_GridViewConfiguration"></a>

Specifies the type of grid layout.

## Contents
<a name="API_media-pipelines-chime_GridViewConfiguration_Contents"></a>

 ** ContentShareLayout **   <a name="chimesdk-Type-media-pipelines-chime_GridViewConfiguration-ContentShareLayout"></a>
Defines the layout of the video tiles when content sharing is enabled.
Type: String
Valid Values: `PresenterOnly | Horizontal | Vertical | ActiveSpeakerOnly`
Required: Yes

 ** ActiveSpeakerOnlyConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_GridViewConfiguration-ActiveSpeakerOnlyConfiguration"></a>
The configuration settings for an `ActiveSpeakerOnly` video tile.
Type: [ActiveSpeakerOnlyConfiguration](API_media-pipelines-chime_ActiveSpeakerOnlyConfiguration.md) object
Required: No

 ** CanvasOrientation **   <a name="chimesdk-Type-media-pipelines-chime_GridViewConfiguration-CanvasOrientation"></a>
The orientation setting, horizontal or vertical.
Type: String
Valid Values: `Landscape | Portrait`
Required: No

 ** HorizontalLayoutConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_GridViewConfiguration-HorizontalLayoutConfiguration"></a>
The configuration settings for a horizontal layout.
Type: [HorizontalLayoutConfiguration](API_media-pipelines-chime_HorizontalLayoutConfiguration.md) object
Required: No

 ** PresenterOnlyConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_GridViewConfiguration-PresenterOnlyConfiguration"></a>
Defines the configuration options for a presenter only video tile.
Type: [PresenterOnlyConfiguration](API_media-pipelines-chime_PresenterOnlyConfiguration.md) object
Required: No

 ** VerticalLayoutConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_GridViewConfiguration-VerticalLayoutConfiguration"></a>
The configuration settings for a vertical layout.
Type: [VerticalLayoutConfiguration](API_media-pipelines-chime_VerticalLayoutConfiguration.md) object
Required: No

 ** VideoAttribute **   <a name="chimesdk-Type-media-pipelines-chime_GridViewConfiguration-VideoAttribute"></a>
The attribute settings for the video tiles.
Type: [VideoAttribute](API_media-pipelines-chime_VideoAttribute.md) object
Required: No

## See Also
<a name="API_media-pipelines-chime_GridViewConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/GridViewConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/GridViewConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/GridViewConfiguration)
