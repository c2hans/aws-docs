---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile PardotConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials"></a>

The connector-specific profile credentials required when using Salesforce Pardot.

## Syntax
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials-syntax.json"></a>

```
{
  "[AccessToken](#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-accesstoken)" : {{String}},
  "[ClientCredentialsArn](#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-clientcredentialsarn)" : {{String}},
  "[ConnectorOAuthRequest](#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-connectoroauthrequest)" : {{ConnectorOAuthRequest}},
  "[RefreshToken](#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-refreshtoken)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials-syntax.yaml"></a>

```
  [AccessToken](#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-accesstoken): {{String}}
  [ClientCredentialsArn](#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-clientcredentialsarn): {{String}}
  [ConnectorOAuthRequest](#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-connectoroauthrequest): {{
    ConnectorOAuthRequest}}
  [RefreshToken](#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-refreshtoken): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials-properties"></a>

`AccessToken`  <a name="cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-accesstoken"></a>
The credentials used to access protected Salesforce Pardot resources.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientCredentialsArn`  <a name="cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-clientcredentialsarn"></a>
The secret manager ARN, which contains the client ID and client secret of the connected app.
*Required*: No
*Type*: String
*Pattern*: `arn:aws:secretsmanager:.*:[0-9]+:.*`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectorOAuthRequest`  <a name="cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-connectoroauthrequest"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorOAuthRequest](aws-properties-appflow-connectorprofile-connectoroauthrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshToken`  <a name="cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-refreshtoken"></a>
The credentials used to acquire new access tokens.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
