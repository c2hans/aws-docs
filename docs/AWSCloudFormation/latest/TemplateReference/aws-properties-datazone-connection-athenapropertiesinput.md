---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-athenapropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection AthenaPropertiesInput
<a name="aws-properties-datazone-connection-athenapropertiesinput"></a>

The Amazon Athena properties of a connection.

## Syntax
<a name="aws-properties-datazone-connection-athenapropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-athenapropertiesinput-syntax.json"></a>

```
{
  "[WorkgroupName](#cfn-datazone-connection-athenapropertiesinput-workgroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-athenapropertiesinput-syntax.yaml"></a>

```
  [WorkgroupName](#cfn-datazone-connection-athenapropertiesinput-workgroupname): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-athenapropertiesinput-properties"></a>

`WorkgroupName`  <a name="cfn-datazone-connection-athenapropertiesinput-workgroupname"></a>
The Amazon Athena workgroup name of a connection.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]+$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
