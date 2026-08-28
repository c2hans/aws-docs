---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-servicenodeportrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ServiceNodePortRange
<a name="aws-properties-eks-cluster-servicenodeportrange"></a>

The port range for Kubernetes NodePort services.

## Syntax
<a name="aws-properties-eks-cluster-servicenodeportrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-servicenodeportrange-syntax.json"></a>

```
{
  "[MaxPort](#cfn-eks-cluster-servicenodeportrange-maxport)" : {{Integer}},
  "[MinPort](#cfn-eks-cluster-servicenodeportrange-minport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-eks-cluster-servicenodeportrange-syntax.yaml"></a>

```
  [MaxPort](#cfn-eks-cluster-servicenodeportrange-maxport): {{Integer}}
  [MinPort](#cfn-eks-cluster-servicenodeportrange-minport): {{Integer}}
```

## Properties
<a name="aws-properties-eks-cluster-servicenodeportrange-properties"></a>

`MaxPort`  <a name="cfn-eks-cluster-servicenodeportrange-maxport"></a>
The maximum port number in the range.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinPort`  <a name="cfn-eks-cluster-servicenodeportrange-minport"></a>
The minimum port number in the range.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
