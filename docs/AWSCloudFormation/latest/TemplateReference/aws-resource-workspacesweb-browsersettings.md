---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspacesweb-browsersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::BrowserSettings
<a name="aws-resource-workspacesweb-browsersettings"></a>

This resource specifies browser settings that can be associated with a web portal. Once associated with a web portal, browser settings control how the browser will behave once a user starts a streaming session for the web portal.

## Syntax
<a name="aws-resource-workspacesweb-browsersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspacesweb-browsersettings-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpacesWeb::BrowserSettings",
  "Properties" : {
      "[AdditionalEncryptionContext](#cfn-workspacesweb-browsersettings-additionalencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[BrowserPolicy](#cfn-workspacesweb-browsersettings-browserpolicy)" : {{String}},
      "[CustomerManagedKey](#cfn-workspacesweb-browsersettings-customermanagedkey)" : {{String}},
      "[Tags](#cfn-workspacesweb-browsersettings-tags)" : {{[ Tag, ... ]}},
      "[WebContentFilteringPolicy](#cfn-workspacesweb-browsersettings-webcontentfilteringpolicy)" : {{WebContentFilteringPolicy}}
    }
}
```

### YAML
<a name="aws-resource-workspacesweb-browsersettings-syntax.yaml"></a>

```
Type: AWS::WorkSpacesWeb::BrowserSettings
Properties:
  [AdditionalEncryptionContext](#cfn-workspacesweb-browsersettings-additionalencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [BrowserPolicy](#cfn-workspacesweb-browsersettings-browserpolicy): {{String}}
  [CustomerManagedKey](#cfn-workspacesweb-browsersettings-customermanagedkey): {{String}}
  [Tags](#cfn-workspacesweb-browsersettings-tags): {{
    - Tag}}
  [WebContentFilteringPolicy](#cfn-workspacesweb-browsersettings-webcontentfilteringpolicy): {{
    WebContentFilteringPolicy}}
```

## Properties
<a name="aws-resource-workspacesweb-browsersettings-properties"></a>

`AdditionalEncryptionContext`  <a name="cfn-workspacesweb-browsersettings-additionalencryptioncontext"></a>
Additional encryption context of the browser settings.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BrowserPolicy`  <a name="cfn-workspacesweb-browsersettings-browserpolicy"></a>
A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions.
*Required*: No
*Type*: String
*Pattern*: `^\{[\S\s]*\}\s*$`
*Minimum*: `2`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomerManagedKey`  <a name="cfn-workspacesweb-browsersettings-customermanagedkey"></a>
The custom managed key of the browser settings.
*Pattern*: `^arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+$`
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-workspacesweb-browsersettings-tags"></a>
The tags to add to the browser settings resource. A tag is a key-value pair.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspacesweb-browsersettings-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebContentFilteringPolicy`  <a name="cfn-workspacesweb-browsersettings-webcontentfilteringpolicy"></a>
The policy that specifies which URLs end users are allowed to access or which URLs or domain categories they are restricted from accessing for enhanced security.
*Required*: No
*Type*: [WebContentFilteringPolicy](aws-properties-workspacesweb-browsersettings-webcontentfilteringpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspacesweb-browsersettings-return-values"></a>

### Ref
<a name="aws-resource-workspacesweb-browsersettings-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource's Amazon Resource Name (ARN).

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-workspacesweb-browsersettings-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspacesweb-browsersettings-return-values-fn--getatt-fn--getatt"></a>

`AssociatedPortalArns`  <a name="AssociatedPortalArns-fn::getatt"></a>
A list of web portal ARNs that the browser settings resource is associated with.

`BrowserSettingsArn`  <a name="BrowserSettingsArn-fn::getatt"></a>
The ARN of the browser settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
