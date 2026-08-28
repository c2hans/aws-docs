---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-events.html
---

# Understanding meeting event files for Amazon Chime SDK media capture pipelines
<a name="meeting-events"></a>

The meeting-events folder contains meeting events in the .txt format, and each event is a JSON object. Messages are visible with all configurations options. File names contain the <yyyy-mm-dd-hour-min-seconds-milleseconds> timestamp. This example shows the fields and data in a typical event file.

```
{
    "Timestamp": "{{string}}",
    "EventType": "AttendeeJoined | AttendeeLeft | AttendeeVideoJoined | AttendeeVideoLeft | ActiveSpeaker | CaptureStarted | CaptureEnded  | AudioTrackMute | AudioTrackUnmute",
    "EventParameters": {
        {{# ...}}
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
