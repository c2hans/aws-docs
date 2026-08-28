---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile GoogleAnalyticsConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials"></a>

 The connector-specific profile credentials required by Google Analytics.

## Syntax
<a name="aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-syntax.json"></a>

```
{
  "[AccessToken](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-accesstoken)" : {{String}},
  "[ClientId](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientid)" : {{String}},
  "[ClientSecret](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientsecret)" : {{String}},
  "[ConnectorOAuthRequest](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-connectoroauthrequest)" : {{ConnectorOAuthRequest}},
  "[RefreshToken](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-refreshtoken)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-syntax.yaml"></a>

```
  [AccessToken](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-accesstoken): {{String}}
  [ClientId](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientid): {{String}}
  [ClientSecret](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientsecret): {{String}}
  [ConnectorOAuthRequest](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-connectoroauthrequest): {{
    ConnectorOAuthRequest}}
  [RefreshToken](#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-refreshtoken): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-properties"></a>

`AccessToken`  <a name="cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-accesstoken"></a>
 The credentials used to access protected Google Analytics resources.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientid"></a>
 The identifier for the desired client.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientsecret"></a>
 The client secret used by the OAuth client to authenticate to the authorization server.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectorOAuthRequest`  <a name="cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-connectoroauthrequest"></a>
 Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.
*Required*: No
*Type*: [ConnectorOAuthRequest](aws-properties-appflow-connectorprofile-connectoroauthrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshToken`  <a name="cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-refreshtoken"></a>
 The credentials used to acquire new access tokens. This is required only for OAuth2 access tokens, and is not required for OAuth1 access tokens.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials--seealso"></a>
+ [GoogleAnalyticsConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_GoogleAnalyticsConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
