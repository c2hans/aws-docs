---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-oauth2properties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection OAuth2Properties
<a name="aws-properties-glue-connection-oauth2properties"></a>

A structure containing properties for OAuth2 authentication.

## Syntax
<a name="aws-properties-glue-connection-oauth2properties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-oauth2properties-syntax.json"></a>

```
{
  "[AuthorizationCodeProperties](#cfn-glue-connection-oauth2properties-authorizationcodeproperties)" : {{AuthorizationCodeProperties}},
  "[OAuth2ClientApplication](#cfn-glue-connection-oauth2properties-oauth2clientapplication)" : {{OAuth2ClientApplication}},
  "[OAuth2Credentials](#cfn-glue-connection-oauth2properties-oauth2credentials)" : {{OAuth2Credentials}},
  "[OAuth2GrantType](#cfn-glue-connection-oauth2properties-oauth2granttype)" : {{String}},
  "[TokenUrl](#cfn-glue-connection-oauth2properties-tokenurl)" : {{String}},
  "[TokenUrlParametersMap](#cfn-glue-connection-oauth2properties-tokenurlparametersmap)" : {{Json}}
}
```

### YAML
<a name="aws-properties-glue-connection-oauth2properties-syntax.yaml"></a>

```
  [AuthorizationCodeProperties](#cfn-glue-connection-oauth2properties-authorizationcodeproperties): {{
    AuthorizationCodeProperties}}
  [OAuth2ClientApplication](#cfn-glue-connection-oauth2properties-oauth2clientapplication): {{
    OAuth2ClientApplication}}
  [OAuth2Credentials](#cfn-glue-connection-oauth2properties-oauth2credentials): {{
    OAuth2Credentials}}
  [OAuth2GrantType](#cfn-glue-connection-oauth2properties-oauth2granttype): {{String}}
  [TokenUrl](#cfn-glue-connection-oauth2properties-tokenurl): {{String}}
  [TokenUrlParametersMap](#cfn-glue-connection-oauth2properties-tokenurlparametersmap): {{Json}}
```

## Properties
<a name="aws-properties-glue-connection-oauth2properties-properties"></a>

`AuthorizationCodeProperties`  <a name="cfn-glue-connection-oauth2properties-authorizationcodeproperties"></a>
Property description not available.
*Required*: No
*Type*: [AuthorizationCodeProperties](aws-properties-glue-connection-authorizationcodeproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2ClientApplication`  <a name="cfn-glue-connection-oauth2properties-oauth2clientapplication"></a>
The client application type. For example, AWS\_MANAGED or USER\_MANAGED.
*Required*: No
*Type*: [OAuth2ClientApplication](aws-properties-glue-connection-oauth2clientapplication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2Credentials`  <a name="cfn-glue-connection-oauth2properties-oauth2credentials"></a>
Property description not available.
*Required*: No
*Type*: [OAuth2Credentials](aws-properties-glue-connection-oauth2credentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2GrantType`  <a name="cfn-glue-connection-oauth2properties-oauth2granttype"></a>
The OAuth2 grant type. For example, `AUTHORIZATION_CODE`, `JWT_BEARER`, or `CLIENT_CREDENTIALS`.
*Required*: No
*Type*: String
*Allowed values*: `AUTHORIZATION_CODE | CLIENT_CREDENTIALS | JWT_BEARER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenUrl`  <a name="cfn-glue-connection-oauth2properties-tokenurl"></a>
The URL of the provider's authentication server, to exchange an authorization code for an access token.
*Required*: No
*Type*: String
*Pattern*: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenUrlParametersMap`  <a name="cfn-glue-connection-oauth2properties-tokenurlparametersmap"></a>
A map of parameters that are added to the token `GET` request.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
