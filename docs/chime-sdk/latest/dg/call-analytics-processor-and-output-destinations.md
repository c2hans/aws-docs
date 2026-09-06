---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics-processor-and-output-destinations.html
---

# Call analytics processor and output destinations for the Amazon Chime SDK
<a name="call-analytics-processor-and-output-destinations"></a>

 You can only specify unique elements once per media insights pipeline configuration. All processors and sinks must reside in the same AWS account, and you must create them in the same AWS Region as the endpoint that you call. For example, if you use the `us-east-1` endpoint for Amazon Chime SDK Media Pipelines, you can't pass a Kinesis Data Stream from the `us-west-2` region.

Expand each section for information about each destination.

## Amazon Transcribe Call Analytics processor destinations
<a name="amazon-transcribe-call-analytics-processor"></a>

Supported sinks: `KinesisDataStreamSink`.

You can't combine this processor with an Amazon Transcribe processor. For more information about Amazon Transcribe Call Analytics, refer to [Real-time call analytics](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics-streaming.html), in the* Amazon Transcribe Developer Guide*. If you enable [Post call analytics](https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html) by including `PostCallAnalyticsSettings` in the `AmazonTranscribeCallAnalyticsProcessorConfiguration` API call, you receive artifacts in the specified Amazon S3 location when the media insights pipeline stops and processing finishes.

**Note**
If you pause the pipeline for more than 35 seconds and then resume it, post-call artifacts are generated in separate files with different session IDs in the Amazon S3 bucket.

Post-call artifacts include an analytics JSON file and audio recording WAV or Opus file. The Amazon S3 bucket URL for redacted (if you enable content redaction) and non-redacted recording files is sent to the Kinesis Data Stream once for each Amazon Transcribe call analytics Post Call session as part of `onetimeMetadata` in the metadata section.

Call analytics with Amazon Transcribe call analytics takes audio data input from the Kinesis Video Stream.
+ Supported media encoding: PCM signed 16-bit little-endian audio.
+ Supported media sample rates: Between 8,000 Hz and 48,000 Hz.

`StreamConfiguration` input for an Amazon Transcribe Analytics process:
+ You must specify the `KinesisVideoStreamArn` for each stream.
+ (Optional) The KVS `FragmentNumber` starts a call analytics job with the chunk after a specified fragment. If not provided, it uses the latest chunk on the Kinesis video stream.
+ The `StreamChannelDefinition` defines who's talking. Amazon Transcribe call analytics requires two-channel audio. You must specify which speaker is on which channel when you call the [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API. For example, if your agent speaks first, you set the `ChannelId` to `0` to indicate the first channel, and `ParticipantRole` to `AGENT` to indicate that the agent is speaking.

**Note**
When you use a Voice Connector to create a `MediaInsightsPipeline` with an Amazon Transcribe call analytics processor, the Voice Connector account leg audio is `AGENT` and the PSTN leg audio is `CUSTOMER` for the `ParticipantRole`.
For Voice Connector SIPREC, we rely on the SIPREC metadata. In most cases, the stream label with the lowest lexicographic value is considered to be the `AGENT`.

The following example shows Kinesis Video Stream input for one dual-channel audio stream.

```
"StreamChannelDefinition" : {
    "NumberOfChannels" : 2
    "ChannelDefinitions": [
        {
            "ChannelId": 0,
            "ParticipantRole": "AGENT"
        },
        {
            "ChannelId": 1,
            "ParticipantRole": "CUSTOMER"
        }
    ]
}
```

 In contrast, the following example shows two mono inputs from two different Kinesis Video streams.

```
KVS-1:
    "StreamChannelDefinition" : {
        "NumberOfChannels"  : 1
        "ChannelDefinitions": [
            {
                "ChannelId": 0,
               "ParticipantRole": "AGENT"
            }
        ]
    }
KVS-2:
    "StreamChannelDefinition" : {
        "NumberOfChannels"  : 1
        "ChannelDefinitions": [
            {
                "ChannelId": 1,
               "ParticipantRole": "CUSTOMER"
            }
        ]
    }
```

## Amazon Transcribe call analytics output
<a name="amazon-transcribe-call-analytics-output"></a>

 Each Amazon Transcribe record contains an `UtteranceEvent` or a `CategoryEvent`, but not both. `CategoryEvents` have a `detail-type` of `TranscribeCallAnalyticsCategoryEvent`.

