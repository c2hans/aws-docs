---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-apikeyconnectionmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector APIKeyConnectionMetadata
<a name="aws-properties-quicksight-actionconnector-apikeyconnectionmetadata"></a>

Configuration for API key-based authentication to external services.

## Syntax
<a name="aws-properties-quicksight-actionconnector-apikeyconnectionmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-apikeyconnectionmetadata-syntax.json"></a>

```
{
  "[ApiKey](#cfn-quicksight-actionconnector-apikeyconnectionmetadata-apikey)" : {{String}},
  "[BaseEndpoint](#cfn-quicksight-actionconnector-apikeyconnectionmetadata-baseendpoint)" : {{String}},
  "[Email](#cfn-quicksight-actionconnector-apikeyconnectionmetadata-email)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-apikeyconnectionmetadata-syntax.yaml"></a>

```
  [ApiKey](#cfn-quicksight-actionconnector-apikeyconnectionmetadata-apikey): {{String}}
  [BaseEndpoint](#cfn-quicksight-actionconnector-apikeyconnectionmetadata-baseendpoint): {{String}}
  [Email](#cfn-quicksight-actionconnector-apikeyconnectionmetadata-email): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-apikeyconnectionmetadata-properties"></a>

`ApiKey`  <a name="cfn-quicksight-actionconnector-apikeyconnectionmetadata-apikey"></a>
The API key used for authentication.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseEndpoint`  <a name="cfn-quicksight-actionconnector-apikeyconnectionmetadata-baseendpoint"></a>
The base URL endpoint for the external service.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Email`  <a name="cfn-quicksight-actionconnector-apikeyconnectionmetadata-email"></a>
The email address associated with the API key, if required.
*Required*: No
*Type*: String
*Pattern*: `^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
