---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/configure-voicecon.html
---

# Configuring Voice Connectors to use call analytics
<a name="configure-voicecon"></a>

**Note**
To complete the steps in this section, you must first create a call analytics configuration. For information about creating configurations, see [Creating call analytics configurations](create-ca-config.md).

You can use Amazon Chime SDK Call Analytics with Amazon Chime SDK Voice Connector to automatically generate insights with Amazon Transcribe and Amazon Transcribe Call Analytics with voice analytics. You do this by associating your call analytics configuration with an Amazon Chime SDK voice connector. For each call, the Voice Connector invokes call analytics in accordance with the configuration that you specify. You can associate one configuration with multiple Voice Connectors, or create a unique configuration for each Voice Connector.

Call Analytics uses the [Amazon Chime Voice Connector service-linked role](using-service-linked-roles-stream.md) to invoke the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API on your behalf.

**To configure a Voice Connector**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice Connectors**.

1. Choose the name of the Voice Connector that you want to associate with a configuration, then choose the **Streaming** tab.

1. If it isn't already selected, choose **Start** to begin streaming to Kinesis Video Streams.

1. Under **Call Analytics**, select **Activate**, and on the menu that appears, choose your Call Analytics Configuration ARN.

1. Choose **Save**.

**Note**
After enabling, disabling, or modifying a configuration associated with a Voice Connector, allow 5 minutes for the new settings to propagate through the service and take effect.
