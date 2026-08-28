---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registry-authorizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Registry AuthorizerConfiguration
<a name="aws-properties-agentregistry-registry-authorizerconfiguration"></a>

The authorizer configuration for the registry. This is a union type; specify exactly one member.

## Syntax
<a name="aws-properties-agentregistry-registry-authorizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registry-authorizerconfiguration-syntax.json"></a>

```
{
  "[CustomJWTAuthorizer](#cfn-agentregistry-registry-authorizerconfiguration-customjwtauthorizer)" : {{CustomJWTAuthorizerConfiguration}}
}
```

### YAML
<a name="aws-properties-agentregistry-registry-authorizerconfiguration-syntax.yaml"></a>

```
  [CustomJWTAuthorizer](#cfn-agentregistry-registry-authorizerconfiguration-customjwtauthorizer): {{
    CustomJWTAuthorizerConfiguration}}
```

## Properties
<a name="aws-properties-agentregistry-registry-authorizerconfiguration-properties"></a>

`CustomJWTAuthorizer`  <a name="cfn-agentregistry-registry-authorizerconfiguration-customjwtauthorizer"></a>
Configuration for a custom JSON Web Token (JWT) authorizer that validates inbound bearer tokens against an OpenID Connect (OIDC) identity provider.
*Required*: Yes
*Type*: [CustomJWTAuthorizerConfiguration](aws-properties-agentregistry-registry-customjwtauthorizerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
