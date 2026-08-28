---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-test-stopped.html
---

# Test run stops before completing
<a name="next-gen-troubleshoot-test-stopped"></a>

**Symptom:** A test run stops on its own before it finishes.

**Cause:** A CloudWatch alarm that you configured as a stop condition breached its threshold, and resilience testing stopped the run to limit impact.

**Solution:** Review the alarm that triggered the stop condition to determine the impact on your service. After you address the underlying issue, start a new test run.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
