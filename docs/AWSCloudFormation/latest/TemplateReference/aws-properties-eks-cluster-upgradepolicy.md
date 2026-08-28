---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-upgradepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster UpgradePolicy
<a name="aws-properties-eks-cluster-upgradepolicy"></a>

The support policy to use for the cluster. Extended support allows you to remain on specific Kubernetes versions for longer. Clusters in extended support have higher costs. The default value is `EXTENDED`. Use `STANDARD` to disable extended support.

 [Learn more about EKS Extended Support in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)

## Syntax
<a name="aws-properties-eks-cluster-upgradepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-upgradepolicy-syntax.json"></a>

```
{
  "[SupportType](#cfn-eks-cluster-upgradepolicy-supporttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-upgradepolicy-syntax.yaml"></a>

```
  [SupportType](#cfn-eks-cluster-upgradepolicy-supporttype): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-upgradepolicy-properties"></a>

`SupportType`  <a name="cfn-eks-cluster-upgradepolicy-supporttype"></a>
If the cluster is set to `EXTENDED`, it will enter extended support at the end of standard support. If the cluster is set to `STANDARD`, it will be automatically upgraded at the end of standard support.
 [Learn more about EKS Extended Support in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | EXTENDED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
