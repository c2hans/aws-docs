---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-4.4---establish-an-emergency-access-process-to-ensure-that-admin-access-is-managed-and-used-when-required..html
---

# Best practice 4.4 – Establish an emergency access process to ensure that admin access is managed and used when required
<a name="best-practice-4.4---establish-an-emergency-access-process-to-ensure-that-admin-access-is-managed-and-used-when-required."></a>

 Emergency access allows expedited access to your workload in the unlikely event of an automated process or pipeline issue. This will help you rely on least privilege access, but still provide users the right level of access when they require it.

## Suggestion 4.4.1 – Ensure that risk analysis is performed on your analytics workload by identifying emergency situations and a procedure to allow emergency access
<a name="suggestion-4.4.1---ensure-that-risk-analysis-is-done-on-your-analytics-workload-by-identifying-emergency-situations-and-a-procedure-to-allow-emergency-access."></a>

 Identify the potential events that can happen from source systems, analytics workload, and downstream systems. Quantify the risk of each event such as likelihood (low, medium, or high) and the size of the business impact (small, medium, or large).

 For example, after you identified priority risks, discuss with the source and downstream system owners on how to allow analytics workload access to the source and downstream systems to continue the data processing business.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
