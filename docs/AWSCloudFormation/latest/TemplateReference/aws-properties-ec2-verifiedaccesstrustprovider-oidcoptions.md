---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessTrustProvider OidcOptions
<a name="aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions"></a>

Describes the options for an OpenID Connect-compatible user-identity trust provider.

## Syntax
<a name="aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions-syntax.json"></a>

```
{
  "[AuthorizationEndpoint](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-authorizationendpoint)" : {{String}},
  "[ClientId](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-clientid)" : {{String}},
  "[ClientSecret](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-clientsecret)" : {{String}},
  "[Issuer](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-issuer)" : {{String}},
  "[Scope](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-scope)" : {{String}},
  "[TokenEndpoint](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-tokenendpoint)" : {{String}},
  "[UserInfoEndpoint](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-userinfoendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions-syntax.yaml"></a>

```
  [AuthorizationEndpoint](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-authorizationendpoint): {{String}}
  [ClientId](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-clientid): {{String}}
  [ClientSecret](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-clientsecret): {{String}}
  [Issuer](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-issuer): {{String}}
  [Scope](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-scope): {{String}}
  [TokenEndpoint](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-tokenendpoint): {{String}}
  [UserInfoEndpoint](#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-userinfoendpoint): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions-properties"></a>

`AuthorizationEndpoint`  <a name="cfn-ec2-verifiedaccesstrustprovider-oidcoptions-authorizationendpoint"></a>
The OIDC authorization endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-ec2-verifiedaccesstrustprovider-oidcoptions-clientid"></a>
The client identifier.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-ec2-verifiedaccesstrustprovider-oidcoptions-clientsecret"></a>
The client secret.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-ec2-verifiedaccesstrustprovider-oidcoptions-issuer"></a>
The OIDC issuer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-ec2-verifiedaccesstrustprovider-oidcoptions-scope"></a>
The OpenID Connect (OIDC) scope specified.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenEndpoint`  <a name="cfn-ec2-verifiedaccesstrustprovider-oidcoptions-tokenendpoint"></a>
The OIDC token endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserInfoEndpoint`  <a name="cfn-ec2-verifiedaccesstrustprovider-oidcoptions-userinfoendpoint"></a>
The OIDC user info endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
