---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-2.4---build-standard-operating-procedures-for-deployment-test-rollback-and-backfill-tasks..html
---

# Best practice 2.4 – Build standard operating procedures for deployment, test, rollback, and backfill tasks
<a name="best-practice-2.4---build-standard-operating-procedures-for-deployment-test-rollback-and-backfill-tasks."></a>

 Standard operating procedures for deployment, test, rollback, and data backfill tasks allow faster deployments, reduce the number of errors that reach production. Using a standard approach also makes remediation easier if a deployment results in unintended consequences.

## Suggestion 2.4.1 – Document and use standard operating procedures for implementing changes in your analytics workload
<a name="suggestion-2.4.1---document-and-use-standard-operating-procedures-for-implementing-changes-in-your-analytics-workload."></a>

 Standard operating procedures allow teams to make changes confidently, thus avoiding repeatable mistakes and reducing the chance of human error.

## Suggestion 2.4.2 – Use automation to perform changes to underlying analytics infrastructure or application logic
<a name="suggestion-2.4.2"></a>

 Automated tests can determine when changes have unintended consequences and can roll back without human intervention.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
