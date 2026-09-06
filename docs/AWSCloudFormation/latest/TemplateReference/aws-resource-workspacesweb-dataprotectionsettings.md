---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspacesweb-dataprotectionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::DataProtectionSettings
<a name="aws-resource-workspacesweb-dataprotectionsettings"></a>

The data protection settings resource that can be associated with a web portal.

## Syntax
<a name="aws-resource-workspacesweb-dataprotectionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspacesweb-dataprotectionsettings-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpacesWeb::DataProtectionSettings",
  "Properties" : {
      "[AdditionalEncryptionContext](#cfn-workspacesweb-dataprotectionsettings-additionalencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[CustomerManagedKey](#cfn-workspacesweb-dataprotectionsettings-customermanagedkey)" : {{String}},
      "[Description](#cfn-workspacesweb-dataprotectionsettings-description)" : {{String}},
      "[DisplayName](#cfn-workspacesweb-dataprotectionsettings-displayname)" : {{String}},
      "[InlineRedactionConfiguration](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration)" : {{InlineRedactionConfiguration}},
      "[Tags](#cfn-workspacesweb-dataprotectionsettings-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-workspacesweb-dataprotectionsettings-syntax.yaml"></a>

```
Type: AWS::WorkSpacesWeb::DataProtectionSettings
Properties:
  [AdditionalEncryptionContext](#cfn-workspacesweb-dataprotectionsettings-additionalencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [CustomerManagedKey](#cfn-workspacesweb-dataprotectionsettings-customermanagedkey): {{String}}
  [Description](#cfn-workspacesweb-dataprotectionsettings-description): {{String}}
  [DisplayName](#cfn-workspacesweb-dataprotectionsettings-displayname): {{String}}
  [InlineRedactionConfiguration](#cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration): {{
    InlineRedactionConfiguration}}
  [Tags](#cfn-workspacesweb-dataprotectionsettings-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-workspacesweb-dataprotectionsettings-properties"></a>

`AdditionalEncryptionContext`  <a name="cfn-workspacesweb-dataprotectionsettings-additionalencryptioncontext"></a>
The additional encryption context of the data protection settings.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomerManagedKey`  <a name="cfn-workspacesweb-dataprotectionsettings-customermanagedkey"></a>
The customer managed key used to encrypt sensitive information in the data protection settings.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-workspacesweb-dataprotectionsettings-description"></a>
The description of the data protection settings.
*Required*: No
*Type*: String
*Pattern*: `^[ _\-\d\w]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-workspacesweb-dataprotectionsettings-displayname"></a>
The display name of the data protection settings.
*Required*: No
*Type*: String
*Pattern*: `^[ _\-\d\w]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InlineRedactionConfiguration`  <a name="cfn-workspacesweb-dataprotectionsettings-inlineredactionconfiguration"></a>
The inline redaction configuration for the data protection settings.
*Required*: No
*Type*: [InlineRedactionConfiguration](aws-properties-workspacesweb-dataprotectionsettings-inlineredactionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-workspacesweb-dataprotectionsettings-tags"></a>
The tags of the data protection settings.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspacesweb-dataprotectionsettings-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspacesweb-dataprotectionsettings-return-values"></a>

### Ref
<a name="aws-resource-workspacesweb-dataprotectionsettings-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-workspacesweb-dataprotectionsettings-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspacesweb-dataprotectionsettings-return-values-fn--getatt-fn--getatt"></a>

`AssociatedPortalArns`  <a name="AssociatedPortalArns-fn::getatt"></a>
A list of web portal ARNs that this data protection settings resource is associated with.

`CreationDate`  <a name="CreationDate-fn::getatt"></a>
The creation date timestamp of the data protection settings.

`DataProtectionSettingsArn`  <a name="DataProtectionSettingsArn-fn::getatt"></a>
The ARN of the data protection settings resource.
