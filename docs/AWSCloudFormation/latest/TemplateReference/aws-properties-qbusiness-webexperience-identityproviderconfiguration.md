---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-webexperience-identityproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::WebExperience IdentityProviderConfiguration
<a name="aws-properties-qbusiness-webexperience-identityproviderconfiguration"></a>

Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

## Syntax
<a name="aws-properties-qbusiness-webexperience-identityproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-webexperience-identityproviderconfiguration-syntax.json"></a>

```
{
  "[OpenIDConnectConfiguration](#cfn-qbusiness-webexperience-identityproviderconfiguration-openidconnectconfiguration)" : {{OpenIDConnectProviderConfiguration}},
  "[SamlConfiguration](#cfn-qbusiness-webexperience-identityproviderconfiguration-samlconfiguration)" : {{SamlProviderConfiguration}}
}
```

### YAML
<a name="aws-properties-qbusiness-webexperience-identityproviderconfiguration-syntax.yaml"></a>

```
  [OpenIDConnectConfiguration](#cfn-qbusiness-webexperience-identityproviderconfiguration-openidconnectconfiguration): {{
    OpenIDConnectProviderConfiguration}}
  [SamlConfiguration](#cfn-qbusiness-webexperience-identityproviderconfiguration-samlconfiguration): {{
    SamlProviderConfiguration}}
```

## Properties
<a name="aws-properties-qbusiness-webexperience-identityproviderconfiguration-properties"></a>

`OpenIDConnectConfiguration`  <a name="cfn-qbusiness-webexperience-identityproviderconfiguration-openidconnectconfiguration"></a>
The OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
*Required*: No
*Type*: [OpenIDConnectProviderConfiguration](aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SamlConfiguration`  <a name="cfn-qbusiness-webexperience-identityproviderconfiguration-samlconfiguration"></a>
The SAML 2.0-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
*Required*: No
*Type*: [SamlProviderConfiguration](aws-properties-qbusiness-webexperience-samlproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
