---
source_url: https://docs.aws.amazon.com/tnb/latest/ug/node-eks-authrole.html
---

# AWS.Compute.EKS.AuthRole
<a name="node-eks-authrole"></a>

An AuthRole allows you to add IAM roles to the Amazon EKS cluster `aws-auth` `ConfigMap` so that users can access the Amazon EKS cluster using an IAM role.

## Syntax
<a name="node-eks-authrole-syntax"></a>

```
tosca.nodes.AWS.Compute.EKS.AuthRole:
  properties:
    role\_mappings: List
      arn: String
      groups: List
  requirements:
    clusters: List
```

## Properties
<a name="node-eks-authrole-properties"></a>

 `role_mappings`
List of mappings that define IAM roles that need to be added to the Amazon EKS cluster `aws-auth` `ConfigMap`.
 `arn`
The ARN of the IAM role.
Required: Yes
Type: String
 `groups`
Kubernetes groups to assign to the role defined in `arn`.
Required: No
Type: List

## Requirements
<a name="node-eks-authrole-requirements"></a>

 `clusters`
An [AWS.Compute.EKS](node-eks.md) node.
Required: Yes
Type: List

## Example
<a name="node-eks-authrole-example"></a>

```
EKSAuthMapRoles:
    type: tosca.nodes.AWS.Compute.EKS.AuthRole
    properties:
        role_mappings:
        - arn: arn:aws:iam::${AWS::TNB::AccountId}:role/{{TNBHookRole1}}
          groups:
          - system:nodes
          - system:bootstrappers
        - arn: arn:aws:iam::${AWS::TNB::AccountId}:role/{{TNBHookRole2}}
          groups:
          - system:nodes
          - system:bootstrappers
    requirements:
         clusters:
         - {{Free5GCEKS1}}
         - {{Free5GCEKS2}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
