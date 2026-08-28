---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/chime-voice-connector-emergency-calling.html
---

# Setting up third-party emergency routing numbers
<a name="chime-voice-connector-emergency-calling"></a>

To use emergency call routing numbers, you need the following:
+ An Amazon Chime SDK Voice Connector.
+ An emergency call routing number from a third-party service provider. This must be a U.S. number, and you supply that number to the Amazon Chime SDK. You can create an Amazon Chime SDK Voice Connector just for emergency calls.

After setup, when you place a call to emergency services, the Amazon Chime SDK uses your emergency number to route calls to your third-party emergency services provider via a public switched telephone network. Your third-party emergency service provider then routes your call to emergency services.

**Setting up emergency call routing numbers outside the United States requires that you perform the following prerequisites:**
+ Obtain emergency call routing numbers from a third-party emergency service provider. Ensure they're US numbers.
+ Turn on and configure termination and origination settings for a Voice Connector. To do that, see [Editing Amazon Chime SDK Voice Connector settings](edit-voicecon.md).

**To set up emergency call routing numbers for your Voice Connector**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Voice Connector.

1. Choose the **Emergency calling** tab.

1. Under **Third Party Emergency Service Provider Configuration**, choose **Add**.

1. For **Call send method**, choose **DNIS** (Dialed Number Identification Service).

1. For **Emergency call routing number for calling emergency services**, enter the third-party phone number for calling emergency services, in E.164 format.

1. For **Test routing number for testing calls to emergency services**, enter the third-party phone number for testing calls to emergency services, in E.164 format.

1. For **Country**, select **United States**.

1. Choose **Add**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
