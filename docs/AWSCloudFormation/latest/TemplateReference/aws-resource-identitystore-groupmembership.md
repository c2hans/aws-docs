---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-identitystore-groupmembership.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IdentityStore::GroupMembership
<a name="aws-resource-identitystore-groupmembership"></a>

Creates a relationship between a member and a group. The following identifiers must be specified: `GroupId`, `IdentityStoreId`, and `MemberId`.

## Syntax
<a name="aws-resource-identitystore-groupmembership-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-identitystore-groupmembership-syntax.json"></a>

```
{
  "Type" : "AWS::IdentityStore::GroupMembership",
  "Properties" : {
      "[GroupId](#cfn-identitystore-groupmembership-groupid)" : {{String}},
      "[IdentityStoreId](#cfn-identitystore-groupmembership-identitystoreid)" : {{String}},
      "[MemberId](#cfn-identitystore-groupmembership-memberid)" : {{MemberId}}
    }
}
```

### YAML
<a name="aws-resource-identitystore-groupmembership-syntax.yaml"></a>

```
Type: AWS::IdentityStore::GroupMembership
Properties:
  [GroupId](#cfn-identitystore-groupmembership-groupid): {{String}}
  [IdentityStoreId](#cfn-identitystore-groupmembership-identitystoreid): {{String}}
  [MemberId](#cfn-identitystore-groupmembership-memberid): {{
    MemberId}}
```

## Properties
<a name="aws-resource-identitystore-groupmembership-properties"></a>

`GroupId`  <a name="cfn-identitystore-groupmembership-groupid"></a>
The identifier for a group in the identity store.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityStoreId`  <a name="cfn-identitystore-groupmembership-identitystoreid"></a>
The globally unique identifier for the identity store.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemberId`  <a name="cfn-identitystore-groupmembership-memberid"></a>
An object containing the identifier of a group member. Setting the `MemberId`'s `UserId` field to a specific User's ID indicates that user is a member of the group.
*Required*: Yes
*Type*: [MemberId](aws-properties-identitystore-groupmembership-memberid.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-identitystore-groupmembership-return-values"></a>

### Ref
<a name="aws-resource-identitystore-groupmembership-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `Physical ID` of the resource created which is the format `GroupMembershipID|IdentityStoreId`.

### Fn::GetAtt
<a name="aws-resource-identitystore-groupmembership-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-identitystore-groupmembership-return-values-fn--getatt-fn--getatt"></a>

`MembershipId`  <a name="MembershipId-fn::getatt"></a>
The identifier for a `GroupMembership` in the identity store.

## Examples
<a name="aws-resource-identitystore-groupmembership--examples"></a>

### Declare a Identity Store Resource
<a name="aws-resource-identitystore-groupmembership--examples--Declare_a_Identity_Store_Resource"></a>

The following example shows how to create a Identity Store `Group Membership` resource:

#### JSON
<a name="aws-resource-identitystore-groupmembership--examples--Declare_a_Identity_Store_Resource--json"></a>

```
{
  "Type": "AWS::IdentityStore::GroupMembership",
  "Properties": {
    "GroupId": {
      "description": "g-1111111111-2222-3333-4444-5555-6666666656",
    },
    "IdentityStoreId": {
      "description": "d-1111111111",
    },
    "MemberId": {
      "description": "m-1111111112-2222-3333-4444-5555-6666666656",
    }
  }
```

#### YAML
<a name="aws-resource-identitystore-groupmembership--examples--Declare_a_Identity_Store_Resource--yaml"></a>

```
Type: AWS::IdentityStore::GroupMembership
    Properties:
      GroupId: "g-1111111111-2222-3333-4444-5555-6666666656"
      IdentityStoreId: "d-1111111111"
      MemberId: "m-1111111112-2222-3333-4444-5555-6666666656"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
