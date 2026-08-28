---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-connectoroauthrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile ConnectorOAuthRequest
<a name="aws-properties-appflow-connectorprofile-connectoroauthrequest"></a>

 Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

## Syntax
<a name="aws-properties-appflow-connectorprofile-connectoroauthrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-connectoroauthrequest-syntax.json"></a>

```
{
  "[AuthCode](#cfn-appflow-connectorprofile-connectoroauthrequest-authcode)" : {{String}},
  "[RedirectUri](#cfn-appflow-connectorprofile-connectoroauthrequest-redirecturi)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-connectoroauthrequest-syntax.yaml"></a>

```
  [AuthCode](#cfn-appflow-connectorprofile-connectoroauthrequest-authcode): {{String}}
  [RedirectUri](#cfn-appflow-connectorprofile-connectoroauthrequest-redirecturi): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-connectoroauthrequest-properties"></a>

`AuthCode`  <a name="cfn-appflow-connectorprofile-connectoroauthrequest-authcode"></a>
 The code provided by the connector when it has been authenticated via the connected app.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedirectUri`  <a name="cfn-appflow-connectorprofile-connectoroauthrequest-redirecturi"></a>
 The URL to which the authentication server redirects the browser after authorization has been granted.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-connectoroauthrequest--seealso"></a>
+ [ConnectorOAuthRequest](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorOAuthRequest.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
