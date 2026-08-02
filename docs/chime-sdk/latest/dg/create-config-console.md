---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-config-console.html
---

# Using the Amazon Chime SDK console to create call analytics configurations
<a name="create-config-console"></a>

After you create the prerequisites listed in the previous section, you can use the Amazon Chime SDK console to create one or more call analytics configurations. You can also use the console to associate one or more Voice Connectors with your configurations. When you complete that process, call analytics begins running with the features that you enable when you create the configuration.

You follow these steps to create a call analytics configuration:

1. Specify the configuration details, including a name and optional tags.

1. Configure your recording settings. Create a call analytics configuration that includes recording and machine-learning powered insights.

1. Configure your analytics services.

1. Select output destinations for consuming real-time insights. Create an optional data lake to perform post-call analytics.

1. Create a new service role or use an existing role.

1. Set up real-time alerts that send notifications via Amazon EventBridge when certain conditions are met.

1. Review your settings and create the configuration

After you create the configuration, you enable call analytics by associating a Voice Connector with the configuration. Once you do that, call analytics starts automatically when a call comes in to that Voice Connector. For more information, refer to [Associating a configuration with a Voice Connector for the Amazon Chime SDK](ca-associate-vc-steps.md), later in this section.

The following sections explain how to complete each step of the process. Expand them in the order listed.

## Specify configuration details
<a name="ca-config-details"></a>

**To specify configuration details**

1. Open the Amazon Chime console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Call Analytics**, choose **Configurations**, then choose **Create configuration**.

1. Under **Basic information**, do the following:

   1. Enter a name for the configuration. The name should reflect your use case and any tags.

   1. (Optional) Under **Tags**, choose **Add new tag**, then enter your tag keys and optional values. You define the keys and values. Tags can help you query the configuration.

   1. Choose **Next**.

## Configuring recording
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

## Understanding voice enhancement
<a name="understand-voice-enhancement"></a>

When you create a call analytics configuration, you can enable call recording and store the recorded calls in an Amazon S3 bucket. As part of that, you can also enable voice enhancement and improve the audio quality of your stored calls. Voice enhancement only applies to recordings generated after the feature is enabled. When the voice enhancement capability is active, an enhanced recording is created in addition to the original recording, and is stored in the same Amazon S3 bucket and format. Voice enhancement will generate enhanced recordings for calls that are up to 30 minutes long. Enhanced recordings will not be generated for calls that are longer than 30 minutes.

Phone calls are narrowband-filtered and sampled at 8 KHz. Voice enhancement boosts the sampling rate from 8kHz to 16kHz and uses a machine learning model to expand the frequency content from narrowband to wideband to make the speech more natural-sounding. Voice enhancement also uses a noise reduction model called Amazon Voice Focus to help reduce background noise in the enhanced audio.

Voice enhancement also uses a noise reduction model called Voice Focus. The model helps reduce background noise in the enhanced audio. Voice enhancement applies the model to the upgraded 16 KHz audio.

**Note**
The voice enhancement feature is only supported in US East (N. Virginia) Region and US West (Oregon) Region.

Voice enhancement recordings metadata are published through your configured KDS into the existing AWS Glue data catalog table *call\_analytics\_recording\_metadata*. To identify the original call recording record from the voice enhanced call recording, a new field called *detail-subtype* with value *VoiceEnhancement* is added to KDS notification and the glue table *call\_analytics\_recording\_metadata*. For more information on the data warehouse schema, see [Call analytics data model for the Amazon Chime SDK](ca-data-model.md).

### Voice enhancement file format
<a name="enhancement-file-format"></a>

Note the following about enhanced recording files.
+ Enhanced recordings are written to the same Amazon S3 bucket as regular recordings. You configure the destination by calling the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkConfiguration.html) or [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration.html)APIs, or by using the Amazon Chime SDK console.
+ Enhanced recordings have **\_enhanced** appended to the base file name. name.
+ Enhanced recordings keep the same file format as the original recording. You configure the file format by calling the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkConfiguration.html) or [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration.html) APIs, or by using the Amazon Chime SDK console.

The following example shows a typical file name format.

```
s3://{{original_file_name}}_enhanced.{{wav}}
```

or

```
s3://{{original_file_name}}_enhanced.{{ogg}}
```

## Configure analytics services
<a name="configure-analytics"></a>

Amazon Transcribe provides text transcriptions of calls. You can then use the transcripts to augment other machine learning services such as Amazon Comprehend or your own machine learning models.

