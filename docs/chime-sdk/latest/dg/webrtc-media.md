---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/webrtc-media.html
---

# How Amazon Chime SDK meetings use WebRTC media
<a name="webrtc-media"></a>

The Amazon Chime SDK supports two types of WebRTC sessions, standard and high-definition. The following topics describe the media available in each type of session when using the Amazon Chime SDK client libraries for JavaScript, React, iOS, and Android.

**Topics**
+ [Audio](#webrtc-audio)
+ [Video](#video)
+ [Content share](#content-share)
+ [Data messages](#data-messages)

## Audio
<a name="webrtc-audio"></a>

Each Amazon Chime client sends one audio stream to the sessions and receives one audio stream from the session. Typically, microphones on local devices generate the audio. The audio received is a mix of the audio sent from the other session clients.

Both session types support sample rates up to 48kHz and up to 2 channels (stereo) encoded with bitrates up to 128kbps using the Opus codec. However, the audio streams sent and received vary by client library type:
+ The Amazon Chime SDK client libraries for JavaScript and React support sending and receiving mono and stereo audio at the highest sample rate supported by the device and browser, up to a maximum of 48kHz.
+ The Amazon Chime SDK client libraries for iOS and Android support sending mono audio up to 48kHz, and receiving stereo audio at 48kHz.

## Video
<a name="video"></a>

Each Amazon Chime client can send one video stream to the session and receive up to 25 video streams from the session. The video sent is typically sourced from the local device's webcam. Each client can select up to 25 video streams to receive, and change the selection at any time during the session.

Standard sessions support video resolutions up to 1280x720 at 30 frames per second encoded with bitrates up to 1500kbps using H.264, VP8, VP9, and AV1.

High-definition sessions support video resolutions up to 1920x1080 at 30 frames per second encoded with bitrates up to 2500kbps using H.264, VP8, VP9, and AV1.

The Amazon Chime SDK client libraries for JavaScript and React support sending video in simulcast at 15 frames per second, or with scalable video coding (SVC). SVC encodes a single video stream with three spatial layers and three temporal layers at 100%, 50%, and 25% of your target values. The service automatically selects the layer to send to each viewer based on the viewers' available bandwidth.

The Amazon Chime SDK client libraries for iOS and Android support sending up to 15 frames per second. However, the actual frame rate and resolution is automatically managed by the Amazon Chime SDK.

Video encoding and decoding uses hardware acceleration where available to improve performance.

 If a client sends video with a bitrate greater than the maximum allowed bitrate, the session first starts sending the client Receiver Estimated Maximum Bitrate messages via the Real-Time Control Protocol. If the client continues to send video with a bitrate greater than the maximum allowed bitrate, the session discards the incoming video stream packets.

## Content share
<a name="content-share"></a>

Up to two clients can share content to the session. A content share can include a video track, an audio track, or both. A common example of a content share is screen share, which uses screen capture as the source of the content. Another example is sharing prerecorded content with video and audio tracks.

Content audio is mixed into the audio stream sent by the session. Content audio supports sample rates up to 48kHz and up to 2 channels (stereo) encoded with bitrates up to 128kbps using the Opus codec.

Video content is sent to the session and forwarded to clients in a separate video stream. Standard sessions support content video up to 1920x1080 at 30 frames per second. High-definition sessions support content video up to 3840 x 2160 at 30 frames per second.

Screen capture for content sharing uses the resolution of the screen or window being captured, up to the maximum content resolution for the session type, and up to 30 frames per second. However, device and browser capabilities may limit those values.

The Amazon Chime SDK client libraries for JavaScript and React support content share from screen capture and other sources.

The Amazon Chime SDK client libraries for iOS and Android only support content share from screen capture.

## Data messages
<a name="data-messages"></a>

Data messages provide a way for a client to broadcast information to other clients in the session. For example, an application may use data messages to share emoji reactions during a session.

Each data message includes:
+ A topic, a string of up to 64 characters.
+ Up to 2 KB of data, including the topic.

A client sends a data message to the session, and the session sends the data message to all connected clients.

The session can optionally cache the data message for up to five minutes. If a client joins or reconnects to a session, the session will automatically send the client any cached data messages that have not been previously sent. The session cache stores a maximum of 1024 data messages.

A session supports up to 100 sent data messages per second. When using [live transcription](https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html), each client receives [transcription messages](https://docs.aws.amazon.com/chime-sdk/latest/dg/process-msgs.html) via data messages, which are counted towards the total sent messages per second.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
