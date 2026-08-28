---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-oauth2credentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile OAuth2Credentials
<a name="aws-properties-appflow-connectorprofile-oauth2credentials"></a>

The OAuth 2.0 credentials required for OAuth 2.0 authentication.

## Syntax
<a name="aws-properties-appflow-connectorprofile-oauth2credentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-oauth2credentials-syntax.json"></a>

```
{
  "[AccessToken](#cfn-appflow-connectorprofile-oauth2credentials-accesstoken)" : {{String}},
  "[ClientId](#cfn-appflow-connectorprofile-oauth2credentials-clientid)" : {{String}},
  "[ClientSecret](#cfn-appflow-connectorprofile-oauth2credentials-clientsecret)" : {{String}},
  "[OAuthRequest](#cfn-appflow-connectorprofile-oauth2credentials-oauthrequest)" : {{ConnectorOAuthRequest}},
  "[RefreshToken](#cfn-appflow-connectorprofile-oauth2credentials-refreshtoken)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-oauth2credentials-syntax.yaml"></a>

```
  [AccessToken](#cfn-appflow-connectorprofile-oauth2credentials-accesstoken): {{String}}
  [ClientId](#cfn-appflow-connectorprofile-oauth2credentials-clientid): {{String}}
  [ClientSecret](#cfn-appflow-connectorprofile-oauth2credentials-clientsecret): {{String}}
  [OAuthRequest](#cfn-appflow-connectorprofile-oauth2credentials-oauthrequest): {{
    ConnectorOAuthRequest}}
  [RefreshToken](#cfn-appflow-connectorprofile-oauth2credentials-refreshtoken): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-oauth2credentials-properties"></a>

`AccessToken`  <a name="cfn-appflow-connectorprofile-oauth2credentials-accesstoken"></a>
The access token used to access the connector on your behalf.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-appflow-connectorprofile-oauth2credentials-clientid"></a>
The identifier for the desired client.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-appflow-connectorprofile-oauth2credentials-clientsecret"></a>
The client secret used by the OAuth client to authenticate to the authorization server.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthRequest`  <a name="cfn-appflow-connectorprofile-oauth2credentials-oauthrequest"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorOAuthRequest](aws-properties-appflow-connectorprofile-connectoroauthrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshToken`  <a name="cfn-appflow-connectorprofile-oauth2credentials-refreshtoken"></a>
The refresh token used to refresh an expired access token.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
