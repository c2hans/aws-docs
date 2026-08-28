---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-fargateprofile-selector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::FargateProfile Selector
<a name="aws-properties-eks-fargateprofile-selector"></a>

An object representing an AWS Fargate profile selector.

## Syntax
<a name="aws-properties-eks-fargateprofile-selector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-fargateprofile-selector-syntax.json"></a>

```
{
  "[Labels](#cfn-eks-fargateprofile-selector-labels)" : {{[ Label, ... ]}},
  "[Namespace](#cfn-eks-fargateprofile-selector-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-fargateprofile-selector-syntax.yaml"></a>

```
  [Labels](#cfn-eks-fargateprofile-selector-labels): {{
    - Label}}
  [Namespace](#cfn-eks-fargateprofile-selector-namespace): {{String}}
```

## Properties
<a name="aws-properties-eks-fargateprofile-selector-properties"></a>

`Labels`  <a name="cfn-eks-fargateprofile-selector-labels"></a>
The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.
*Required*: No
*Type*: Array of [Label](aws-properties-eks-fargateprofile-label.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-eks-fargateprofile-selector-namespace"></a>
The Kubernetes `namespace` that the selector should match.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
