---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::WebExperience OpenIDConnectProviderConfiguration
<a name="aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration"></a>

Information about the OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

## Syntax
<a name="aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration-syntax.json"></a>

```
{
  "[SecretsArn](#cfn-qbusiness-webexperience-openidconnectproviderconfiguration-secretsarn)" : {{String}},
  "[SecretsRole](#cfn-qbusiness-webexperience-openidconnectproviderconfiguration-secretsrole)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration-syntax.yaml"></a>

```
  [SecretsArn](#cfn-qbusiness-webexperience-openidconnectproviderconfiguration-secretsarn): {{String}}
  [SecretsRole](#cfn-qbusiness-webexperience-openidconnectproviderconfiguration-secretsrole): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration-properties"></a>

`SecretsArn`  <a name="cfn-qbusiness-webexperience-openidconnectproviderconfiguration-secretsarn"></a>
The Amazon Resource Name (ARN) of a Secrets Manager secret containing the OIDC client secret.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsRole`  <a name="cfn-qbusiness-webexperience-openidconnectproviderconfiguration-secretsrole"></a>
An IAM role with permissions to access AWS KMS to decrypt the Secrets Manager secret containing your OIDC client secret.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
