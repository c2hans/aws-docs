---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/run-experiment.html
---

# Start an experiment
<a name="run-experiment"></a>

You start an experiment from an experiment template. For more information, see [Start an experiment from a template](start-experiment-from-template.md).

You can schedule your experiments as a one-time task or recurring tasks using Amazon EventBridge. For more information, see [Tutorial: Schedule a recurring experiment](fis-tutorial-recurring-experiment.md).

You can monitor your experiment using any of the following features:
+ View your experiments in the AWS FIS console. For more information, see [View your experiments](view-experiment-progress.md).
+ View Amazon CloudWatch metrics for the target resources in your experiments or view AWS FIS usage metrics. For more information, see [Monitor using CloudWatch](monitoring-cloudwatch.md).
+ Enable experiment logging to capture detailed information about your experiment as it runs. For more information see [Experiment logging](monitoring-logging.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
