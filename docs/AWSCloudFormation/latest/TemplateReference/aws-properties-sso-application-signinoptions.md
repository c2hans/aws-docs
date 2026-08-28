---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sso-application-signinoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::Application SignInOptions
<a name="aws-properties-sso-application-signinoptions"></a>

A structure that describes the sign-in options for an application portal.

## Syntax
<a name="aws-properties-sso-application-signinoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sso-application-signinoptions-syntax.json"></a>

```
{
  "[ApplicationUrl](#cfn-sso-application-signinoptions-applicationurl)" : {{String}},
  "[Origin](#cfn-sso-application-signinoptions-origin)" : {{String}}
}
```

### YAML
<a name="aws-properties-sso-application-signinoptions-syntax.yaml"></a>

```
  [ApplicationUrl](#cfn-sso-application-signinoptions-applicationurl): {{String}}
  [Origin](#cfn-sso-application-signinoptions-origin): {{String}}
```

## Properties
<a name="aws-properties-sso-application-signinoptions-properties"></a>

`ApplicationUrl`  <a name="cfn-sso-application-signinoptions-applicationurl"></a>
The URL that accepts authentication requests for an application. This is a required parameter if the `Origin` parameter is `APPLICATION`.
*Required*: No
*Type*: String
*Pattern*: `^http(s)?:\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&bb@#\/%?=~_|]$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Origin`  <a name="cfn-sso-application-signinoptions-origin"></a>
This determines how IAM Identity Center navigates the user to the target application. It can be one of the following values:
+ `APPLICATION`: IAM Identity Center redirects the customer to the configured `ApplicationUrl`.
+ `IDENTITY_CENTER`: IAM Identity Center uses SAML identity-provider initiated authentication to sign the customer directly into a SAML-based application.
*Required*: Yes
*Type*: String
*Allowed values*: `IDENTITY_CENTER | APPLICATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
