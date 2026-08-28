---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-integrationresourceproperty-sourceprocessingproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::IntegrationResourceProperty SourceProcessingProperties
<a name="aws-properties-glue-integrationresourceproperty-sourceprocessingproperties"></a>

The structure used to define the resource properties associated with the integration source.

## Syntax
<a name="aws-properties-glue-integrationresourceproperty-sourceprocessingproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-integrationresourceproperty-sourceprocessingproperties-syntax.json"></a>

```
{
  "[RoleArn](#cfn-glue-integrationresourceproperty-sourceprocessingproperties-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-integrationresourceproperty-sourceprocessingproperties-syntax.yaml"></a>

```
  [RoleArn](#cfn-glue-integrationresourceproperty-sourceprocessingproperties-rolearn): {{String}}
```

## Properties
<a name="aws-properties-glue-integrationresourceproperty-sourceprocessingproperties-properties"></a>

`RoleArn`  <a name="cfn-glue-integrationresourceproperty-sourceprocessingproperties-rolearn"></a>
The IAM role to access the AWS Glue connection.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
