---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-posixuser.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue PosixUser
<a name="aws-properties-deadline-queue-posixuser"></a>

The POSIX user.

## Syntax
<a name="aws-properties-deadline-queue-posixuser-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-posixuser-syntax.json"></a>

```
{
  "[Group](#cfn-deadline-queue-posixuser-group)" : {{String}},
  "[User](#cfn-deadline-queue-posixuser-user)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-queue-posixuser-syntax.yaml"></a>

```
  [Group](#cfn-deadline-queue-posixuser-group): {{String}}
  [User](#cfn-deadline-queue-posixuser-user): {{String}}
```

## Properties
<a name="aws-properties-deadline-queue-posixuser-properties"></a>

`Group`  <a name="cfn-deadline-queue-posixuser-group"></a>
The name of the POSIX user's group.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[a-z][a-z0-9-]{0,30})?$`
*Minimum*: `0`
*Maximum*: `31`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-deadline-queue-posixuser-user"></a>
The name of the POSIX user.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[a-z][a-z0-9-]{0,30})?$`
*Minimum*: `0`
*Maximum*: `31`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
