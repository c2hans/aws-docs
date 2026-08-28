---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-urlredirectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack UrlRedirectionConfig
<a name="aws-properties-appstream-stack-urlredirectionconfig"></a>

<a name="aws-properties-appstream-stack-urlredirectionconfig-description"></a>The `UrlRedirectionConfig` property type specifies Property description not available. for an [AWS::AppStream::Stack](aws-resource-appstream-stack.md).

## Syntax
<a name="aws-properties-appstream-stack-urlredirectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-urlredirectionconfig-syntax.json"></a>

```
{
  "[AllowedUrls](#cfn-appstream-stack-urlredirectionconfig-allowedurls)" : {{[ String, ... ]}},
  "[DeniedUrls](#cfn-appstream-stack-urlredirectionconfig-deniedurls)" : {{[ String, ... ]}},
  "[Enabled](#cfn-appstream-stack-urlredirectionconfig-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-appstream-stack-urlredirectionconfig-syntax.yaml"></a>

```
  [AllowedUrls](#cfn-appstream-stack-urlredirectionconfig-allowedurls): {{
    - String}}
  [DeniedUrls](#cfn-appstream-stack-urlredirectionconfig-deniedurls): {{
    - String}}
  [Enabled](#cfn-appstream-stack-urlredirectionconfig-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-appstream-stack-urlredirectionconfig-properties"></a>

`AllowedUrls`  <a name="cfn-appstream-stack-urlredirectionconfig-allowedurls"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeniedUrls`  <a name="cfn-appstream-stack-urlredirectionconfig-deniedurls"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-appstream-stack-urlredirectionconfig-enabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
