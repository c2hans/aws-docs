---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/transcription-events.html
---

# Understanding Amazon Chime SDK live transcription events
<a name="transcription-events"></a>

The Amazon Chime SDK sends transcription lifecycle events, which you can use to trigger notifications and initiate downstream work flows. Some examples of using transcription events include:
+ Measuring the adoption of live transcription in Amazon Chime SDK meetings
+ Tracking language preferences

You can send events to Amazon EventBridge, Amazon Simple Notification Service, and Amazon Simple Queue Service. For more information, refer to [Events from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html) in the *Amazon EventBridge User Guide*.

## Amazon Chime SDK meeting transcription started
<a name="transcript-start"></a>

The Amazon Chime SDK sends this event when meeting transcription is started or the [TranscriptionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_TranscriptionConfiguration.html) is updated.

**Example: Event data**
The following is example data for this event.

```
{
    "version": "0",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "id": "{{12345678-1234-1234-1234-111122223333}}",
    "region": "us-east-1",
    "detail-type": "Chime Meeting State Change",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "eventType": "chime:TranscriptionStarted",
        "timestamp": {{12344566754}},
        "meetingId": "{{87654321-4321-4321-1234-111122223333}}",
        "externalMeetingId": "{{mymeeting}}",
        "mediaRegion": "us-west-1",
        "transcriptionRegion": "us-west-2",
        "[transcriptionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html)": "{{{...}}}"
    }
}
```

## Amazon Chime SDK meeting transcription stopped
<a name="transcript-stop"></a>

The Amazon Chime SDK sends this event when meeting transcription is stopped.

**Example: Event data**
The following is example data for this event.

```
{
    "version": "0",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "id": "{{12345678-1234-1234-1234-111122223333}}",
    "region": "us-east-1",
    "detail-type": "Chime Meeting State Change",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "eventType": "chime:TranscriptionStopped",
        "timestamp": {{12344566754}},
        "meetingId": "{{87654321-4321-4321-1234-111122223333}}",
        "externalMeetingId": "{{mymeeting}}",
        "mediaRegion": "us-west-1",
        "transcriptionRegion": "us-west-2",
        "[transcriptionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html)": "{{{...}}}"
    }
}
```

## Amazon Chime SDK meeting transcription interrupted
<a name="transcript-interrupted"></a>

The Amazon Chime SDK sends this event if meeting transcription is interrupted.

**Example: Event data**
The following is example data for this event.

```
{
    "version": "0",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "id": "{{12345678-1234-1234-1234-111122223333}}",
    "region": "us-east-1",
    "detail-type": "Chime Meeting State Change",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "eventType": "chime:TranscriptionInterrupted",
        "timestamp": {{12344566754}},
        "meetingId": "{{87654321-4321-4321-1234-111122223333}}",
        "externalMeetingId": "{{mymeeting}}",
        "message": "Internal server error",
        "mediaRegion": "us-west-1",
        "transcriptionRegion": "us-west-2",
        "[transcriptionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_TranscriptionConfiguration.html)": "{{{...}}}"
    }
}
```

## Amazon Chime SDK meeting transcription resumed
<a name="transcript-resumed"></a>

The Amazon Chime SDK sends this event if meeting transcription is resumed after an interruption.

**Example: Event data**
The following is example data for this event.

```
{
    "version": "0",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "id": "{{12345678-1234-1234-1234-111122223333}}",
    "region": "us-east-1",
    "detail-type": "Chime Meeting State Change",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "eventType": "chime:TranscriptionResumed",
        "timestamp": {{12344566754}},
        "meetingId": "{{87654321-4321-4321-1234-111122223333}}",
        "externalMeetingId": "{{mymeeting}}",
        "mediaRegion": "us-west-1",
        "transcriptionRegion": "us-west-2",
        "[transcriptionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_TranscriptionConfiguration.html)": "{{{...}}}"
    }
}
```

## Amazon Chime SDK meeting transcription failed
<a name="transcript-failed"></a>

The Amazon Chime SDK sends this event if meeting transcription failed to start, or failed to resume after an interruption.

**Example: Event data**
The following is example data for this event.

```
{
    "version": "0",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "id": "{{12345678-1234-1234-1234-111122223333}}",
    "region": "us-east-1",
    "detail-type": "Chime Meeting State Change",
    "time": "yyyy-mm-ddThh:mm:ssZ",
    "resources": []
    "detail": {
        "version": "0",
        "eventType": "chime:TranscriptionFailed",
        "timestamp": {{12344566754}},
        "meetingId": "{{87654321-4321-4321-1234-111122223333}}",
        "externalMeetingId": "{{mymeeting}}",
        "message": "Internal server error",
        "mediaRegion": "us-west-1",
        "transcriptionRegion": "us-west-2",
        "[transcriptionConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_TranscriptionConfiguration.html)": "{{{...}}}"
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
