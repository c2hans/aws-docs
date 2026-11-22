---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-urlredirectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack UrlRedirectionConfig

Configuration for URL redirection in a specific direction (host-to-client or client-to-host). When enabled, URLs matching the allowed or denied patterns are redirected accordingly. The denied list takes precedence over the allowed list.

## Syntax
<a name="aws-properties-appstream-stack-urlredirectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-urlredirectionconfig-syntax.json"></a>

```json
{
  "[AllowedUrls](#cfn-appstream-stack-urlredirectionconfig-allowedurls)" : {{[ String, ... ]}},
  "[DeniedUrls](#cfn-appstream-stack-urlredirectionconfig-deniedurls)" : {{[ String, ... ]}},
  "[Enabled](#cfn-appstream-stack-urlredirectionconfig-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-appstream-stack-urlredirectionconfig-syntax.yaml"></a>

```yaml
  [AllowedUrls](#cfn-appstream-stack-urlredirectionconfig-allowedurls): {{
    - String}}
  [DeniedUrls](#cfn-appstream-stack-urlredirectionconfig-deniedurls): {{
    - String}}
  [Enabled](#cfn-appstream-stack-urlredirectionconfig-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-appstream-stack-urlredirectionconfig-properties"></a>

`AllowedUrls`  <a name="cfn-appstream-stack-urlredirectionconfig-allowedurls"></a>
List of URL patterns that are allowed to be redirected. URLs matching these patterns will be redirected unless they also match a pattern in the denied list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeniedUrls`  <a name="cfn-appstream-stack-urlredirectionconfig-deniedurls"></a>
List of URL patterns that are denied from redirection. This list takes precedence over the allowed list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-appstream-stack-urlredirectionconfig-enabled"></a>
Whether URL redirection is enabled for this direction.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
