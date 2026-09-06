---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-identitystore-groupmembership-memberid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IdentityStore::GroupMembership MemberId
<a name="aws-properties-identitystore-groupmembership-memberid"></a>

An object that contains the identifier of a group member. Setting the `UserID` field to the specific identifier for a user indicates that the user is a member of the group.

## Syntax
<a name="aws-properties-identitystore-groupmembership-memberid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-identitystore-groupmembership-memberid-syntax.json"></a>

```
{
  "[UserId](#cfn-identitystore-groupmembership-memberid-userid)" : {{String}}
}
```

### YAML
<a name="aws-properties-identitystore-groupmembership-memberid-syntax.yaml"></a>

```
  [UserId](#cfn-identitystore-groupmembership-memberid-userid): {{String}}
```

## Properties
<a name="aws-properties-identitystore-groupmembership-memberid-properties"></a>

`UserId`  <a name="cfn-identitystore-groupmembership-memberid-userid"></a>
An object containing the identifiers of resources that can be members.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
