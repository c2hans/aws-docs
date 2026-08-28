---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-licensespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider LicenseSpecification
<a name="aws-properties-bedrockagentcore-capacityprovider-licensespecification"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-licensespecification-description"></a>The `LicenseSpecification` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-licensespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-licensespecification-syntax.json"></a>

```
{
  "[LicenseConfigurationArn](#cfn-bedrockagentcore-capacityprovider-licensespecification-licenseconfigurationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-licensespecification-syntax.yaml"></a>

```
  [LicenseConfigurationArn](#cfn-bedrockagentcore-capacityprovider-licensespecification-licenseconfigurationarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-licensespecification-properties"></a>

`LicenseConfigurationArn`  <a name="cfn-bedrockagentcore-capacityprovider-licensespecification-licenseconfigurationarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:license-manager:[a-z0-9-]+:[0-9]{12}:license-configuration:[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
