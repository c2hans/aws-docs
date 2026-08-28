---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-blockstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster BlockStorage
<a name="aws-properties-eks-cluster-blockstorage"></a>

Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account. For more information, see EKS Auto Mode block storage capability in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-cluster-blockstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-blockstorage-syntax.json"></a>

```
{
  "[Enabled](#cfn-eks-cluster-blockstorage-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-eks-cluster-blockstorage-syntax.yaml"></a>

```
  [Enabled](#cfn-eks-cluster-blockstorage-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-eks-cluster-blockstorage-properties"></a>

`Enabled`  <a name="cfn-eks-cluster-blockstorage-enabled"></a>
Indicates if the block storage capability is enabled on your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
