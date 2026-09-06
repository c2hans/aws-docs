---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolGroup
<a name="aws-resource-cognito-userpoolgroup"></a>

A user pool group. Contains details about the group and the way that it contributes to IAM role decisions with identity pools. Identity pools can make decisions about the IAM role to assign based on groups: users get credentials for the role associated with their highest-priority group.

## Syntax
<a name="aws-resource-cognito-userpoolgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-userpoolgroup-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::UserPoolGroup",
  "Properties" : {
      "[Description](#cfn-cognito-userpoolgroup-description)" : {{String}},
      "[GroupName](#cfn-cognito-userpoolgroup-groupname)" : {{String}},
      "[Precedence](#cfn-cognito-userpoolgroup-precedence)" : {{Integer}},
      "[RoleArn](#cfn-cognito-userpoolgroup-rolearn)" : {{String}},
      "[UserPoolId](#cfn-cognito-userpoolgroup-userpoolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-userpoolgroup-syntax.yaml"></a>

```
Type: AWS::Cognito::UserPoolGroup
Properties:
  [Description](#cfn-cognito-userpoolgroup-description): {{String}}
  [GroupName](#cfn-cognito-userpoolgroup-groupname): {{String}}
  [Precedence](#cfn-cognito-userpoolgroup-precedence): {{Integer}}
  [RoleArn](#cfn-cognito-userpoolgroup-rolearn): {{String}}
  [UserPoolId](#cfn-cognito-userpoolgroup-userpoolid): {{String}}
```

## Properties
<a name="aws-resource-cognito-userpoolgroup-properties"></a>

`Description`  <a name="cfn-cognito-userpoolgroup-description"></a>
A description of the group that you're creating.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupName`  <a name="cfn-cognito-userpoolgroup-groupname"></a>
A name for the group. This name must be unique in your user pool.
*Required*: No
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Precedence`  <a name="cfn-cognito-userpoolgroup-precedence"></a>
A non-negative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. Zero is the highest precedence value. Groups with lower `Precedence` values take precedence over groups with higher or null `Precedence` values. If a user belongs to two or more groups, it is the group with the lowest precedence value whose role ARN is given in the user's tokens for the `cognito:roles` and `cognito:preferred_role` claims.
Two groups can have the same `Precedence` value. If this happens, neither group takes precedence over the other. If two groups with the same `Precedence` have the same role ARN, that role is used in the `cognito:preferred_role` claim in tokens for users in each group. If the two groups have different role ARNs, the `cognito:preferred_role` claim isn't set in users' tokens.
The default `Precedence` value is null. The maximum `Precedence` value is `2^31-1`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-cognito-userpoolgroup-rolearn"></a>
The Amazon Resource Name (ARN) for the IAM role that you want to associate with the group. A group role primarily declares a preferred role for the credentials that you get from an identity pool. Amazon Cognito ID tokens have a `cognito:preferred_role` claim that presents the highest-precedence group that a user belongs to. Both ID and access tokens also contain a `cognito:groups` claim that list all the groups that a user is a member of.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-userpoolgroup-userpoolid"></a>
The ID of the user pool where you want to create a user group.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-userpoolgroup-return-values"></a>

### Ref
<a name="aws-resource-cognito-userpoolgroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the user pool group. For example: `Admins`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-cognito-userpoolgroup--examples"></a>

### Creating a new user group in a user pool
<a name="aws-resource-cognito-userpoolgroup--examples--Creating_a_new_user_group_in_a_user_pool"></a>

The following example creates a group named "ExampleGroup" with an IAM role and a precedence of 1.

#### JSON
<a name="aws-resource-cognito-userpoolgroup--examples--Creating_a_new_user_group_in_a_user_pool--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Provision a new user group to an Amazon Cognito user pool\n",
    "Resources": {
        "ExampleGroup": {
            "Properties": {
                "Description": "My Example Group",
                "GroupName": "ExampleGroup",
                "Precedence": 1,
                "RoleArn": "arn:aws:iam::123456789012:role/my-test-cognito-role",
                "UserPoolId": "us-west-2_EXAMPLE"
            },
            "Type": "AWS::Cognito::UserPoolGroup"
        }
    }
}
```

#### YAML
<a name="aws-resource-cognito-userpoolgroup--examples--Creating_a_new_user_group_in_a_user_pool--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"

Description: |
  Provision a new user group to an Amazon Cognito user pool

Resources:
  ExampleGroup:
    Type: AWS::Cognito::UserPoolGroup
    Properties:
      Description: My Example Group
      GroupName: ExampleGroup
      Precedence: 1
      RoleArn: arn:aws:iam::123456789012:role/my-test-cognito-role
      UserPoolId: us-west-2_EXAMPLE
```
