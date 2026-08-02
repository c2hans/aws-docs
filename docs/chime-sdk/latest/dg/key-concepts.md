---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/key-concepts.html
---

# Understanding key concepts of the Amazon Chime SDK client library for JavaScript
<a name="key-concepts"></a>

To fully understand how to create and manage meetings and users, you need to understand these concepts:

 ** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Meeting.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Meeting.html) ** – A multi-party media session. Every meeting has a unique meeting identifier. You can create meetings in one of the supported AWS Regions. When you create a meeting, a list of Media URLs are returned. Those are a key part of the data needed to join the meeting, and you need to disseminate that data to all users trying to join the meeting.

 ** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Attendee.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_Attendee.html) ** – A user trying to join a multi-party media session. Every attendee has a unique identifier, an external user identifier that can be passed in to map the attendee to a user in the developer's system, plus a signed join token that grants them access to the meeting.

 ** [https://aws.github.io/amazon-chime-sdk-js/interfaces/meetingsession.html](https://aws.github.io/amazon-chime-sdk-js/interfaces/meetingsession.html) ** and [https://aws.github.io/amazon-chime-sdk-js/classes/defaultmeetingsession.html](https://aws.github.io/amazon-chime-sdk-js/classes/defaultmeetingsession.html) – The root object of the Amazon Chime SDK client library for JavaScript that represents each user’s session in a meeting. The web applications start by instantiating MeetingSession and configuring it with the right meeting and attendee information.

 ** [https://aws.github.io/amazon-chime-sdk-js/classes/meetingsessionconfiguration.html](https://aws.github.io/amazon-chime-sdk-js/classes/meetingsessionconfiguration.html) ** – Stores the meeting and attendee data needed to join a meeting session. That data is the response of the `CreateMeeting` and `CreateAttendee` API calls made by the server application. The server application passes this data to the web application, which uses it to instantiate the `MeetingSession`.

 ** [https://aws.github.io/amazon-chime-sdk-js/interfaces/devicecontroller.html](https://aws.github.io/amazon-chime-sdk-js/interfaces/devicecontroller.html) ** (DefaultDeviceController) – Used to enumerate the list of available audio and video devices on a user's system. You can also use the device controller during a meeting to switch active devices.

 ** [https://aws.github.io/amazon-chime-sdk-js/interfaces/audiovideofacade.html](https://aws.github.io/amazon-chime-sdk-js/interfaces/audiovideofacade.html) ** (DefaultAudioVideoFacade) – The key interface that powers a meeting. It provides the APIs that start, control, and end a meeting. It also provides APIs that listen for the key events that drive user experience changes, such as a roster of attendees, by tracking users joining or leaving, being muted or unmuted, actively speaking, or having poor connectivity. You can also use those APIs to bind the audio control HTML element to the meeting's audio output and play it through the selected audio output device.

 ** [https://aws.github.io/amazon-chime-sdk-js/interfaces/activespeakerdetectorfacade.html](https://aws.github.io/amazon-chime-sdk-js/interfaces/activespeakerdetectorfacade.html) ** (DefaultActiveSpeakerDetector) – The API that subscribes to active speaker events. Periodically returns a list of attendees ordered by their mic volume over time. You can override and tweak the active speaker policy as needed.

 ** [https://aws.github.io/amazon-chime-sdk-js/interfaces/contentsharecontroller.html](https://aws.github.io/amazon-chime-sdk-js/interfaces/contentsharecontroller.html) ** (DefaultContentShareController) – APIs that start-stop and pause-unpause content sharing. It also provides APIs to listen to lifecycle events to track content sharing status.

 ** [https://aws.github.io/amazon-chime-sdk-js/interfaces/logger.html](https://aws.github.io/amazon-chime-sdk-js/interfaces/logger.html) ** [https://aws.github.io/amazon-chime-sdk-js/interfaces/logger.html](https://aws.github.io/amazon-chime-sdk-js/interfaces/logger.html) – The interface used to leverage the console logs, or pass in a logger object to override the current logging implementation and get different levels of logs from the Amazon Chime SDK.
