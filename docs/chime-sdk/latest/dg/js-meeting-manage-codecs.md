---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/js-meeting-manage-codecs.html
---

# Configuring video codecs for Amazon Chime SDK meetings
<a name="js-meeting-manage-codecs"></a>

A client device uses a video codec to compress raw video before it is sent to the service, and to decompress received video before it's rendered.

When using the Amazon Chime SDK client library for JavaScript, you can specify your codec preferences for sending video.

The Amazon Chime SDK client libraries for iOS and Android automatically select the codec for you, based on the device’s capabilities.

## Setting video codec preferences
<a name="codec-list"></a>

In the Amazon Chime SDK client library for JavaScript, you can specify independent video codec preferences for webcam and content video.

Use the [ AudioVideoControllerFacade.setVideoCodecSendPreferences ](https://aws.github.io/amazon-chime-sdk-js/interfaces/audiovideocontrollerfacade.html#setvideocodecsendpreferences) function to set your codec preferences for sending webcam video. The link takes you to GitHub.

Your preferences are passed as an ordered array, with your most preferred codec first and your least preferred codec last.

When providing multiple codec preferences, the service automatically selects the most preferred codec that all session attendees can decode.

The following example shows how to set a video codec preference for VP9 with a fallback option of VP8:

```
// A meeting session has already been created and stored in `this.meetingSession`
this.meetingSession.audioVideo.setVideoCodecSendPreferences(
	[
		VideoCodecCapability.vp9(),
		VideoCodecCapability.vp8()
	]
);
```

The following scenarios apply to the preferences:
+ **Optimal ** – The client encodes video using the VP9 codec.
+ **Local Fallback** – If the client doesn't support VP9 encoding, it falls back to VP8 encoding. If the client does not support VP8 encoding, it falls back to any codec supported by the browser and the service.
+ **Remote Fallback** – If another client in the session does not have a VP9 decoder, this client falls back to VP8 encoding.
+ **Local Failure** – If the client does not support VP9 or VP8 encoding, it will not send video.

To set preferences for content sharing, use the [ ContentShareControllerFacade.setContentShareVideoCodecPreferences ](https://aws.github.io/amazon-chime-sdk-js/interfaces/contentsharecontrollerfacade.html#setcontentsharevideocodecpreferences) function to set your codec preferences for sending content video. This link takes you to GitHub.

 The following example sets a content video codec preference for VP9 with a fallback option of VP8.

```
// A meeting session has already been created and stored in `this.meetingSession`
    this.meetingSession.audioVideo.setContentShareVideoCodecPreferences(
	[
	VideoCodecCapability.vp9(),
	VideoCodecCapability.vp8()
	]
);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
