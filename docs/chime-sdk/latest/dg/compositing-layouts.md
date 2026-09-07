---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/compositing-layouts.html
---

# Using the layout configurations for compositing in Amazon Chime SDK meetings
<a name="compositing-layouts"></a>

The following topics explain how to use the different configuration layouts. The layouts only take effect when someone starts a content share. Expand each section to learn more.

## ActiveSpeakerOnlyConfiguration
<a name="active-speaker-only"></a>

`ActiveSpeakerOnlyConfiguration` displays the content share and the active speaker’s video, meaning the person talking appears in the small video tile that overlays the content share stream.

The following image shows the configuration and the available locations for the speaker tile.

![Image showing a large video tile in the center of a window and a small tile in the upper-left.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/compositing-active-speaker-4x.png)

The following example shows how to implement the `ActiveSpeakerOnly` layout programmatically. In this case, the presenter tile appears in the upper-left corner.

```
{
   "CompositedVideo":{
      "Layout":"GridView",
      "Resolution":"FHD",
      "GridViewConfiguration":{
         "ContentShareLayout":"ActiveSpeakerOnly",
         "ActiveSpeakerOnlyConfiguration":{
            "ActiveSpeakerPosition":"TopLeft"
         }
      }
   }
}
```

**ActiveSpeakerOnlyConfiguration**
*Description* – The configuration settings for an `ActiveSpeakerOnly` video tile
*Type* – ActiveSpeakerOnlyConfiguration object
*Required* – No

**ActiveSpeakerOnlyConfiguration.ActiveSpeakerPosition**
*Description* – The position of the active speaker video tile
*Type* – String
*Valid values* – `TopLeft` \| `TopRight` \| `BottomLeft` \| `BottomRight`
*Required* – No
*Default* – `TopRight`

## PresenterOnlyConfiguration
<a name="presenter-only"></a>

`PresenterOnlyConfiguration` displays the content share and only the presenter’s video regardless of who talks. The following image shows the configuration.

![Image of four screens. Each screen has a share window in the middle and a video tile in each corner.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/compositing-presenter-only-4x.png)

The following example shows how to implement the layout programmatically with the presenter at top-right.

```
{
    "CompositedVideo": {
    "Layout": "GridView",
    "Resolution": "FHD",
     "GridViewConfiguration": {
         "ContentShareLayout": "PresenterOnly",
         "PresenterOnlyConfiguration": {
             "PresenterPosition": "TopRight"
             }
         }
     }
}
```

**PresenterOnlyConfiguration**
*Description* – The configuration settings for a `PresenterOnly` layout
*Type* – `PresenterOnlyConfiguration` object
*Required* – No

**PresenterOnlyConfiguration.PresenterPosition**
*Description* – The position of the presenter video tile
*Type* – String
*Valid values* – `TopLeft` \| `TopRight` \| `BottomLeft` \| `BottomRight`
*Required* – No
*Default* – `TopRight`

## HorizontalLayoutConfiguration
<a name="horizontal-layout"></a>

`HorizontalLayoutConfiguration` displays the content sharing and video streams horizontally. You can use the `TilePosition` setting to display the tiles above or below the content share stream. Presenters always appear on the left. Additional tiles appear in the order dictated by `JoinSequence`.

The following image shows the tiles below the content share stream.

![Image showing a large central tile and 4 smaller tiles in a line below.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/compositing-horizontal-bottom.png)

The following example shows how to implement a horizontal layout programmatically. In this case, the layout orders the tiles by `SpeakerSequence` and places them below the screen share. The layout allows a maximum of four tiles and applies a 16/9 aspect ratio.

```
{
   "CompositedVideo":{
      "Layout":"GridView",
      "Resolution":"FHD",
      "GridViewConfiguration":{
         "ContentShareLayout":"Horizontal",
         "HorizontalLayoutConfiguration":{
            "TileOrder":"SpeakerSequence",
            "TilePosition":"Bottom",
            "TileCount":4,
            "TileAspectRatio":"16/9"
         }
      }
   }
}
```

**HorizontalLayoutConfiguration**
*Description* – The configuration settings for a horizontal layout
*Type* – HorizontalLayoutConfiguration object
*Required* – No

**HorizontalLayoutConfiguration.TilePosition**
*Description* – Places tiles above or below a content share.
*Type* - String
*Valid values* – `Bottom` \| `Top`
*Required* – No
*Default* – Bottom

**HorizontalLayoutConfiguration.TileOrder**
*Description* – Orders tiles by when users join or when they speak
*Type* – String
*Valid values* – `JoinSequence` \| `SpeakerSequence`
*Required* – No
*Default* – JoinSequence

**HorizontalLayoutConfiguration.TileCount**
*Description* – Specifies the number of tiles that remain visible during a screen share
*Type* – Integer
*Valid values* – 1–10
*Required* – No
*Default* – 4

**HorizontalLayoutConfiguration.TileAspectRatio**
*Description* – Specifies the tiles' aspect ratio
*Type* – Integer
*Valid values* – *n***/***n*
*Required* – No
*Default* – 16/9, value applies to all tiles

## VerticalLayoutConfiguration
<a name="vertical-layout"></a>

`VerticalLayoutConfiguration` displays the content share and the four most recent videos stacked on the right. Presenters always appear on top. Other attendees appear in the order dictated by `TileOrder`.

![Image showing a large video tile in the center of a window and 4 smaller tiles stacked on the right.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/grid-vertical.png)

The following example shows how to implement the vertical layout programmatically. In this case, the layout orders tiles by JoinSequence and places them to the right of the screen share. The layout allows a maximum of four tiles and applies a 16/9 aspect ratio.

```
{
   "CompositedVideo":{
      "Layout": "GridView",
      "Resolution": "FHD",
      "GridViewConfiguration":{
         "ContentShareLayout": "Vertical",
         "VerticalLayoutConfiguration":{
            "TileOrder": "JoinSequence",
            "TilePosition": "Right",
            "TileCount": 4,
            "TileAspectRatio": "16/9"
         }
      }
   }
}
```

**VerticalLayoutConfiguration**
*Description* – The configuration settings for a vertical layout
*Type* – VerticalLayoutConfiguration object
*Required* – No

**VerticalLayoutConfiguration.TilePosition**
*Description* – Places tiles to the right or left of a content share.
*Type* – String
*Valid values* – `Bottom` \| `Top`
*Required* – No
*Default* – Bottom

**VerticalLayoutConfiguration.TileOrder**
*Description* – Orders tiles by when users join or when they speak
*Type* – String
*Valid values* – `JoinSequence` \| `SpeakerSequence`
*Required* – No
*Default* – JoinSequence

**VerticalLayoutConfiguration.TileCount**
*Description* – Specifies the number of tiles
*Type* – Integer
*Valid values* – 1–10
*Required* – No
*Default* – 4

**VerticalLayoutConfiguration.TileAspectRatio**
*Description* – Specifies the tiles' aspect ratio
*Type* – Integer
*Valid values* – *n***/***n*
*Required* – No
*Default* – 9/16, value applies to all tiles
