---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.delete-endpoint-group.html
---

# Remove a standard endpoint group
<a name="about-endpoint-groups.delete-endpoint-group"></a>

This section explains how to remove a standard endpoint groups on the AWS Global Accelerator console. If you want to use API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

**Warning**
Removing an endpoint group can cause traffic disruption or degraded availability. Make sure to confirm that you have a failover process in place, if needed, before you remove an endpoint group.

# To remove a standard endpoint group

1. Open the Global Accelerator console at [ https://us-west-2.console.aws.amazon.com/globalaccelerator/home\#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:).

1. On the **Accelerators** page, choose an accelerator.

1. In the **Listeners** section, choose a listener.

1. In the **Endpoint groups** section, choose an endpoint group, and then choose **Remove**.

1. On the confirmation dialog box, choose **Remove**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
