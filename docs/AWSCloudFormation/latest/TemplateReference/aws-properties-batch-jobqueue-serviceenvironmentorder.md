---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobqueue-serviceenvironmentorder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobQueue ServiceEnvironmentOrder
<a name="aws-properties-batch-jobqueue-serviceenvironmentorder"></a>

Specifies the order of a service environment for a job queue. This determines the priority order when multiple service environments are associated with the same job queue.

## Syntax
<a name="aws-properties-batch-jobqueue-serviceenvironmentorder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobqueue-serviceenvironmentorder-syntax.json"></a>

```
{
  "[Order](#cfn-batch-jobqueue-serviceenvironmentorder-order)" : {{Integer}},
  "[ServiceEnvironment](#cfn-batch-jobqueue-serviceenvironmentorder-serviceenvironment)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobqueue-serviceenvironmentorder-syntax.yaml"></a>

```
  [Order](#cfn-batch-jobqueue-serviceenvironmentorder-order): {{Integer}}
  [ServiceEnvironment](#cfn-batch-jobqueue-serviceenvironmentorder-serviceenvironment): {{String}}
```

## Properties
<a name="aws-properties-batch-jobqueue-serviceenvironmentorder-properties"></a>

`Order`  <a name="cfn-batch-jobqueue-serviceenvironmentorder-order"></a>
The order of the service environment. Job queues with a higher priority are evaluated first when associated with the same service environment.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceEnvironment`  <a name="cfn-batch-jobqueue-serviceenvironmentorder-serviceenvironment"></a>
The name or ARN of the service environment.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
