---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/delete-input.html
---

# Deleting an input
<a name="delete-input"></a>

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Inputs**. On the **Inputs** page, find the input that you want to delete, and then look at the **State** column.
   + If the state is **Detached**, then choose the input and choose**Delete**.
   + If the state is **Attached** and you want to delete the input but keep the channel, first [detach the input](detach-input.md). Then come back to this **Inputs **page, choose the input, and choose**Delete**.
   + If the state is **Attached** and you want to delete both the input and its channel, then first [delete the channel](editing-deleting-channel.md#deleting-a-channel). Then come back to this **Inputs **page, choose the input, and choose**Delete**.

The results are as follows:
+ If the input is an Elemental Link input, MediaLive deletes the input. But the Link input device remains in the **Devices** list, and you can attach it to a new input at any time.
+ If the input is a MediaConnect push input, the corresponding outputs in MediaConnect are automatically deleted. You don't have to delete the outputs.
+ If the input is an RTP VPC input or an RTMP VPC push input, the elastic network interfaces of the endpoints are deleted and the IPv4 addresses in the subnet are released for use by another resource. You don't have to delete the network interfaces.

The input security group that is attached to the input (if any) is *not* deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
