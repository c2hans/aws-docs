---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/exposure-findings-generate.html
---

# Generating exposure findings
<a name="exposure-findings-generate"></a>

 Security Hub generates exposure findings in near real-time. As new security findings are ingested and existing findings are updated, Security Hub generates or updates exposure findings in near real time. Security Hub generates one exposure finding per resource ID.

Security Hub does not publish exposure findings for resource types not supported by exposure findings. When a resource has a significant number and combination of traits, Security Hub generates an exposure finding. The number and combination of traits also determine the severity level of the exposure finding.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
