---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider Tag
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-tag"></a>

A key-value pair to associate with a resource.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-tag-syntax.json"></a>

```
{
  "[Key](#cfn-bedrockagentcore-paymentcredentialprovider-tag-key)" : {{String}},
  "[Value](#cfn-bedrockagentcore-paymentcredentialprovider-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-tag-syntax.yaml"></a>

```
  [Key](#cfn-bedrockagentcore-paymentcredentialprovider-tag-key): {{String}}
  [Value](#cfn-bedrockagentcore-paymentcredentialprovider-tag-value): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-tag-properties"></a>

`Key`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-tag-value"></a>
The value for the tag. You can specify a value that's 0 to 256 characters in length.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
