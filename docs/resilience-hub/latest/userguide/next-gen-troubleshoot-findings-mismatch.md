---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-findings-mismatch.html
---

# Failure mode findings not matching expected policy
<a name="next-gen-troubleshoot-findings-mismatch"></a>

**Symptom:** Assessment failure mode findings don't seem to relate to your applied policy.

**Possible causes:**
+ Policy was applied after the assessment ran – re-run the assessment.
+ Multiple policies apply (from user journey and service level) – check all applied policies.
+ The failure mode finding relates to a Well-Architected best practice, not a specific policy requirement.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
