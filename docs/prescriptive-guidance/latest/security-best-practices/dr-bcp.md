---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/dr-bcp.html
---

# Step 2. Incorporate backup in DR and the BCP
<a name="dr-bcp"></a>

[Disaster recovery (DR)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) is the process of preparing for, responding to, and recovering from a disaster. An important part of your resiliency strategy, the DR plan concerns how your workload responds when a disaster strikes. A disaster could be a technical failure, a human action, or a natural event. The[ Business Continuity Plan (BCP)](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html) outlines how an organization intends to continue normal business operations during an unplanned disruption.

Your DR plan should be a subset of your organization's BCP. The BCP should also include AWS Backup procedures. For example, a security event that affects production data might require you to invoke a DR plan that uses AWS Backup to fail over to backup data from another AWS Region. Ensure that your employees are familiar with and have practiced using AWS Backup along with your organizational procedures, so that if disaster strikes, your organization can continue its normal operations with little or no service disruption. More information about using AWS Backup is provided in other sections in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
