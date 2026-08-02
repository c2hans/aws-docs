---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-identitystore-allgroupmemberships-memberid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IdentityStore::AllGroupMemberships MemberId
<a name="aws-properties-identitystore-allgroupmemberships-memberid"></a>

An object containing the identifier of a group member.

## Syntax
<a name="aws-properties-identitystore-allgroupmemberships-memberid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-identitystore-allgroupmemberships-memberid-syntax.json"></a>

```
{
  "[UserId](#cfn-identitystore-allgroupmemberships-memberid-userid)" : {{String}}
}
```

### YAML
<a name="aws-properties-identitystore-allgroupmemberships-memberid-syntax.yaml"></a>

```
  [UserId](#cfn-identitystore-allgroupmemberships-memberid-userid): {{String}}
```

## Properties
<a name="aws-properties-identitystore-allgroupmemberships-memberid-properties"></a>

`UserId`  <a name="cfn-identitystore-allgroupmemberships-memberid-userid"></a>
An object containing the identifiers of resources that can be members.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `47`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
