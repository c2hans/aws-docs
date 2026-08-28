---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/use-tags-voice-con.html
---

# Using tags with Voice Connectors
<a name="use-tags-voice-con"></a>

The topics in this section explain how to use tags with your existing Amazon Chime SDK Voice Connectors. Tags allow you to assign metadata to your AWS resources, such as Voice Connectors. A tag consists of a key and an optional value that stores information about the resource, or the data retained on that resource. You define all keys and values. For example, you can create a tag key named `CostCenter` with a value of `98765` and use the pair for cost allocation purposes. You can add up to 50 tags to a Voice Connector.

## Adding tags to Voice Connectors
<a name="add-tags-voice-con"></a>

You can add tags to existing Amazon Chime SDK Voice Connectors.

**To add tags to Voice Connectors**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice Connectors**.

1. Choose the name of Voice Connector that you want use.

1. Choose the **Tags** tab, then choose **Manage tags**.

1. Choose **Add new tag**, then enter a key and optional value.

1. As needed, choose **Add new tag** to create another tag.

1. When finished, choose **Save changes**.

## Editing tags
<a name="edit-tags-voice-con"></a>

If you have the necessary permissions, you can edit any tags in your AWS account regardless of who created them. However, IAM policies may prevent you from doing so.

**To edit tags**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice Connectors**.

1. Choose the name of Voice Connector that you want use.

1. Choose the **Tags** tab, then choose **Manage tags**.

1. In the **Key** or **Value** boxes, enter a new value.

1. When finished, choose **Save changes**.

## Removing tags
<a name="remove-tags-voice-con"></a>

If you have the necessary permissions, you can remove any tags in your AWS account regardless of who created them. However, IAM policies may prevent you from doing so.

**To remove tags**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice Connectors**.

1. Choose the name of Voice Connector that you want use.

1. Choose the **Tags** tab, then choose **Manage tags**.

1. Choose **Remove** next to the tag that you want to remove.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