The following example shows one-time metadata output format for Amazon Transcribe.

```
{
    "time": "{{string}}", // ISO8601 format
    "service-type": "CallAnalytics",
    "detail-type": "CallAnalyticsMetadata",
    "mediaInsightsPipelineId": "{{string}}",
    "metadata": "{{string}}" // JSON encoded string of the metadata object
}

// metadata object
{
    "voiceConnectorId": "{{string}}",
    "callId": "{{string}}",
    "transactionId": "{{string}}",
    "fromNumber": "{{string}}",
    "toNumber": "{{string}}",
    "direction": "{{string}}",
    "oneTimeMetadata": "{{string}}" // JSON encoded string of oneTimeMetadata object
}

// onetimeMetadata object
{
    "inviteHeaders": "{{string}}", // JSON encoded string of SIP Invite headers key-value pair
    "siprecMetadata": "{{string}}", // siprec metadata in XML
    "siprecMetadataJson": "{{string}}", // siprec metadata in JSON (converted from above XML)

    // If PostcallSettings are enabled for Amazon Transcribe Call Analytics
    "s3RecordingUrl": "{{string}}",
    "s3RecordingUrlRedacted": "{{string}}"
}

// inviteHeaders object
{
    "{{string}}": "{{string}}"
}
```

 The following example shows the Amazon Transcribe Call Analytics output format.

```
{
    "time": "{{string}}", // ISO8601 format
    "service-type": "CallAnalytics",
    "detail-type": "TranscribeCallAnalytics",
    "mediaInsightsPipelineId": "{{string}}",
    "metadata": {
        "voiceConnectorId": "{{string}}",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "direction": "{{string}}"
    },
    "UtteranceEvent": {
        "UtteranceId": "{{string}}",
        "ParticipantRole": "{{string}}",
        "IsPartial": {{boolean}},
        "BeginOffsetMillis": {{number}},
        "EndOffsetMillis": {{number}},
        "Transcript": "{{string}}",
        "Sentiment": "{{string}}",
        "Items": [{
            "Content": "{{string}}",
            "Confidence": {{number}},
            "VocabularyFilterMatch": {{boolean}},
            "Stable": {{boolean}},
            "ItemType": "{{string}}",
            "BeginOffsetMillis": {{number}},
            "EndOffsetMillis": {{number}},
        }, ]
        "Entities": [{
            "Content": "{{string}}",
            "Confidence": {{number}},
            "Category": "{{string}}", // Only PII is supported currently
            "Type": "{{string}}",
            "BeginOffset": {{number}},
            "EndOffset": {{number}},
        }, ],
        "IssuesDetected": [{
            "CharacterOffsets": {
                "Begin": {{number}},
                "End": {{number}}
            }
        }]
    },
    "CategoryEvent": {
        "MatchedCategories": ["{{string}}"],
        "MatchedDetails": {
            "{{string}}": {
                "TimestampRanges": [{
                    "BeginOffsetMillis": {{number}},
                    "EndOffsetMillis": {{number}}
                }]
            }
        }
    }
}
```

## Amazon Chime SDK Voice Connector streaming updates metadata
<a name="cvc-stream-update-metadata"></a>

