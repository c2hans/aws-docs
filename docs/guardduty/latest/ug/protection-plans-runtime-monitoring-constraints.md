---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/protection-plans-runtime-monitoring-constraints.html
---

# Bidirectional constraints
<a name="protection-plans-runtime-monitoring-constraints"></a>

The Runtime Monitoring sub-features and infrastructure have the following relationships:

Enable a sub-feature
Automatically enables Runtime Monitoring Infrastructure if it was disabled.

Disable a sub-feature
No effect on Runtime Monitoring Infrastructure.

Enable Runtime Monitoring Infrastructure
No effect on sub-features.

Disable Runtime Monitoring Infrastructure
Disables all sub-features.

For auto-enable settings, the following constraints apply:

Raise a sub-feature's auto-enable
Runtime Monitoring Infrastructure always equals the maximum of all sub-features.

Lower a sub-feature's auto-enable
Runtime Monitoring Infrastructure recalculates to the new maximum of all sub-features.

Raise Runtime Monitoring Infrastructure's auto-enable
No effect on sub-features.

Lower Runtime Monitoring Infrastructure's auto-enable
Lowers any sub-feature that exceeds the new parent value to match it.

**Note**
A warning appears when any sub-feature has a different value from Runtime Monitoring Infrastructure (either toggle or auto-enable mismatch). Enabling only Runtime Monitoring Infrastructure puts you in manual mode without auto-management of the security agent. Enable Runtime Monitoring for EKS, ECS, or EC2 to automatically manage the security agent for your workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
