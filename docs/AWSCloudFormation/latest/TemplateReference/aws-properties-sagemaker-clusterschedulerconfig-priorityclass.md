---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-clusterschedulerconfig-priorityclass.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ClusterSchedulerConfig PriorityClass
<a name="aws-properties-sagemaker-clusterschedulerconfig-priorityclass"></a>

Priority class configuration. When included in `PriorityClasses`, these class configurations define how tasks are queued.

## Syntax
<a name="aws-properties-sagemaker-clusterschedulerconfig-priorityclass-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-clusterschedulerconfig-priorityclass-syntax.json"></a>

```
{
  "[Name](#cfn-sagemaker-clusterschedulerconfig-priorityclass-name)" : {{String}},
  "[Weight](#cfn-sagemaker-clusterschedulerconfig-priorityclass-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-clusterschedulerconfig-priorityclass-syntax.yaml"></a>

```
  [Name](#cfn-sagemaker-clusterschedulerconfig-priorityclass-name): {{String}}
  [Weight](#cfn-sagemaker-clusterschedulerconfig-priorityclass-weight): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-clusterschedulerconfig-priorityclass-properties"></a>

`Name`  <a name="cfn-sagemaker-clusterschedulerconfig-priorityclass-name"></a>
Name of the priority class.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([-a-z0-9]*[a-z0-9]){0,39}?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-sagemaker-clusterschedulerconfig-priorityclass-weight"></a>
Weight of the priority class. The value is within a range from 0 to 100, where 0 is the default.
A weight of 0 is the lowest priority and 100 is the highest. Weight 0 is the default.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
