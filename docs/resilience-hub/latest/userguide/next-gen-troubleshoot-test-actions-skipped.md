---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-test-actions-skipped.html
---

# Test run completes with all actions skipped
<a name="next-gen-troubleshoot-test-actions-skipped"></a>

**Symptom:** A test run completes but no faults were injected. All actions show `skipped`.

**Cause:** No resources match any action's target resource type in the selected Availability Zone or Region.

**Solution:** Verify resource discovery has completed and you selected the correct Availability Zone or Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
