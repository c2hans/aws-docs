---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-fcapolicyassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicyAssociation

Associates a Flex Cost Allocation (FCA) policy with a network resource such as a NAT gateway, EC2 instance, or VPC peering connection.

## Syntax
<a name="aws-resource-ec2-fcapolicyassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-fcapolicyassociation-syntax.json"></a>

```json
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

```yaml
Type: AWS::EC2::FcaPolicyAssociation
Properties:
  [FcaPolicyId](#cfn-ec2-fcapolicyassociation-fcapolicyid): {{String}}
  [NetworkResourceId](#cfn-ec2-fcapolicyassociation-networkresourceid): {{String}}
  [NetworkResourceScopeType](#cfn-ec2-fcapolicyassociation-networkresourcescopetype): {{String}}
```

## Properties
<a name="aws-resource-ec2-fcapolicyassociation-properties"></a>

`FcaPolicyId`  <a name="cfn-ec2-fcapolicyassociation-fcapolicyid"></a>
The ID of the FCA policy to associate, such as `fcap-1234567890abcdef0`.
*Required*: Yes
*Type*: String
*Pattern*: `^fcap-[a-f0-9]{17}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkResourceId`  <a name="cfn-ec2-fcapolicyassociation-networkresourceid"></a>
The ID of the network resource to associate the FCA policy with.
When `NetworkResourceScopeType` is omitted, this is the ID of a specific network resource, for example a NAT gateway or an instance, and its type must match the policy's `NetworkResourceType`. When `NetworkResourceScopeType` is set, this is the ID of the scope, for example an account, VPC, or subnet.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkResourceScopeType`  <a name="cfn-ec2-fcapolicyassociation-networkresourcescopetype"></a>
Associate by scope instead of directly. When set, `NetworkResourceId` is the ID of the scope (an account ID, a VPC ID, or a subnet ID) and the association covers every eligible network resource in that scope. When omitted, `NetworkResourceId` is a direct network resource (for example, a NAT gateway or instance) and must match the policy's `NetworkResourceType`.
*Required*: No
*Type*: String
*Allowed values*: `account | vpc | subnet`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-fcapolicyassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-fcapolicyassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the FCA policy association.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-fcapolicyassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-fcapolicyassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociatedAt`  <a name="AssociatedAt-fn::getatt"></a>
The timestamp when the association was created.

`AssociationMode`  <a name="AssociationMode-fn::getatt"></a>
The mode of the association.

`ExpectedEffectiveAt`  <a name="ExpectedEffectiveAt-fn::getatt"></a>
The timestamp when the association is expected to take effect.

`FcaPolicyAssociationId`  <a name="FcaPolicyAssociationId-fn::getatt"></a>
The ID of the FCA policy association, such as `fcapassoc-1234567890abcdef0`.

`ManagedBy`  <a name="ManagedBy-fn::getatt"></a>
Indicates who manages the association: the account that created it, or a declarative policy.

`OwnerAccount`  <a name="OwnerAccount-fn::getatt"></a>
The ID of the AWS account that owns the FCA policy association.

## Examples
<a name="aws-resource-ec2-fcapolicyassociation--examples"></a>

### Associate an FCA policy with a NAT gateway
<a name="aws-resource-ec2-fcapolicyassociation--examples--Associate_an_FCA_policy_with_a_NAT_gateway"></a>

The following example associates an FCA policy with a NAT gateway.

#### YAML
<a name="aws-resource-ec2-fcapolicyassociation--examples--Associate_an_FCA_policy_with_a_NAT_gateway--yaml"></a>

```yaml
MyFcaPolicyAssociation:
  Type: AWS::EC2::FcaPolicyAssociation
  Properties:
    FcaPolicyId: fcap-1234567890abcdef0
    NetworkResourceId: nat-1234567890abcdef0
```

#### JSON
<a name="aws-resource-ec2-fcapolicyassociation--examples--Associate_an_FCA_policy_with_a_NAT_gateway--json"></a>

```json
{
    "MyFcaPolicyAssociation": {
        "Type": "AWS::EC2::FcaPolicyAssociation",
        "Properties": {
            "FcaPolicyId": "fcap-1234567890abcdef0",
            "NetworkResourceId": "nat-1234567890abcdef0"
        }
    }
}
```
