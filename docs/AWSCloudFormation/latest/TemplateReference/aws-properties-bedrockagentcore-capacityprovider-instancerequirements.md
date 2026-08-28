---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-instancerequirements.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider InstanceRequirements
<a name="aws-properties-bedrockagentcore-capacityprovider-instancerequirements"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-instancerequirements-description"></a>The `InstanceRequirements` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-instancerequirements-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-instancerequirements-syntax.json"></a>

```
{
  "[AllowedInstanceTypes](#cfn-bedrockagentcore-capacityprovider-instancerequirements-allowedinstancetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-instancerequirements-syntax.yaml"></a>

```
  [AllowedInstanceTypes](#cfn-bedrockagentcore-capacityprovider-instancerequirements-allowedinstancetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-instancerequirements-properties"></a>

`AllowedInstanceTypes`  <a name="cfn-bedrockagentcore-capacityprovider-instancerequirements-allowedinstancetypes"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
