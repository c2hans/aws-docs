---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-lifecycleexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecycleExecution
<a name="aws-resource-imagebuilder-lifecycleexecution"></a>

Contains metadata from a runtime instance of a lifecycle policy.

## Syntax
<a name="aws-resource-imagebuilder-lifecycleexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-lifecycleexecution-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::LifecycleExecution",
  "Properties" : {
      "[ResourceArn](#cfn-imagebuilder-lifecycleexecution-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-lifecycleexecution-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::LifecycleExecution
Properties:
  [ResourceArn](#cfn-imagebuilder-lifecycleexecution-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-imagebuilder-lifecycleexecution-properties"></a>

`ResourceArn`  <a name="cfn-imagebuilder-lifecycleexecution-resourcearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-imagebuilder-lifecycleexecution-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-lifecycleexecution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-imagebuilder-lifecycleexecution-return-values-fn--getatt"></a>

####
<a name="aws-resource-imagebuilder-lifecycleexecution-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`EndTime`  <a name="EndTime-fn::getatt"></a>
The timestamp when the lifecycle runtime instance completed.

`LifecycleExecutionId`  <a name="LifecycleExecutionId-fn::getatt"></a>
Identifies the lifecycle policy runtime instance.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The timestamp when the lifecycle runtime instance started.
