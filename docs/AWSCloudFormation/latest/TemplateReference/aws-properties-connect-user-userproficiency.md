---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-userproficiency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User UserProficiency
<a name="aws-properties-connect-user-userproficiency"></a>

**Note**
A predefined attribute must be created before using `UserProficiencies` in the Cloudformation *User* template. For more information, see [Predefined attributes](https://docs.aws.amazon.com/connect/latest/adminguide/predefined-attributes.html).

Proficiency of a user.

## Syntax
<a name="aws-properties-connect-user-userproficiency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-userproficiency-syntax.json"></a>

```
{
  "[AttributeName](#cfn-connect-user-userproficiency-attributename)" : {{String}},
  "[AttributeValue](#cfn-connect-user-userproficiency-attributevalue)" : {{String}},
  "[Level](#cfn-connect-user-userproficiency-level)" : {{Number}}
}
```

### YAML
<a name="aws-properties-connect-user-userproficiency-syntax.yaml"></a>

```
  [AttributeName](#cfn-connect-user-userproficiency-attributename): {{String}}
  [AttributeValue](#cfn-connect-user-userproficiency-attributevalue): {{String}}
  [Level](#cfn-connect-user-userproficiency-level): {{Number}}
```

## Properties
<a name="aws-properties-connect-user-userproficiency-properties"></a>

`AttributeName`  <a name="cfn-connect-user-userproficiency-attributename"></a>
The name of user’s proficiency. You must use a predefined attribute name that is present in the Amazon Connect instance.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AttributeValue`  <a name="cfn-connect-user-userproficiency-attributevalue"></a>
The value of user’s proficiency. You must use a predefined attribute value that is present in the Amazon Connect instance.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-connect-user-userproficiency-level"></a>
The level of the proficiency. The valid values are 1, 2, 3, 4 and 5.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
