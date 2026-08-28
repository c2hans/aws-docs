---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-configurationprofile-validators.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::ConfigurationProfile Validators
<a name="aws-properties-appconfig-configurationprofile-validators"></a>

A validator provides a syntactic or semantic check to ensure the configuration that you want to deploy functions as intended. To validate your application configuration data, you provide a schema or an AWS Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid. For more information, see [About validators](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html#appconfig-creating-configuration-and-profile-validators) in the *AWS AppConfig User Guide*.

## Syntax
<a name="aws-properties-appconfig-configurationprofile-validators-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-configurationprofile-validators-syntax.json"></a>

```
{
  "[Content](#cfn-appconfig-configurationprofile-validators-content)" : {{String}},
  "[Type](#cfn-appconfig-configurationprofile-validators-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-appconfig-configurationprofile-validators-syntax.yaml"></a>

```
  [Content](#cfn-appconfig-configurationprofile-validators-content): {{String}}
  [Type](#cfn-appconfig-configurationprofile-validators-type): {{String}}
```

## Properties
<a name="aws-properties-appconfig-configurationprofile-validators-properties"></a>

`Content`  <a name="cfn-appconfig-configurationprofile-validators-content"></a>
Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `32768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-appconfig-configurationprofile-validators-type"></a>
AWS AppConfig supports validators of type `JSON_SCHEMA` and `LAMBDA`
*Required*: No
*Type*: String
*Allowed values*: `JSON_SCHEMA | LAMBDA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
