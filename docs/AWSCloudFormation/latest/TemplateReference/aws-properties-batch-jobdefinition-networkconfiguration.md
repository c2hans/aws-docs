---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition NetworkConfiguration
<a name="aws-properties-batch-jobdefinition-networkconfiguration"></a>

The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.

## Syntax
<a name="aws-properties-batch-jobdefinition-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-networkconfiguration-syntax.json"></a>

```
{
  "[AssignPublicIp](#cfn-batch-jobdefinition-networkconfiguration-assignpublicip)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-networkconfiguration-syntax.yaml"></a>

```
  [AssignPublicIp](#cfn-batch-jobdefinition-networkconfiguration-assignpublicip): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-networkconfiguration-properties"></a>

`AssignPublicIp`  <a name="cfn-batch-jobdefinition-networkconfiguration-assignpublicip"></a>
Indicates whether the job has a public IP address. For a job that's running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see [Amazon ECS task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*. The default value is "`DISABLED`".
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
