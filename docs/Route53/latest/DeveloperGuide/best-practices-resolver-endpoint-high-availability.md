---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-high-availability.html
---

# High availability for Resolver endpoints
<a name="best-practices-resolver-endpoint-high-availability"></a>

When you create your VPC Resolver inbound endpoints, Route 53 requires that you create at least two IP addresses that the DNS resolvers on your network will forward queries to. You should also specify IP addresses in at least two Availability Zones for redundancy.

If you require more than one elastic network interface endpoint to be available at all times, we recommend that you create at least one more network interface than you need, to make sure you have additional capacity available for handling possible traffic surges. The additional network interface also ensures availability during service operations like maintenance or upgrades.

For more information, see this detailed blog article: [How to achieve DNS high availability with Resolver endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-achieve-dns-high-availability-with-route-53-resolver-endpoints/) and [Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
