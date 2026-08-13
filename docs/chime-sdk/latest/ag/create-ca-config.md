---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/create-ca-config.html
---

# Creating call analytics configurations
<a name="create-ca-config"></a>

To use call analytics, you start by creating a *configuration*, a static structure that holds the information needed to create a call analytics pipeline. You can use the Amazon Chime SDK console to create a configuration, or call the [CreateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipelineConfiguration.html) API.

A call analytics configuration includes details about audio processors, such as recording, voice analytics, or Amazon Transcribe. It also includes insight destinations and alert event configuration. Optionally, you can save your call data to an Amazon S3 bucket for further analysis.

However, *configurations do not include specific audio sources*. That allows you reuse the configuration across multiple call analytics workflows. For example, you can use the same call analytics configuration with different Voice Connectors or across different Amazon Kinesis Video Streams (KVS) sources.

You use the configurations to create pipelines when SIP calls occur through a Voice Connector, or when new media is sent to an Amazon Kinesis Video Stream (KVS). The pipelines, in turn, process the media according to the specifications in the configuration.

You can stop a pipeline programmatically at any time. Pipelines also stop processing media when a Voice Connector call ends. In addition, you can pause a pipeline. Doing so disables calls to the underlying Amazon machine learning services and resumes them when desired. However, call recording runs while you pause a pipeline.

