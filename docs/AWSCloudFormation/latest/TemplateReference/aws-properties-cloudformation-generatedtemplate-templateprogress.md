---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-generatedtemplate-templateprogress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::GeneratedTemplate TemplateProgress
<a name="aws-properties-cloudformation-generatedtemplate-templateprogress"></a>

A summary of the progress of the template generation.

## Syntax
<a name="aws-properties-cloudformation-generatedtemplate-templateprogress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-generatedtemplate-templateprogress-syntax.json"></a>

```
{
  "[ResourcesFailed](#cfn-cloudformation-generatedtemplate-templateprogress-resourcesfailed)" : {{Integer}},
  "[ResourcesPending](#cfn-cloudformation-generatedtemplate-templateprogress-resourcespending)" : {{Integer}},
  "[ResourcesProcessing](#cfn-cloudformation-generatedtemplate-templateprogress-resourcesprocessing)" : {{Integer}},
  "[ResourcesSucceeded](#cfn-cloudformation-generatedtemplate-templateprogress-resourcessucceeded)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudformation-generatedtemplate-templateprogress-syntax.yaml"></a>

```
  [ResourcesFailed](#cfn-cloudformation-generatedtemplate-templateprogress-resourcesfailed): {{Integer}}
  [ResourcesPending](#cfn-cloudformation-generatedtemplate-templateprogress-resourcespending): {{Integer}}
  [ResourcesProcessing](#cfn-cloudformation-generatedtemplate-templateprogress-resourcesprocessing): {{Integer}}
  [ResourcesSucceeded](#cfn-cloudformation-generatedtemplate-templateprogress-resourcessucceeded): {{Integer}}
```

## Properties
<a name="aws-properties-cloudformation-generatedtemplate-templateprogress-properties"></a>

`ResourcesFailed`  <a name="cfn-cloudformation-generatedtemplate-templateprogress-resourcesfailed"></a>
The number of resources that failed the template generation.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesPending`  <a name="cfn-cloudformation-generatedtemplate-templateprogress-resourcespending"></a>
The number of resources that are still pending the template generation.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesProcessing`  <a name="cfn-cloudformation-generatedtemplate-templateprogress-resourcesprocessing"></a>
The number of resources that are in-process for the template generation.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesSucceeded`  <a name="cfn-cloudformation-generatedtemplate-templateprogress-resourcessucceeded"></a>
The number of resources that succeeded the template generation.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
