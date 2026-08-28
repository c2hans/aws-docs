---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-authorizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness AuthorizerConfiguration
<a name="aws-properties-bedrockagentcore-harness-authorizerconfiguration"></a>

Represents inbound authorization configuration options used to authenticate incoming requests.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-authorizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-authorizerconfiguration-syntax.json"></a>

```
{
  "[CustomJWTAuthorizer](#cfn-bedrockagentcore-harness-authorizerconfiguration-customjwtauthorizer)" : {{CustomJWTAuthorizerConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-authorizerconfiguration-syntax.yaml"></a>

```
  [CustomJWTAuthorizer](#cfn-bedrockagentcore-harness-authorizerconfiguration-customjwtauthorizer): {{
    CustomJWTAuthorizerConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-authorizerconfiguration-properties"></a>

`CustomJWTAuthorizer`  <a name="cfn-bedrockagentcore-harness-authorizerconfiguration-customjwtauthorizer"></a>
The inbound JWT-based authorization, specifying how incoming requests should be authenticated.
*Required*: No
*Type*: [CustomJWTAuthorizerConfiguration](aws-properties-bedrockagentcore-harness-customjwtauthorizerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
