---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rolesanywhere-trustanchor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RolesAnywhere::TrustAnchor
<a name="aws-resource-rolesanywhere-trustanchor"></a>

 Creates a TrustAnchor.

## Syntax
<a name="aws-resource-rolesanywhere-trustanchor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rolesanywhere-trustanchor-syntax.json"></a>

```
{
  "Type" : "AWS::RolesAnywhere::TrustAnchor",
  "Properties" : {
      "[Enabled](#cfn-rolesanywhere-trustanchor-enabled)" : {{Boolean}},
      "[Name](#cfn-rolesanywhere-trustanchor-name)" : {{String}},
      "[NotificationSettings](#cfn-rolesanywhere-trustanchor-notificationsettings)" : {{[ NotificationSetting, ... ]}},
      "[Source](#cfn-rolesanywhere-trustanchor-source)" : {{Source}},
      "[Tags](#cfn-rolesanywhere-trustanchor-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rolesanywhere-trustanchor-syntax.yaml"></a>

```
Type: AWS::RolesAnywhere::TrustAnchor
Properties:
  [Enabled](#cfn-rolesanywhere-trustanchor-enabled): {{Boolean}}
  [Name](#cfn-rolesanywhere-trustanchor-name): {{String}}
  [NotificationSettings](#cfn-rolesanywhere-trustanchor-notificationsettings): {{
    - NotificationSetting}}
  [Source](#cfn-rolesanywhere-trustanchor-source): {{
    Source}}
  [Tags](#cfn-rolesanywhere-trustanchor-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rolesanywhere-trustanchor-properties"></a>

`Enabled`  <a name="cfn-rolesanywhere-trustanchor-enabled"></a>
Indicates whether the trust anchor is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-rolesanywhere-trustanchor-name"></a>
The name of the trust anchor.
*Required*: Yes
*Type*: String
*Pattern*: `[ a-zA-Z0-9-_]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationSettings`  <a name="cfn-rolesanywhere-trustanchor-notificationsettings"></a>
A list of notification settings to be associated to the trust anchor.
*Required*: No
*Type*: Array of [NotificationSetting](aws-properties-rolesanywhere-trustanchor-notificationsetting.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-rolesanywhere-trustanchor-source"></a>
The trust anchor type and its related certificate data.
*Required*: Yes
*Type*: [Source](aws-properties-rolesanywhere-trustanchor-source.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rolesanywhere-trustanchor-tags"></a>
The tags to attach to the trust anchor.
*Required*: No
*Type*: Array of [Tag](aws-properties-rolesanywhere-trustanchor-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rolesanywhere-trustanchor-return-values"></a>

### Ref
<a name="aws-resource-rolesanywhere-trustanchor-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`TrustAnchorId`.

### Fn::GetAtt
<a name="aws-resource-rolesanywhere-trustanchor-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rolesanywhere-trustanchor-return-values-fn--getatt-fn--getatt"></a>

`TrustAnchorArn`  <a name="TrustAnchorArn-fn::getatt"></a>
The ARN of the trust anchor.

`TrustAnchorId`  <a name="TrustAnchorId-fn::getatt"></a>
The unique identifier of the trust anchor.
