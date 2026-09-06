---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/stream-pipe-events.html
---

# Understanding Amazon Chime SDK media stream pipeline events
<a name="stream-pipe-events"></a>

Media stream pipelines send the following events. Expand each section to learn more.

## Amazon Chime Media Stream Pipeline Kinesis Video Stream Start
<a name="stream-pipe-kvs-start"></a>

The Amazon Chime SDK media pipeline sends this event when the media stream pipeline starts receiving audio from the meeting and streaming that audio to KVS. Empty `AttendeeId` and `ExternalUserId` fields indicate that the media pipeline sent mixed audio to the KVS stream.

```
{
    "version": "0",
    "id": "5ee6265a-0a40-104e-d8fd-a3b4bdd78483",
    "detail-type": "Chime Media Pipeline State Change",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{2021-07-28T20:20:49Z}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "eventType": "chime:MediaPipelineKinesisVideoStreamStart",
        "timestamp": {{1627503649251}},
        "meetingId": "{{1e6bf4f5-f4b5-4917-b8c9-bda45c340706}}",
        "externalMeetingId": "{{Meeting_Id}}",
        "mediaPipelineId": "{{e40ee45e-2ed1-408e-9156-f52b8208a491}}",
        "mediaRegion": "{{ap-southeast-1}}",

        "attendeeId": "{{Attendee_Id}}",
        "externalUserId": "{{External_User_Id}}",

        "kinesisVideoStreamArn": "arn:aws:kinesisvideo:{{us-east-1}}:{{123456}}:stream/Chime*",
        "startFragmentNumber": "{{1234567899444}}",
        "startTime": "{{yyyy-mm-ddThh:mm:ssZ}}"

    }
}
```

## Amazon Chime Media Stream Pipeline Kinesis Video Stream End
<a name="stream-pipe-kvs-stop"></a>

The media pipeline sends this event to Event Bridge when streaming to KVS ends.

```
{
    "version": "0",
    "id": "5ee6265a-0a40-104e-d8fd-a3b4bdd78483",
    "detail-type": "Chime Media Pipeline State Change",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{2021-07-28T20:20:49Z}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "eventType": "chime:MediaPipelineKinesisVideoStreamEnd",
        "timestamp": {{1627503649251}},
        "meetingId": "{{1e6bf4f5-f4b5-4917-b8c9-bda45c340706}}",
        "externalMeetingId": "{{Meeting_Id}}",
        "mediaPipelineId": "{{e40ee45e-2ed1-408e-9156-f52b8208a491}}",
        "mediaRegion": "{{ap-southeast-1}}",

        "attendeeId": "{{Attendee_Id}}",
        "externalUserId": "{{External_User_Id}}",

        "kinesisVideoStreamArn": "arn:aws:kinesisvideo:{{us-east-1}}:{{123456}}:stream/Chime*",
        "startFragmentNumber": "{{1234567899444}}",
        "startTime": "{{yyyy-mm-ddThh:mm:ssZ}}",
        "endTime": "{{yyyy-mm-ddThh:mm:ssZ}}",
        "endFragmentNumber": "{{1234567899555}}"
    }
}
```
