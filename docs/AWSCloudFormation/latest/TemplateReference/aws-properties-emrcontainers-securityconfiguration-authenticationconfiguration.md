---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration AuthenticationConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration"></a>

Contains the authentication settings for a security configuration, including Identity Center and IAM configuration options.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration-syntax.json"></a>

```
{
  "[IAMConfiguration](#cfn-emrcontainers-securityconfiguration-authenticationconfiguration-iamconfiguration)" : {{IAMConfiguration}},
  "[IdentityCenterConfiguration](#cfn-emrcontainers-securityconfiguration-authenticationconfiguration-identitycenterconfiguration)" : {{IdentityCenterConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration-syntax.yaml"></a>

```
  [IAMConfiguration](#cfn-emrcontainers-securityconfiguration-authenticationconfiguration-iamconfiguration): {{
    IAMConfiguration}}
  [IdentityCenterConfiguration](#cfn-emrcontainers-securityconfiguration-authenticationconfiguration-identitycenterconfiguration): {{
    IdentityCenterConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration-properties"></a>

`IAMConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-authenticationconfiguration-iamconfiguration"></a>
The IAM configuration to use for authentication.
*Required*: No
*Type*: [IAMConfiguration](aws-properties-emrcontainers-securityconfiguration-iamconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityCenterConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-authenticationconfiguration-identitycenterconfiguration"></a>
The IAM Identity Center configuration to use for authentication.
*Required*: No
*Type*: [IdentityCenterConfiguration](aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
