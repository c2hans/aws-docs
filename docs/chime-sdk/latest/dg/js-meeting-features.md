---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/js-meeting-features.html
---

# Selecting meeting features using the Amazon Chime SDK
<a name="js-meeting-features"></a>

When you call the [CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html) API, you can specify features to make available to the clients that join the session. Note that some feature options incur additional billing.

The following features are available for sessions:
+ `Audio.EchoReduction` – Machine learning echo reduction.
+ `Video.MaxResolution` – Maximum webcam video resolution.
+ `Content.MaxResolution` – Maximum content sharing resolution..
+ `Attendees.MaxCount` – Mmaximum number of attendees.

**Topics**
+ [Using Audio.EchoReduction](#audio-echo-reduction)
+ [Using Video.MaxResolution](#video-max-resolution)
+ [Using Content.MaxResolution](#js-content-resolution)
+ [Using Attendees.MaxCount](#js-max-attendees)
+ [Using meeting features in a client app](#meeting-features-client-app)

## Using Audio.EchoReduction
<a name="audio-echo-reduction"></a>

Use `Audio.EchoReduction` to help keep sound from a user’s loudspeaker from circulating back into meeting.

Echo reduction is ideal for situations in which a user's loudspeaker will be the primary output device for meeting audio. For example, when multiple users are attending a meeting from the same device in a conference room, or when an individual remote attendee is not wearing headphones.

Echo reduction is available in the JavaScript and React client libraries. For more information, refer to the [documentation on GitHub](https://aws.github.io/amazon-chime-sdk-js/modules/amazonvoice_focus.html#what-is-echo-reduction). Additional costs apply, refer to the [Amazon Chime SDK Pricing page](https://aws.amazon.com/chime/chime-sdk/pricing/) for details.

## Using Video.MaxResolution
<a name="video-max-resolution"></a>

Use `Video.MaxResolution` to specify the maximum webcam video resolution for the meeting. The feature provides the following options:
+ `None`: no camera video allowed
+ `HD`: high-definition camera video (1280x720p)
+ `FHD`: full-high-definition camera video (1920x1080)

If FHD (1080p) Video is requested, a high-definition WebRTC session is created. Refer to the [Amazon Chime SDK Pricing page](https://aws.amazon.com/chime/chime-sdk/pricing/) for details.

If a client attemps to send webcam video above a specified maximum, the service rejects the video and sends the following error:

`Disabled video/content send capability, reason: Video resolution is above limit of current meeting feature selection.`

## Using Content.MaxResolution
<a name="js-content-resolution"></a>

Use `Content.MaxResolution` to specify the maximum content share resolution for the meeting. The feature provides the following options:
+ `None`: no content share allowed
+ `FHD`: full-high-definition content share (1920x1080)
+ `UHD`: ultra-high-definition content share (3840x2160)

If UHD (4K) content is requested, a high-definition WebRTC session is created.

If a client attems to send a content share beyond the maximum resolution, that resolution is scaled down to the specified maximum. You scale by applying `MediaTrackConstraints` to the content share track. The following examples shows how to scale a share track.

```
const constraint: MediaTrackConstraints = {
    width: { ideal: videoQualitySettings.videoWidth },
    height: { ideal: videoQualitySettings.videoHeight },
    frameRate: { ideal: videoQualitySettings.videoFrameRate },
  };
  this.context.logger.info(
    `Video track (content = ${isContentAttendee}) with constraint: ${JSON.stringify(
      constraint
    )}, trackSettings: ${JSON.stringify(trackSettings)}`
  );
  try {
    await mediaStreamTrack.applyConstraints(constraint);
  } catch (error) {
    this.context.logger.info(
      `Could not apply constraint for video track (content = ${isContentAttendee})`
    );
  }
```

The following table shows the expected behavior for content sharing.

| Content feature | Content share native resolution | Scaling | Content coding resolution |
| --- | --- | --- | --- |
| FHD | 1280x720 | No | 1280x720 |
| FHD | 1920x1080 | No | 1920x1080 |
| FHD | 3840x2160 | Yes | 1920x1080 |
| UHD | 1920x1080 | No | 1920x1080 |
| UHD | 3840x2160 | No | 3840x2160 |
| UHD | 4200x2400 | Yes | 3780x2160 |

## Using Attendees.MaxCount
<a name="js-max-attendees"></a>

Use `Attendee.MaxCount` to specify the maximum number of attendees allowed into a meeting. The upper limit of Attendee.MaxCount depends on the session type. For a standard session, you can select a maximum of 250 attendees. For a high-definition session, you *must* select a value of up to 25 attendees.

If you request FHD (1080p) video or UHD (4K) content, your session will be a high-definition session.

Attendee capacity costs apply for high-definition sessions. Refer to the [Amazon Chime SDK Pricing page](https://aws.amazon.com/chime/chime-sdk/pricing/) for details.

## Using meeting features in a client app
<a name="meeting-features-client-app"></a>

### Creating a meeting with specified features
<a name="js-create-meetings-sdk-namespace"></a>

To create a meeting, call the [CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html) API and specify the desired meeting features. The following example shows how to specify all the features.

```
// You must migrate to the Amazon Chime SDK Meetings namespace.
const chime = AWS.ChimeSDKMeetings({ region: "{{eu-central-1}}" });

// Create meeting
const meetingInfo = await chime.createMeeting({
    ...
    MeetingFeatures: {
      Audio: {
        EchoReduction: '{{AVAILABLE}}'
      },
      Video: {
        MaxResolution: '{{FHD}}'
      },
      Content: {
        MaxResolution: '{{UHD}}'
      },
      Attendee: {
        MaxCount: {{25}}
      },
    }
  }).promise();
```

### Using meeting features in a client
<a name="js-client-level"></a>

After you create a meeting with the desired features, you can pass in the `joinInfo` when you create the `MeetingSessionConfiguration` object. The meeting features are used at `meetingSession` creation to set webcam video resolution and bitrate, and the content share resolution and bitrate.

```
const configuration = new MeetingSessionConfiguration(this.joinInfo.Meeting, this.joinInfo.Attendee);

this.meetingSession = new DefaultMeetingSession(
    configuration,
    this.meetingLogger,
    this.deviceController,
    new DefaultEventController(configuration, this.meetingLogger, this.eventReporter)
);
```
