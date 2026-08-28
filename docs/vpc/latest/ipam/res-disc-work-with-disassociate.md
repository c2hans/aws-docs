---
source_url: https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with-disassociate.html
---

# Disassociate a resource discovery
<a name="res-disc-work-with-disassociate"></a>

This section describes how to disassociate a resource discovery from an IPAM. When you disassociate a resource discovery from an IPAM, the IPAM no longer monitors all resources CIDRs and accounts discovered under the resource discovery.

**Note**
You cannot disassociate a default resource discovery association. A default resource discovery association is one that is created automatically when you create an IPAM. The default resource discovery association is deleted, however, if you delete the IPAM.

This step must be completed by the **Primary Org IPAM Account**. For more information about the roles involved in this process, see [Process overview](enable-integ-ipam-outside-org-process.md).

------
#### [ AWS Management Console ]

**To disassociate a resource discovery**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/).

1. In the navigation pane, choose **IPAMs**.

1. Select **Associated discoveries,** and then choose **Disassociate resource discoveries**.

1. Under **IPAM resource discoveries**, choose a resource discovery that's been shared with you by the **Secondary Org Admin Account**.

1. Choose **Disassociate**.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.
+ To disassociate a resource discovery: [disassociate-ipam-resource-discovery](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-ipam-resource-discovery.html)

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
