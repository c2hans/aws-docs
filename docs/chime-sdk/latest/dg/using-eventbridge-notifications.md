---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/using-eventbridge-notifications.html
---

# Using Amazon EventBridge notifications for the Amazon Chime SDK
<a name="using-eventbridge-notifications"></a>

Amazon Chime SDK Call Analytics supports sending events to the default EventBridge bus when the state of the media insights pipeline changes, or when call analytics real-time alert conditions are met. For the media insights pipeline error status updates, we recommend that you configure an EventBridge target to notify you if your resources fail asynchronously. Call analytics notifications have a aws.chime source and various detail types, which are shared in the following sections. For more information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

**Topics**
+ [Status updates](#status-updates)
+ [Real-time alerts](#realtime-alerts)

## Status updates
<a name="status-updates"></a>

 Media insights pipelines send EventBridge notifications as a call analytics session progresses and either ends successfully or encounters errors. You receive an EventBridge notification with the “Media Insights State Change" detail type when:
+ The status of a media insights pipeline changes.
+ The status of a media insights pipeline element changes.
+ Any pipeline element is stopped.
+ Any pipeline element fails.

The detail section always includes the following fields:
+ `version`
+ `mediaInsightsPipelineArn`
+ `eventType`

The detail section also includes a `mediaInsightsPipelineElementStatuses` field if the media insights pipeline contains multiple elements, such as analytics processors and data sinks. This field indicates the statuses of each element in the pipeline. The possible status for each pipeline element could be:
+ `NotStarted`
+ `InProgress`
+ `Stopped`
+ `Failed`

 The detail section also includes any key-value pairs specified in `MediaInsightsRuntimeMetadata` during the [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API call. If a call analytics session was initiated by a Voice Connector, the metadata section is populated with the following parameters automatically:
+ `transactionId`
+ `fromNumber`
+ `toNumber`
+ `callId`
+ `voiceConnectorId`
+ `direction`

 The following event types may appear whenever a media insights pipeline contains a single element. Expand each section to learn more.

### Amazon Chime SDK media insights in progress
<a name="insights-in-progress"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsInProgress",
        "version": "0",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### Amazon Chime SDK media insights paused
<a name="insights-paused"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsPaused",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### Amazon Chime SDK media insights stopped
<a name="insights-stoppped"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsStopped",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### Amazon Chime SDK media insights temporary failure
<a name="insights-temp-failure"></a>

Indicates that the service encountered a temporary failure and will attempt to retry. No action is required from you.

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsTemporaryFailure",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### Amazon Chime SDK media insights permanent failure
<a name="insights-perm-failure"></a>

Indicates a failure that requires action from you. Use the `failureReason` to troubleshoot the problem. Typical failures could include the following:
+ Insufficient permissions on the resource access role
+ Missing or deleted resources
+ Throttling from an AWS service that call analytics invokes on your behalf, such as Amazon Transcribe or Amazon Kinesis.
+ Incompatible media formats on KVS streams

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsPermanentFailure",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}",
        "failureReason": "{{string}}"
    }
}
```

**Note**
The `failureReason` field is optional. For example, a typical reason could be `Access denied when assuming resource access role`.

The following event types may appear whenever a media insights pipeline is created, or the creation attempt fails, for a call analytics session initiated by an Amazon Chime SDK Voice Connector. Expand each section to learn more.

### Amazon Chime SDK media insights created
<a name="vc-pipeline-created"></a>

This example shows a typical success event.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail":
    {
        "version": "0",
        "mediaInsightsPipelineConfigurationArn": "{{string}}",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsCreated",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}",
    }
}
```

### Amazon Chime SDK media insights create failed
<a name="vc-pipeline-failed"></a>

This example shows a typical failure event.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": []
    "detail":
    {
        "version": "0",
        "mediaInsightsPipelineConfigurationArn": "{{string}}",
        "eventType": "chime:MediaInsightsCreateFailed",
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}",
        "failureOrigin": "Voice Connector",
        "httpStatusCode": "{{string}}",
        "failureReason": "{{string}}"
    }
}
```

The following event types may appear when a media insights pipeline contains multiple elements. The example notifications are for `AmazonTranscribeProcessor` combined with `S3RecordingSink`. Expand each section to learn more.

### AmazonTranscribeProcessor is in progress and S3RecordingSink has not started
<a name="processor-running-sink-not-started"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsInProgress",
        "mediaInsightsPipelineElementStatuses": [
            {
                "type": "AmazonTranscribeProcessor",
                "status": "InProgress",
                "updatedOn": 1686184070655
            },
            {
                "type": "S3RecordingSink",
                "status": "NotStarted",
                "updatedOn": 1686184070655
            }
        ]
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### AmazonTranscribeProcessor has succeeded and S3RecordingSink is in progress
<a name="processor-success-sink-in-progress"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsInProgress",
        "mediaInsightsPipelineElementStatuses": [
            {
                "type": "AmazonTranscribeProcessor",
                "status": "Stopped",
                "updatedOn": 1686184070655
            },
            {
                "type": "S3RecordingSink",
                "status": "InProgress",
                "updatedOn": 1686184070655
            }
        ]
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### AmazonTranscribeProcessor has failed and S3RecordingSink is in progress
<a name="processor-fail-sink-in-process"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsInProgress",
        "mediaInsightsPipelineElementStatuses": [
            {
                "type": "AmazonTranscribeProcessor",
                "status": "Failed",
                "updatedOn": 1686184070655
            },
            {
                "type": "S3RecordingSink",
                "status": "InProgress",
                "updatedOn": 1686184070655
            }
        ]
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### AmazonTranscribeProcessor has failed and S3RecordingSink has succeeded
<a name="processor-fail-record-finish"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsPermanentFailure",
        "mediaInsightsPipelineElementStatuses": [
            {
                "type": "AmazonTranscribeProcessor",
                "status": "Failed",
                "updatedOn": 1686184070655
            },
            {
                "type": "S3RecordingSink",
                "status": "Stopped",
                "updatedOn": 1686184070655
            }
        ]
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}",
        "failureReason": "{{string}}"
    }
}
```

