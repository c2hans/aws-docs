---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/monitoring-link-device-thumbnails.html
---

# Monitoring Link with thumbnails
<a name="monitoring-link-device-thumbnails"></a>

You can view display thumbnails of the content that is currently being pushed to MediaLive by an AWS Elemental Link hardware device. The thumbnails appear if the AWS Elemental Link hardware is pushing content. You don't have to have an input or a channel that is using this content.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Input devices**, find the card for the Link input device that you want. If there are many Link input devices, enter part of the name to filter the list.

   The card shows a thumbnail panel. If the device is pushing content and the device is connected to AWS (as shown in the **Connection state** field), the thumbnail refreshes every 5 seconds.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
