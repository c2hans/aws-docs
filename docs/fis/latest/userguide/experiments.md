---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/experiments.html
---

# Managing your AWS FIS experiments
<a name="experiments"></a>

AWS FIS enables you to perform fault injection experiments on your AWS workloads. To get started, create an [experiment template](experiment-templates.md). After you create an experiment template, you can use it to start an experiment.

An experiment is finished when one of the following occurs:
+ All [actions](action-sequence.md) in the template completed successfully.
+ A [stop condition](stop-conditions.md) is triggered.
+ An action cannot be completed because of an error. For example, if the [target](targets.md) cannot be found.
+ The experiment is [stopped manually](stop-experiment.md).

You cannot resume a stopped or failed experiment. You also cannot rerun a completed experiment. However, you can start a new experiment from the same experiment template. You can optionally update the experiment template before you specify it again in a new experiment.

**Topics**
+ [Start an experiment](run-experiment.md)
+ [View your experiments](view-experiment-progress.md)
+ [Tag an experiment](tag-experiment.md)
+ [Stop an experiment](stop-experiment.md)
+ [List resolved targets](list-experiment-resolved-targets.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
