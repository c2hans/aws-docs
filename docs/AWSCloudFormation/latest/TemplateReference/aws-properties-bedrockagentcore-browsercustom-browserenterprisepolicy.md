---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-browsercustom-browserenterprisepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom BrowserEnterprisePolicy
<a name="aws-properties-bedrockagentcore-browsercustom-browserenterprisepolicy"></a>

Browser enterprise policy configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-browsercustom-browserenterprisepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-browsercustom-browserenterprisepolicy-syntax.json"></a>

```
{
  "[Location](#cfn-bedrockagentcore-browsercustom-browserenterprisepolicy-location)" : {{S3Location}},
  "[Type](#cfn-bedrockagentcore-browsercustom-browserenterprisepolicy-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-browsercustom-browserenterprisepolicy-syntax.yaml"></a>

```
  [Location](#cfn-bedrockagentcore-browsercustom-browserenterprisepolicy-location): {{
    S3Location}}
  [Type](#cfn-bedrockagentcore-browsercustom-browserenterprisepolicy-type): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-browsercustom-browserenterprisepolicy-properties"></a>

`Location`  <a name="cfn-bedrockagentcore-browsercustom-browserenterprisepolicy-location"></a>
The location of the enterprise policy file.
*Required*: Yes
*Type*: [S3Location](aws-properties-bedrockagentcore-browsercustom-s3location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-bedrockagentcore-browsercustom-browserenterprisepolicy-type"></a>
The type of browser enterprise policy. Available values are `MANAGED` and `RECOMMENDED`.
*Required*: Yes
*Type*: String
*Allowed values*: `MANAGED | RECOMMENDED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
