---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-domainconfiguration-authorizerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::DomainConfiguration AuthorizerConfig
<a name="aws-properties-iot-domainconfiguration-authorizerconfig"></a>

An object that specifies the authorization service for a domain.

## Syntax
<a name="aws-properties-iot-domainconfiguration-authorizerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-domainconfiguration-authorizerconfig-syntax.json"></a>

```
{
  "[AllowAuthorizerOverride](#cfn-iot-domainconfiguration-authorizerconfig-allowauthorizeroverride)" : {{Boolean}},
  "[DefaultAuthorizerName](#cfn-iot-domainconfiguration-authorizerconfig-defaultauthorizername)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-domainconfiguration-authorizerconfig-syntax.yaml"></a>

```
  [AllowAuthorizerOverride](#cfn-iot-domainconfiguration-authorizerconfig-allowauthorizeroverride): {{Boolean}}
  [DefaultAuthorizerName](#cfn-iot-domainconfiguration-authorizerconfig-defaultauthorizername): {{String}}
```

## Properties
<a name="aws-properties-iot-domainconfiguration-authorizerconfig-properties"></a>

`AllowAuthorizerOverride`  <a name="cfn-iot-domainconfiguration-authorizerconfig-allowauthorizeroverride"></a>
A Boolean that specifies whether the domain configuration's authorization service can be overridden.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultAuthorizerName`  <a name="cfn-iot-domainconfiguration-authorizerconfig-defaultauthorizername"></a>
The name of the authorization service for a domain configuration.
*Required*: No
*Type*: String
*Pattern*: `^[\w=,@-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
