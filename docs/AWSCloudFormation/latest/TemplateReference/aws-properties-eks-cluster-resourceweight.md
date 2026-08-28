---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-resourceweight.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ResourceWeight
<a name="aws-properties-eks-cluster-resourceweight"></a>

A resource weight entry for the scheduler scoring strategy.

## Syntax
<a name="aws-properties-eks-cluster-resourceweight-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-resourceweight-syntax.json"></a>

```
{
  "[Name](#cfn-eks-cluster-resourceweight-name)" : {{String}},
  "[Weight](#cfn-eks-cluster-resourceweight-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-eks-cluster-resourceweight-syntax.yaml"></a>

```
  [Name](#cfn-eks-cluster-resourceweight-name): {{String}}
  [Weight](#cfn-eks-cluster-resourceweight-weight): {{Integer}}
```

## Properties
<a name="aws-properties-eks-cluster-resourceweight-properties"></a>

`Name`  <a name="cfn-eks-cluster-resourceweight-name"></a>
The name of the resource (for example, `cpu` or `memory`).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-eks-cluster-resourceweight-weight"></a>
The weight assigned to the resource for scoring. Must be between 1 and 100.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