If the call analytics configuration is associated with an Amazon Chime SDK Voice Connector, the following Voice Connector Update payload will be sent when there is a [Voice Connector streaming update](https://docs.aws.amazon.com/chime-sdk/latest/ag/automating-chime-with-cloudwatch-events.html).

The following example shows an update metadata format for Amazon Transcribe processor and Transcribe Call Analytics processor.

```
{
    "time": "{{string}}", // ISO8601 format
    "service-type": "CallAnalytics",
    "detail-type": "CallAnalyticsMetadata",
    "callevent-type": "Update",
    "metadata": "{{string}}" // JSON encoded string of the metadata object
}

// metadata object
{
    "voiceConnectorId": "{{string}}",
    "callId": "{{string}}",
    "transactionId": "{{string}}",
    "fromNumber": "{{string}}",
    "toNumber": "{{string}}",
    "direction": "{{string}}",
    "oneTimeMetadata": "{{string}}" // JSON encoded string of oneTimeMetadata object
}

// onetimeMetadata object
{
    "sipHeaders": "{{string}}", // JSON encoded string of SIP Invite headers key-value pair
    "siprecMetadata": "{{string}}", // siprec metadata in XML
    "siprecMetadataJson": "{{string}}" // siprec metadata in JSON (converted from above XML)
}

// sipHeaders object
{
    "string": "{{string}}"
}
```

The following example shows an update metadata format for Call Analytics Amazon S3 Recording.

```
{
    "time": "{{string}}", // ISO8601 format
    "service-type": "CallAnalytics",
    "detail-type": "Recording",
    "callevent-type": "Update",
    "metadata": "string" // JSON encoded string of the metadata object
}

// metadata object
{
    "voiceConnectorId": "{{string}}",
    "callId": "{{string}}",
    "transactionId": "{{string}}",
    "fromNumber": "{{string}}",
    "toNumber": "{{string}}",
    "direction": "{{string}}",
    "oneTimeMetadata": "{{string}}" // JSON encoded in string of oneTimeMetadata object
}

// onetimeMetadata object
{
    "sipHeaders": "{{string}}", // JSON encoded string of SIP Invite headers key-value pair
    "siprecMetadata": "{{string}}", // siprec metadata in XML
    "siprecMetadataJson": "{{string}}" // siprec metadata in JSON (converted from above XML)
}

// sipHeaders object
{
    "{{string}}": "{{string}}"
}
```

## SIP call recording metadata
<a name="sip-update-metadata"></a>

The following examples show the metadata for recording a SIP call between two people, Alice and Bob. Both participants send and receive audio and video. For simplicity, the example only has snippets of SIP and SDP, and SRC records the streams of each participant to SRS without mixing.

```
INVITE sip:recorder@example.com SIP/2.0
   Via: SIP/2.0/TCP src.example.com;branch=z9hG4bKdf6b622b648d9
   From: <sip:2000@example.com>;tag=35e195d2-947d-4585-946f-09839247
   To: <sip:recorder@example.com>
   Call-ID: d253c800-b0d1ea39-4a7dd-3f0e20a
   Session-ID: ab30317f1a784dc48ff824d0d3715d86
    ;remote=00000000000000000000000000000000
   CSeq: 101 INVITE
   Max-Forwards: 70
   Require: siprec
   Accept: application/sdp, application/rs-metadata,
   application/rs-metadata-request
   Contact: <sip:2000@src.example.com>;+sip.src
   Content-Type: multipart/mixed;boundary={{boundary}}
   Content-Length: [length]

   Content-Type: application/SDP
   ...
   m=audio 49170 RTP/AVP 0
   a=rtpmap:0 PCMU/8000
   a=label:96
   a=sendonly
   ...
   m=video 49174 RTP/AVPF 96
   a=rtpmap:96 H.264/90000
   a=label:97
   a=sendonly
   ...
   m=audio 51372 RTP/AVP 0
   a=rtpmap:0 PCMU/8000
   a=label:98
   a=sendonly
   ...
   m=video 49176 RTP/AVPF 96
   a=rtpmap:96 H.264/90000
   a=label:99
   a=sendonly
   ....

Content-Type: application/rs-metadata
Content-Disposition: recording-session

<?xml version="1.0" encoding="UTF-8"?>
<recording xmlns='urn:ietf:params:xml:ns:recording:1'>
  <datamode>complete</datamode>
        <group group_id="7+OTCyoxTmqmqyA/1weDAg==">
                <associate-time>2010-12-16T23:41:07Z</associate-time>
                <!-- Standardized extension -->
                <call-center xmlns='urn:ietf:params:xml:ns:callcenter'>
                        <supervisor>sip:alice@atlanta.com</supervisor>
                </call-center>
                <mydata xmlns='http://example.com/my'>
                        <structure>structure!</structure>
                        <whatever>structure</whatever>
                </mydata>
        </group>
        <session session_id="hVpd7YQgRW2nD22h7q60JQ==">
                <sipSessionID>ab30317f1a784dc48ff824d0d3715d86;
                                      remote=47755a9de7794ba387653f2099600ef2</sipSessionID>
                <group-ref>7+OTCyoxTmqmqyA/1weDAg==
                </group-ref>
                <!-- Standardized extension -->
                <mydata xmlns='http://example.com/my'>
                        <structure>FOO!</structure>
                        <whatever>bar</whatever>
                </mydata>
        </session>
        <participant
              participant_id="srfBElmCRp2QB23b7Mpk0w==">
                <nameID aor="sip:alice@atlanta.com">
                        <naSRCme xml:lang="it">Alice</name>
                </nameID>
                <!-- Standardized extension -->
                <mydata xmlns='http://example.com/my'>
                        <structure>FOO!</structure>
                        <whatever>bar</whatever>
                </mydata>
        </participant>
        <participant
               participant_id="zSfPoSvdSDCmU3A3TRDxAw==">
                <nameID aor="sip:bob@biloxy.com">
                        <name xml:lang="it">Bob</name>
                </nameID>
                <!-- Standardized extension -->
                <mydata xmlns='http://example.com/my'>
                        <structure>FOO!</structure>
                        <whatever>bar</whatever>
                </mydata>
        </participant>
        <stream stream_id="UAAMm5GRQKSCMVvLyl4rFw=="
               session_id="hVpd7YQgRW2nD22h7q60JQ==">
                <label>96</label>
        </stream>
        <stream stream_id="i1Pz3to5hGk8fuXl+PbwCw=="
               session_id="hVpd7YQgRW2nD22h7q60JQ==">
                <label>97</label>
        </stream>
        <stream stream_id="8zc6e0lYTlWIINA6GR+3ag=="
               session_id="hVpd7YQgRW2nD22h7q60JQ==">
                <label>98</label>
        </stream>
        <stream stream_id="EiXGlc+4TruqqoDaNE76ag=="
               session_id="hVpd7YQgRW2nD22h7q60JQ==">
                <label>99</label>
        </stream>
        <sessionrecordingassoc session_id="hVpd7YQgRW2nD22h7q60JQ==">
            <associate-time>2010-12-16T23:41:07Z</associate-time>
        </sessionrecordingassoc>
        <participantsessionassoc
              participant_id="srfBElmCRp2QB23b7Mpk0w=="
              session_id="hVpd7YQgRW2nD22h7q60JQ==">
                <associate-time>2010-12-16T23:41:07Z</associate-time>
        </participantsessionassoc>
        <participantsessionassoc
               participant_id="zSfPoSvdSDCmU3A3TRDxAw=="
               session_id="hVpd7YQgRW2nD22h7q60JQ==">
                <associate-time>2010-12-16T23:41:07Z</associate-time>
        </participantsessionassoc>
        <participantstreamassoc
              participant_id="srfBElmCRp2QB23b7Mpk0w==">
                <send>i1Pz3to5hGk8fuXl+PbwCw==</send>
                <send>UAAMm5GRQKSCMVvLyl4rFw==</send>
                <recv>8zc6e0lYTlWIINA6GR+3ag==</recv>
                <recv>EiXGlc+4TruqqoDaNE76ag==</recv>
        </participantstreamassoc>
        <participantstreamassoc
               participant_id="zSfPoSvdSDCmU3A3TRDxAw==">
                <send>8zc6e0lYTlWIINA6GR+3ag==</send>
                <send>EiXGlc+4TruqqoDaNE76ag==</send>
                <recv>UAAMm5GRQKSCMVvLyl4rFw==</recv>
                <recv>i1Pz3to5hGk8fuXl+PbwCw==</recv>
        </participantstreamassoc>
</recording>
```

The following example shows the updated metadata when one call participant puts the other on hold. In this case, `participant_id srfBElmCRp2QB23b7Mpk0w==` only receives media streams and does not send any media, so the `send` XML element is omitted. In contrast, `participant_id zSfPoSvdSDCmU3A3TRDxAw==` sends media to, but does not receive media from, the other participant, so the `recv` XML element is omitted.

```
INVITE sip:recorder@example.com SIP/2.0
            Via: SIP/2.0/TCP src.example.com;branch=z9hG4bKdf6b622b648d9
      From: <sip:2000@example.com>;tag=35e195d2-947d-4585-946f-09839247
      To: <sip:recorder@example.com>
      Call-ID: d253c800-b0d1ea39-4a7dd-3f0e20a
      Session-ID: ab30317f1a784dc48ff824d0d3715d86
       ;remote=f81d4fae7dec11d0a76500a0c91e6bf6
      CSeq: 101 INVITE
      Max-Forwards: 70
      Require: siprec
      Accept: application/sdp, application/rs-metadata,
      application/rs-metadata-request
      Contact: <sip:2000@src.example.com>;+sip.src
      Content-Type: multipart/mixed;boundary=foobar
      Content-Length: [length]

      Content-Type: application/SDP
      ...
      m=audio 49170 RTP/AVP 0
      a=rtpmap:0 PCMU/8000
      a=label:96
      a=sendonly
      ...
      m=video 49174 RTP/AVPF 96
      a=rtpmap:96 H.264/90000
      a=label:97
      a=sendonly
      ...
      m=audio 51372 RTP/AVP 0
      a=rtpmap:0 PCMU/8000
      a=label:98
      a=sendonly
      ...
      m=video 49176 RTP/AVPF 96
      a=rtpmap:96 H.264/90000
      a=label:99
      a=sendonly
      ....

   Content-Type: application/rs-metadata
   Content-Disposition: recording-session

      <?xml version="1.0" encoding="UTF-8"?>
        <recording xmlns='urn:ietf:params:xml:ns:recording:1'>
          <datamode>partial</datamode>
            <participantstreamassoc
             participant_id="srfBElmCRp2QB23b7Mpk0w==">
             <recv>8zc6e0lYTlWIINA6GR+3ag==</recv>
             <recv>EiXGlc+4TruqqoDaNE76ag==</recv>
            </participantstreamassoc>
            <participantstreamassoc
             participant_id="zSfPoSvdSDCmU3A3TRDxAw==">
              <send>8zc6e0lYTlWIINA6GR+3ag==</send>
              <send>EiXGlc+4TruqqoDaNE76ag==</send>
             </participantstreamassoc>
           </recording>
```

The following example shows the metadata update when the call resumes. The payload now has the `send` and `recv` XML elements.

```
INVITE sip:recorder@example.com SIP/2.0
      Via: SIP/2.0/TCP src.example.com;branch=z9hG4bKdf6b622b648d9
      From: <sip:2000@example.com>;tag=35e195d2-947d-4585-946f-09839247
      To: <sip:recorder@example.com>
      Call-ID: d253c800-b0d1ea39-4a7dd-3f0e20a
      Session-ID: ab30317f1a784dc48ff824d0d3715d86
       ;remote=f81d4fae7dec11d0a76500a0c91e6bf6
      CSeq: 101 INVITE
      Max-Forwards: 70
      Require: siprec
      Accept: application/sdp, application/rs-metadata,
      application/rs-metadata-request
      Contact: <sip:2000@src.example.com>;+sip.src
      Content-Type: multipart/mixed;boundary=foobar
      Content-Length: [length]

      Content-Type: application/SDP
      ...
      m=audio 49170 RTP/AVP 0
      a=rtpmap:0 PCMU/8000
      a=label:96
      a=sendonly
      ...
      m=video 49174 RTP/AVPF 96
      a=rtpmap:96 H.264/90000
      a=label:97
      a=sendonly
      ...
      m=audio 51372 RTP/AVP 0
      a=rtpmap:0 PCMU/8000
      a=label:98
      a=sendonly
      ...
      m=video 49176 RTP/AVPF 96
      a=rtpmap:96 H.264/90000
      a=label:99
      a=sendonly
      ....

   Content-Type: application/rs-metadata
   Content-Disposition: recording-session

      <?xml version="1.0" encoding="UTF-8"?>
        <recording xmlns='urn:ietf:params:xml:ns:recording:1'>
          <datamode>partial</datamode>
            <participantstreamassoc
             participant_id="srfBElmCRp2QB23b7Mpk0w==">
             <send>i1Pz3to5hGk8fuXl+PbwCw==</send>
             <send>UAAMm5GRQKSCMVvLyl4rFw==</send>
             <recv>8zc6e0lYTlWIINA6GR+3ag==</recv>
             <recv>EiXGlc+4TruqqoDaNE76ag==</recv>
            </participantstreamassoc>
            <participantstreamassoc
             participant_id="zSfPoSvdSDCmU3A3TRDxAw==">
              <send>8zc6e0lYTlWIINA6GR+3ag==</send>
              <send>EiXGlc+4TruqqoDaNE76ag==</send>
              <recv>i1Pz3to5hGk8fuXl+PbwCw==</recv>
             <recv>UAAMm5GRQKSCMVvLyl4rFw==</recv>
             </participantstreamassoc>
           </recording>
```

## Amazon Transcribe processor destinations
<a name="amazon-transcribe-processors"></a>

Supported sinks: `KinesisDataStreamSink`.

You can't combine this processor with the Amazon Transcribe call analytics. For more information on the input to, and output of, Amazon Transcribe, refer to [ Transcribe streaming audio](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html) in the *Amazon Transcribe Developer Guide*.

Call analytics session with Amazon Transcribe takes audio data input from Kinesis Video Stream.
+ Supported MediaEncoding: PCM signed 16-bit little-endian audio.
+ Supported MediaSampleRate sample rates: Between 8,000 Hz and 48,000 Hz.

 `StreamConfiguration` input for Amazon Transcribe processors:
+ You must specify the `KinesisVideoStreamArn` for each stream.
+ (Optional) KVS `FragmentNumber` - Starts a call analytics job with the chunk after a specific fragment. If not provided, it will use the latest available chunk on the Kinesis Video Stream.
+ `StreamChannelDefinition` Amazon Transcribe currently supports audio with two channels. You have to specify the `NumberOfChannels` in the runtime `StreamChannelDefinition`. Additionally, you must pass the `ChannelId` if you send mono audio in two separate channels. In your transcript, channels are assigned the labels `ch_0` and `ch_1`. The following example shows the KVS input for one mono audio channel stream.

```
"StreamChannelDefinition" : {"
    NumberOfChannels" : 1
}
```

 The following example shows the KVS input for two mono audio inputs in two different streams.

```
KVS-1:
    "StreamChannelDefinition" : {
        "NumberOfChannels"  : 1
        "ChannelDefinitions": [
            {
                "ChannelId": 0
            }
        ]
    }
KVS-2:
    "StreamChannelDefinition" : {
        "NumberOfChannels"  : 1
        "ChannelDefinitions": [
            {
                "ChannelId": 1
            }
        ]
    }
```

**Note**
For the Voice Connector created `MediaInsightsPipeline` with an Amazon Transcribe processor, the Voice Connector account leg audio is assigned to `channel-0` and the PSTN leg audio to `channel-1`.
For Voice Connector SIPREC, we rely on the SIPREC metadata. In most cases, the stream label with the lowest lexicographic value is assigned to `channel-0`.
For the Amazon Transcribe and Amazon Transcribe call analytics processors, if you pass two Kinesis Video streams, and each stream contains a mono audio channel, we interleave both channels to a single audio stream before processing Transcribe or Transcribe call analytics data.

## Amazon Transcribe output
<a name="amazon-transcribe-output"></a>

The following example shows a one-time metadata output format for Amazon Transcribe.

```
{
    "time": "{{string}}", // ISO8601 format
    "service-type": "CallAnalytics",
    "detail-type": "CallAnalyticsMetadata",
    "mediaInsightsPipelineId": "{{string}}",
    "metadata": "{{string}}" // JSON encoded string of the metadata object
}

// metadata object
{
    "voiceConnectorId": "{{string}}",
    "callId": "{{string}}",
    "transactionId": "{{string}}",
    "fromNumber": "{{string}}",
    "toNumber": "{{string}}",
    "direction": "{{string}}",
    "oneTimeMetadata": "{{string}}" // JSON encoded string of oneTimeMetadata object
}

// onetimeMetadata object
{
    "inviteHeaders": "{{string}}", // JSON encoded string of SIP Invite headers key-value pair
    "siprecMetadata": "{{string}}", // siprec metadata in XML
    "siprecMetadataJson": "{{string}}" // siprec metadata in JSON (converted from above XML)
}

// inviteHeaders object
{
    "{{string}}": "{{string}}"
}
```

The following example shows the Amazon Transcribe output format.

```
{
    "time": "{{string}}", // ISO8601 format
    "service-type": "CallAnalytics",
    "detail-type": "Transcribe",
    "mediaInsightsPipelineId": "{{string}}",
    "metadata": {
        "voiceconnectorId": "{{string}}",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "direction": "{{string}}"
    }
    "TranscriptEvent": {
        "Transcript": {
            "Results": [{
                "Alternatives": [{
                    "Entities": [{
                        "Category": "{{string}}",
                        "Confidence": {{number}},
                        "Content": "{{string}}",
                        "EndTime": {{number}},
                        "StartTime": {{number}},
                        "Type": "{{string}}"
                    }],
                    "Items": [{
                        "Confidence": {{number}},
                        "Content": "{{string}}",
                        "EndTime": {{number}},
                        "Speaker": "{{string}}",
                        "Stable": {{boolean}},
                        "StartTime": {{number}},
                        "Type": "{{string}}",
                        "VocabularyFilterMatch": {{boolean}}
                    }],
                    "Transcript": "{{string}}"
                }],
                "ChannelId": "{{string}}",
                "EndTime": {{number}},
                "IsPartial": {{boolean}},
                "LanguageCode": "{{string}}",
                "LanguageIdentification": [{
                    "LanguageCode": "{{string}}",
                    "Score": {{number}}
                }],
                "ResultId": "{{string}}",
                "StartTime": {{number}}
            }]
        }
    }
}
```

## Voice analytics processor destinations
<a name="voice-analytics-processor"></a>

 Supported sinks: `KinesisDataStreamSink`, `SqsQueueSink`, `SnsTopicSink`, and `LambdaFunctionSink`.

 You can combine this processor with the Amazon Transcribe call analytics processor, the Amazon Transcribe processor, or call recording. You must use the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html) or [StartVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartVoiceToneAnalysisTask.html) APIs to invoke a voice analytics processor. For more information about using voice analytics, refer to [Using Amazon Chime SDK voice analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/voice-analytics.html).

