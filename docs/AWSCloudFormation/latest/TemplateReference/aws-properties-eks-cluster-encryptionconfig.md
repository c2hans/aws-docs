---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-encryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster EncryptionConfig
<a name="aws-properties-eks-cluster-encryptionconfig"></a>

The encryption configuration for the cluster.

## Syntax
<a name="aws-properties-eks-cluster-encryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-encryptionconfig-syntax.json"></a>

```
{
  "[Provider](#cfn-eks-cluster-encryptionconfig-provider)" : {{Provider}},
  "[Resources](#cfn-eks-cluster-encryptionconfig-resources)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-eks-cluster-encryptionconfig-syntax.yaml"></a>

```
  [Provider](#cfn-eks-cluster-encryptionconfig-provider): {{
    Provider}}
  [Resources](#cfn-eks-cluster-encryptionconfig-resources): {{
    - String}}
```

## Properties
<a name="aws-properties-eks-cluster-encryptionconfig-properties"></a>

`Provider`  <a name="cfn-eks-cluster-encryptionconfig-provider"></a>
The encryption provider for the cluster.
*Required*: No
*Type*: [Provider](aws-properties-eks-cluster-provider.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Resources`  <a name="cfn-eks-cluster-encryptionconfig-resources"></a>
Specifies the resources to be encrypted. The only supported value is `secrets`.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
