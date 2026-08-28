---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-oauth2properties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection OAuth2Properties
<a name="aws-properties-datazone-connection-oauth2properties"></a>

The OAuth2 properties.

## Syntax
<a name="aws-properties-datazone-connection-oauth2properties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-oauth2properties-syntax.json"></a>

```
{
  "[AuthorizationCodeProperties](#cfn-datazone-connection-oauth2properties-authorizationcodeproperties)" : {{AuthorizationCodeProperties}},
  "[OAuth2ClientApplication](#cfn-datazone-connection-oauth2properties-oauth2clientapplication)" : {{OAuth2ClientApplication}},
  "[OAuth2Credentials](#cfn-datazone-connection-oauth2properties-oauth2credentials)" : {{GlueOAuth2Credentials}},
  "[OAuth2GrantType](#cfn-datazone-connection-oauth2properties-oauth2granttype)" : {{String}},
  "[TokenUrl](#cfn-datazone-connection-oauth2properties-tokenurl)" : {{String}},
  "[TokenUrlParametersMap](#cfn-datazone-connection-oauth2properties-tokenurlparametersmap)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-datazone-connection-oauth2properties-syntax.yaml"></a>

```
  [AuthorizationCodeProperties](#cfn-datazone-connection-oauth2properties-authorizationcodeproperties): {{
    AuthorizationCodeProperties}}
  [OAuth2ClientApplication](#cfn-datazone-connection-oauth2properties-oauth2clientapplication): {{
    OAuth2ClientApplication}}
  [OAuth2Credentials](#cfn-datazone-connection-oauth2properties-oauth2credentials): {{
    GlueOAuth2Credentials}}
  [OAuth2GrantType](#cfn-datazone-connection-oauth2properties-oauth2granttype): {{String}}
  [TokenUrl](#cfn-datazone-connection-oauth2properties-tokenurl): {{String}}
  [TokenUrlParametersMap](#cfn-datazone-connection-oauth2properties-tokenurlparametersmap): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-datazone-connection-oauth2properties-properties"></a>

`AuthorizationCodeProperties`  <a name="cfn-datazone-connection-oauth2properties-authorizationcodeproperties"></a>
The authorization code properties of the OAuth2 properties.
*Required*: No
*Type*: [AuthorizationCodeProperties](aws-properties-datazone-connection-authorizationcodeproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2ClientApplication`  <a name="cfn-datazone-connection-oauth2properties-oauth2clientapplication"></a>
The OAuth2 client application of the OAuth2 properties.
*Required*: No
*Type*: [OAuth2ClientApplication](aws-properties-datazone-connection-oauth2clientapplication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2Credentials`  <a name="cfn-datazone-connection-oauth2properties-oauth2credentials"></a>
The OAuth2 credentials of the OAuth2 properties.
*Required*: No
*Type*: [GlueOAuth2Credentials](aws-properties-datazone-connection-glueoauth2credentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2GrantType`  <a name="cfn-datazone-connection-oauth2properties-oauth2granttype"></a>
The OAuth2 grant type of the OAuth2 properties.
*Required*: No
*Type*: String
*Allowed values*: `AUTHORIZATION_CODE | CLIENT_CREDENTIALS | JWT_BEARER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenUrl`  <a name="cfn-datazone-connection-oauth2properties-tokenurl"></a>
The OAuth2 token URL of the OAuth2 properties.
*Required*: No
*Type*: String
*Pattern*: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenUrlParametersMap`  <a name="cfn-datazone-connection-oauth2properties-tokenurlparametersmap"></a>
The OAuth2 token URL parameter map of the OAuth2 properties.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
