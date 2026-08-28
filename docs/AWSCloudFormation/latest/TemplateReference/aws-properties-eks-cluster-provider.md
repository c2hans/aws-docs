---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-provider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster Provider
<a name="aws-properties-eks-cluster-provider"></a>

Identifies the AWS Key Management Service (AWS KMS) key used to encrypt the secrets.

## Syntax
<a name="aws-properties-eks-cluster-provider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-provider-syntax.json"></a>

```
{
  "[KeyArn](#cfn-eks-cluster-provider-keyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-provider-syntax.yaml"></a>

```
  [KeyArn](#cfn-eks-cluster-provider-keyarn): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-provider-properties"></a>

`KeyArn`  <a name="cfn-eks-cluster-provider-keyarn"></a>
Amazon Resource Name (ARN) or alias of the KMS key. The KMS key must be symmetric and created in the same AWS Region as the cluster. If the KMS key was created in a different account, the [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) must have access to the KMS key. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
