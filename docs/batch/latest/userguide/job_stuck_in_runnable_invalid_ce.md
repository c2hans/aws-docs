---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/job_stuck_in_runnable_invalid_ce.html
---

# Jobs stuck in RUNNABLE due to invalid compute environments
<a name="job_stuck_in_runnable_invalid_ce"></a>

All compute environments are invalid. For more information, see [`INVALID` compute environment](invalid_compute_environment.md). Note: You can't configure a programmable action through the `jobStateTimeLimitActions` parameter to resolve this error.
+ **`statusReason` message while the job is stuck:** `ACTION_REQUIRED - CE(s) associated with the job queue are invalid.`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
