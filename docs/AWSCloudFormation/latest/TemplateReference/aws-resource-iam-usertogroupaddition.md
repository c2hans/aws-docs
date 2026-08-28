---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::UserToGroupAddition
<a name="aws-resource-iam-usertogroupaddition"></a>

Adds the specified user to the specified group.

## Syntax
<a name="aws-resource-iam-usertogroupaddition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iam-usertogroupaddition-syntax.json"></a>

```
{
  "Type" : "AWS::IAM::UserToGroupAddition",
  "Properties" : {
      "[GroupName](#cfn-iam-usertogroupaddition-groupname)" : {{String}},
      "[Users](#cfn-iam-usertogroupaddition-users)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iam-usertogroupaddition-syntax.yaml"></a>

```
Type: AWS::IAM::UserToGroupAddition
Properties:
  [GroupName](#cfn-iam-usertogroupaddition-groupname): {{String}}
  [Users](#cfn-iam-usertogroupaddition-users): {{
    - String}}
```

## Properties
<a name="aws-resource-iam-usertogroupaddition-properties"></a>

`GroupName`  <a name="cfn-iam-usertogroupaddition-groupname"></a>
The name of the group to update.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
*Required*: Yes
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Users`  <a name="cfn-iam-usertogroupaddition-users"></a>
A list of the names of the users that you want to add to the group.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iam-usertogroupaddition-return-values"></a>

### Ref
<a name="aws-resource-iam-usertogroupaddition-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns the resource name.

For example:

 `{ "Ref": "MyUserToGroupAddition" }`

For the `AWS::IAM::UserToGroupAddition` resource with the logical ID `MyUserToGroupAddition`, `Ref` will return the AWS resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iam-usertogroupaddition-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iam-usertogroupaddition-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
 The stable and unique string identifying the group. For more information about IDs, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.

## See also
<a name="aws-resource-iam-usertogroupaddition--seealso"></a>
+ To view `AWS::IAM::UserToGroupAddition` template example snippets, see [Add Users to a Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-addusertogroup).
+ [AddUserToGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddUserToGroup.html) in the *AWS Identity and Access Management API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
