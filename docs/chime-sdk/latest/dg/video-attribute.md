---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/video-attribute.html
---

# Setting border and corner attributes for compositing in Amazon Chime SDK meetings
<a name="video-attribute"></a>

As desired, you can use the `VideoAttribute` parameter to specify border and corner settings for your video tiles. You can specify colors, widths, and rounded corners. You can also specify a highlight color, and the border changes to that color when someone speaks.

Your attribute settings apply to all layouts, regardless of content sharing.

The following image shows a video tile with a border color and corner radius applied.

![Image of a screen share and video tile with a red border and rounded corners.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/compositing-speaker-border.png)

The following example shows how to use each attribute. In this case, video tiles have rounded corners with a five-pixel radius. The tiles have a green border, also five pixels wide. When the speaker talks, the `HighlightColor` attribute changes the border color to red.

```
{
   "CompositedVideo":{
      "Layout":"GridView",
      "Resolution":"FHD",
      "GridViewConfiguration":{
         "ContentShareLayout":"ActiveSpeakerOnly",
         "ActiveSpeakerOnlyConfiguration":{
            "ActiveSpeakerPosition":"TopRight"
         }
         "VideoAttribute": {
            "CornerRadius"   : 10,
            "BorderColor"    : "Green",
            "HighlightColor" : "Red",
            "BorderThickness": 5
          },
       }
   }
}
```

**VideoAttribute**
*Description* – Specifies the settings for video tile borders and rounded corners
*Allowed values* – `BorderColor` \| `BorderThickness` \| `CornerRadius` \| `HighlightColor`
*Required* – No

**VideoAttribute.BorderColor**
*Description* – Defines the border color for all video tiles
*Allowed values* – Color names, such as Red, Green, or Blue
*Required* – No

**VideoAttribute.BorderThickness**
*Description* – Defines the border thickness in pixels for all video tiles
*Type* – Integer
*Allowed values* – 1–20
*Required* – No

**VideoAttribute.CornerRadius**
*Description* – Defines the corner radius in pixels for all video tiles.
*Type* – Integer
*Allowed values* – 1–20
*Required* – No

**VideoAttribute.HighlightColor**
*Description* – Defines a border color that appears when a presenter or speaker talks
*Allowed values* – Color names, such as Red, Green, or Blue
*Required* – No
