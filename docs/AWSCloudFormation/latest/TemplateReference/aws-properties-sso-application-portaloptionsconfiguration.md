---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sso-application-portaloptionsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::Application PortalOptionsConfiguration
<a name="aws-properties-sso-application-portaloptionsconfiguration"></a>

A structure that describes the options for the portal associated with an application.

## Syntax
<a name="aws-properties-sso-application-portaloptionsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sso-application-portaloptionsconfiguration-syntax.json"></a>

```
{
  "[SignInOptions](#cfn-sso-application-portaloptionsconfiguration-signinoptions)" : {{SignInOptions}},
  "[Visibility](#cfn-sso-application-portaloptionsconfiguration-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-sso-application-portaloptionsconfiguration-syntax.yaml"></a>

```
  [SignInOptions](#cfn-sso-application-portaloptionsconfiguration-signinoptions): {{
    SignInOptions}}
  [Visibility](#cfn-sso-application-portaloptionsconfiguration-visibility): {{String}}
```

## Properties
<a name="aws-properties-sso-application-portaloptionsconfiguration-properties"></a>

`SignInOptions`  <a name="cfn-sso-application-portaloptionsconfiguration-signinoptions"></a>
A structure that describes the sign-in options for the access portal.
*Required*: No
*Type*: [SignInOptions](aws-properties-sso-application-signinoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-sso-application-portaloptionsconfiguration-visibility"></a>
Indicates whether this application is visible in the access portal.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
