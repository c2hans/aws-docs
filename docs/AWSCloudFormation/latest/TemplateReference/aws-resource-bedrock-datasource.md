---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource
<a name="aws-resource-bedrock-datasource"></a>

**Important**
Properties with `__Update requires: Replacement__` can result in the creation of a new data source and deletion of the old one. This can happen if you also change the Name of the data source.

Specifies a data source as a resource in a top-level template. Minimally, you must specify the following properties:
+ Name – Specify a name for the data source.
+ KnowledgeBaseId – Specify the ID of the knowledge base for the data source to belong to.
+ DataSourceConfiguration – Specify information about the Amazon S3 bucket containing the data source. The following sub-properties are required:
  + Type – Specify the value `S3`.

For more information about setting up data sources in Amazon Bedrock, see [Set up a data source for your knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrock-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-datasource-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::DataSource",
  "Properties" : {
      "[DataDeletionPolicy](#cfn-bedrock-datasource-datadeletionpolicy)" : {{String}},
      "[DataSourceConfiguration](#cfn-bedrock-datasource-datasourceconfiguration)" : {{DataSourceConfiguration}},
      "[Description](#cfn-bedrock-datasource-description)" : {{String}},
      "[KnowledgeBaseId](#cfn-bedrock-datasource-knowledgebaseid)" : {{String}},
      "[Name](#cfn-bedrock-datasource-name)" : {{String}},
      "[ServerSideEncryptionConfiguration](#cfn-bedrock-datasource-serversideencryptionconfiguration)" : {{ServerSideEncryptionConfiguration}},
      "[VectorIngestionConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration)" : {{VectorIngestionConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-datasource-syntax.yaml"></a>

```
Type: AWS::Bedrock::DataSource
Properties:
  [DataDeletionPolicy](#cfn-bedrock-datasource-datadeletionpolicy): {{String}}
  [DataSourceConfiguration](#cfn-bedrock-datasource-datasourceconfiguration): {{
    DataSourceConfiguration}}
  [Description](#cfn-bedrock-datasource-description): {{String}}
  [KnowledgeBaseId](#cfn-bedrock-datasource-knowledgebaseid): {{String}}
  [Name](#cfn-bedrock-datasource-name): {{String}}
  [ServerSideEncryptionConfiguration](#cfn-bedrock-datasource-serversideencryptionconfiguration): {{
    ServerSideEncryptionConfiguration}}
  [VectorIngestionConfiguration](#cfn-bedrock-datasource-vectoringestionconfiguration): {{
    VectorIngestionConfiguration}}
```

## Properties
<a name="aws-resource-bedrock-datasource-properties"></a>

`DataDeletionPolicy`  <a name="cfn-bedrock-datasource-datadeletionpolicy"></a>
The data deletion policy for the data source.
*Required*: No
*Type*: String
*Allowed values*: `RETAIN | DELETE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSourceConfiguration`  <a name="cfn-bedrock-datasource-datasourceconfiguration"></a>
The connection configuration for the data source.
*Required*: Yes
*Type*: [DataSourceConfiguration](aws-properties-bedrock-datasource-datasourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-datasource-description"></a>
The description of the data source.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KnowledgeBaseId`  <a name="cfn-bedrock-datasource-knowledgebaseid"></a>
The unique identifier of the knowledge base to which the data source belongs.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrock-datasource-name"></a>
The name of the data source.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerSideEncryptionConfiguration`  <a name="cfn-bedrock-datasource-serversideencryptionconfiguration"></a>
Contains details about the configuration of the server-side encryption.
*Required*: No
*Type*: [ServerSideEncryptionConfiguration](aws-properties-bedrock-datasource-serversideencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VectorIngestionConfiguration`  <a name="cfn-bedrock-datasource-vectoringestionconfiguration"></a>
Contains details about how to ingest the documents in the data source.
*Required*: No
*Type*: [VectorIngestionConfiguration](aws-properties-bedrock-datasource-vectoringestionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-datasource-return-values"></a>

### Ref
<a name="aws-resource-bedrock-datasource-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the knowledge base ID and the data source ID, separated by a pipe (`|`).

For example, `{ "Ref": "myDataSource" }` could return the value `"KB12345678|DS12345678"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-datasource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-datasource-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the data source was created.

`DataSourceConfiguration.WebConfiguration.CrawlerConfiguration.UserAgentHeader`  <a name="DataSourceConfiguration.WebConfiguration.CrawlerConfiguration.UserAgentHeader-fn::getatt"></a>
Property description not available.

`DataSourceId`  <a name="DataSourceId-fn::getatt"></a>
The unique identifier of the data source.

`DataSourceStatus`  <a name="DataSourceStatus-fn::getatt"></a>
The status of the data source. The following statuses are possible:
+ Available – The data source has been created and is ready for ingestion into the knowledge base.
+ Deleting – The data source is being deleted.

`FailureReasons`  <a name="FailureReasons-fn::getatt"></a>
The detailed reasons on the failure to delete a data source.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the data source was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
