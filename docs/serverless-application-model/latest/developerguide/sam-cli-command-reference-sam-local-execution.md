---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-execution.html
---

# sam local execution
<a name="sam-cli-command-reference-sam-local-execution"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam local execution` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam local execution` command allows you to manage and inspect local durable function executions during development and testing.

**Note**
These commands may not require access to AWS credentials.

## Usage
<a name="sam-cli-command-reference-sam-local-execution-usage"></a>

```
$ sam local execution {{<subcommand>}} {{<options>}}
```

## Options
<a name="sam-cli-command-reference-sam-local-execution-options"></a>

`--help, -h`  <a name="sam-cli-command-reference-sam-local-execution-options-help"></a>
Show this message and exit.

## Subcommands
<a name="sam-cli-command-reference-sam-local-execution-subcommands"></a>

`get`  <a name="sam-cli-command-reference-sam-local-execution-subcommands-get"></a>
Get details of a durable function execution. For more information, see [sam local execution get](sam-cli-command-reference-sam-local-execution-get.md).

`history`  <a name="sam-cli-command-reference-sam-local-execution-subcommands-history"></a>
Get execution history of a durable function execution. For more information, see [sam local execution history](sam-cli-command-reference-sam-local-execution-history.md).

`stop`  <a name="sam-cli-command-reference-sam-local-execution-subcommands-stop"></a>
Stop a durable function execution. For more information, see [sam local execution stop](sam-cli-command-reference-sam-local-execution-stop.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
