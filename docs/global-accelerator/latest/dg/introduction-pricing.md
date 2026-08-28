---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-pricing.html
---

# Pricing for AWS Global Accelerator
<a name="introduction-pricing"></a>

With AWS Global Accelerator, you are charged a *fixed hourly fee* for each accelerator that is provisioned in your account (whether it's enabled or disabled), and an *incremental charge*, in addition to standard data transfer rates, for every hour of traffic in the dominant direction that flows through the accelerator. The incremental rate depends on the AWS Region that serves the request (the source) and the AWS edge location where the responses are directed (the destination). Customers typically create one accelerator for each application, but customers with complex applications might require more accelerators.

In addition, you will incur standard public IPv4 address charges for IPv4 addresses used with your accelerators.

For details about pricing, information about pricing by source and destination Regions, and a pricing example, see [AWS Global Accelerator pricing](https://aws.amazon.com/global-accelerator/pricing).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
