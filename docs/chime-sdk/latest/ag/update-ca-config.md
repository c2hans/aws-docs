---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/update-ca-config.html
---

# Updating call analytics configurations
<a name="update-ca-config"></a>

The steps in this section explain how to update a call analytics configuration.

**To update a configuration**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **Call Analytics**, choose **Configurations**, then choose the configuration that you want to update.

1. In the upper-right corner, choose **Edit**.

1. Follow the steps in [Creating call analytics configurations](create-ca-config.md) as needed to change the configuration settings.

   You might need to modify the policies on the service role to be compatible with the updated configuration or choose a new service role.

1. When finished, choose **Update configuration**.

**Note**
If the configuration is associated with a Voice Connector, the Voice Connector uses that configuration automatically. However, if you enable, disable, or adjust a voice analytics notification target, allow five minutes for those new settings to take effect.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
