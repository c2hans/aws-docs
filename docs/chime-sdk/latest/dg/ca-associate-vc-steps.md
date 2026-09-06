---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-associate-vc-steps.html
---

# Associating a configuration with a Voice Connector for the Amazon Chime SDK
<a name="ca-associate-vc-steps"></a>

After you use the console to create a call analytics configuration, you use the configuration by associating a Voice Connector with it. The Voice Connector then automatically invokes call the analytics services specified in your configuration. The Voice Connector invokes call analytics for each call.

**To associate a Voice Connector**

1. Open the Amazon Chime console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice Connectors**.

1. Choose the name of the Voice Connector that you want to associate with a configuration, then choose the **Streaming** tab.

1. If it isn't already selected, choose **Start** to begin streaming to Kinesis Video Streams.

1. Under **Call Analytics**, select **Activate**, and on the menu that appears, choose your call analytics configuration ARN.

1. Choose **Save**.

**Note**
After enabling, disabling, or modifying a configuration associated with a Voice Connector, allow 5 minutes for the new settings to propagate through the service and take effect.
