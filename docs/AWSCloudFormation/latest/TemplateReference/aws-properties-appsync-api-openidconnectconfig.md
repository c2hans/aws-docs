---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-api-openidconnectconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Api OpenIDConnectConfig
<a name="aws-properties-appsync-api-openidconnectconfig"></a>

Describes an OpenID Connect (OIDC) configuration.

## Syntax
<a name="aws-properties-appsync-api-openidconnectconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-api-openidconnectconfig-syntax.json"></a>

```
{
  "[AuthTTL](#cfn-appsync-api-openidconnectconfig-authttl)" : {{Number}},
  "[ClientId](#cfn-appsync-api-openidconnectconfig-clientid)" : {{String}},
  "[IatTTL](#cfn-appsync-api-openidconnectconfig-iatttl)" : {{Number}},
  "[Issuer](#cfn-appsync-api-openidconnectconfig-issuer)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-api-openidconnectconfig-syntax.yaml"></a>

```
  [AuthTTL](#cfn-appsync-api-openidconnectconfig-authttl): {{Number}}
  [ClientId](#cfn-appsync-api-openidconnectconfig-clientid): {{String}}
  [IatTTL](#cfn-appsync-api-openidconnectconfig-iatttl): {{Number}}
  [Issuer](#cfn-appsync-api-openidconnectconfig-issuer): {{String}}
```

## Properties
<a name="aws-properties-appsync-api-openidconnectconfig-properties"></a>

`AuthTTL`  <a name="cfn-appsync-api-openidconnectconfig-authttl"></a>
The number of milliseconds that a token is valid after being authenticated.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-appsync-api-openidconnectconfig-clientid"></a>
The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IatTTL`  <a name="cfn-appsync-api-openidconnectconfig-iatttl"></a>
The number of milliseconds that a token is valid after it's issued to a user.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-appsync-api-openidconnectconfig-issuer"></a>
The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of `iss` in the ID token.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
