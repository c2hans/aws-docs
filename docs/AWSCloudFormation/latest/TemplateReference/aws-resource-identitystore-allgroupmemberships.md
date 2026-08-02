---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-identitystore-allgroupmemberships.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IdentityStore::AllGroupMemberships
<a name="aws-resource-identitystore-allgroupmemberships"></a>

<a name="aws-resource-identitystore-allgroupmemberships-description"></a>The `AWS::IdentityStore::AllGroupMemberships` resource Property description not available. for IdentityStore.

## Syntax
<a name="aws-resource-identitystore-allgroupmemberships-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-identitystore-allgroupmemberships-syntax.json"></a>

```
{
  "Type" : "AWS::IdentityStore::AllGroupMemberships",
  "Properties" : {
      "[GroupId](#cfn-identitystore-allgroupmemberships-groupid)" : {{String}},
      "[IdentityStoreId](#cfn-identitystore-allgroupmemberships-identitystoreid)" : {{String}},
      "[MemberId](#cfn-identitystore-allgroupmemberships-memberid)" : {{MemberId}}
    }
}
```

### YAML
<a name="aws-resource-identitystore-allgroupmemberships-syntax.yaml"></a>

```
Type: AWS::IdentityStore::AllGroupMemberships
Properties:
  [GroupId](#cfn-identitystore-allgroupmemberships-groupid): {{String}}
  [IdentityStoreId](#cfn-identitystore-allgroupmemberships-identitystoreid): {{String}}
  [MemberId](#cfn-identitystore-allgroupmemberships-memberid): {{
    MemberId}}
```

## Properties
<a name="aws-resource-identitystore-allgroupmemberships-properties"></a>

`GroupId`  <a name="cfn-identitystore-allgroupmemberships-groupid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityStoreId`  <a name="cfn-identitystore-allgroupmemberships-identitystoreid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemberId`  <a name="cfn-identitystore-allgroupmemberships-memberid"></a>
An object containing the identifier of a group member.
*Required*: No
*Type*: [MemberId](aws-properties-identitystore-allgroupmemberships-memberid.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-identitystore-allgroupmemberships-return-values"></a>

### Ref
<a name="aws-resource-identitystore-allgroupmemberships-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-identitystore-allgroupmemberships-return-values-fn--getatt"></a>

####
<a name="aws-resource-identitystore-allgroupmemberships-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
Property description not available.

`MembershipId`  <a name="MembershipId-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.

`UpdatedBy`  <a name="UpdatedBy-fn::getatt"></a>
Property description not available.
