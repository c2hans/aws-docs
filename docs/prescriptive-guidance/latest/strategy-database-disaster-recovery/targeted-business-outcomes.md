---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/targeted-business-outcomes.html
---

# Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This section discusses the expected outcomes associated with defining and building a disaster recovery (DR) plan for your databases on AWS.

## Curb financial losses
<a name="curb-losses"></a>

If you have a well-designed DR solution for databases that store your application data, you can recover from catastrophic events faster and with minimal or no data loss. This minimizes financial losses that can potentially result from your application being unavailable for prolonged periods, or, in the worst case, from permanently losing your data.

## Reduce the impact to critical business processes
<a name="reduce-impact"></a>

When you identify your tier 0 services and processes, and plan your DR strategy to recover these quickly, you will be able to reduce significant impact to these services and processes, and handle the recovery of dependent processes as well.

## Reduce manual coordination during a real event (automation)
<a name="automation"></a>

If you choose to automate your DR solution, you can reduce the manual coordination required to run the DR solution when there is an event. Automation is beneficial even when you're testing your [business continuity plan (BCP)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html), which specifies how you sustain standard business operations during an unplanned disruption.

## Retain your customers
<a name="retain-customers"></a>

In a competitive market, your DR strategy affects how you earn customer loyalty and retain customers. If your organization has the ability to recover quickly from disasters, you can build confidence with your customers.

## Enhance security
<a name="security"></a>

A well-planned cross-Region DR strategy can help restrict the impact of a ransomware attack to one AWS Region and enable you to use your data in another Region freely without losing your data.

## Increase employee productivity
<a name="productivity"></a>

If your employees understand the DR process well and are comfortable with it, a DR event won't cause panic. You can follow well-defined runbooks to implement the DR solution, and your employees can make the best use of their time to get your business back to normal.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
