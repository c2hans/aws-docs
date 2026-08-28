---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-webexperience-samlproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::WebExperience SamlProviderConfiguration
<a name="aws-properties-qbusiness-webexperience-samlproviderconfiguration"></a>

Information about the SAML 2.0-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

## Syntax
<a name="aws-properties-qbusiness-webexperience-samlproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-webexperience-samlproviderconfiguration-syntax.json"></a>

```
{
  "[AuthenticationUrl](#cfn-qbusiness-webexperience-samlproviderconfiguration-authenticationurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-webexperience-samlproviderconfiguration-syntax.yaml"></a>

```
  [AuthenticationUrl](#cfn-qbusiness-webexperience-samlproviderconfiguration-authenticationurl): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-webexperience-samlproviderconfiguration-properties"></a>

`AuthenticationUrl`  <a name="cfn-qbusiness-webexperience-samlproviderconfiguration-authenticationurl"></a>
The URL where Amazon Q Business end users will be redirected for authentication.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Minimum*: `1`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
