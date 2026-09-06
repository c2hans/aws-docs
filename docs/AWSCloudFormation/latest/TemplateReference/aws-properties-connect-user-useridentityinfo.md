---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-useridentityinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User UserIdentityInfo
<a name="aws-properties-connect-user-useridentityinfo"></a>

Contains information about the identity of a user.

**Note**
For Connect Customer instances that are created with the `EXISTING_DIRECTORY` identity management type, `FirstName`, `LastName`, and `Email` cannot be updated from within Connect Customer because they are managed by the directory.

**Important**
The `FirstName` and `LastName` length constraints below apply only to instances using SAML for identity management. If you are using Connect Customer for identity management, the length constraints are 1-255 for `FirstName`, and 1-256 for `LastName`.

## Syntax
<a name="aws-properties-connect-user-useridentityinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-useridentityinfo-syntax.json"></a>

```
{
  "[Email](#cfn-connect-user-useridentityinfo-email)" : {{String}},
  "[FirstName](#cfn-connect-user-useridentityinfo-firstname)" : {{String}},
  "[LastName](#cfn-connect-user-useridentityinfo-lastname)" : {{String}},
  "[Mobile](#cfn-connect-user-useridentityinfo-mobile)" : {{String}},
  "[SecondaryEmail](#cfn-connect-user-useridentityinfo-secondaryemail)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-user-useridentityinfo-syntax.yaml"></a>

```
  [Email](#cfn-connect-user-useridentityinfo-email): {{String}}
  [FirstName](#cfn-connect-user-useridentityinfo-firstname): {{String}}
  [LastName](#cfn-connect-user-useridentityinfo-lastname): {{String}}
  [Mobile](#cfn-connect-user-useridentityinfo-mobile): {{String}}
  [SecondaryEmail](#cfn-connect-user-useridentityinfo-secondaryemail): {{String}}
```

## Properties
<a name="aws-properties-connect-user-useridentityinfo-properties"></a>

`Email`  <a name="cfn-connect-user-useridentityinfo-email"></a>
The email address. If you are using SAML for identity management and include this parameter, an error is returned.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirstName`  <a name="cfn-connect-user-useridentityinfo-firstname"></a>
The first name. This is required if you are using Connect Customer or SAML for identity management. Inputs must be in Unicode Normalization Form C (NFC). Text containing characters in a non-NFC form (for example, decomposed characters or combining marks) are not accepted.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastName`  <a name="cfn-connect-user-useridentityinfo-lastname"></a>
The last name. This is required if you are using Connect Customer or SAML for identity management. Inputs must be in Unicode Normalization Form C (NFC). Text containing characters in a non-NFC form (for example, decomposed characters or combining marks) are not accepted.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mobile`  <a name="cfn-connect-user-useridentityinfo-mobile"></a>
The user's mobile number.
*Required*: No
*Type*: String
*Pattern*: `^\+[1-9]\d{1,14}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryEmail`  <a name="cfn-connect-user-useridentityinfo-secondaryemail"></a>
The user's secondary email address. If you provide a secondary email, the user receives email notifications -- other than password reset notifications -- to this email address instead of to their primary email address.
*Pattern*: `(?=^.{0,265}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}`
*Required*: No
*Type*: String
*Pattern*: `(?=^.{0,265}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
