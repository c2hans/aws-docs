---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-workforce-oidcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Workforce OidcConfig
<a name="aws-properties-sagemaker-workforce-oidcconfig"></a>

Use this parameter to configure your OIDC Identity Provider (IdP).

## Syntax
<a name="aws-properties-sagemaker-workforce-oidcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-workforce-oidcconfig-syntax.json"></a>

```
{
  "[AuthenticationRequestExtraParams](#cfn-sagemaker-workforce-oidcconfig-authenticationrequestextraparams)" : {{{{{Key}}: {{Value}}, ...}}},
  "[AuthorizationEndpoint](#cfn-sagemaker-workforce-oidcconfig-authorizationendpoint)" : {{String}},
  "[ClientId](#cfn-sagemaker-workforce-oidcconfig-clientid)" : {{String}},
  "[ClientSecret](#cfn-sagemaker-workforce-oidcconfig-clientsecret)" : {{String}},
  "[Issuer](#cfn-sagemaker-workforce-oidcconfig-issuer)" : {{String}},
  "[JwksUri](#cfn-sagemaker-workforce-oidcconfig-jwksuri)" : {{String}},
  "[LogoutEndpoint](#cfn-sagemaker-workforce-oidcconfig-logoutendpoint)" : {{String}},
  "[Scope](#cfn-sagemaker-workforce-oidcconfig-scope)" : {{String}},
  "[TokenEndpoint](#cfn-sagemaker-workforce-oidcconfig-tokenendpoint)" : {{String}},
  "[UserInfoEndpoint](#cfn-sagemaker-workforce-oidcconfig-userinfoendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-workforce-oidcconfig-syntax.yaml"></a>

```
  [AuthenticationRequestExtraParams](#cfn-sagemaker-workforce-oidcconfig-authenticationrequestextraparams): {{
    {{Key}}: {{Value}}}}
  [AuthorizationEndpoint](#cfn-sagemaker-workforce-oidcconfig-authorizationendpoint): {{String}}
  [ClientId](#cfn-sagemaker-workforce-oidcconfig-clientid): {{String}}
  [ClientSecret](#cfn-sagemaker-workforce-oidcconfig-clientsecret): {{String}}
  [Issuer](#cfn-sagemaker-workforce-oidcconfig-issuer): {{String}}
  [JwksUri](#cfn-sagemaker-workforce-oidcconfig-jwksuri): {{String}}
  [LogoutEndpoint](#cfn-sagemaker-workforce-oidcconfig-logoutendpoint): {{String}}
  [Scope](#cfn-sagemaker-workforce-oidcconfig-scope): {{String}}
  [TokenEndpoint](#cfn-sagemaker-workforce-oidcconfig-tokenendpoint): {{String}}
  [UserInfoEndpoint](#cfn-sagemaker-workforce-oidcconfig-userinfoendpoint): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-workforce-oidcconfig-properties"></a>

`AuthenticationRequestExtraParams`  <a name="cfn-sagemaker-workforce-oidcconfig-authenticationrequestextraparams"></a>
A string to string map of identifiers specific to the custom identity provider (IdP) being used.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationEndpoint`  <a name="cfn-sagemaker-workforce-oidcconfig-authorizationendpoint"></a>
The OIDC IdP authorization endpoint used to configure your private workforce.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-sagemaker-workforce-oidcconfig-clientid"></a>
The OIDC IdP client ID used to configure your private workforce.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w+]+$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-sagemaker-workforce-oidcconfig-clientsecret"></a>
The OIDC IdP client secret used to configure your private workforce.
*Required*: No
*Type*: String
*Pattern*: `^[\w+]+$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Issuer`  <a name="cfn-sagemaker-workforce-oidcconfig-issuer"></a>
The OIDC IdP issuer used to configure your private workforce.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JwksUri`  <a name="cfn-sagemaker-workforce-oidcconfig-jwksuri"></a>
The OIDC IdP JSON Web Key Set (Jwks) URI used to configure your private workforce.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogoutEndpoint`  <a name="cfn-sagemaker-workforce-oidcconfig-logoutendpoint"></a>
The OIDC IdP logout endpoint used to configure your private workforce.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-sagemaker-workforce-oidcconfig-scope"></a>
An array of string identifiers used to refer to the specific pieces of user data or claims that the client application wants to access.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+$`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenEndpoint`  <a name="cfn-sagemaker-workforce-oidcconfig-tokenendpoint"></a>
The OIDC IdP token endpoint used to configure your private workforce.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserInfoEndpoint`  <a name="cfn-sagemaker-workforce-oidcconfig-userinfoendpoint"></a>
The OIDC IdP user information endpoint used to configure your private workforce.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