### AmazonTranscribeProcessor has succeeded and S3RecordingSink has failed
<a name="processor-success-recording-fail"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsPermanentFailure",
        "mediaInsightsPipelineElementStatuses": [
            {
                "type": "AmazonTranscribeProcessor",
                "status": "Stopped",
                "updatedOn": 1686184070655
            },
            {
                "type": "S3RecordingSink",
                "status": "Failed",
                "updatedOn": 1686184070655
            }
        ]
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}",
        "failureReason": "{{string}}"
    }
}
```

### AmazonTranscribeProcessor is paused and S3RecordingSink has not started
<a name="processor-pause-recording-no-start"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsPaused",
        "mediaInsightsPipelineElementStatuses": [
            {
                "type": "AmazonTranscribeProcessor",
                "status": "Paused",
                "updatedOn": 1686184070655
            },
            {
                "type": "S3RecordingSink",
                "status": "NotStarted",
                "updatedOn": 1686184070655
            }
        ]
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### AmazonTranscribeProcessor has temporarily failed and S3RecordingSink has not started
<a name="processor-temp-fail-recording-no-start"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsTemporaryFailure",
        "mediaInsightsPipelineElementStatuses": [
            {
                "type": "AmazonTranscribeProcessor",
                "status": "TemporarilyFailed",
                "updatedOn": 1686184070655
            },
            {
                "type": "S3RecordingSink",
                "status": "NotStarted",
                "updatedOn": 1686184070655
            }
        ]
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### AmazonTranscribeProcessor and S3RecordingSink succeeded
<a name="processor-sink-success"></a>

This example shows a typical event structure.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights State Change",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{string}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail": {
        "version": "0",
        "mediaInsightsPipelineArn": "{{string}}",
        "eventType": "chime:MediaInsightsStopped",
        "mediaInsightsPipelineElementStatuses": [
            {
                "type": "AmazonTranscribeProcessor",
                "status": "Stopped",
                "updatedOn": 1686184070655
            },
            {
                "type": "S3RecordingSink",
                "status": "Stopped",
                "updatedOn": 1686184070655
            }
        ]
        "callId": "{{string}}",
        "transactionId": "{{string}}",
        "fromNumber": "{{string}}",
        "toNumber": "{{string}}",
        "voiceConnectorId": "{{string}}",
        "direction": "{{string}}"
    }
}
```

### S3RecordingSink succeeded and VoiceEnhancement in progress
<a name="voice-enhancement-sink-inprogress"></a>

This example shows a typical event structure.

```
{
  "version": "0",
  "id": "{{string}}",
  "detail-type": "Media Insights State Change",
  "source": "aws.chime",
  "account": {{number}},
  "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
  "region": "{{string}}",
  "detail": {
    "mediaInsightsPipelineArn": "{{string}}",
    "eventType": "chime:MediaInsightsInProgress",
    "version": "0",
    "mediaInsightsPipelineElementStatuses": [
      {
        "type": "VoiceEnhancementSink",
        "status": "InProgress",
        "updatedOn": 1686184070655
      },
      {
        "type": "S3RecordingSink",
        "status": "Stopped",
        "updatedOn": 1686184070655
      }
    ]
  }
}
```

### S3RecordingSink succeeded and VoiceEnhancement failed due to calls longer than 30 minutes
<a name="voice-enhancement-sink-fail-longerthan30minutes"></a>

This example shows a typical event structure.

```
{
  "version": "0",
  "id": "{{string}}",
  "detail-type": "Media Insights State Change",
  "source": "aws.chime",
  "account": {{number}},
  "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
  "region": "{{string}}",
  "detail": {
    "mediaInsightsPipelineArn": "{{string}}",
    "eventType": "chime:MediaInsightsStopped",
    "version": "0",
    "mediaInsightsPipelineElementStatuses": [
      {
        "type": "VoiceEnhancement",
        "status": "NotSupported",
        "updatedOn": 1686184070655,
        "statusDetail": "Unsupported recording length"
      },
      {
        "type": "S3RecordingSink",
        "status": "Stopped",
        "updatedOn": 1686184070655
      }
    ]
  }
}
```

