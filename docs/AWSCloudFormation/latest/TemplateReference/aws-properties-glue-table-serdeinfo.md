---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-serdeinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table SerdeInfo
<a name="aws-properties-glue-table-serdeinfo"></a>

Information about a serialization/deserialization program (SerDe) that serves as an extractor and loader.

## Syntax
<a name="aws-properties-glue-table-serdeinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-serdeinfo-syntax.json"></a>

```
{
  "[Name](#cfn-glue-table-serdeinfo-name)" : {{String}},
  "[Parameters](#cfn-glue-table-serdeinfo-parameters)" : {{Json}},
  "[SerializationLibrary](#cfn-glue-table-serdeinfo-serializationlibrary)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-table-serdeinfo-syntax.yaml"></a>

```
  [Name](#cfn-glue-table-serdeinfo-name): {{String}}
  [Parameters](#cfn-glue-table-serdeinfo-parameters): {{Json}}
  [SerializationLibrary](#cfn-glue-table-serdeinfo-serializationlibrary): {{String}}
```

## Properties
<a name="aws-properties-glue-table-serdeinfo-properties"></a>

`Name`  <a name="cfn-glue-table-serdeinfo-name"></a>
Name of the SerDe.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-glue-table-serdeinfo-parameters"></a>
These key-value pairs define initialization parameters for the SerDe.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SerializationLibrary`  <a name="cfn-glue-table-serdeinfo-serializationlibrary"></a>
Usually the class that implements the SerDe. An example is `org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-glue-table-serdeinfo--seealso"></a>
+ [SerDeInfo Structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-SerDeInfo) in the *AWS Glue Developer Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
