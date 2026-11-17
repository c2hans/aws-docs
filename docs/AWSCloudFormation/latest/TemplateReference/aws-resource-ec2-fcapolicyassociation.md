---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-fcapolicyassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicyAssociation
<a name="aws-resource-ec2-fcapolicyassociation"></a>

<a name="aws-resource-ec2-fcapolicyassociation-description"></a>The `AWS::EC2::FcaPolicyAssociation` resource Property description not available. for EC2.

## Syntax
<a name="aws-resource-ec2-fcapolicyassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-fcapolicyassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::FcaPolicyAssociation",
  "Properties" : {
      "[FcaPolicyId](#cfn-ec2-fcapolicyassociation-fcapolicyid)" : {{String}},
      "[NetworkResourceId](#cfn-ec2-fcapolicyassociation-networkresourceid)" : {{String}},
      "[NetworkResourceScopeType](#cfn-ec2-fcapolicyassociation-networkresourcescopetype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-fcapolicyassociation-syntax.yaml"></a>

```
Type: AWS::EC2::FcaPolicyAssociation
Properties:
  [FcaPolicyId](#cfn-ec2-fcapolicyassociation-fcapolicyid): {{String}}
  [NetworkResourceId](#cfn-ec2-fcapolicyassociation-networkresourceid): {{String}}
  [NetworkResourceScopeType](#cfn-ec2-fcapolicyassociation-networkresourcescopetype): {{String}}
```

## Properties
<a name="aws-resource-ec2-fcapolicyassociation-properties"></a>

`FcaPolicyId`  <a name="cfn-ec2-fcapolicyassociation-fcapolicyid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^fcap-[a-f0-9]{17}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkResourceId`  <a name="cfn-ec2-fcapolicyassociation-networkresourceid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkResourceScopeType`  <a name="cfn-ec2-fcapolicyassociation-networkresourcescopetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `account | vpc | subnet`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-fcapolicyassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-fcapolicyassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-fcapolicyassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-fcapolicyassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociatedAt`  <a name="AssociatedAt-fn::getatt"></a>
Property description not available.

`AssociationMode`  <a name="AssociationMode-fn::getatt"></a>
Property description not available.

`ExpectedEffectiveAt`  <a name="ExpectedEffectiveAt-fn::getatt"></a>
Property description not available.

`FcaPolicyAssociationId`  <a name="FcaPolicyAssociationId-fn::getatt"></a>
Property description not available.

`ManagedBy`  <a name="ManagedBy-fn::getatt"></a>
Property description not available.

`OwnerAccount`  <a name="OwnerAccount-fn::getatt"></a>
Property description not available.
