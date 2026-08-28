---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-computeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ComputeConfig
<a name="aws-properties-eks-cluster-computeconfig"></a>

Indicates the current configuration of the compute capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your AWS account. For more information, see EKS Auto Mode compute capability in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-cluster-computeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-computeconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-eks-cluster-computeconfig-enabled)" : {{Boolean}},
  "[NodePools](#cfn-eks-cluster-computeconfig-nodepools)" : {{[ String, ... ]}},
  "[NodeRoleArn](#cfn-eks-cluster-computeconfig-noderolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-computeconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-eks-cluster-computeconfig-enabled): {{Boolean}}
  [NodePools](#cfn-eks-cluster-computeconfig-nodepools): {{
    - String}}
  [NodeRoleArn](#cfn-eks-cluster-computeconfig-noderolearn): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-computeconfig-properties"></a>

`Enabled`  <a name="cfn-eks-cluster-computeconfig-enabled"></a>
Request to enable or disable the compute capability on your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your AWS account.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodePools`  <a name="cfn-eks-cluster-computeconfig-nodepools"></a>
Configuration for node pools that defines the compute resources for your EKS Auto Mode cluster. For more information, see EKS Auto Mode Node Pools in the *Amazon EKS User Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeRoleArn`  <a name="cfn-eks-cluster-computeconfig-noderolearn"></a>
The ARN of the IAM Role EKS will assign to EC2 Managed Instances in your EKS Auto Mode cluster. This value cannot be changed after the compute capability of EKS Auto Mode is enabled. For more information, see the IAM Reference in the *Amazon EKS User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
