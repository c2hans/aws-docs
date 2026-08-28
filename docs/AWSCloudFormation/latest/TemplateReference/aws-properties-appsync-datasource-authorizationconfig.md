---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-authorizationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource AuthorizationConfig
<a name="aws-properties-appsync-datasource-authorizationconfig"></a>

The `AuthorizationConfig` property type specifies the authorization type and configuration for an AWS AppSync http data source.

`AuthorizationConfig` is a property of the [AWS AppSync DataSource HttpConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html) property type.

## Syntax
<a name="aws-properties-appsync-datasource-authorizationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-authorizationconfig-syntax.json"></a>

```
{
  "[AuthorizationType](#cfn-appsync-datasource-authorizationconfig-authorizationtype)" : {{String}},
  "[AwsIamConfig](#cfn-appsync-datasource-authorizationconfig-awsiamconfig)" : {{AwsIamConfig}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-authorizationconfig-syntax.yaml"></a>

```
  [AuthorizationType](#cfn-appsync-datasource-authorizationconfig-authorizationtype): {{String}}
  [AwsIamConfig](#cfn-appsync-datasource-authorizationconfig-awsiamconfig): {{
    AwsIamConfig}}
```

## Properties
<a name="aws-properties-appsync-datasource-authorizationconfig-properties"></a>

`AuthorizationType`  <a name="cfn-appsync-datasource-authorizationconfig-authorizationtype"></a>
The authorization type that the HTTP endpoint requires.
+ **AWS\_IAM**: The authorization type is Signature Version 4 (SigV4).
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_IAM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsIamConfig`  <a name="cfn-appsync-datasource-authorizationconfig-awsiamconfig"></a>
The AWS Identity and Access Management settings.
*Required*: No
*Type*: [AwsIamConfig](aws-properties-appsync-datasource-awsiamconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
