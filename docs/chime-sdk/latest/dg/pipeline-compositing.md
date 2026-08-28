---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/pipeline-compositing.html
---

# Compositing audio and video into a single view in Amazon Chime SDK meetings
<a name="pipeline-compositing"></a>

The Amazon Chime SDK media pipelines support compositing of audio, webcam videos, and content-share video streams into a single view. You can then use live connector to send that single view to streaming services such as Amazon Interactive Video Service, Twitch, or YouTube Live. Composited video can also be captured to Amazon Simple Storage Service for storage or further consumption.

Compositing uses a default screen layout called `GridView`, which has the following behaviors.
+ When only webcam videos are active, `GridView` organizes the streams in the following grid pattern:
![A four-column, four-row grid showing the outlines of people.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/grid-no-content-share.png)

  The grid displays a maximum of 25 webcam streams, and it orders the tiles by when users turn on their cameras.
+ `GridView` provides two canvas orientations, `Landscape` and `Portrait`. Landscape, the default orientation, supports video resolutions of 1280x720 and 1920x1080 for FHD. Portrait supports resolutions of 720x1280 and 1080x1920 for FHD.
+ You can configure the order, position, total number, tile aspect ratio, corner radius, border color, border thickness and highlight color of the video tiles.
+ During a meeting, when someone shares their screen, the webcam video tiles transition dynamically to make room for the content share. You control those transitions, and the locations of the video tiles, by using one of the layout configurations described in the next section.

**About the layout configurations**
When someone starts a content share, you can choose how to composite the content share and webcam video streams by using one of the following layout configurations.
+ `ActiveSpeakerOnlyConfiguration` composites the content video full screen, with the active speaker’s webcam video overlaid in a corner. You can specify the corner.
+ `PresenterOnlyConfiguration` composites the content video full screen, with the presenter's webcam video overlaid in a corner. You can specify the corner.
+ `VerticalLayoutConfiguration` composites the content video with the webcam video in an adjacent vertical column. You can display the column to the right or left of the content share.
+ `HorizontalLayoutConfiguration` composites the content video with the webcam video in an adjacent horizontal row. You can display the row above or below the content share.

Composited layouts automatically transition between `GridView` and your chosen layout, based on whether content share is active or not.

The following topics explain how to use the global `GridView` settings and each configuration layout.

**Topics**
+ [Setting canvas orientation for compositing in Amazon Chime SDK meetings](canvas-orientation.md)
+ [Setting border and corner attributes for compositing in Amazon Chime SDK meetings](video-attribute.md)
+ [Using the layout configurations for compositing in Amazon Chime SDK meetings](compositing-layouts.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
