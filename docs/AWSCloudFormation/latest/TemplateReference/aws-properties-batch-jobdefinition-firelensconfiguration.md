---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-firelensconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition FirelensConfiguration
<a name="aws-properties-batch-jobdefinition-firelensconfiguration"></a>

The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see [Custom log](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) routing in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-batch-jobdefinition-firelensconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-firelensconfiguration-syntax.json"></a>

```
{
  "[Options](#cfn-batch-jobdefinition-firelensconfiguration-options)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Type](#cfn-batch-jobdefinition-firelensconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-firelensconfiguration-syntax.yaml"></a>

```
  [Options](#cfn-batch-jobdefinition-firelensconfiguration-options): {{
    {{Key}}: {{Value}}}}
  [Type](#cfn-batch-jobdefinition-firelensconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-firelensconfiguration-properties"></a>

`Options`  <a name="cfn-batch-jobdefinition-firelensconfiguration-options"></a>
The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is `"options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"}`. For more information, see [Creating a task definition that uses a FireLens configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-batch-jobdefinition-firelensconfiguration-type"></a>
The log router to use. The valid values are `fluentd` or `fluentbit`.
*Required*: Yes
*Type*: String
*Allowed values*: `fluentd | fluentbit`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
