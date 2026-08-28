---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/recovery-plans-retry.html
---

# Retrying a failed step
<a name="recovery-plans-retry"></a>

Retrying a step recovers only the servers in that step that failed or timed out. Servers in the step that already recovered stay as they are, and AWS Elastic Disaster Recovery does not recover them a second time. After the retried step completes, the execution continues automatically with the steps that follow it.

```
aws drs retry-recovery-plan-execution-step \
    --recovery-plan-execution-step-arn {{EXECUTION_STEP_ARN}}
```

The following conditions apply to a retry:
+ The execution must be `FAILED`. You cannot retry a step while the execution is still in progress.
+ The step must be `FAILED`.
+ You cannot retry a wait step. Skip it instead.
+ No other execution of the same plan may be running.

**Important**
An execution that stopped because it reached the 24-hour limit reports `TIMED_OUT`, not `FAILED`. You cannot retry or resume it. To finish the recovery in that case, start a new execution of the plan, or recover the remaining servers individually.

Each retry increments the step's attempt count, which is returned with the step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
