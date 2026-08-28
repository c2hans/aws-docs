---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-httpconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource HttpConfig
<a name="aws-properties-appsync-datasource-httpconfig"></a>

Use the `HttpConfig` property type to specify `HttpConfig` for an AWS AppSync data source.

`HttpConfig` is a property of the [AWS::AppSync::DataSource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html) resource.

## Syntax
<a name="aws-properties-appsync-datasource-httpconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-httpconfig-syntax.json"></a>

```
{
  "[AuthorizationConfig](#cfn-appsync-datasource-httpconfig-authorizationconfig)" : {{AuthorizationConfig}},
  "[Endpoint](#cfn-appsync-datasource-httpconfig-endpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-httpconfig-syntax.yaml"></a>

```
  [AuthorizationConfig](#cfn-appsync-datasource-httpconfig-authorizationconfig): {{
    AuthorizationConfig}}
  [Endpoint](#cfn-appsync-datasource-httpconfig-endpoint): {{String}}
```

## Properties
<a name="aws-properties-appsync-datasource-httpconfig-properties"></a>

`AuthorizationConfig`  <a name="cfn-appsync-datasource-httpconfig-authorizationconfig"></a>
The authorization configuration.
*Required*: No
*Type*: [AuthorizationConfig](aws-properties-appsync-datasource-authorizationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-appsync-datasource-httpconfig-endpoint"></a>
The endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
