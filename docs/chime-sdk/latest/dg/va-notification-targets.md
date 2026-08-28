---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-notification-targets.html
---

# Understanding notifications for the Amazon Chime SDK
<a name="va-notification-targets"></a>

Voice analytics automatically sends events to a target when speaker search or voice tone analysis tasks start, while they run, and when they finish. You use notification targets to receive those events. We recommend using multiple notification targets if your workflow or application needs high availability.

Also, you must use an IAM role with the policies needed to access your notification targets. For more information, see [Using the call analytics resource access role for the Amazon Chime SDK](call-analytics-resource-access-role.md).

**Note**
For Amazon SQS and Amazon SNS, we do not support first-in-first-out queues. As a result, messages may arrive out of order. We recommend checking the timestamps to order messages as needed, and persisting messages in a data store such as Amazon DynamoDB. You can also use the Get APIs described in [Polling for task results for the Amazon Chime SDK](va-task-result-poll.md) to receive the latest results.

The following table lists the events and their corresponding detail types.

| Notification event | Detail type |
| --- | --- |
| Voice analytics metadata | `VoiceAnalyticsStatus` |
| Speaker search | `SpeakerSearchStatus` |
| Voice tone analysis | `VoiceToneAnalysisStatus` |

## Speaker search events
<a name="va-speaker-search-events"></a>

Speaker search events have the `SpeakerSearchStatus` detail type.

Amazon Chime SDK Voice Connectors send the following speaker search events:
+ Identification matches
+ Voice embedding generation

The events can have the following statuses:
+ `IdentificationSuccessful` – Successfully identified at least one matching voice profile ID with a high confidence score in the given voice profile domain.
+ `IdentificationFailure` – Failed to perform identification. Causes: the caller doesn't talk for at least 10 seconds, poor audio quality.
+ `IdentificationNoMatchesFound` – Unable to find a high confidence match in the given voice profile domain. The caller may be new, or their voice may have changed.
+ `VoiceprintGenerationSuccessful` – The system generated a voice embedding using 20 seconds of non-silent audio.
+ `VoiceprintGenerationFailure` – The system failed to generate a voice embedding. Causes: caller doesn't talk for at least 20 seconds, poor audio quality.

### Identification matches
<a name="va-id-matches"></a>

After the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartSpeakerSearchTask) API is called for a given `transactionId`, the Voice Connector service returns an identification match notification after 10 seconds of non-silent speech. The service returns the top 10 matches, along with a voice profile ID and confidence score ranging from [0, 1]. The higher the confidence score, the more likely the speaker from the call matches the voice profile ID. If the machine learning model finds no matches, the notification's `detailStatus` field contains `IdentificationNoMatchesFound`.

The following example shows notification for a successful match.

```
{
    "version": "0",
    "id": "{{12345678-1234-1234-1234-111122223333}}",
    "detail-type": "SpeakerSearchStatus",
    "service-type": "VoiceAnalytics",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "taskId": "{{uuid}}",
        "detailStatus": "{{IdentificationSuccessful}}",
        "speakerSearchDetails" : {
            "results": [
                {
                    "voiceProfileId": "{{vp-505e0992-82da-49eb-9d4a-4b34772b96b6}}",
                    "confidenceScore": "{{0.94567856}}",
                },
                {
                    "voiceProfileId": "{{vp-fba9cbfa-4b8d-4f10-9e41-9dfdd66545ab}}",
                    "confidenceScore": "{{0.82783350}}",
                },
                {
                    "voiceProfileId": "{{vp-746995fd-16dc-45b9-8965-89569d1cf787}}",
                    "confidenceScore": "{{0.77136436}}",
                }
            ]
        },
        "mediaInsightsPipelineId": "{{87654321-33ca-4dc6-9cdf-abcde6612345}}",
        "sourceArn": "arn:aws:chime:{{us-east-1}}:{{111122223333}}:media-pipeline/{{87654321-33ca-4dc6-9cdf-abcde6612345}}",
        "streamArn": "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/{{my-stream}}/{{0123456789012}}",
        "channelId": 0
    }
}
```

### Voice embedding generation
<a name="va-voice-print-generation"></a>

After an additional 10 seconds of non-silent speech, the Voice Connector sends a voice embedding generation notification to the notification targets. You can enroll new voice embeddings in a voice profile, or update a print already in a voice profile.

The following example shows the notification for a successful match, meaning you can update the associated voice profile.

```
{
    "version": "0",
    "id": "{{12345678-1234-1234-1234-111122223333}}",
    "detail-type": "SpeakerSearchStatus",
    "service-type": "VoiceAnalytics",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "taskId": "{{guid}}",
        "detailStatus": "{{VoiceprintGenerationSuccess}}",
        "mediaInsightsPipelineId": "{{87654321-33ca-4dc6-9cdf-abcde6612345}}",
        "sourceArn": "arn:aws:chime:{{us-east-1}}:{{111122223333}}:media-pipeline/{{87654321-33ca-4dc6-9cdf-abcde6612345}}",
        "streamArn": "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/{{my-stream}}/{{0123456789012}}",
        "channelId": 0
    }
}
```

