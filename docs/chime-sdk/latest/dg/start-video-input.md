---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/start-video-input.html
---

# Starting video input for the Amazon Chime SDK
<a name="start-video-input"></a>

The following example shows how to use the `VideoTransformDevice` object to start video input.

```
// assuming that meetingSession has already been created
await meetingSession.audioVideo.startVideoInput(videoTransformDevice);
meetingSession.audioVideo.start();
meetingSession.audioVideo.startLocalVideoTile();
```
