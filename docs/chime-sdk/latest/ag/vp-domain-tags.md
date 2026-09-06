---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/vp-domain-tags.html
---

# Using tags with voice profile domains
<a name="vp-domain-tags"></a>

The topics in this section explain how to use tags with your existing Amazon Chime SDK voice profile domains. Tags allow you to assign metadata to your domains. A tag consists of a key and an optional value that stores information about the resource, or the data retained on that resource. You define all keys and values. For example, you can create a tag key named *CostCenter* with a value of *98765* and use the pair for cost allocation purposes. You can add up to 50 tags to a voice profile domain.

## Adding tags to voice profile domains
<a name="domain-add-tags"></a>

Follow these steps to add tags to an existing voice profile domain.

**To add tags**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, choose **Voice profile domains**.

1. Choose the domain that you want to add tags to.

1. Choose **Manage tags**, then choose **Add new tag**.

1. Enter a value in the **Key** box and an optional value in the **Value** box.

1. As needed, choose **Add new tag** to create another tag.

1. When finished, choose **Save changes**.

## Editing voice profile domain tags
<a name="domain-edit-tags"></a>

If you have the necessary permissions, you can edit any tags in your AWS account, regardless of who created them. However, IAM policies may prevent you from doing so.

**To edit tags**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, choose **Voice profile domains.**.

1. Choose the domain that has the tags you want to edit.

1. Choose **Manage tags**.

1. As needed, change the values in the **Key** and **Value** boxes.

   —OR—

   Choose **Add new tag** and add one or more tags.

1. When finished, choose **Save changes**.

## Removing voice profile domain tags
<a name="domain-remove-tags"></a>

If you have the necessary permissions, you can remove any tags in your AWS account regardless of who created them. However, IAM policies may prevent you from doing so.

**To remove tags**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, choose **Voice profile domains.**.

1. Choose the domain that has the tags you want to edit.

1. Choose **Manage tags**.

1. Choose **Remove** under each of the tags that you want to delete.

1. When finished, choose **Save changes**.
