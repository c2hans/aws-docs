---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-queueenvironment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::QueueEnvironment
<a name="aws-resource-deadline-queueenvironment"></a>

Creates an environment for a queue that defines how jobs in the queue run.

## Syntax
<a name="aws-resource-deadline-queueenvironment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-queueenvironment-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::QueueEnvironment",
  "Properties" : {
      "[FarmId](#cfn-deadline-queueenvironment-farmid)" : {{String}},
      "[Priority](#cfn-deadline-queueenvironment-priority)" : {{Integer}},
      "[QueueId](#cfn-deadline-queueenvironment-queueid)" : {{String}},
      "[Template](#cfn-deadline-queueenvironment-template)" : {{String}},
      "[TemplateType](#cfn-deadline-queueenvironment-templatetype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-deadline-queueenvironment-syntax.yaml"></a>

```
Type: AWS::Deadline::QueueEnvironment
Properties:
  [FarmId](#cfn-deadline-queueenvironment-farmid): {{String}}
  [Priority](#cfn-deadline-queueenvironment-priority): {{Integer}}
  [QueueId](#cfn-deadline-queueenvironment-queueid): {{String}}
  [Template](#cfn-deadline-queueenvironment-template): {{String}}
  [TemplateType](#cfn-deadline-queueenvironment-templatetype): {{String}}
```

## Properties
<a name="aws-resource-deadline-queueenvironment-properties"></a>

`FarmId`  <a name="cfn-deadline-queueenvironment-farmid"></a>
The identifier assigned to the farm that contains the queue.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-deadline-queueenvironment-priority"></a>
The queue environment's priority.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueId`  <a name="cfn-deadline-queueenvironment-queueid"></a>
The unique identifier of the queue that contains the environment.
*Required*: Yes
*Type*: String
*Pattern*: `^queue-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Template`  <a name="cfn-deadline-queueenvironment-template"></a>
A JSON or YAML template that describes the processing environment for the queue.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `15000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateType`  <a name="cfn-deadline-queueenvironment-templatetype"></a>
Specifies whether the template for the queue environment is JSON or YAML.
*Required*: Yes
*Type*: String
*Allowed values*: `JSON | YAML`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-deadline-queueenvironment-return-values"></a>

### Ref
<a name="aws-resource-deadline-queueenvironment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a reference to a queue environment object.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-deadline-queueenvironment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-queueenvironment-return-values-fn--getatt-fn--getatt"></a>

`Name`  <a name="Name-fn::getatt"></a>
The name of the queue environment.

`QueueEnvironmentId`  <a name="QueueEnvironmentId-fn::getatt"></a>
The queue environment ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
