---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-browsercustom-browsersigning.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom BrowserSigning
<a name="aws-properties-bedrockagentcore-browsercustom-browsersigning"></a>

Configuration for enabling browser signing capabilities that allow agents to cryptographically identify themselves to websites using HTTP message signatures.

## Syntax
<a name="aws-properties-bedrockagentcore-browsercustom-browsersigning-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-browsercustom-browsersigning-syntax.json"></a>

```
{
  "[Enabled](#cfn-bedrockagentcore-browsercustom-browsersigning-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-browsercustom-browsersigning-syntax.yaml"></a>

```
  [Enabled](#cfn-bedrockagentcore-browsercustom-browsersigning-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-bedrockagentcore-browsercustom-browsersigning-properties"></a>

`Enabled`  <a name="cfn-bedrockagentcore-browsercustom-browsersigning-enabled"></a>
Specifies whether browser signing is enabled. When enabled, the browser will cryptographically sign HTTP requests to identify itself as an AI agent to bot control vendors.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
