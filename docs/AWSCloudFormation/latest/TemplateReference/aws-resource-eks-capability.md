---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-eks-capability.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Capability
<a name="aws-resource-eks-capability"></a>

An object representing a managed capability in an Amazon EKS cluster. This includes all configuration, status, and health information for the capability.

## Syntax
<a name="aws-resource-eks-capability-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-eks-capability-syntax.json"></a>

```
{
  "Type" : "AWS::EKS::Capability",
  "Properties" : {
      "[CapabilityName](#cfn-eks-capability-capabilityname)" : {{String}},
      "[ClusterName](#cfn-eks-capability-clustername)" : {{String}},
      "[Configuration](#cfn-eks-capability-configuration)" : {{CapabilityConfiguration}},
      "[DeletePropagationPolicy](#cfn-eks-capability-deletepropagationpolicy)" : {{String}},
      "[RoleArn](#cfn-eks-capability-rolearn)" : {{String}},
      "[Tags](#cfn-eks-capability-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-eks-capability-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-eks-capability-syntax.yaml"></a>

```
Type: AWS::EKS::Capability
Properties:
  [CapabilityName](#cfn-eks-capability-capabilityname): {{String}}
  [ClusterName](#cfn-eks-capability-clustername): {{String}}
  [Configuration](#cfn-eks-capability-configuration): {{
    CapabilityConfiguration}}
  [DeletePropagationPolicy](#cfn-eks-capability-deletepropagationpolicy): {{String}}
  [RoleArn](#cfn-eks-capability-rolearn): {{String}}
  [Tags](#cfn-eks-capability-tags): {{
    - Tag}}
  [Type](#cfn-eks-capability-type): {{String}}
```

## Properties
<a name="aws-resource-eks-capability-properties"></a>

`CapabilityName`  <a name="cfn-eks-capability-capabilityname"></a>
The unique name of the capability within the cluster.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterName`  <a name="cfn-eks-capability-clustername"></a>
The name of the Amazon EKS cluster that contains this capability.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-eks-capability-configuration"></a>
The configuration settings for the capability. The structure varies depending on the capability type.
*Required*: No
*Type*: [CapabilityConfiguration](aws-properties-eks-capability-capabilityconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletePropagationPolicy`  <a name="cfn-eks-capability-deletepropagationpolicy"></a>
The delete propagation policy for the capability. Currently, the only supported value is `RETAIN`, which keeps all resources managed by the capability when the capability is deleted.
*Required*: Yes
*Type*: String
*Allowed values*: `RETAIN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-eks-capability-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that the capability uses to interact with AWS services.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:iam::[0-9]+:role/[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-eks-capability-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-eks-capability-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-eks-capability-type"></a>
The type of capability. Valid values are `ACK`, `ARGOCD`, or `KRO`.
*Required*: Yes
*Type*: String
*Allowed values*: `ARGOCD | ACK | KRO`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-eks-capability-return-values"></a>

### Ref
<a name="aws-resource-eks-capability-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-eks-capability-return-values-fn--getatt"></a>

####
<a name="aws-resource-eks-capability-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the capability.

`Configuration.ArgoCd.AwsIdc.IdcManagedApplicationArn`  <a name="Configuration.ArgoCd.AwsIdc.IdcManagedApplicationArn-fn::getatt"></a>
Property description not available.

`Configuration.ArgoCd.ServerUrl`  <a name="Configuration.ArgoCd.ServerUrl-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix epoch timestamp in seconds for when the capability was created.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The Unix epoch timestamp in seconds for when the capability was last modified.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the capability. Valid values include:
+ `CREATING` – The capability is being created.
+ `ACTIVE` – The capability is running and available.
+ `UPDATING` – The capability is being updated.
+ `DELETING` – The capability is being deleted.
+ `CREATE_FAILED` – The capability creation failed.
+ `UPDATE_FAILED` – The capability update failed.
+ `DELETE_FAILED` – The capability deletion failed.

`Version`  <a name="Version-fn::getatt"></a>
The version of the capability software that is currently running.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
