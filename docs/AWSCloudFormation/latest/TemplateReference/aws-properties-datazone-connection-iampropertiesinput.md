---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-iampropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection IamPropertiesInput
<a name="aws-properties-datazone-connection-iampropertiesinput"></a>

The IAM properties of a connection.

## Syntax
<a name="aws-properties-datazone-connection-iampropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-iampropertiesinput-syntax.json"></a>

```
{
  "[GlueLineageSyncEnabled](#cfn-datazone-connection-iampropertiesinput-gluelineagesyncenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-datazone-connection-iampropertiesinput-syntax.yaml"></a>

```
  [GlueLineageSyncEnabled](#cfn-datazone-connection-iampropertiesinput-gluelineagesyncenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-datazone-connection-iampropertiesinput-properties"></a>

`GlueLineageSyncEnabled`  <a name="cfn-datazone-connection-iampropertiesinput-gluelineagesyncenabled"></a>
Specifies whether AWS Glue lineage sync is enabled for a connection.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
