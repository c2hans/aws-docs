---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/cli-commands.html
---

# Use common Agent CLI commands
<a name="cli-commands"></a>

The following table provides a set of common use cases and corresponding commands for working with the AWS Kinesis agent.

| Use case | Command |
| --- | --- |
| Automatically start the agent on system start up |  <pre>sudo chkconfig aws-kinesis-agent on</pre>  |
| Check the status of the agent |  <pre>sudo service aws-kinesis-agent status</pre>  |
| Stop the agent |  <pre>sudo service aws-kinesis-agent stop</pre>  |
| Read the agent's log file from this location |  <pre>/var/log/aws-kinesis-agent/aws-kinesis-agent.log</pre>  |
| Uninstall the agent |  <pre>sudo yum remove aws-kinesis-agent</pre>  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