**Note**
Amazon Transcribe also provides automatic language recognition. However, You can't use that feature with custom language models or content redaction. Also, if you use language identification with other features, you can only use the languages that those features support. For more information, refer to [Language identification with streaming transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/lang-id-stream.html), in the *Amazon Transcribe Developer Guide*.

Amazon Transcribe Call Analytics is a machine-learning powered API that provides call transcripts, sentiment, and real-time conversation insights. The service eliminates the need for note-taking, and it can enable immediate action on detected issues. The service also provides post-call analytics, such as caller sentiment, call drivers, non-talk time, interruptions, talk speed, and conversation characteristics.

**Note**
By default, post-call analytics streams call recordings to your Amazon S3 bucket. To avoid creating duplicate recordings, do not enable call recording and post-call analytics at the same time.

Finally, Transcribe Call Analytics can automatically tag conversations based on specific phrases and help redact sensitive information from audio and text. For more information on the call analytics media processors, insights generated by these processors, and output destinations see [Call analytics processor and output destinations for the Amazon Chime SDK](call-analytics-processor-and-output-destinations.md), later in this section.

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

## Configure output details
<a name="configure-output"></a>

After you finish the media processing steps, you select a destination for the analytics output. Call analytics provides live insights via Amazon Kinesis Data Streams, and optionally through a data warehouse in an Amazon S3 bucket of your choice. To create the data warehouse, you use a CloudFormation Template. The template helps you create the infrastructure that delivers the call metadata and insights to your Amazon S3 bucket. For more information on the data warehouse creation, refer to [Creating an Amazon Chime SDK data lake](ca-data-lake.md), later in this section. For more information on the data warehouse schema, refer to [Call analytics data model for the Amazon Chime SDK](ca-data-model.md), also later in this section.

If you enabled voice analytics in the previous section, you can also add voice analytics notification destinations such as AWS Lambda, Amazon Simple Queue Service, or Amazon Simple Notification Service. The following steps explain how.

**To configure output details**

1. Open the **Kinesis data stream** list and select your data stream.
**Note**
If you want to visualize your data, you must select the Kinesis data stream used by the Amazon S3 bucket and Amazon Kinesis Data Firehose.

1. (Optional) Expand **Additional voice analytics notification destinations** and select any combination of AWS Lambda, Amazon SNS, and Amazon SQS destinations.

1. (Optional) Under **Analyze and visualize insights**, select the **Perform historical analysis with data lake** checkbox. For more information about data lakes, refer to [Creating an Amazon Chime SDK data lake](ca-data-lake.md), later in this section.

1. When finished, choose **Next**.

## Configure access permissions
<a name="configure-perms"></a>

To enable call analytics, the machine learning service and other resources must have permissions to access data media and deliver insights. You can use an existing service role or use the console to create a new role. For more information about roles, refer to [Using the call analytics resource access role for the Amazon Chime SDK](call-analytics-resource-access-role.md), later in this section.

**To configure access permissions**

1. On the **Configure access permissions** page, do one of the following:

   1. Select **Create and use a new service role**.

   1. In the **Service role name suffix** box, enter a descriptive suffix for the role.

   —or—

   1. Select **Use an existing service role**.

   1. Open the **Service role** list and select a role.

1. Choose **Next**.

## (Optional) Configure real-time alerts
<a name="configure-alerts"></a>

**Important**
To use real-time alerts, you must first enable Amazon Transcribe or Amazon Transcribe Analytics.

You can create a set of rules that send real-time alerts to Amazon EventBridge. When an insight generated by Amazon Transcribe or Amazon Transcribe Call Analytics matches your specified rule during an analytics session, an alert is sent. Alerts have the detail type `Media Insights Rules Matched`. EventBridge supports integration with downstream services such as Amazon Lambda, Amazon SQS, and Amazon SNS to trigger notifications for the end user or initiate other custom business logic. For more information, refer to [Using Amazon EventBridge notifications for the Amazon Chime SDK](using-eventbridge-notifications.md), later in this section.

**To configure alerts**

1. Under **Real-time alerts**, choose **Active real-time alerts**.

1. Under **Rules**, select **Create rule**.

1. In the **Rule name** box, enter a name for the rule.

1. Open the **Rule type** list and select the type of rule you want to use.

1. Use the controls that appear to add keywords to the rule and apply logic, such as **mentioned** or **not mentioned**.

1. Choose **Next**.

## Review and create
<a name="review-create"></a>

**To create the configuration**

1. Review the settings in each section. As needed choose **Edit** to change a setting.

1. Choose **Create configuration**.

Your configuration appears on the **Configurations** page of the Amazon Chime SDK console.
