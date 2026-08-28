---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/jl-lcc-debug.html
---

# Debug lifecycle configurations
<a name="jl-lcc-debug"></a>

The following topics show how to get information about and debug your lifecycle configurations.

**Topics**
+ [Verify lifecycle configuration process from CloudWatch Logs](#jl-lcc-debug-logs)
+ [Lifecycle configuration timeout](#jl-lcc-debug-timeout)

## Verify lifecycle configuration process from CloudWatch Logs
<a name="jl-lcc-debug-logs"></a>

Lifecycle configurations only log `STDOUT` and `STDERR`.

`STDOUT` is the default output for bash scripts. You can write to `STDERR` by appending `>&2` to the end of a bash command. For example, `echo 'hello'>&2`.

Logs for your lifecycle configurations are published to your AWS account using Amazon CloudWatch. These logs can be found in the `/aws/sagemaker/studio` log stream in the CloudWatch console.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Logs** from the left navigation pane. From the dropdown menu, select **Log groups**.

1. On the **Log groups** page, search for `aws/sagemaker/studio`.

1. Select the log group.

1. On the **Log group details** page, choose the **Log streams** tab.

1. To find the logs for a specific space, search the log streams using the following format:

   ```
   {{domain-id}}/{{space-name}}/{{app-type}}/default/LifecycleConfigOnStart
   ```

   For example, to find the lifecycle configuration logs for domain ID `d-m85lcu8vbqmz`, space name `i-sonic-js`, and application type `JupyterLab`, use the following search string:

   ```
   d-m85lcu8vbqmz/i-sonic-js/JupyterLab/default/LifecycleConfigOnStart
   ```

## Lifecycle configuration timeout
<a name="jl-lcc-debug-timeout"></a>

There is a lifecycle configuration timeout limitation of 5 minutes. If a lifecycle configuration script takes longer than 5 minutes to run, you get an error.

To resolve this error, make sure that your lifecycle configuration script completes in less than 5 minutes.

To help decrease the runtime of scripts, try the following:
+ Reduce unnecessary steps. For example, limit which conda environments to install large packages in.
+ Run tasks in parallel processes.
+ Use the nohup command in your script to make sure that hangup signals are ignored so that the script runs without stopping.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
