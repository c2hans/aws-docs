---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-usersetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory UserSetting
<a name="aws-properties-workspaces-directory-usersetting"></a>

Information about the user's permission settings.

## Syntax
<a name="aws-properties-workspaces-directory-usersetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-usersetting-syntax.json"></a>

```
{
  "[Action](#cfn-workspaces-directory-usersetting-action)" : {{String}},
  "[MaximumLength](#cfn-workspaces-directory-usersetting-maximumlength)" : {{Integer}},
  "[Permission](#cfn-workspaces-directory-usersetting-permission)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-usersetting-syntax.yaml"></a>

```
  [Action](#cfn-workspaces-directory-usersetting-action): {{String}}
  [MaximumLength](#cfn-workspaces-directory-usersetting-maximumlength): {{Integer}}
  [Permission](#cfn-workspaces-directory-usersetting-permission): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-usersetting-properties"></a>

`Action`  <a name="cfn-workspaces-directory-usersetting-action"></a>
Indicates the type of action.
*Required*: Yes
*Type*: String
*Allowed values*: `CLIPBOARD_COPY_FROM_LOCAL_DEVICE | CLIPBOARD_COPY_TO_LOCAL_DEVICE | PRINTING_TO_LOCAL_DEVICE | SMART_CARD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumLength`  <a name="cfn-workspaces-directory-usersetting-maximumlength"></a>
Indicates the maximum character length for the specified user setting.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permission`  <a name="cfn-workspaces-directory-usersetting-permission"></a>
Indicates if the setting is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
