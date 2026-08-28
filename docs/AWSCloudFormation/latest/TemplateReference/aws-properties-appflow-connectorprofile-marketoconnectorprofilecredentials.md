---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile MarketoConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials"></a>

 The connector-specific profile credentials required by Marketo.

## Syntax
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials-syntax.json"></a>

```
{
  "[AccessToken](#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-accesstoken)" : {{String}},
  "[ClientId](#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientid)" : {{String}},
  "[ClientSecret](#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientsecret)" : {{String}},
  "[ConnectorOAuthRequest](#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-connectoroauthrequest)" : {{ConnectorOAuthRequest}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials-syntax.yaml"></a>

```
  [AccessToken](#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-accesstoken): {{String}}
  [ClientId](#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientid): {{String}}
  [ClientSecret](#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientsecret): {{String}}
  [ConnectorOAuthRequest](#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-connectoroauthrequest): {{
    ConnectorOAuthRequest}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials-properties"></a>

`AccessToken`  <a name="cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-accesstoken"></a>
 The credentials used to access protected Marketo resources.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientid"></a>
 The identifier for the desired client.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientsecret"></a>
 The client secret used by the OAuth client to authenticate to the authorization server.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectorOAuthRequest`  <a name="cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-connectoroauthrequest"></a>
 Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.
*Required*: No
*Type*: [ConnectorOAuthRequest](aws-properties-appflow-connectorprofile-connectoroauthrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials--seealso"></a>
+ [MarketoConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_MarketoConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
