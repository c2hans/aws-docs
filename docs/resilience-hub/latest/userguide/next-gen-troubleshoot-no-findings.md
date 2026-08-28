---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-no-findings.html
---

# Assessment produces no failure mode findings
<a name="next-gen-troubleshoot-no-findings"></a>

**Symptom:** Assessment completes successfully but returns zero failure mode findings.

**Possible causes:**
+ Service has very few resources (assessment needs sufficient architecture to analyze).
+ No policy is applied (assessments without policies produce fewer findings).
+ Architecture already meets all requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
