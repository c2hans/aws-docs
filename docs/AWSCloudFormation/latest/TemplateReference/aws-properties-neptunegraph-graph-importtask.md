---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-neptunegraph-graph-importtask.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::Graph ImportTask
<a name="aws-properties-neptunegraph-graph-importtask"></a>

The import task details to import data into the graph at creation time.

## Syntax
<a name="aws-properties-neptunegraph-graph-importtask-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-neptunegraph-graph-importtask-syntax.json"></a>

```
{
  "[BlankNodeHandling](#cfn-neptunegraph-graph-importtask-blanknodehandling)" : {{String}},
  "[FailOnError](#cfn-neptunegraph-graph-importtask-failonerror)" : {{Boolean}},
  "[Format](#cfn-neptunegraph-graph-importtask-format)" : {{String}},
  "[ImportOptions](#cfn-neptunegraph-graph-importtask-importoptions)" : {{ImportOptions}},
  "[MaxProvisionedMemory](#cfn-neptunegraph-graph-importtask-maxprovisionedmemory)" : {{Integer}},
  "[MinProvisionedMemory](#cfn-neptunegraph-graph-importtask-minprovisionedmemory)" : {{Integer}},
  "[ParquetType](#cfn-neptunegraph-graph-importtask-parquettype)" : {{String}},
  "[RoleArn](#cfn-neptunegraph-graph-importtask-rolearn)" : {{String}},
  "[Source](#cfn-neptunegraph-graph-importtask-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-neptunegraph-graph-importtask-syntax.yaml"></a>

```
  [BlankNodeHandling](#cfn-neptunegraph-graph-importtask-blanknodehandling): {{String}}
  [FailOnError](#cfn-neptunegraph-graph-importtask-failonerror): {{Boolean}}
  [Format](#cfn-neptunegraph-graph-importtask-format): {{String}}
  [ImportOptions](#cfn-neptunegraph-graph-importtask-importoptions): {{
    ImportOptions}}
  [MaxProvisionedMemory](#cfn-neptunegraph-graph-importtask-maxprovisionedmemory): {{Integer}}
  [MinProvisionedMemory](#cfn-neptunegraph-graph-importtask-minprovisionedmemory): {{Integer}}
  [ParquetType](#cfn-neptunegraph-graph-importtask-parquettype): {{String}}
  [RoleArn](#cfn-neptunegraph-graph-importtask-rolearn): {{String}}
  [Source](#cfn-neptunegraph-graph-importtask-source): {{String}}
```

## Properties
<a name="aws-properties-neptunegraph-graph-importtask-properties"></a>

`BlankNodeHandling`  <a name="cfn-neptunegraph-graph-importtask-blanknodehandling"></a>
The method to handle blank nodes in the dataset. Currently, only `convertToIri` is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is `NTRIPLES`. For more information, see [Handling RDF values](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling).
*Required*: No
*Type*: String
*Allowed values*: `convertToIri`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FailOnError`  <a name="cfn-neptunegraph-graph-importtask-failonerror"></a>
If set to `true`, the task halts when an import error is encountered. If set to `false`, the task skips the data that caused the error and continues if possible.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Format`  <a name="cfn-neptunegraph-graph-importtask-format"></a>
Specifies the format of S3 data to be imported. Valid values are `CSV`, which identifies the [Gremlin CSV format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html), `OPEN_CYPHER`, which identifies the [openCypher load format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html), `PARQUET`, which identifies the Apache Parquet format, or `NTRIPLES`, which identifies the [RDF n-triples](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html) format.
*Required*: No
*Type*: String
*Allowed values*: `CSV | OPEN_CYPHER | PARQUET | NTRIPLES`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImportOptions`  <a name="cfn-neptunegraph-graph-importtask-importoptions"></a>
Contains options for controlling the import process. Currently, only `NeptuneImportOptions` is available.
*Required*: No
*Type*: [ImportOptions](aws-properties-neptunegraph-graph-importoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxProvisionedMemory`  <a name="cfn-neptunegraph-graph-importtask-maxprovisionedmemory"></a>
The maximum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 1024, or the approved upper limit for your account.
If both the minimum and maximum values are specified, the final `provisioned-memory` will be chosen per the actual size of your imported data. If neither value is specified, 128 m-NCUs are used.
*Required*: No
*Type*: Integer
*Minimum*: `16`
*Maximum*: `24576`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinProvisionedMemory`  <a name="cfn-neptunegraph-graph-importtask-minprovisionedmemory"></a>
The minimum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 16
*Required*: No
*Type*: Integer
*Minimum*: `16`
*Maximum*: `24576`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParquetType`  <a name="cfn-neptunegraph-graph-importtask-parquettype"></a>
The parquet type of the import task. Currently, only `COLUMNAR` is supported. Required when `Format` is `PARQUET`.
*Required*: No
*Type*: String
*Allowed values*: `COLUMNAR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-neptunegraph-graph-importtask-rolearn"></a>
The ARN of the IAM role that will allow access to the data that is to be imported.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws[^:]*:iam::[0-9]{12}:(role|role/service-role)(/[\w+=,.@-]+)+`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Source`  <a name="cfn-neptunegraph-graph-importtask-source"></a>
A URL that identifies the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
