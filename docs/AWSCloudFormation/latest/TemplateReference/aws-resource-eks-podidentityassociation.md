---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eks-podidentityassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::PodIdentityAssociation
<a name="aws-resource-eks-podidentityassociation"></a>

Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.

## Syntax
<a name="aws-resource-eks-podidentityassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-eks-podidentityassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EKS::PodIdentityAssociation",
  "Properties" : {
      "[ClusterName](#cfn-eks-podidentityassociation-clustername)" : {{String}},
      "[DisableSessionTags](#cfn-eks-podidentityassociation-disablesessiontags)" : {{Boolean}},
      "[Namespace](#cfn-eks-podidentityassociation-namespace)" : {{String}},
      "[Policy](#cfn-eks-podidentityassociation-policy)" : {{String}},
      "[RoleArn](#cfn-eks-podidentityassociation-rolearn)" : {{String}},
      "[ServiceAccount](#cfn-eks-podidentityassociation-serviceaccount)" : {{String}},
      "[Tags](#cfn-eks-podidentityassociation-tags)" : {{[ Tag, ... ]}},
      "[TargetRoleArn](#cfn-eks-podidentityassociation-targetrolearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-eks-podidentityassociation-syntax.yaml"></a>

```
Type: AWS::EKS::PodIdentityAssociation
Properties:
  [ClusterName](#cfn-eks-podidentityassociation-clustername): {{String}}
  [DisableSessionTags](#cfn-eks-podidentityassociation-disablesessiontags): {{Boolean}}
  [Namespace](#cfn-eks-podidentityassociation-namespace): {{String}}
  [Policy](#cfn-eks-podidentityassociation-policy): {{String}}
  [RoleArn](#cfn-eks-podidentityassociation-rolearn): {{String}}
  [ServiceAccount](#cfn-eks-podidentityassociation-serviceaccount): {{String}}
  [Tags](#cfn-eks-podidentityassociation-tags): {{
    - Tag}}
  [TargetRoleArn](#cfn-eks-podidentityassociation-targetrolearn): {{String}}
```

## Properties
<a name="aws-resource-eks-podidentityassociation-properties"></a>

`ClusterName`  <a name="cfn-eks-podidentityassociation-clustername"></a>
The name of the cluster that the association is in.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DisableSessionTags`  <a name="cfn-eks-podidentityassociation-disablesessiontags"></a>
The state of the automatic sessions tags. The value of *true* disables these tags.
EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to AWS resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see [List of session tags added by EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags) in the *Amazon EKS User Guide*.
*Required*: No
*Type*: Boolean
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-eks-podidentityassociation-namespace"></a>
The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the Pods that use the service account must be in this namespace.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-eks-podidentityassociation-policy"></a>
An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-eks-podidentityassociation-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to associate with the service account. The EKS Pod Identity agent manages credentials to assume this role for applications in the containers in the Pods that use this service account.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceAccount`  <a name="cfn-eks-podidentityassociation-serviceaccount"></a>
The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-eks-podidentityassociation-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource – 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length – 128 Unicode characters in UTF-8
+ Maximum value length – 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
*Required*: No
*Type*: Array of [Tag](aws-properties-eks-podidentityassociation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRoleArn`  <a name="cfn-eks-podidentityassociation-targetrolearn"></a>
The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-eks-podidentityassociation-return-values"></a>

### Ref
<a name="aws-resource-eks-podidentityassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "myAssociation" }`

For the Amazon EKS Pod Identity association `myAssociation`, Ref returns the physical resource ID of the association. For example, `a-abcdefghijklmnop1`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-eks-podidentityassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-eks-podidentityassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationArn`  <a name="AssociationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the association.

`AssociationId`  <a name="AssociationId-fn::getatt"></a>
The ID of the association.

`ExternalId`  <a name="ExternalId-fn::getatt"></a>
The unique identifier for this EKS Pod Identity association for a target IAM role. You put this value in the trust policy of the target role, in a `Condition` to match the `sts.ExternalId`. This ensures that the target role can only be assumed by this association. This prevents the *confused deputy problem*. For more information about the confused deputy problem, see [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.
If you want to use the same target role with multiple associations or other roles, use independent statements in the trust policy to allow `sts:AssumeRole` access from each role.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
