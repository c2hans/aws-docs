---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-workflow-sourcereference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Workflow SourceReference
<a name="aws-properties-omics-workflow-sourcereference"></a>

Contains information about the source reference in a code repository, such as a branch, tag, or commit.

## Syntax
<a name="aws-properties-omics-workflow-sourcereference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-workflow-sourcereference-syntax.json"></a>

```
{
  "[type](#cfn-omics-workflow-sourcereference-type)" : {{String}},
  "[value](#cfn-omics-workflow-sourcereference-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-omics-workflow-sourcereference-syntax.yaml"></a>

```
  [type](#cfn-omics-workflow-sourcereference-type): {{String}}
  [value](#cfn-omics-workflow-sourcereference-value): {{String}}
```

## Properties
<a name="aws-properties-omics-workflow-sourcereference-properties"></a>

`type`  <a name="cfn-omics-workflow-sourcereference-type"></a>
The type of source reference, such as branch, tag, or commit.
*Required*: No
*Type*: String
*Allowed values*: `BRANCH | TAG | COMMIT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`value`  <a name="cfn-omics-workflow-sourcereference-value"></a>
The value of the source reference, such as the branch name, tag name, or commit ID.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