### S3RecordingSink succeeded and VoiceEnhancement failed due to calls less than 30 minutes
<a name="voice-enhancement-sink-fail-lessthan30minutes"></a>

This example shows a typical event structure.

```
{
  "version": "0",
  "id": "{{string}}",
  "detail-type": "Media Insights State Change",
  "source": "aws.chime",
  "account": {{number}},
  "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
  "region": "{{string}}",
  "detail": {
    "mediaInsightsPipelineArn": "{{string}}",
    "eventType": "chime:MediaInsightsPermanentFailure",
    "version": "0",
    "mediaInsightsPipelineElementStatuses": [
      {
        "type": "VoiceEnhancement",
        "status": "Failed",
        "updatedOn": 1686184070655
      },
      {
        "type": "S3RecordingSink",
        "status": "Stopped",
        "updatedOn": 1686184070655
      }
    ]
  }
}
```

## Real-time alerts
<a name="realtime-alerts"></a>

**Note**
Only Amazon Transcribe and Amazon Transcribe Call Analytics processors support real-time alerts.

 Amazon Chime SDK call analytics allows developers to set up rules for sending real-time alerts through a processor during an analytics session. Alerts are sent to Amazon EventBridge with the detail type `Media Insights Rules Matched`. EventBridge supports integration with downstream services such as Lambda, Amazon SQS, and Amazon SNS to trigger notifications for the end user or initiate other custom business logic.

 Real-time alerts are set up as a part of the `RealTimeAlertConfiguration` field for the `MediaInsightsPipelineConfiguration`. You can use the Amazon Chime SDK console to configure the field, or you can call the [CreateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipelineConfiguration.html) or [UpdateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration.html) APIs.

 This example shows how to create or update a real-time alert configuration through the API.

```
{
    "MediaInsightsPipelineConfigurationName": "config_name",
    "ResourceAccessRoleArn": "arn:aws:iam::{{account_id}}:role/{{role_name"}},
    "RealTimeAlertConfiguration": {
        "Disabled": false,
        "Rules": [{
                "Type": "KeywordMatch",
                "KeywordMatchConfiguration": {
                    "RuleName": "{{rule_name_1}}",
                    "Keywords": [
                        "{{hello}}",
                        "{{thank you}}"
                    ],
                    "Negate": false
                }
            },
            {
                "Type": "Sentiment",
                "RuleName": "{{rule_name_2}}",
                "SentimentType": "NEGATIVE",
                "TimePeriod": 60
            },
            {
                "Type": "IssueDetection",
                "RuleName": "{{rule_name_3}}"
            }
        ]
    },
    "Elements": [{
            "Type": "AmazonTranscribeCallAnalyticsProcessor",
            "AmazonTranscribeCallAnalyticsProcessorConfiguration": {
                "LanguageCode": "{{en-US}}"
            }
        },
        {
            "Type": "KinesisDataStreamSink",
            "KinesisDataStreamSinkConfiguration": {
                "InsightsTarget": "arn:aws:kinesis:us-east-1:{{account_id}}:stream/{{stream_name}}"
            }
        }
    ]
}
```

Each rule in a real-time alert configuration is triggered independently. You may receive multiple EventBridge notifications if multiple rule conditions are met at the same time. To create a list of rules for your alerts, you can select among the following rule types:

Keyword Match
Alerts when a specified set of keyword or phrases are matched in an utterance or transcript event. You can configure the alert to emit an event if:
+ Any specified keywords are spoken, and `Negate` is set to `false`.
+ All specified keywords are unspoken for the entirety of the call, if `Negate` is set to `true`.
Amazon Transcribe and Amazon Transcribe Analytics support this rule type.

Sentiment Analysis
Alerts when a particular sentiment type is ongoing for a rolling window period. Only Transcribe Call Analytics support this rule.

Issue Detection
Alerts when an issue is detected in an utterance event. Only Transcribe Call Analytics supports this rule type.

The following example shows a real-time alert event for a `KeywordMatch` rule.

```
{
    "version": "0",
    "id": "{{string}}",
    "detail-type": "Media Insights Rules Matched",
    "source": "aws.chime",
    "account": {{number}},
    "region": "{{us-east-1}}",
    "time": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "resources": [],
    "detail":   {
        "version": "0",
        "sourceMetadata": {}
        "ruleName": "{{string}}"
        "utteranceId": "{{string}}",
        "beginTimestamp": "{{yyyy-mm-ddThh:mm:ssZ}}",
    }
}
```

Some EventBridge fields are specific to the rule type that is matched:

**Keyword match fields**
`utteranceId`: ID of the transcript that contains a matched keyword if you use Amazon Transcribe Call Analytics. For spoken keyword match only.
`resultId`: ID of the transcript that contains a matched keyword if you use Amazon Transcribe. For spoken keyword match only.
`beginTimestamp`: Start time of the transcript that contains a matched keyword. For spoken keyword match only.

**Sentiment analysis fields**
`beginTimestamp`: Start time of the rolling window for the matched sentiment.
`endTimestamp`: End time of the rolling window for the matched sentiment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
