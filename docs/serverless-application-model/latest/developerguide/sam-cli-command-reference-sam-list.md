---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-list.html
---

# sam list
<a name="sam-cli-command-reference-sam-list"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam list` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam list` command outputs important information about the resources in your serverless application and the state of your serverless application. Use **sam list** before and after deployment to assist during local and cloud development.

## Usage
<a name="sam-cli-command-reference-sam-list-usage"></a>

```
$ sam list {{<options>}} {{<subcommand>}}
```

## Options
<a name="sam-cli-command-reference-sam-list-options"></a>

`--help, -h`  <a name="sam-cli-command-reference-sam-list-options-help"></a>
Show this message and exit.

## Subcommands
<a name="sam-cli-command-reference-sam-list-subcommands"></a>

`endpoints`  <a name="sam-cli-command-reference-sam-list-subcommands-endpoints"></a>
Displays a list of cloud and local endpoints from your CloudFormation stack. For more information, see [sam list endpoints](sam-cli-command-reference-sam-list-endpoints.md).

`resources`  <a name="sam-cli-command-reference-sam-list-subcommands-resources"></a>
Displays the resources in your AWS Serverless Application Model (AWS SAM) template that are created in AWS CloudFormation at deployment. For more information, see [sam list resources](sam-cli-command-reference-sam-list-resources.md).

`stack-outputs`  <a name="sam-cli-command-reference-sam-list-subcommands-stack-outputs"></a>
Displays the outputs of your CloudFormation stack from an AWS SAM or CloudFormation template. For more information, see [sam list stack-outputs](sam-cli-command-reference-sam-list-stack-outputs.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
