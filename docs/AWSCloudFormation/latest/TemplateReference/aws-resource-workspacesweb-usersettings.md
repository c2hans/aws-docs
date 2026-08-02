---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspacesweb-usersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::UserSettings
<a name="aws-resource-workspacesweb-usersettings"></a>

This resource specifies user settings that can be associated with a web portal. Once associated with a web portal, user settings control how users can transfer data between a streaming session and the their local devices.

## Syntax
<a name="aws-resource-workspacesweb-usersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspacesweb-usersettings-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpacesWeb::UserSettings",
  "Properties" : {
      "[AdditionalEncryptionContext](#cfn-workspacesweb-usersettings-additionalencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[BrandingConfiguration](#cfn-workspacesweb-usersettings-brandingconfiguration)" : {{BrandingConfiguration}},
      "[CookieSynchronizationConfiguration](#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration)" : {{CookieSynchronizationConfiguration}},
      "[CopyAllowed](#cfn-workspacesweb-usersettings-copyallowed)" : {{String}},
      "[CustomerManagedKey](#cfn-workspacesweb-usersettings-customermanagedkey)" : {{String}},
      "[DeepLinkAllowed](#cfn-workspacesweb-usersettings-deeplinkallowed)" : {{String}},
      "[DisconnectTimeoutInMinutes](#cfn-workspacesweb-usersettings-disconnecttimeoutinminutes)" : {{Number}},
      "[DownloadAllowed](#cfn-workspacesweb-usersettings-downloadallowed)" : {{String}},
      "[IdleDisconnectTimeoutInMinutes](#cfn-workspacesweb-usersettings-idledisconnecttimeoutinminutes)" : {{Number}},
      "[PasteAllowed](#cfn-workspacesweb-usersettings-pasteallowed)" : {{String}},
      "[PrintAllowed](#cfn-workspacesweb-usersettings-printallowed)" : {{String}},
      "[Tags](#cfn-workspacesweb-usersettings-tags)" : {{[ Tag, ... ]}},
      "[ToolbarConfiguration](#cfn-workspacesweb-usersettings-toolbarconfiguration)" : {{ToolbarConfiguration}},
      "[UploadAllowed](#cfn-workspacesweb-usersettings-uploadallowed)" : {{String}},
      "[WebAuthnAllowed](#cfn-workspacesweb-usersettings-webauthnallowed)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-workspacesweb-usersettings-syntax.yaml"></a>

```
Type: AWS::WorkSpacesWeb::UserSettings
Properties:
  [AdditionalEncryptionContext](#cfn-workspacesweb-usersettings-additionalencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [BrandingConfiguration](#cfn-workspacesweb-usersettings-brandingconfiguration): {{
    BrandingConfiguration}}
  [CookieSynchronizationConfiguration](#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration): {{
    CookieSynchronizationConfiguration}}
  [CopyAllowed](#cfn-workspacesweb-usersettings-copyallowed): {{String}}
  [CustomerManagedKey](#cfn-workspacesweb-usersettings-customermanagedkey): {{String}}
  [DeepLinkAllowed](#cfn-workspacesweb-usersettings-deeplinkallowed): {{String}}
  [DisconnectTimeoutInMinutes](#cfn-workspacesweb-usersettings-disconnecttimeoutinminutes): {{Number}}
  [DownloadAllowed](#cfn-workspacesweb-usersettings-downloadallowed): {{String}}
  [IdleDisconnectTimeoutInMinutes](#cfn-workspacesweb-usersettings-idledisconnecttimeoutinminutes): {{Number}}
  [PasteAllowed](#cfn-workspacesweb-usersettings-pasteallowed): {{String}}
  [PrintAllowed](#cfn-workspacesweb-usersettings-printallowed): {{String}}
  [Tags](#cfn-workspacesweb-usersettings-tags): {{
    - Tag}}
  [ToolbarConfiguration](#cfn-workspacesweb-usersettings-toolbarconfiguration): {{
    ToolbarConfiguration}}
  [UploadAllowed](#cfn-workspacesweb-usersettings-uploadallowed): {{String}}
  [WebAuthnAllowed](#cfn-workspacesweb-usersettings-webauthnallowed): {{String}}
```

## Properties
<a name="aws-resource-workspacesweb-usersettings-properties"></a>

`AdditionalEncryptionContext`  <a name="cfn-workspacesweb-usersettings-additionalencryptioncontext"></a>
The additional encryption context of the user settings.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BrandingConfiguration`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration"></a>
The branding configuration that customizes the appearance of the web portal for end users. This includes a custom logo, favicon, localized strings, color theme, and optionally a wallpaper and terms of service.
*Required*: No
*Type*: [BrandingConfiguration](aws-properties-workspacesweb-usersettings-brandingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CookieSynchronizationConfiguration`  <a name="cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration"></a>
The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.
*Required*: No
*Type*: [CookieSynchronizationConfiguration](aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CopyAllowed`  <a name="cfn-workspacesweb-usersettings-copyallowed"></a>
Specifies whether the user can copy text from the streaming session to the local device.
*Required*: Yes
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomerManagedKey`  <a name="cfn-workspacesweb-usersettings-customermanagedkey"></a>
The customer managed key used to encrypt sensitive information in the user settings.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeepLinkAllowed`  <a name="cfn-workspacesweb-usersettings-deeplinkallowed"></a>
Specifies whether the user can use deep links that open automatically when connecting to a session.
*Required*: No
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisconnectTimeoutInMinutes`  <a name="cfn-workspacesweb-usersettings-disconnecttimeoutinminutes"></a>
The amount of time that a streaming session remains active after users disconnect.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DownloadAllowed`  <a name="cfn-workspacesweb-usersettings-downloadallowed"></a>
Specifies whether the user can download files from the streaming session to the local device.
*Required*: Yes
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdleDisconnectTimeoutInMinutes`  <a name="cfn-workspacesweb-usersettings-idledisconnecttimeoutinminutes"></a>
The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PasteAllowed`  <a name="cfn-workspacesweb-usersettings-pasteallowed"></a>
Specifies whether the user can paste text from the local device to the streaming session.
*Required*: Yes
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrintAllowed`  <a name="cfn-workspacesweb-usersettings-printallowed"></a>
Specifies whether the user can print to the local device.
*Required*: Yes
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-workspacesweb-usersettings-tags"></a>
The tags to add to the user settings resource. A tag is a key-value pair.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspacesweb-usersettings-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolbarConfiguration`  <a name="cfn-workspacesweb-usersettings-toolbarconfiguration"></a>
The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.
*Required*: No
*Type*: [ToolbarConfiguration](aws-properties-workspacesweb-usersettings-toolbarconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UploadAllowed`  <a name="cfn-workspacesweb-usersettings-uploadallowed"></a>
Specifies whether the user can upload files from the local device to the streaming session.
*Required*: Yes
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebAuthnAllowed`  <a name="cfn-workspacesweb-usersettings-webauthnallowed"></a>
Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.
*Required*: No
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspacesweb-usersettings-return-values"></a>

### Ref
<a name="aws-resource-workspacesweb-usersettings-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource's Amazon Resource Name (ARN).

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-workspacesweb-usersettings-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspacesweb-usersettings-return-values-fn--getatt-fn--getatt"></a>

`AssociatedPortalArns`  <a name="AssociatedPortalArns-fn::getatt"></a>
A list of web portal ARNs that this user settings resource is associated with.

`UserSettingsArn`  <a name="UserSettingsArn-fn::getatt"></a>
The ARN of the user settings.
