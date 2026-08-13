---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecycleExecution LifecycleExecutionResourcesImpactedSummary
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary"></a>

Contains details for an image resource that was identified for a lifecycle action.

## Syntax
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary-syntax.json"></a>

```
{
  "[HasImpactedResources](#cfn-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary-hasimpactedresources)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary-syntax.yaml"></a>

```
  [HasImpactedResources](#cfn-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary-hasimpactedresources): {{Boolean}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary-properties"></a>

`HasImpactedResources`  <a name="cfn-imagebuilder-lifecycleexecution-lifecycleexecutionresourcesimpactedsummary-hasimpactedresources"></a>
Indicates whether an image resource that was identified for a lifecycle action has associated resources that are also impacted.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
