---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resiliencehubv2-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Policy
<a name="aws-resource-resiliencehubv2-policy"></a>

Represents a resilience policy that defines availability and disaster recovery requirements.

## Syntax
<a name="aws-resource-resiliencehubv2-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resiliencehubv2-policy-syntax.json"></a>

```
{
  "Type" : "AWS::ResilienceHubV2::Policy",
  "Properties" : {
      "[AvailabilitySlo](#cfn-resiliencehubv2-policy-availabilityslo)" : {{AvailabilitySlo}},
      "[DataRecovery](#cfn-resiliencehubv2-policy-datarecovery)" : {{DataRecoveryTargets}},
      "[Description](#cfn-resiliencehubv2-policy-description)" : {{String}},
      "[KmsKeyId](#cfn-resiliencehubv2-policy-kmskeyid)" : {{String}},
      "[MultiAz](#cfn-resiliencehubv2-policy-multiaz)" : {{MultiAzTargets}},
      "[MultiRegion](#cfn-resiliencehubv2-policy-multiregion)" : {{MultiRegionTargets}},
      "[Name](#cfn-resiliencehubv2-policy-name)" : {{String}},
      "[Tags](#cfn-resiliencehubv2-policy-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-resiliencehubv2-policy-syntax.yaml"></a>

```
Type: AWS::ResilienceHubV2::Policy
Properties:
  [AvailabilitySlo](#cfn-resiliencehubv2-policy-availabilityslo): {{
    AvailabilitySlo}}
  [DataRecovery](#cfn-resiliencehubv2-policy-datarecovery): {{
    DataRecoveryTargets}}
  [Description](#cfn-resiliencehubv2-policy-description): {{String}}
  [KmsKeyId](#cfn-resiliencehubv2-policy-kmskeyid): {{String}}
  [MultiAz](#cfn-resiliencehubv2-policy-multiaz): {{
    MultiAzTargets}}
  [MultiRegion](#cfn-resiliencehubv2-policy-multiregion): {{
    MultiRegionTargets}}
  [Name](#cfn-resiliencehubv2-policy-name): {{String}}
  [Tags](#cfn-resiliencehubv2-policy-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-resiliencehubv2-policy-properties"></a>

`AvailabilitySlo`  <a name="cfn-resiliencehubv2-policy-availabilityslo"></a>
The availability SLO defined in the policy.
*Required*: No
*Type*: [AvailabilitySlo](aws-properties-resiliencehubv2-policy-availabilityslo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataRecovery`  <a name="cfn-resiliencehubv2-policy-datarecovery"></a>
The data recovery targets defined in the policy.
*Required*: No
*Type*: [DataRecoveryTargets](aws-properties-resiliencehubv2-policy-datarecoverytargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-resiliencehubv2-policy-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `615`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-resiliencehubv2-policy-kmskeyid"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
*Required*: No
*Type*: String
*Pattern*: `^((arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+))$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MultiAz`  <a name="cfn-resiliencehubv2-policy-multiaz"></a>
The multi-AZ disaster recovery targets defined in the policy.
*Required*: No
*Type*: [MultiAzTargets](aws-properties-resiliencehubv2-policy-multiaztargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiRegion`  <a name="cfn-resiliencehubv2-policy-multiregion"></a>
The multi-Region disaster recovery targets defined in the policy.
*Required*: No
*Type*: [MultiRegionTargets](aws-properties-resiliencehubv2-policy-multiregiontargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-resiliencehubv2-policy-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-resiliencehubv2-policy-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-resiliencehubv2-policy-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-resiliencehubv2-policy-return-values"></a>

### Ref
<a name="aws-resource-resiliencehubv2-policy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-resiliencehubv2-policy-return-values-fn--getatt"></a>

####
<a name="aws-resource-resiliencehubv2-policy-return-values-fn--getatt-fn--getatt"></a>

`AssociatedServiceCount`  <a name="AssociatedServiceCount-fn::getatt"></a>
The number of services associated with this policy.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the policy was created.

`PolicyArn`  <a name="PolicyArn-fn::getatt"></a>
ARN identifier.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the policy was last updated.
