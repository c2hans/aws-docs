---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.creating-editing.html
---

# Create accelerator
<a name="about-accelerators.creating-editing"></a>

This section explains how to create a standard accelerator on the console. To work with Global Accelerator programmatically, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

# To create a standard accelerator

1. Open the Global Accelerator console at [ https://us-west-2.console.aws.amazon.com/globalaccelerator/home\#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:).

1. Choose **Create accelerator**.

1. Provide a name for your accelerator.

1. For **Accelerator type**, select **Standard**.

1. For **IP address type**, select **IPv4** or **DUAL-STACK**.

1. Optionally, if you brought your own IP address ranges to AWS (BYOIP), you can specify a static IP address for your accelerator, one from each address pool. Make this choice for each of the two static IP addresses for your accelerator.
   + For each static IP address, choose the IP address pool to use.
**Note**
You must choose a different IP address pool for each static IP address. This restriction is because Global Accelerator assigns each address range to a different network zone, for high availability.
   + If you chose your own IP address pool, also choose a specific IP address from the pool. If you choose the default Amazon IP address pool, Global Accelerator assigns a specific IP address to your accelerator.

   For more information about the requirements for specifying or updating static IP addresses with BYOIP, see [Requirements when you update an accelerator to change the IP address.](using-byoip.update-accelerator.md#AGAUpdateAccRequirements)

1. Optionally, add one or more tags to help you identify your accelerator resources.

1. Choose **Next** to add listeners, endpoint groups, and endpoints.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
