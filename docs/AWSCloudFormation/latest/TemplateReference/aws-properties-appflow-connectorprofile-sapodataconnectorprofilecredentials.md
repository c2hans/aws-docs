---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile SAPODataConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials"></a>

 The connector-specific profile credentials required when using SAPOData.

## Syntax
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials-syntax.json"></a>

```
{
  "[BasicAuthCredentials](#cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-basicauthcredentials)" : {{BasicAuthCredentials}},
  "[OAuthCredentials](#cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-oauthcredentials)" : {{OAuthCredentials}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials-syntax.yaml"></a>

```
  [BasicAuthCredentials](#cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-basicauthcredentials): {{
    BasicAuthCredentials}}
  [OAuthCredentials](#cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-oauthcredentials): {{
    OAuthCredentials}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials-properties"></a>

`BasicAuthCredentials`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-basicauthcredentials"></a>
 The SAPOData basic authentication credentials.
*Required*: No
*Type*: [BasicAuthCredentials](aws-properties-appflow-connectorprofile-basicauthcredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthCredentials`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-oauthcredentials"></a>
 The SAPOData OAuth type authentication credentials.
*Required*: No
*Type*: [OAuthCredentials](aws-properties-appflow-connectorprofile-oauthcredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
