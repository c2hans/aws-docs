---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-plugin-pluginauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Plugin PluginAuthConfiguration
<a name="aws-properties-qbusiness-plugin-pluginauthconfiguration"></a>

Authentication configuration information for an Amazon Q Business plugin.

## Syntax
<a name="aws-properties-qbusiness-plugin-pluginauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-plugin-pluginauthconfiguration-syntax.json"></a>

```
{
  "[BasicAuthConfiguration](#cfn-qbusiness-plugin-pluginauthconfiguration-basicauthconfiguration)" : {{BasicAuthConfiguration}},
  "[NoAuthConfiguration](#cfn-qbusiness-plugin-pluginauthconfiguration-noauthconfiguration)" : {{Json}},
  "[OAuth2ClientCredentialConfiguration](#cfn-qbusiness-plugin-pluginauthconfiguration-oauth2clientcredentialconfiguration)" : {{OAuth2ClientCredentialConfiguration}}
}
```

### YAML
<a name="aws-properties-qbusiness-plugin-pluginauthconfiguration-syntax.yaml"></a>

```
  [BasicAuthConfiguration](#cfn-qbusiness-plugin-pluginauthconfiguration-basicauthconfiguration): {{
    BasicAuthConfiguration}}
  [NoAuthConfiguration](#cfn-qbusiness-plugin-pluginauthconfiguration-noauthconfiguration): {{Json}}
  [OAuth2ClientCredentialConfiguration](#cfn-qbusiness-plugin-pluginauthconfiguration-oauth2clientcredentialconfiguration): {{
    OAuth2ClientCredentialConfiguration}}
```

## Properties
<a name="aws-properties-qbusiness-plugin-pluginauthconfiguration-properties"></a>

`BasicAuthConfiguration`  <a name="cfn-qbusiness-plugin-pluginauthconfiguration-basicauthconfiguration"></a>
Information about the basic authentication credentials used to configure a plugin.
*Required*: No
*Type*: [BasicAuthConfiguration](aws-properties-qbusiness-plugin-basicauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoAuthConfiguration`  <a name="cfn-qbusiness-plugin-pluginauthconfiguration-noauthconfiguration"></a>
Information about invoking a custom plugin without any authentication.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2ClientCredentialConfiguration`  <a name="cfn-qbusiness-plugin-pluginauthconfiguration-oauth2clientcredentialconfiguration"></a>
Information about the OAuth 2.0 authentication credential/token used to configure a plugin.
*Required*: No
*Type*: [OAuth2ClientCredentialConfiguration](aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
