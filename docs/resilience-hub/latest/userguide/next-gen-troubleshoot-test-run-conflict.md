---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-test-run-conflict.html
---

# Test run fails to start
<a name="next-gen-troubleshoot-test-run-conflict"></a>

**Symptom:** Starting a test run returns a `ConflictException`.

**Cause:** Next generation Resilience Hub runs a single test run at a time for a target. The previous run for the service is still in progress.

**Solution:** Wait for the current run to complete, or stop it with `StopTestRun`, and then start the new run.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
