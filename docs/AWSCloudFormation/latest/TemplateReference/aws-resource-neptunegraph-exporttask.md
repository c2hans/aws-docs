---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-neptunegraph-exporttask.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::ExportTask
<a name="aws-resource-neptunegraph-exporttask"></a>

<a name="aws-resource-neptunegraph-exporttask-description"></a>The `AWS::NeptuneGraph::ExportTask` resource Property description not available. for NeptuneGraph.

## Syntax
<a name="aws-resource-neptunegraph-exporttask-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-neptunegraph-exporttask-syntax.json"></a>

```
{
  "Type" : "AWS::NeptuneGraph::ExportTask",
  "Properties" : {
      "[Destination](#cfn-neptunegraph-exporttask-destination)" : {{String}},
      "[ExportFilter](#cfn-neptunegraph-exporttask-exportfilter)" : {{ExportFilter}},
      "[Format](#cfn-neptunegraph-exporttask-format)" : {{String}},
      "[GraphIdentifier](#cfn-neptunegraph-exporttask-graphidentifier)" : {{String}},
      "[KmsKeyIdentifier](#cfn-neptunegraph-exporttask-kmskeyidentifier)" : {{String}},
      "[ParquetType](#cfn-neptunegraph-exporttask-parquettype)" : {{String}},
      "[RoleArn](#cfn-neptunegraph-exporttask-rolearn)" : {{String}},
      "[Tags](#cfn-neptunegraph-exporttask-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-neptunegraph-exporttask-syntax.yaml"></a>

```
Type: AWS::NeptuneGraph::ExportTask
Properties:
  [Destination](#cfn-neptunegraph-exporttask-destination): {{String}}
  [ExportFilter](#cfn-neptunegraph-exporttask-exportfilter): {{
    ExportFilter}}
  [Format](#cfn-neptunegraph-exporttask-format): {{String}}
  [GraphIdentifier](#cfn-neptunegraph-exporttask-graphidentifier): {{String}}
  [KmsKeyIdentifier](#cfn-neptunegraph-exporttask-kmskeyidentifier): {{String}}
  [ParquetType](#cfn-neptunegraph-exporttask-parquettype): {{String}}
  [RoleArn](#cfn-neptunegraph-exporttask-rolearn): {{String}}
  [Tags](#cfn-neptunegraph-exporttask-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-neptunegraph-exporttask-properties"></a>

`Destination`  <a name="cfn-neptunegraph-exporttask-destination"></a>
The Amazon S3 URI of the export task where data will be exported to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExportFilter`  <a name="cfn-neptunegraph-exporttask-exportfilter"></a>
Property description not available.
*Required*: No
*Type*: [ExportFilter](aws-properties-neptunegraph-exporttask-exportfilter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Format`  <a name="cfn-neptunegraph-exporttask-format"></a>
The format of the export task.
*Required*: Yes
*Type*: String
*Allowed values*: `PARQUET | CSV`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GraphIdentifier`  <a name="cfn-neptunegraph-exporttask-graphidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^g-[a-z0-9]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyIdentifier`  <a name="cfn-neptunegraph-exporttask-kmskeyidentifier"></a>
The KMS key identifier of the export task.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParquetType`  <a name="cfn-neptunegraph-exporttask-parquettype"></a>
The parquet type of the export task.
*Required*: No
*Type*: String
*Allowed values*: `COLUMNAR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-neptunegraph-exporttask-rolearn"></a>
The ARN of the IAM role that will allow the data to be exported to the destination.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-neptunegraph-exporttask-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-neptunegraph-exporttask-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-neptunegraph-exporttask-return-values"></a>

### Ref
<a name="aws-resource-neptunegraph-exporttask-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-neptunegraph-exporttask-return-values-fn--getatt"></a>

####
<a name="aws-resource-neptunegraph-exporttask-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the export task.

`TaskId`  <a name="TaskId-fn::getatt"></a>
The unique identifier of the export task.