## Voice tone analysis events
<a name="va-tone-status"></a>

Voice tone analysis events have the `VoiceToneAnalysisStatus` detail type. The analyses can return these statuses:
+ `VoiceToneAnalysisSuccessful` – Successfully analyzed the caller and agent voices into probabilities of sentiment—positive, negative, or neutral.
+ `VoiceToneAnalysisFailure` – Failed to perform tone analysis. This can happen if the caller hangs without talking for 10 seconds, or if the audio quality becomes too poor.
+ `VoiceToneAnalysisCompleted` – Successfully analyzed the user and agent voices into probabilities of sentiment for the entire call. This is the final event, sent when the voice tone analysis finishes.

The following example shows a typical voice tone analysis event.

```
{
  "detail-type": "VoiceToneAnalysisStatus",
  "service-type": "VoiceAnalytics",
  "source": "aws.chime",
  "account": "{{216539279014}}",
  "time": "{{2022-08-26T17:55:15.563441Z}}",
  "region": "{{us-east-1}}",
  "detail": {
    "taskId": "{{uuid}}",
    "detailStatus": "{{VoiceToneAnalysisSuccessful}}",
    "voiceToneAnalysisDetails": {
      "currentAverageVoiceTone": {
          "startTime": "{{2022-08-26T17:55:15.563Z}}",
          "endTime": "{{2022-08-26T17:55:45.720Z}}",
          "voiceToneLabel": "{{neutral}}",
          "voiceToneScore": {
            "neutral": "{{0.83}}",
            "positive": "{{0.13}}",
            "negative": "{{0.04}}"
          }
      },
      "overallAverageVoiceTone": {
          "startTime": "{{2022-08-26T16:23:13.344Z}}",
          "endTime": "{{2022-08-26T17:55:45.720Z}}",
          "voiceToneLabel": "{{positive}}",
          "voiceToneScore": {
            "neutral": "{{0.25}}",
            "positive": "{{0.65}}",
            "negative": "{{0.1}}"
          }
      }
    },
        "startFragmentNumber": "{{01234567890123456789}}",
        "mediaInsightsPipelineId": "{{87654321-33ca-4dc6-9cdf-abcde6612345}}",
        "sourceArn": "arn:aws:chime:{{us-east-1}}:{{111122223333}}:media-pipeline/{{87654321-33ca-4dc6-9cdf-abcde6612345}}",
        "streamArn": "arn:aws:kinesisvideo:{{us-east-1}}:{{111122223333}}:stream/{{my-stream}}/{{0123456789012}}",
        "channelId": 0
  },
  "version": "0",
  "id": "{{Id-f928dfe3-f44b-4965-8a17-612f9fb92d59}}"
}
```

## Post-call summary events
<a name="va-post-call-summary-events"></a>

Post call summary events are sent 5 minutes after the call has ended. These summaries provide an overview of the speaker search tasks that occurred throughout the call.

The following example shows a post call summary with the best voice profile match, confirmed speaker identity, and a list of the voice profiles created or updated through the `CreateVoiceProfile` and `UpdateVoiceProfile` API calls made during the call.

```
{
    "version": "0",
    "id": "{{12345678-1234-1234-1234-111122223333}}",
    "detail-type": "VoiceAnalyticsStatus",
    "service-type": "VoiceAnalytics",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "detailStatus": "PostCallVoiceAnalytics",
        "callId": "{{22e8dee8-bbd7-4f94-927b-2d0ebaeddc1c}}",
        "transactionId": "{{daaeb6bf-2fe2-4e51-984e-d0fbf2f09436}}",
        "voiceConnectorId": "{{abcdef1ghij2klmno3pqr4}}",
        "isCaller": {{true | false}},
        "speakerSearchResults": {
            "bestMatchedVoiceProfileId": "{{vp-04c25ba1-a059-4fd3-8495-4ac91b55e2bf}}",
            "customerValidatedCallerIdentity": "{{vp-04c25ba1-a059-4fd3-8495-4ac91b55e2bf}}",
            "createVoiceProfileTransactions": [
                {
                    "voiceProfileId": "{{vp-04c25ba1-a059-4fd3-8495-4ac91b55e2bf}}",
                    "requestTimestamp": "{{2022-12-14T18:38:38.796Z}}"
                },
                {
                    "voiceProfileId": "{{vp-04c25ba1-a059-4fd3-8495-4ac91b55e2bf}}",
                    "requestTimestamp": "{{2022-12-14T18:38:38.796Z}}",
                }
            ],
            "updateVoiceProfileTransactions": [
                {
                    "voiceProfileId": "{{vp-04c25ba1-a059-4fd3-8495-4ac91b55e2bf}}",
                    "requestTimestamp": "{{2022-12-14T18:38:38.796Z}}",
                },
                {
                    "voiceProfileId": "{{vp-04c25ba1-a059-4fd3-8495-4ac91b55e2bf}}",
                    "requestTimestamp": "{{2022-12-14T18:38:38.796Z}}",
                }
            ]
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
