---
source_url: https://docs.aws.amazon.com/ivs/latest/BroadcastSWIntegAPIReference/structures-PreferencesDescription.html
---

# PreferencesDescription
<a name="structures-PreferencesDescription"></a>

Complex type specifying preferences configured on the client.

**Note:** The configuration that is returned takes into account user preferences. If the preference name starts with `maximum_`, it is considered a limit set by the user. However, user preferences may be overridden by the limitations of the service. For example, if the user sets `maximum_video_tracks` to 4 but the service only supports 3, the returned configuration contains only 3 video tracks.

## Contents
<a name="structures-PreferencesDescription-contente"></a>
+ **canvas\_height**
  + The height in pixels of the canvas being encoded.
  + Type: Integer
  + Required: Yes
+ **canvas\_width**
  + The width in pixels of the canvas being encoded.
  + Type: Integer
  + Required: Yes
+ **composition\_gpu\_index**
  + An index (zero-based) specifying which [GpuDescription](structures-GpuDescription.md) object the client is using for graphics composition and streaming.
  + Type: Integer
  + Required: No
+ **framerate**
  + Requested framerate.
  + Type: [Framerate](structures-Framerate.md) object
  + Required: Yes
+ **height**
  + Requested output resolution height in pixels. Must be less or equal to `canvas_height`.
  + Type: Integer
  + Required: Yes
+ **maximum\_streaming\_bandwidth**
  + Maximum bandwidth in kilobits per second that the user allocated for streaming. Default: null (no user preference).
  + Type: Integer
  + Required: No
+ **maximum\_resolution**
  + Maximum resolution of the highest quality video track. Default: null (no user preference).
  + Type: String
  + Valid Values: `SD` \| `HD` \| `FULL_HD`
  + Required: No
+ **maximum\_video\_tracks**
  + Maximum number of video tracks that the user allocates for multitrack video streaming. Default: null (no user preference).
  + Type: Integer
  + Required: No
+ **vod\_track\_audio**
  + Whether an audio track will be created for video on demand, separate from the live stream. Default: `false` (no separate audio track for video on demand).

    **Note:** This parameter is ignored if the stream key provided in the `authentication` field of the request does not start with `live_`.
  + Type: Boolean
  + Required: No
+ **width**
  + Requested output resolution width in pixels. Must be less or equal to `canvas_width`.
  + Type: Integer
  + Required: Yes