**Topics**
+ [Prerequisites](#ca-ag-prereqs)
+ [Creating a call analytics configuration](#create-config-steps)

## Prerequisites
<a name="ca-ag-prereqs"></a>

To use call analytics with Amazon Transcribe, Amazon Transcribe Analytics, or Amazon Chime SDK voice analytics, you must have the following items:
+ An Amazon Chime SDK Voice Connector. If not, see [Creating an Amazon Chime SDK Voice Connector](create-voicecon.md), earlier in this guide.
+ Amazon EventBridge targets. If not, refer to [Monitoring the Amazon Chime SDK with Amazon CloudWatch](monitoring-cloudwatch.md), earlier in this guide.
+ A service-linked role that allows the Voice Connector to access actions on the EventBridge targets. For more information, refer to [Using the Amazon Chime SDK Voice Connector service linked role policy](using-service-linked-roles-stream.md), earlier in this guide.
+ An Amazon Kinesis Data Stream. If not, see [Create a Kinesis Video Stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-createstream.html) in the *Amazon Kinesis Video Stream Developer Guide*. Voice analytics and transcription require a Kinesis stream.
+ To analyze calls offline, you must create an Amazon Chime SDK data lake. To do that, refer to [ Creating an Amazon Chime SDK data lake](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-lake.html) in the *Amazon Chime SDK Developer Guide*.

## Creating a call analytics configuration
<a name="create-config-steps"></a>

After you create the configuration, you enable call analytics by associating a Voice Connector with the configuration. Once you do that, call analytics starts automatically when a call comes in to that Voice Connector. For more information, refer to [Configuring Voice Connectors to use call analytics](configure-voicecon.md), earlier in this guide.

The following sections explain how to complete each step of the process. Expand them in the order listed.

### Specify configuration details
<a name="ca-config-details"></a>

**To specify configuration details**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Call Analytics**, choose **Configurations**, then choose **Create configuration**.

1. Under **Basic information**, do the following:

   1. Enter a name for the configuration. The name should reflect your use case and any tags.

   1. (Optional) Under **Tags**, choose **Add new tag**, then enter your tag keys and optional values. You define the keys and values. Tags can help you query the configuration.

   1. Choose **Next**.

### Configuring recording
<a name="recording-details"></a>

**To configure recording**
+ On the **Configure recording** page, do the following:

  1. Choose the **Activate call recording** checkbox. This enables recording for Voice Connector calls or KVS streams and sending the data to your Amazon S3 bucket.

  1. Under **File format**, choose **WAV with PCM** for the best audio quality.

     —or—

     Choose **OGG with OPUS** to compress the audio and optimize storage.

  1. (Optional) As needed, choose the **Create an Amazon S3 bucket** link and follow those steps to create an Amazon S3 bucket.

  1. Enter the URI of your Amazon S3 bucket, or choose **Browse** to locate a bucket.

  1. (Optional) Choose **Activate voice enhancement** to help improve the audio quality of your recordings.

  1. Choose **Next**.

For more information about voice enhancement, expand the next section.

### Understanding voice enhancement
<a name="understand-voice-enhancement"></a>

Voice enhancement helps improve the audio quality of the recorded phone calls in your customers' Amazon S3 buckets. Phone calls are narrowband-filtered and sampled at an 8 kHz rate. Voice enhancement boosts the sampling rate from 8kHz to 16kHz and uses a machine learning model to expand the frequency content from narrowband to wideband to make the speech more natural-sounding. Voice enhancement also uses a noise reduction model called Amazon Voice Focus to help reduce background noise in the enhanced audio.

When voice enhancement is enabled, voice enhancement processing is performed after the call recording is completed. The enhanced audio file is written to your Amazon S3 bucket as the original recording and and has the suffix **\_enhanced** added to the base file name of the original recording. Voice enhancement can process calls up to 30 minutes long. Enhanced recordings will not be generated for calls that are longer than 30 minutes.

For information about using voice enhancement programmatically, refer to [Using APIs to create call analytics configurations](https://docs.aws.amazon.com/chime-sdk/latest/dg/create-config-apis.html), in the *Amazon Chime SDK Developer Guide*.

For more information about voice enhancement, refer to [Understanding voice enhancement ](https://docs.aws.amazon.com/chime-sdk/latest/dg/understand-voice-enhancement.html), in the *https://docs.aws.amazon.com/chime/latest/dg/*.

### Configure analytics services
<a name="configure-analytics"></a>

Amazon Transcribe provides text transcriptions of calls. You can then use the transcripts to augment other machine learning services such as Amazon Comprehend or your own machine learning models.

**Note**
Amazon Transcribe also provides automatic language recognition. However, You can't use that feature with custom language models or content redaction. Also, if you use language identification with other features, you can only use the languages that those features support. For more information, refer to [Language identification with streaming transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/lang-id-stream.html), in the *Amazon Transcribe Developer Guide*.

Amazon Transcribe Call Analytics is a machine-learning powered API that provides call transcripts, sentiment, and real-time conversation insights. The service eliminates the need for note-taking, and it can enable immediate action on detected issues. The service also provides post-call analytics, such as caller sentiment, call drivers, non-talk time, interruptions, talk speed, and conversation characteristics.

**Note**
By default, post-call analytics streams call recordings to your Amazon S3 bucket. To avoid creating duplicate recordings, do not enable call recording and post-call analytics at the same time.

Finally, Transcribe Call Analytics can automatically tag conversations based on specific phrases and help redact sensitive information from audio and text. For more information on the call analytics media processors, insights generated by these processors, and output destinations, refer to [Call analytics processor and output destinations](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics-processor-and-output-destinations.html), in the *Amazon Chime SDK Developer Guide*.

**To configure analytics services**

1. On the **Configure analytics services** page, select the check boxes next to **Voice analytics** or **Transcription services**. You can select both items.

   Select the **Voice analytics**, checkbox to enable any combination of **Speaker search** and **Voice tone analysis**.

   Select the **Transcription services** checkbox to enable Amazon Transcribe or Transcribe Call Analytics.

   1. **To enable Speaker search**
      + Select the **Yes, I agree to the Consent Acknowledgement for Amazon Chime SDK voice analytics** checkbox, then choose **Accept**.

   1. To enable Voice tone analysis
      + Select the **Voice tone analysis** checkbox.

   1. To enable Amazon Transcribe

      1. Choose the **Amazon Transcribe** button.

      1. Under **Language settings**, do either of the following:

         1. If your callers speak a single language, choose **Specific language**, then open the **Language** list and select the language.

         1. If your callers speak multiple languages, you can automatically identify them. Choose **Automatic language detection**.

         1. Open the **Language options for automatic language identification** list and select at least two languages.

         1. (Optional) Open the **Preferred language** list and specify a preferred language. When the languages you selected in the previous step have matching confidence scores, the service transcribes the preferred language.

         1. (Optional) Expand **Content removal settings**, select one or more options, then choose one or more of the additional options that appear. Helper text explains each option.

         1. (Optional) Expand **Additional settings**, select one or more options, then choose one or more of the additional options that appear. Helper text explains each option.

   1. To enable Amazon Transcribe Call Analytics

      1. Choose the **Amazon Transcribe Call Analytics** button.

      1. Open the **Language** list and select a language.

      1. (Optional) Expand **Content removal settings**, select one or more options, then choose one or more of the additional options that appear. Helper text explains each option.

      1. (Optional) Expand **Additional settings**, select one or more options, then choose one or more of the additional options that appear. Helper text explains each option.

      1. (Optional) Expand **Post-call analytics settings** and do the following:

         1. Choose the **Post-call analysis** checkbox.

         1. Enter the URI of your Amazon S3 bucket.

         1. Select a content redaction type.

1. When you finish making your selections, choose **Next**.

### Configure output details
<a name="configure-output"></a>

After you finish the media processing steps, you select a destination for the analytics output. Call analytics provides live insights via Amazon Kinesis Data Streams, and optionally through a data warehouse in an Amazon S3 bucket of your choice. To create the data warehouse, you use a CloudFormation Template. The template helps you create the infrastructure that delivers the call metadata and insights to your Amazon S3 bucket. For more information about creating the data warehouse, refer to [Creating an Amazon Chime data lake](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-lake.html) and [Call analytics data model](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-data-model.html), in the *Amazon Chime SDK Developer Guide*.

If you enable voice analytics when you create a configuration, you can also add a voice analytics notification destinations such as AWS Lambda, Amazon Simple Queue Service, or Amazon Simple Notification Service. The following steps explain how.

**To configure output details**

1. Open the **Kinesis data stream** list and select your data stream.
**Note**
If you want to visualize your data, you must select the Kinesis data stream used by the Amazon S3 bucket and Amazon Kinesis Data Firehose.

1. (Optional) Expand **Additional voice analytics notification destinations** and select any combination of AWS Lambda, Amazon SNS, and Amazon SQS destinations.

1. (Optional) Under **Analyze and visualize insights**, select the **Perform historical analysis with data lake** checkbox.

1. When finished, choose **Next**.

### Configure access permissions
<a name="configure-perms"></a>

To enable call analytics, the machine learning service and other resources must have permissions to access data media and deliver insights. For more information, refer to [Using the call analytics resource access role](https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics-resource-access-role.html), in the *Amazon Chime SDK Developer Guide*.

**To configure access permissions**

1. On the **Configure access permissions** page, do one of the following:

   1. Select **Create and use a new service role**.

   1. In the **Service role name suffix** box, enter a descriptive suffix for the role.

   —or—

   1. Select **Use an existing service role**.

   1. Open the **Service role** list and select a role.

1. Choose **Next**.

### (Optional) Configure real-time alerts
<a name="configure-alerts"></a>

**Important**
To use real-time alerts, you must first enable Amazon Transcribe or Amazon Transcribe Call Analytics.

You can create a set of rules that send real-time alerts to Amazon EventBridge. When an insight generated by Amazon Transcribe or Amazon Transcribe Call Analytics matches your specified rule during an analytics session, an alert is sent. Alerts have the detail type `Media Insights Rules Matched`. EventBridge supports integration with downstream services such as Amazon Lambda, Amazon SQS, and Amazon SNS to trigger notifications for the end user or initiate other custom business logic. For more information, refer to [Automating the Amazon Chime SDK with EventBridge](automating-chime-with-cloudwatch-events.md), later in this section.

**To configure alerts**

1. Under **Real-time alerts**, choose **Active real-time alerts**.

1. Under **Rules**, select **Create rule**.

1. In the **Rule name** box, enter a name for the rule.

1. Open the **Rule type** list and select the type of rule you want to use.

1. Use the controls that appear to add keywords to the rule and apply logic, such as **mentioned** or **not mentioned**.

1. Choose **Next**.

### Review and create
<a name="review-create"></a>

**To create the configuration**

1. Review the settings in each section. As needed choose **Edit** to change a setting.

1. Choose **Create configuration**.

Your configuration appears on the **Configurations** page of the Amazon Chime SDK console.
