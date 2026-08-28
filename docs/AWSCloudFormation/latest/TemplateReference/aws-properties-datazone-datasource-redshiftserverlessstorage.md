---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-redshiftserverlessstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource RedshiftServerlessStorage
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage"></a>

The details of the Amazon Redshift Serverless workgroup storage.

## Syntax
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage-syntax.json"></a>

```
{
  "[WorkgroupName](#cfn-datazone-datasource-redshiftserverlessstorage-workgroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage-syntax.yaml"></a>

```
  [WorkgroupName](#cfn-datazone-datasource-redshiftserverlessstorage-workgroupname): {{String}}
```

## Properties
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage-properties"></a>

`WorkgroupName`  <a name="cfn-datazone-datasource-redshiftserverlessstorage-workgroupname"></a>
The name of the Amazon Redshift Serverless workgroup.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
