---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolusertogroupattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolUserToGroupAttachment
<a name="aws-resource-cognito-userpoolusertogroupattachment"></a>

Adds a user to a group. A user who is in a group can present a preferred-role claim to an identity pool, and populates a `cognito:groups` claim to their access and identity tokens.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Syntax
<a name="aws-resource-cognito-userpoolusertogroupattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-userpoolusertogroupattachment-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::UserPoolUserToGroupAttachment",
  "Properties" : {
      "[GroupName](#cfn-cognito-userpoolusertogroupattachment-groupname)" : {{String}},
      "[Username](#cfn-cognito-userpoolusertogroupattachment-username)" : {{String}},
      "[UserPoolId](#cfn-cognito-userpoolusertogroupattachment-userpoolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-userpoolusertogroupattachment-syntax.yaml"></a>

```
Type: AWS::Cognito::UserPoolUserToGroupAttachment
Properties:
  [GroupName](#cfn-cognito-userpoolusertogroupattachment-groupname): {{String}}
  [Username](#cfn-cognito-userpoolusertogroupattachment-username): {{String}}
  [UserPoolId](#cfn-cognito-userpoolusertogroupattachment-userpoolid): {{String}}
```

## Properties
<a name="aws-resource-cognito-userpoolusertogroupattachment-properties"></a>

`GroupName`  <a name="cfn-cognito-userpoolusertogroupattachment-groupname"></a>
The name of the group that you want to add your user to.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Username`  <a name="cfn-cognito-userpoolusertogroupattachment-username"></a>
The user's username.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserPoolId`  <a name="cfn-cognito-userpoolusertogroupattachment-userpoolid"></a>
The ID of the user pool that contains the group that you want to add the user to.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-userpoolusertogroupattachment-return-values"></a>

### Ref
<a name="aws-resource-cognito-userpoolusertogroupattachment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a generated ID, such as `UserToGroupAttachment-YejJvzrEXAMPLE`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-cognito-userpoolusertogroupattachment--examples"></a>

### Adding users to a group
<a name="aws-resource-cognito-userpoolusertogroupattachment--examples--Adding_users_to_a_group"></a>

The following template adds the users "testuser1" and "testuser2" to the user group "ExampleGroup" in the requested user pool.

#### JSON
<a name="aws-resource-cognito-userpoolusertogroupattachment--examples--Adding_users_to_a_group--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Add a user to a group in an Amazon Cognito user pool\n",
    "Resources": {
        "TestUser2ToExampleGroup": {
            "Properties": {
                "GroupName": "ExampleGroup",
                "Username": "testuser1",
                "UserPoolId": "us-west-2_EXAMPLE"
            },
            "Type": "AWS::Cognito::UserPoolUserToGroupAttachment"
        },
        "TestUserToExampleGroup": {
            "Properties": {
                "GroupName": "ExampleGroup",
                "Username": "testuser2",
                "UserPoolId": "us-west-2_EXAMPLE"
            },
            "Type": "AWS::Cognito::UserPoolUserToGroupAttachment"
        }
    }
}
```

#### YAML
<a name="aws-resource-cognito-userpoolusertogroupattachment--examples--Adding_users_to_a_group--yaml"></a>

```
AWSTemplateFormatVersion: "2010-09-09"

Description: |
  Add a user to a group in an Amazon Cognito user pool

Resources:
  TestUser2ToExampleGroup:
    Type: AWS::Cognito::UserPoolUserToGroupAttachment
    Properties:
      GroupName: ExampleGroup
      Username: testuser1
      UserPoolId: us-west-2_EXAMPLE

  TestUserToExampleGroup:
    Type: AWS::Cognito::UserPoolUserToGroupAttachment
    Properties:
      GroupName: ExampleGroup
      Username: testuser2
      UserPoolId: us-west-2_EXAMPLE
```