## Using Kinesis Data Stream as a sink
<a name="kinesis-data-stream-destination"></a>

The Kinesis Data Stream (KDS) records generated by call analytics include the media pipeline ID, detail type, metadata, and processor-specific sections. For information about consuming data from a Kinesis Data Stream, refer to [Reading Data from Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html), in the *Amazon Kinesis Streams Developer guide*. To create a configuration with this sink, you must have `kinesis:DescribeStream` permission on the specified stream.

 **Metadata**

 The `metadata` section of the generated KDS records contains any key-value pairs specified in `CallAnalyticsRuntimeMetadata` during the [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API call. If a call analytics session was initiated by a Voice Connector, the metadata section is automatically populated with the following parameters:
+ `transactionId`
+ `fromNumber`
+ `toNumber`
+ `callId`
+ `voiceConnectorId`
+ `direction`

 In addition to the parameters shown above, the metadata section for Voice Connector initiated call analytics sessions will be populated with a `oneTimeMetadata` field that contains:
+ `inviteHeaders`
+ `siprecMetadata`

This is published to Kinesis Data Streams only once at the beginning of the session and has a `detail-type` of `CallAnalyticsMetadata`.

You can pass unique identifiers in the `MediaInsightsRuntimeMetadata` for each [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API call so that you can uniquely identify the source of each record delivered to your Kinesis Data Stream.

## Amazon S3 call recording
<a name="amazon-s3-call-recording"></a>

 Call analytics recording reads audio from a KVS stream, records it as an audio file, and uploads the file to the specified Amazon S3 Bucket. After recording call analytics also sends the call metadata along with the file location to KDS. If you enable a data warehouse, the call metadata (including SIPREC metadata if SIPREC was used) is delivered to the data warehouse in a set of Parquet tables that you can query.

Like any other call analytics processor, you need to first create a configuration for the pipeline. You can use the Amazon Chime SDK Console or the CLI to create the configuration. You then use the CLI to create the pipeline. For more information on using the console to create recording configurations, refer to [Creating call analytics configurations for the Amazon Chime SDK](creating-ca-configuration.md), earlier in this section. For more information about using the recording workflows, refer to [Understanding workflows for recording calls for the Amazon Chime SDK](recording-workflows.md), earlier in this section.

 **To use the CLI to create a configuration**

 Run the following command:

```
aws chime-sdk-media-pipeline create-media-insights-pipeline-configuration --cli-input-json file://configuration.json
```

 The following example shows a configuration JSON file with only recording enabled:

```
{
    "MediaInsightsPipelineConfigurationName": configuration_name,
    "ResourceAccessRoleArn": {{role_arn}},
    "Elements": [
        {
            "KinesisDataStreamSinkConfiguration": {
                "InsightsTarget": {{KDS_arn}} //Where recording live metadata will be delivered.
            },
            "Type": "KinesisDataStreamSink"
        },
        {
            "S3RecordingSinkConfiguration": {
                "Destination": "arn:aws:s3:::kvs-recording-testing",
                "RecordingFileFormat": {{file_format}} // Specify "Opus" or "WAV" as the recording file format.
            },
            "Type": "S3RecordingSink"
        }
    ]
}
```

Remember the following:
+ To enable call recording through Kinesis Video Streams, audio should be PCM signed 16-bit little-endian. The sample rate must be 8KHz.
+ Builders must set a long enough data retention period for the Kinesis Video Stream to ensure the fragments are retained and consumable by call analytics.
+ If you enable call recording, either by itself or in combination with other processors, you must supply two Kinesis Video Stream ARNs for recording. Call recording does not support a single stereo audio input.

## Amazon S3 call recording metadata output
<a name="s3-recording-metadata-output"></a>

The following example shows metadata output format for call analytics Amazon S3 recording.

```
{
    "time": "{{string}}", // ISO8601 format
    "service-type": "CallAnalytics",
    "detail-type": "Recording",
    "mediaInsightsPipelineId": "{{string}}",
    "s3MediaObjectConsoleUrl": "{{string}}",
    "recordingDurationSeconds": "{{number}}",
    "metadata": "{{string}}" // JSON encoded string of the metadata object
}

// metadata object
{
    "voiceConnectorId": "{{string}}",
    "callId": "{{string}}",
    "transactionId": "{{string}}",
    "fromNumber": "{{string}}",
    "toNumber": "{{string}}",
    "direction": "{{string}}",
    "startTime": "{{string}}", // ISO8601 format
    "endTime": "{{string}}", // ISO8601 format
    "oneTimeMetadata": "{{string}}" // JSON encoded in string of oneTimeMetadata object
}

// onetimeMetadata object
{
    "sipHeaders": "{{string}}", // JSON encoded string of SIP Invite headers key-value pair
    "siprecMetadata": "{{string}}", // siprec metadata in XML
    "siprecMetadataJson": "{{string}}" // siprec metadata in JSON (converted from above XML)
}

// sipHeaders object
{
    "{{string}}": "{{string}}"
}
```

## Enable voice enhancement
<a name="voice-enhancement-sink"></a>

To enable voice enhancement, include a `VoiceEnhancementSinkConfiguration` element in a [CreateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipelineConfiguration.html) API call.

This example shows a typical element.

```
{
  "Type":"VoiceEnhancementSink",
  "VoiceEnhancementSinkConfiguration": {
       "Disabled": {{Boolean}} (string) // FALSE ==> Voice Enhancement will be performed
}
```

To update a configuration, add the `VoiceEnhancementSinkConfiguration` element to a [UpdateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration.html) API call. When you do, the [GetMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaInsightsPipelineConfiguration.html) API includes the `VoiceEnhancementSinkConfiguration` element in the results.

This example request shows how to enable Voice Enhancement and Amazon S3 recording.

```
POST /media-insights-pipeline-configurations HTTP/1.1
Content-type: application/json

{
   "MediaInsightsPipelineConfigurationName":"{{media_insights_configuration_name}}",
   "ResourceAccessRoleArn":"arn:aws:iam::{{account_id}}:role/{{resource_access_role}}",
   "Elements":[
      {
         "Type":"S3RecordingSink",
         "S3RecordingSinkConfiguration":{
            "Destination":"arn:aws:s3:::{{input_bucket_path}}",
            "RecordingFileFormat":"{{Wav}}"
         }
      },
      {
         "Type":"VoiceEnhancementSink",
         "VoiceEnhancementSinkConfiguration": {
            "disabled":"{{false}}"
         }
      }
   ],
   "ClientRequestToken":"{{client_request_token}}"
}
```

**Note**
The `VoiceEnhancementSink` element always requires an `S3RecordingSink` element in a call analytics configuration.
