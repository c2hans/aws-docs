---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-contentredirection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack ContentRedirection

Configuration for bidirectional URL redirection between the streaming session and the local client. Use HostToClient to redirect URLs from the remote desktop to the local browser.

## Syntax
<a name="aws-properties-appstream-stack-contentredirection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-contentredirection-syntax.json"></a>

```
{
  "[HostToClient](#cfn-appstream-stack-contentredirection-hosttoclient)" : {{UrlRedirectionConfig}}
}
```

### YAML
<a name="aws-properties-appstream-stack-contentredirection-syntax.yaml"></a>

```
  [HostToClient](#cfn-appstream-stack-contentredirection-hosttoclient): {{
    UrlRedirectionConfig}}
```

## Properties
<a name="aws-properties-appstream-stack-contentredirection-properties"></a>

`HostToClient`  <a name="cfn-appstream-stack-contentredirection-hosttoclient"></a>
Configuration for redirecting URLs from the remote desktop to the local client browser.
*Required*: No
*Type*: [UrlRedirectionConfig](aws-properties-appstream-stack-urlredirectionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
