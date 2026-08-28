---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-apikeydetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service ApiKeyDetails
<a name="aws-properties-devopsagent-service-apikeydetails"></a>

API key authentication details for an MCP server.

## Syntax
<a name="aws-properties-devopsagent-service-apikeydetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-apikeydetails-syntax.json"></a>

```
{
  "[ApiKeyHeader](#cfn-devopsagent-service-apikeydetails-apikeyheader)" : {{String}},
  "[ApiKeyName](#cfn-devopsagent-service-apikeydetails-apikeyname)" : {{String}},
  "[ApiKeyValue](#cfn-devopsagent-service-apikeydetails-apikeyvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-apikeydetails-syntax.yaml"></a>

```
  [ApiKeyHeader](#cfn-devopsagent-service-apikeydetails-apikeyheader): {{String}}
  [ApiKeyName](#cfn-devopsagent-service-apikeydetails-apikeyname): {{String}}
  [ApiKeyValue](#cfn-devopsagent-service-apikeydetails-apikeyvalue): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-apikeydetails-properties"></a>

`ApiKeyHeader`  <a name="cfn-devopsagent-service-apikeydetails-apikeyheader"></a>
The HTTP header name used to send the API key.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeyName`  <a name="cfn-devopsagent-service-apikeydetails-apikeyname"></a>
A friendly name for the API key.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\s-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeyValue`  <a name="cfn-devopsagent-service-apikeydetails-apikeyvalue"></a>
The API key value.
*Required*: Yes
*Type*: String
*Pattern*: `^[!-~]([ \t]*[!-~])*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
