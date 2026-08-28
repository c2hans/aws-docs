---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks-updating.html
---

# Update a global network using AWS Network Manager
<a name="global-networks-updating"></a>

Update a global network by modifying the description or tags.

**To update your global network**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. Choose **Edit**.

1. For **Description**, enter a new description for the global network.

1. For **Tags**, choose **Remove tag** to remove an existing tag, or choose **Add tag** to add a new tag.

1. Choose **Edit global network**.

**To update a global network using the AWS CLI**
Use the [update-global-network](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/update-global-network.html) command to update the description. Use the [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/tag-resource.html) and [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/untag-resource.html) commands to update the tags.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
