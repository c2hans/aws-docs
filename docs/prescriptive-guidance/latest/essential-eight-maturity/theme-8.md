---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-8.html
---

# Theme 8: Implement mechanisms for manual processes

**Essential Eight strategies covered**: Application control, patch applications

Amazon has a saying: [Good intentions don't work—mechanisms do](https://aws.amazon.com/blogs/enterprise-strategy/strategy-is-a-winding-road-mechanisms-keep-you-on-track/) (AWS blog post). This means that you replace informal, ad hoc efforts with automated, repeatable, scalable processes and tools to achieve the desired outcomes.

As shown in the following diagram, a *mechanism* is a complete process where you create a tool, drive adoption of the tool, and then inspect the results to make adjustments. It is a cycle that reinforces and improves itself as it operates. It takes controllable inputs and transforms them into ongoing outputs to address a recurring business challenge. For more information, see [Building mechanisms](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/building-mechanisms.html) in the AWS Well-Architected Framework.

![A flow diagram of a mechanism that transforms controllable inputs into ongoing outputs.](https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/images/guide-img/018fe23c-66d3-4a4f-b452-f579e8efd497/images/0bc35568-9ce7-4950-a56a-d0631fd7f71f.png)

## Related best practices in the AWS Well-Architected Framework
<a name="theme-8-best-practices"></a>
+ [OPS02-BP01 Resources have identified owners](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_resource_owners.html)
+ [OPS02-BP02 Processes and procedures have identified owners](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_proc_owners.html)
+ [OPS02-BP03 Operations activities have identified owners responsible for their performance](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_activity_owners.html)
+ [OPS02-BP04 Mechanisms exist to manage responsibilities and ownership](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_responsibilities_ownership.html)
+ [OPS03-BP01 Provide executive sponsorship](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_executive_sponsor.html)
+ [OPS03-BP03 Escalation is encouraged](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_escalation.html)

## Implementing this theme
<a name="theme-8-implementation"></a>
+ Establish mechanisms to review and address compliance gaps
+ Establish mechanisms to update security policies
+ Remove unsupported applications and add them to the AWS Config rule deny list
+ Validate access policies with AWS Identity and Access Management Access Analyzer
+ Enable Amazon Inspector, which helps you keep vulnerability registers up to date through automated scanning
+ At a minimum, review application control rule sets annually
+ Consider implementing automation, such as [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html), to reduce the burden of manual processes
+ Consider using [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) to gain visibility into which instances are running software required by your software policy

## Monitoring this theme
<a name="theme-8-monitoring"></a>
+ Establish oversight so that executive sponsors can track progress toward goals, including compliance, gap inspection, and mechanism evaluation.
