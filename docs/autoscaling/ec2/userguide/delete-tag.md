---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/delete-tag.html
---

# Delete tags
<a name="delete-tag"></a>

You can delete a tag associated with your Auto Scaling group at any time.

**Topics**
+ [Delete tags (console)](#delete-tag-console)
+ [Delete tags (AWS CLI)](#delete-tag-aws-cli)

## Delete tags (console)
<a name="delete-tag-console"></a>

**To delete a tag**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to an existing group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Details** tab, choose **Tags**, **Edit**.

1. Choose **Remove** next to the tag.

1. Choose **Update**.

## Delete tags (AWS CLI)
<a name="delete-tag-aws-cli"></a>

Use the [delete-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-tags.html) command to delete a tag. For example, the following command deletes a tag with a key of `environment`.

```
aws autoscaling delete-tags --tags "ResourceId={{my-asg}},ResourceType=auto-scaling-group,Key={{environment}}"
```

You must specify the tag key, but you don't have to specify the value. If you specify a value and the value is incorrect, the tag is not deleted.
