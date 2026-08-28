---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/misconceptions.html
---

# Anti-patterns for adopting a multicloud strategy
<a name="misconceptions"></a>

As outlined in the previous section, there are valid reasons for adopting a multicloud strategy. There are also misconceptions (or anti-patterns) that do not justify adopting a multicloud environment. These include:
+ **Improved resilience** – Some FIs decide on a multicloud approach to reduce service disruption in the event that their primary CSP has an outage. Multicloud failover presumes that an application can be switched over to another cloud. However, this requires the company to maintain full portability between two CSPs, which adds complexity, risk, and additional work that make true portability nearly impossible. Adopting a multicloud strategy to improve resilience often adds complexity and is likely to reduce resilience instead of enhancing it.
+ **Avoiding vendor lock-in** – Many firms cite the fear of lock-in—both contractual and technological—as a justification for pursuing a multicloud strategy. However, you should consider the potential cost of exiting one CSP and moving to another, along with the likelihood of needing to undertake that exit. You should also consider that the cloud is inherently more open (that is, it offers more open source technologies and standards) than traditional IT models. Avoiding lock-in doesn't require a multicloud approach. For more information, see the section [Consider the advantages and disadvantages of vendor lock-in](vendor-lockin.md) later in this paper.
+ **Better pricing** – Traditional procurement approaches that use multiple suppliers to ensure price competitiveness do not adapt well to the pay-as-you-go purchasing, volume discounts, and price competition of the cloud. Companies often underestimate the operational complexity of managing multiple cloud environments and fail to properly evaluate whether the benefits justify this added complexity in competitive sourcing decisions.

For more information about these misconceptions, see [Tenet 2](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/tenet-2.html) in *Proven practices for developing a multicloud strategy*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
