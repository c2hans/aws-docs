---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-remote-test-event.html
---

# sam remote test-event
<a name="sam-cli-command-reference-remote-test-event"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam remote test-event` command.
+ For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)
+ For documentation on using the AWS SAM CLI `sam remote test-event` command, see [Introduction to cloud testing with sam remote test-event](using-sam-cli-remote-test-event.md).

The `sam remote test-event` command interacts with shareable test events in the Amazon EventBridge schema registry.

## Usage
<a name="sam-cli-command-reference-remote-test-event-usage"></a>

```
$ sam remote test-event {{<options> <subcommand>}}
```

## Options
<a name="sam-cli-command-reference-remote-test-event-options"></a>

`--help, -h`  <a name="sam-cli-command-reference-remote-invoke-options-help"></a>
Show the help message and exit.

## Subcommands
<a name="sam-cli-command-reference-remote-test-event-subcommands"></a>

`delete`
Delete a shareable test event from the EventBridge schema registry. For more reference information, see [sam remote test-event delete](sam-cli-command-reference-remote-test-event-delete.md).

`get`
Get a shareable test event from the EventBridge schema registry. For more reference information, see [sam remote test-event get](sam-cli-command-reference-remote-test-event-get.md).

`list`
List existing shareable test events for an AWS Lambda function. For more reference information, see [sam remote test-event list](sam-cli-command-reference-remote-test-event-list.md).

`put`
Save an event from a local file to the EventBridge schema registry. For more reference information, see [sam remote test-event put](sam-cli-command-reference-remote-test-event-put.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
