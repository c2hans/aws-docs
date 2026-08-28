---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-basicauthconnectionmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector BasicAuthConnectionMetadata
<a name="aws-properties-quicksight-actionconnector-basicauthconnectionmetadata"></a>

Metadata for basic authentication using username and password.

## Syntax
<a name="aws-properties-quicksight-actionconnector-basicauthconnectionmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-basicauthconnectionmetadata-syntax.json"></a>

```
{
  "[BaseEndpoint](#cfn-quicksight-actionconnector-basicauthconnectionmetadata-baseendpoint)" : {{String}},
  "[Password](#cfn-quicksight-actionconnector-basicauthconnectionmetadata-password)" : {{String}},
  "[Username](#cfn-quicksight-actionconnector-basicauthconnectionmetadata-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-basicauthconnectionmetadata-syntax.yaml"></a>

```
  [BaseEndpoint](#cfn-quicksight-actionconnector-basicauthconnectionmetadata-baseendpoint): {{String}}
  [Password](#cfn-quicksight-actionconnector-basicauthconnectionmetadata-password): {{String}}
  [Username](#cfn-quicksight-actionconnector-basicauthconnectionmetadata-username): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-basicauthconnectionmetadata-properties"></a>

`BaseEndpoint`  <a name="cfn-quicksight-actionconnector-basicauthconnectionmetadata-baseendpoint"></a>
The base URL endpoint for the external service.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Password`  <a name="cfn-quicksight-actionconnector-basicauthconnectionmetadata-password"></a>
The password for basic authentication.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-quicksight-actionconnector-basicauthconnectionmetadata-username"></a>
The username for basic authentication.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
