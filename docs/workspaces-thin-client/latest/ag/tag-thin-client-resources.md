---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/tag-thin-client-resources.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Using tags on WorkSpaces Thin Client resources
<a name="tag-thin-client-resources"></a>

 You can organize and manage the resources for your WorkSpaces Thin Client by assigning your own metadata to each resource as tags. You specify a key and a value for each tag. A key can be a general category, such as "project," "owner," or "environment," with specific associated values. You can use tags as a simple yet powerful way to manage AWS resources and to organize data, including billing data.

When you add tags to an existing resource, those tags don't appear in your cost allocation report until the first day of the following month. For example, if you add tags to an existing WorkSpaces Thin Client device on July 15, the tags won't appear in your cost allocation report until August 1. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.

**Note**
To view your WorkSpaces Thin Client resource tags in the Cost Explorer, you must activate the tags that you have applied to your WorkSpaces Thin Client resources by following the instructions in [Activating User-Defined Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the *AWS Billing User Guide*.
Tags appear 24 hours after activation, but it can take 4–5 days for values associated with those tags to appear in the Cost Explorer. Additionally, to appear and provide cost data in Cost Explorer, WorkSpaces Thin Client resources that have been tagged must incur charges during that time. Cost Explorer only shows cost data from the time when the tags were activated. No historical data is available at this time.

**Resources that you can tag:**
+ You can add tags to the following resources when you create them—WorkSpaces Thin Client environments.
+ You can add tags to existing resources of the following types—WorkSpaces Thin Client environments, devices, and software sets.
+ You can configure the tags for a device in an environment to be automatically applied when you register a device.

**Tag restrictions**
+ Maximum number of tags per resource—50
+ Maximum key length—128 Unicode characters
+ Maximum value length—256 Unicode characters
+ Tag keys and values are case-sensitive. Allowed characters are letters, spaces, and numbers representable in UTF-8, plus the following special characters: \+ - = . \_ : / @. Do not use leading or trailing spaces.
+ Do not use the `aws:` prefix in your tag names or values because it is reserved for AWS use. You can't edit or delete tag names or values with this prefix.

**To manage tags for an existing environment by using the console**

1. Open the [WorkSpaces Thin Client console](https://console.aws.amazon.com/workspaces-thin-client/environment).

1. Select the **Environment** to open its details page

1. Choose **Edit**.

1. In **Tags** section, do one or more of the following:.
   + To add a tag, choose **Add new tag** and then edit the values of **Key** and **Value**.
   + To update a tag, edit the value of **Value**.
   + To delete a tag, choose the **Remove** next to the tag.

1. When you are finished updating the tags, choose **Save**.

**To manage tags for an existing device by using the console**

1. Open the [WorkSpaces Thin Client console](https://console.aws.amazon.com/workspaces-thin-client/device).

1. Select the device to open its details page.

1. Choose **Tags**.

1. Choose **Manage tags**.

1. Do one or more of the following:
   + To add a tag, choose **Add new tag** and then edit the values of **Key** and **Value**.
   + To update a tag, edit the value of **Value**.
   + To delete a tag, choose the **Remove** next to the tag.

1. When you are finished updating the tags, choose **Save**.

**To manage tags for a new device by using the console**

1. Open the [WorkSpaces Thin Client console](https://console.aws.amazon.com/workspaces-thin-client/softwareset).

1. Select the **Environment** to open its details page.

1. Choose **Edit**.

1. In **Device creation tags** section, do one or more of the following:
   + To add a tag, choose **Add new tag** and then edit the values of **Key** and **Value**.
   + To update a tag, edit the value of **Value**.
   + To delete a tag, choose the **Remove** next to the tag.

1. When you are finished updating the tags, choose Save.

When a device is created, it is registered with the environment and the device creation tags are applied. This only happens during new device registration. Additionally, the `aws:thinclient:environment-id` system tag is applied with the environment Id used as value.

**To manage tags for a software update by using the console**

1. Open the [WorkSpaces Thin Client console](https://console.aws.amazon.com/workspaces-thin-client/softwareset).

1. Select the **Software update** to open its details page.

1. In **Tags** section, choose **Manage tags**.

1. Do one or more of the following:
   + To add a tag, choose **Add new tag** and then edit the values of **Key** and **Value**.
   + To update a tag, edit the value of **Value**.
   + To delete a tag, choose the **Remove** next to the tag.

1. When you are finished updating the tags, choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
