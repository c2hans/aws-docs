---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-global.html
---

# Managing global settings for the Amazon Chime SDK
<a name="manage-global"></a>

Manage call detail record settings for the Amazon Chime SDK.

## Configuring call detail records
<a name="call-detail"></a>

Before you can configure call detail record settings for your Amazon Chime SDK administrative account, you must first create an Amazon Simple Storage Service bucket. The Amazon S3 bucket is used as the log destination for your call detail records. When you configure your call detail record settings, you grant the Amazon Chime SDK read and write access to the Amazon S3 bucket in order to save and manage your data. For more information about creating an Amazon S3 bucket, see [Getting started with Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) in the *Amazon Simple Storage Service User Guide*.

You can configure call detail record settings for Amazon Chime SDK Voice Connectors. For more information about Amazon Chime SDK Voice Connectors, see [Managing phone numbers in Amazon Chime SDK](phone-numbers.md).

**To configure call detail record settings**

1. Create an Amazon S3 bucket by following the steps at [Getting started with Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) in the *Amazon Simple Storage Service User Guide*.

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Call detail records**.

1. Open the **Log destination** list and choose an S3 bucket.

1. Choose **Save**.

You can stop logging call detail records at any time.

**To stop logging call detail records**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Call detail records**.

1. Choose **Disable logging**.

## Amazon Chime SDK Voice Connector call detail records
<a name="vc-cdr"></a>

When you choose to receive call detail records for your Amazon Chime SDK Voice Connector, they are sent to your Amazon S3 bucket. The following example shows the general format of an Amazon Chime SDK Voice Connector call detail record name.

```
Amazon-Chime-Voice-Connector-CDRs/json/{{abcdef1ghij2klmno3pqr4}}/{{2019/03/01}}/{{17.10.00.020}}_{{123abc4d-efg5-6789-h012-j3456789k012}}
```

The following example shows the data that is represented in the call detail record name.

```
Amazon-Chime-Voice-Connector-CDRs/json/{{voiceConnectorID}}/{{year/month/day}}/{{callStartTime}}-{{voiceConnectorTransactionID}}
```

The following example shows the general format of an Amazon Chime SDK Voice Connector call detail record.

```
{
    "AwsAccountId": "111122223333",
    "TransactionId": "123abc4d-efg5-6789-h012-j3456789k012",
    "CallId": "123a4b567890123c456789012d3456e7@203.0.113.9:8080",
    "VoiceConnectorId": "abcdef1ghij2klmno3pqr4",
    "Status": "Completed",
    "StatusMessage": "OK",
    "SipAuthUser": "XXXX",
    "BillableDurationSeconds": 6,
    "BillableDurationMinutes": 0.1,
    "SchemaVersion": "2.0",
    "SourcePhoneNumber": "+12065550100",
    "SourcePhoneNumberName": "North Campus Reception",
    "SourceCountry": "US",
    "DestinationPhoneNumber": "+12065550101",
    "DestinationPhoneNumberName": "South Campus Reception",
    "DestinationCountry": "US",
    "UsageType": "USE1-US-US-outbound-minutes",
    "ServiceCode": "AmazonChimeVoiceConnector",
    "Direction": "Outbound",
    "StartTimeEpochSeconds": 1565399625,
    "EndTimeEpochSeconds": 1565399629,
    "Region": "us-east-1",
    "Streaming": true
}
```

## Amazon Chime SDK Voice Connector streaming detail records
<a name="vc-sdr"></a>

When you choose to receive call detail records for your Amazon Chime SDK Voice Connector, and you stream media to Kinesis Video Streams or send SIPREC requests, streaming detail records are sent to your Amazon S3 bucket. For more information, see [Streaming Amazon Chime SDK Voice Connector media to Kinesis](start-kinesis-vc.md).

The following example shows the general format of a streaming detail record name.

```
Amazon-Chime-Voice-Connector-SDRs/json/{{abcdef1ghij2klmno3pqr4}}/{{2019/03/01}}/{{17.10.00.020}}_{{123abc4d-efg5-6789-h012-j3456789k012}}
```

The following example shows the data that is represented in the streaming detail record name.

```
Amazon-Chime-Voice-Connector-SDRs/json/{{voiceConnectorID}}/{{year/month/day}}/{{callStartTime}}-{{voiceConnectorTransactionID}}
```

The following example shows the general format of a streaming detail record.

```
{
    "SchemaVersion": "1.0",
    "AwsAccountId": "111122223333",
    "TransactionId": "123abc4d-efg5-6789-h012-j3456789k012",
    "CallId": "123a4b567890123c456789012d3456e7@203.0.113.9:8080",
    "VoiceConnectorId": "abcdef1ghij2klmno3pqr4",
    "StartTimeEpochSeconds": 1565399625,
    "EndTimeEpochSeconds": 1565399629,
    "Status": "Completed",
    "StatusMessage": "Streaming succeeded",
    "ServiceCode": "AmazonChime",
    "UsageType": "USE1-VC-kinesis-audio-streaming",
    "BillableDurationSeconds": 6,
    "Region": "us-east-1"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
