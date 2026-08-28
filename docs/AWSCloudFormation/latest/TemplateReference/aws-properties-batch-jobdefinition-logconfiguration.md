---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition LogConfiguration
<a name="aws-properties-batch-jobdefinition-logconfiguration"></a>

Log configuration options to send to a custom log driver for the container.

## Syntax
<a name="aws-properties-batch-jobdefinition-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-logconfiguration-syntax.json"></a>

```
{
  "[LogDriver](#cfn-batch-jobdefinition-logconfiguration-logdriver)" : {{String}},
  "[Options](#cfn-batch-jobdefinition-logconfiguration-options)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SecretOptions](#cfn-batch-jobdefinition-logconfiguration-secretoptions)" : {{[ Secret, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-logconfiguration-syntax.yaml"></a>

```
  [LogDriver](#cfn-batch-jobdefinition-logconfiguration-logdriver): {{String}}
  [Options](#cfn-batch-jobdefinition-logconfiguration-options): {{
    {{Key}}: {{Value}}}}
  [SecretOptions](#cfn-batch-jobdefinition-logconfiguration-secretoptions): {{
    - Secret}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-logconfiguration-properties"></a>

`LogDriver`  <a name="cfn-batch-jobdefinition-logconfiguration-logdriver"></a>
The log driver to use for the container. The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.
The supported log drivers are `awsfirelens`, `awslogs`, `fluentd`, `gelf`, `json-file`, `journald`, `logentries`, `syslog`, and `splunk`.
Jobs that are running on Fargate resources are restricted to the `awslogs` and `splunk` log drivers.
awsfirelens
Specifies the firelens logging driver. For more information on configuring Firelens, see [Send Amazon ECS logs to an AWS service or AWS Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) in the *Amazon Elastic Container Service Developer Guide*.
awslogs
Specifies the Amazon CloudWatch Logs logging driver. For more information, see [Using the awslogs log driver](https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html) in the *AWS Batch User Guide* and [Amazon CloudWatch Logs logging driver](https://docs.docker.com/config/containers/logging/awslogs/) in the Docker documentation.
fluentd
Specifies the Fluentd logging driver. For more information including usage and options, see [Fluentd logging driver](https://docs.docker.com/config/containers/logging/fluentd/) in the *Docker documentation*.
gelf
Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see [Graylog Extended Format logging driver](https://docs.docker.com/config/containers/logging/gelf/) in the *Docker documentation*.
journald
Specifies the journald logging driver. For more information including usage and options, see [Journald logging driver](https://docs.docker.com/config/containers/logging/journald/) in the *Docker documentation*.
json-file
Specifies the JSON file logging driver. For more information including usage and options, see [JSON File logging driver](https://docs.docker.com/config/containers/logging/json-file/) in the *Docker documentation*.
splunk
Specifies the Splunk logging driver. For more information including usage and options, see [Splunk logging driver](https://docs.docker.com/config/containers/logging/splunk/) in the *Docker documentation*.
syslog
Specifies the syslog logging driver. For more information including usage and options, see [Syslog logging driver](https://docs.docker.com/config/containers/logging/syslog/) in the *Docker documentation*.
If you have a custom driver that's not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that's [available on GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesn't currently support running modified copies of this software.
This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`
*Required*: Yes
*Type*: String
*Allowed values*: `json-file | syslog | journald | gelf | fluentd | awslogs | splunk | awsfirelens`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-batch-jobdefinition-logconfiguration-options"></a>
The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretOptions`  <a name="cfn-batch-jobdefinition-logconfiguration-secretoptions"></a>
The secrets to pass to the log configuration. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: Array of [Secret](aws-properties-batch-jobdefinition-secret.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
