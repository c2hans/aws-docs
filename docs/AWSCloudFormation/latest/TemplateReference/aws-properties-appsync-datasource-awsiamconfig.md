---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-awsiamconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource AwsIamConfig
<a name="aws-properties-appsync-datasource-awsiamconfig"></a>

Use the `AwsIamConfig` property type to specify `AwsIamConfig` for a AWS AppSync authorizaton.

`AwsIamConfig` is a property of the [AWS AppSync DataSource AuthorizationConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig-authorizationconfig.html) resource.

## Syntax
<a name="aws-properties-appsync-datasource-awsiamconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-awsiamconfig-syntax.json"></a>

```
{
  "[SigningRegion](#cfn-appsync-datasource-awsiamconfig-signingregion)" : {{String}},
  "[SigningServiceName](#cfn-appsync-datasource-awsiamconfig-signingservicename)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-awsiamconfig-syntax.yaml"></a>

```
  [SigningRegion](#cfn-appsync-datasource-awsiamconfig-signingregion): {{String}}
  [SigningServiceName](#cfn-appsync-datasource-awsiamconfig-signingservicename): {{String}}
```

## Properties
<a name="aws-properties-appsync-datasource-awsiamconfig-properties"></a>

`SigningRegion`  <a name="cfn-appsync-datasource-awsiamconfig-signingregion"></a>
The signing Region for AWS Identity and Access Management authorization.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SigningServiceName`  <a name="cfn-appsync-datasource-awsiamconfig-signingservicename"></a>
The signing service name for AWS Identity and Access Management authorization.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
