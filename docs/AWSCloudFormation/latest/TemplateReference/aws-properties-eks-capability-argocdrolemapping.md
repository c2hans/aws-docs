---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-capability-argocdrolemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Capability ArgoCdRoleMapping
<a name="aws-properties-eks-capability-argocdrolemapping"></a>

A mapping between an Argo CD role and IAM Identity CenterIAM; Identity Center identities. This defines which users or groups have specific permissions in Argo CD.

## Syntax
<a name="aws-properties-eks-capability-argocdrolemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-capability-argocdrolemapping-syntax.json"></a>

```
{
  "[Identities](#cfn-eks-capability-argocdrolemapping-identities)" : {{[ SsoIdentity, ... ]}},
  "[Role](#cfn-eks-capability-argocdrolemapping-role)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-capability-argocdrolemapping-syntax.yaml"></a>

```
  [Identities](#cfn-eks-capability-argocdrolemapping-identities): {{
    - SsoIdentity}}
  [Role](#cfn-eks-capability-argocdrolemapping-role): {{String}}
```

## Properties
<a name="aws-properties-eks-capability-argocdrolemapping-properties"></a>

`Identities`  <a name="cfn-eks-capability-argocdrolemapping-identities"></a>
A list of IAM Identity CenterIAM; Identity Center identities (users or groups) that should be assigned this Argo CD role.
*Required*: Yes
*Type*: Array of [SsoIdentity](aws-properties-eks-capability-ssoidentity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Role`  <a name="cfn-eks-capability-argocdrolemapping-role"></a>
The Argo CD role to assign. Valid values are:
+ `ADMIN` – Full administrative access to Argo CD.
+ `EDITOR` – Edit access to Argo CD resources.
+ `VIEWER` – Read-only access to Argo CD resources.
*Required*: Yes
*Type*: String
*Allowed values*: `ADMIN | EDITOR | VIEWER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
