---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-browsersettings-webcontentfilteringpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::BrowserSettings WebContentFilteringPolicy
<a name="aws-properties-workspacesweb-browsersettings-webcontentfilteringpolicy"></a>

The policy that specifies which URLs end users are allowed to access or which URLs or domain categories they are restricted from accessing for enhanced security.

## Syntax
<a name="aws-properties-workspacesweb-browsersettings-webcontentfilteringpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-browsersettings-webcontentfilteringpolicy-syntax.json"></a>

```
{
  "[AllowedUrls](#cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-allowedurls)" : {{[ String, ... ]}},
  "[BlockedCategories](#cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-blockedcategories)" : {{[ String, ... ]}},
  "[BlockedUrls](#cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-blockedurls)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-workspacesweb-browsersettings-webcontentfilteringpolicy-syntax.yaml"></a>

```
  [AllowedUrls](#cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-allowedurls): {{
    - String}}
  [BlockedCategories](#cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-blockedcategories): {{
    - String}}
  [BlockedUrls](#cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-blockedurls): {{
    - String}}
```

## Properties
<a name="aws-properties-workspacesweb-browsersettings-webcontentfilteringpolicy-properties"></a>

`AllowedUrls`  <a name="cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-allowedurls"></a>
URLs and domains that are always accessible to end users.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockedCategories`  <a name="cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-blockedcategories"></a>
Categories of websites that are blocked on the end user's browsers.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockedUrls`  <a name="cfn-workspacesweb-browsersettings-webcontentfilteringpolicy-blockedurls"></a>
URLs and domains that end users cannot access.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
