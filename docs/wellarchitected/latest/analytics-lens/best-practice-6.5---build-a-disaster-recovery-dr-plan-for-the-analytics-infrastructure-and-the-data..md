---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-6.5---build-a-disaster-recovery-dr-plan-for-the-analytics-infrastructure-and-the-data..html
---

# Best practice 6.5 – Build a disaster recovery (DR) plan for the analytics infrastructure and the data
<a name="best-practice-6.5---build-a-disaster-recovery-dr-plan-for-the-analytics-infrastructure-and-the-data."></a>

 Discuss with business stakeholders to understand maximum amount of data loss (RPO) and maximum amount of service loss (RTO).

## Suggestion 6.5.1 – Confirm the business requirement of the disaster recovery (DR) plan
<a name="suggestion-6.5.1-confirm-the-business-requirement-of-the-disaster-recovery-dr-plan."></a>

 Agree with the business shareholders what the internal and external SLAs are for your analytics processes. For example, not all business reports are business critical so it’s important that your DR plans are aligned with the severity of the outage.

## Suggestion 6.5.2 – Design the disaster recovery (DR) solution for each layer of the solution
<a name="suggestion-6.5.2---design-the-disaster-recovery-dr-solution-for-each-layer-of-the-solution."></a>

 Review the architecture for your data and analytics pipeline and select the DR pattern that meets your DR requirements, working backwards from the most important information that must be saved in the event of a DR scenario, to the least important.

## Suggestion 6.5.3 – Implement and test your backup solution based on the RPO and RTO
<a name="suggestion-6.5.3---implement-and-test-your-backup-solution-based-on-the-rpo-and-rto."></a>

 Backup solutions must be implemented to reduce data loss. Test your backup to ensure it is performing correctly by periodically restoring the data and validating the results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
