---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/canvas-orientation.html
---

# Setting canvas orientation for compositing in Amazon Chime SDK meetings
<a name="canvas-orientation"></a>

In compositing, the *canvas* contains all your video streams. You can specify a `Landscape` or `Portrait` orientation for the canvas. Landscape provides a 16:9 aspect ratio. Portrait provides a 9:16 aspect ratio.

The following image shows the portrait orientation.

![Image showing two video tiles in a portrait (vertical) window.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/compositing-portrait-with-tile.png)

The following example shows how to implement a portrait canvas with the video tile in the upper-right corner. In this example, the active speaker appears in the tile. For more information, see [ActiveSpeakerOnlyConfiguration](compositing-layouts.md#active-speaker-only)

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
      },
      "CanvasOrientation": "Portrait"
   }
}
```

The following image shows the landscape orientation.

![Image showing two video tiles in a landscape (horizontal) window.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/compositing-landscape-with-tile.png)

**CanvasOrientation**
*Description* – The orientation setting, Landscape or Portrait.
*Allowed values* – `Landscape` \| `Portrait`
*Required* – No
*Default* – Landscape
