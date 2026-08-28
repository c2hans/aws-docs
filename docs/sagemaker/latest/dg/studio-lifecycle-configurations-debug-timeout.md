---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations-debug-timeout.html
---

# Lifecycle configuration timeout
<a name="studio-lifecycle-configurations-debug-timeout"></a>

There is a lifecycle configuration timeout limitation of 5 minutes. If a lifecycle configuration script takes longer than 5 minutes to run, you get an error.

To resolve this error, make sure that your lifecycle configuration script completes in less than 5 minutes.

To help decrease the runtime of scripts, try the following:
+ Reduce unnecessary steps. For example, limit which conda environments to install large packages in.
+ Run tasks in parallel processes.
+ Use the nohup command in your script to make sure that hangup signals are ignored so that the script runs without stopping.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
