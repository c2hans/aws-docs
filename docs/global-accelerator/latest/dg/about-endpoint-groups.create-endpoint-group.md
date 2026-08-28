---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.create-endpoint-group.html
---

# Add a standard endpoint group
<a name="about-endpoint-groups.create-endpoint-group"></a>

You work with endpoint groups on the AWS Global Accelerator console or by using an API operation. You can add or remove endpoints from an endpoint group at any time.

This section explains how to add a standard endpoint groups on the AWS Global Accelerator console. If you want to use API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To add a standard endpoint group

1. Open the Global Accelerator console at [ https://us-west-2.console.aws.amazon.com/globalaccelerator/home\#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:).

1. On the **Accelerators** page, choose an accelerator.

1. In the **Listeners** section, for **Listener ID**, choose the ID of the listener that you want to add an endpoint group to.

1. Choose **Add endpoint group**.

1. In the section for a listener, specify a Region for the endpoint group by choosing one from the dropdown list.

1. Optionally, for **Traffic dial**, enter a number from 0 to 100 to set a percentage of traffic for this endpoint group. The percentage is applied only to the traffic that is already directed to this endpoint group, not all listener traffic. By default, the traffic dial is set to 100.

1. Optionally, to override the listener port used for routing traffic to endpoints and reroute traffic to specific ports on your endpoints, choose **Configure port overrides**. For more information, see [Override listener ports for restricted ports or connection collisions](about-endpoint-groups-port-override.md).

1. Optionally, to specify custom health check values to be applied to EC2 instance and Elastic IP address endpoints, choose **Configure health checks**. For more information, see [Ensure health check access for your accelerator](about-endpoint-groups-health-check-options.md).

1. Optionally, choose **Add endpoint group** to add additional endpoint groups for this listener or other listeners.

1. Choose **Add endpoint group**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
