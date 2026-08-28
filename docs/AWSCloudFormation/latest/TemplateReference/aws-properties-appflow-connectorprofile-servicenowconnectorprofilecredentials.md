---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile ServiceNowConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials"></a>

 The connector-specific profile credentials required when using ServiceNow.

## Syntax
<a name="aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials-syntax.json"></a>

```
{
  "[OAuth2Credentials](#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-oauth2credentials)" : {{OAuth2Credentials}},
  "[Password](#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-password)" : {{String}},
  "[Username](#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials-syntax.yaml"></a>

```
  [OAuth2Credentials](#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-oauth2credentials): {{
    OAuth2Credentials}}
  [Password](#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-password): {{String}}
  [Username](#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-username): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials-properties"></a>

`OAuth2Credentials`  <a name="cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-oauth2credentials"></a>
 The OAuth 2.0 credentials required to authenticate the user.
*Required*: No
*Type*: [OAuth2Credentials](aws-properties-appflow-connectorprofile-oauth2credentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Password`  <a name="cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-password"></a>
 The password that corresponds to the user name.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-username"></a>
 The name of the user.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials--seealso"></a>
+ [ServiceNowConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ServiceNowConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
