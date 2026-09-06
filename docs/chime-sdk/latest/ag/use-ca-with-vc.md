---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/use-ca-with-vc.html
---

# Using Amazon Chime SDK voice analytics with Voice Connectors
<a name="use-ca-with-vc"></a>

You use Amazon Chime SDK call analytics with your Voice Connectors to automatically generate insights into your calls. Specifically, you can identify users and predict their tone, either positive, negative, or neutral.

Call analytics works with Amazon Transcribe, Amazon Transcribe Call Analytics, and Amazon Chime SDK voice analytics.

The process follows these broad steps:

1. Create a call analytics *configuration*, a static structure that contains the instructions for processing data.

1. Associate the configuration with one or more Voice Connectors. You can associate one configuration with multiple Voice Connectors, or create a unique configuration for each Voice Connector.

1. The Voice Connector invokes call analytics in accordance with the configuration.

Call analytics uses the [Amazon Chime Voice Connector service-linked role](using-service-linked-roles-stream.md) to invoke the [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API on your behalf.

**Note**
The following steps explain how to associate a call analytics session with a Voice Connector. To complete them, you first need to create a call analytics configuration. To do that, see [Creating call analytics configurations](create-ca-config.md) in this guide. The creation process assigns an ARN to the configuration. Copy the ARN for use in these steps.

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice Connectors**, then choose a Voice Connector.

1. Choose the **Streaming** tab.

1. Under **Sending to Kinesis Video Streams**, choose **Start**.

1. Under **Call Analytics**, choose **Activate**, choose a configuration from the list, then choose **Save**.
