---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-qbusiness-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource
<a name="aws-resource-qbusiness-datasource"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates a data source connector for an Amazon Q Business application.

`CreateDataSource` is a synchronous operation. The operation returns 200 if the data source was successfully created. Otherwise, an exception is raised.

## Syntax
<a name="aws-resource-qbusiness-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-qbusiness-datasource-syntax.json"></a>

```
{
  "Type" : "AWS::QBusiness::DataSource",
  "Properties" : {
      "[ApplicationId](#cfn-qbusiness-datasource-applicationid)" : {{String}},
      "[Configuration](#cfn-qbusiness-datasource-configuration)" : {{}},
      "[Description](#cfn-qbusiness-datasource-description)" : {{String}},
      "[DisplayName](#cfn-qbusiness-datasource-displayname)" : {{String}},
      "[DocumentEnrichmentConfiguration](#cfn-qbusiness-datasource-documentenrichmentconfiguration)" : {{DocumentEnrichmentConfiguration}},
      "[IndexId](#cfn-qbusiness-datasource-indexid)" : {{String}},
      "[MediaExtractionConfiguration](#cfn-qbusiness-datasource-mediaextractionconfiguration)" : {{MediaExtractionConfiguration}},
      "[RoleArn](#cfn-qbusiness-datasource-rolearn)" : {{String}},
      "[SyncSchedule](#cfn-qbusiness-datasource-syncschedule)" : {{String}},
      "[Tags](#cfn-qbusiness-datasource-tags)" : {{[ Tag, ... ]}},
      "[VpcConfiguration](#cfn-qbusiness-datasource-vpcconfiguration)" : {{DataSourceVpcConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-qbusiness-datasource-syntax.yaml"></a>

```
Type: AWS::QBusiness::DataSource
Properties:
  [ApplicationId](#cfn-qbusiness-datasource-applicationid): {{String}}
  [Configuration](#cfn-qbusiness-datasource-configuration): {{
    }}
  [Description](#cfn-qbusiness-datasource-description): {{String}}
  [DisplayName](#cfn-qbusiness-datasource-displayname): {{String}}
  [DocumentEnrichmentConfiguration](#cfn-qbusiness-datasource-documentenrichmentconfiguration): {{
    DocumentEnrichmentConfiguration}}
  [IndexId](#cfn-qbusiness-datasource-indexid): {{String}}
  [MediaExtractionConfiguration](#cfn-qbusiness-datasource-mediaextractionconfiguration): {{
    MediaExtractionConfiguration}}
  [RoleArn](#cfn-qbusiness-datasource-rolearn): {{String}}
  [SyncSchedule](#cfn-qbusiness-datasource-syncschedule): {{String}}
  [Tags](#cfn-qbusiness-datasource-tags): {{
    - Tag}}
  [VpcConfiguration](#cfn-qbusiness-datasource-vpcconfiguration): {{
    DataSourceVpcConfiguration}}
```

## Properties
<a name="aws-resource-qbusiness-datasource-properties"></a>

`ApplicationId`  <a name="cfn-qbusiness-datasource-applicationid"></a>
 The identifier of the Amazon Q Business application the data source will be attached to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-qbusiness-datasource-configuration"></a>
Use this property to specify a JSON or YAML schema with configuration properties specific to your data source connector to connect your data source repository to Amazon Q Business. You must use the JSON or YAML schema provided by Amazon Q.
The following links have the configuration properties and schemas for AWS CloudFormation for the following connectors:
+  [Amazon Simple Storage Service](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-cfn.html)
+  [Amazon Q Web Crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-cfn.html)
Similarly, you can find configuration templates and properties for your specific data source using the following steps:

1. Navigate to the [Supported connectors](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html) page in the Amazon Q Business User Guide, and select the data source connector of your choice.

1. Then, from that specific data source connector's page, choose the topic containing **Using CloudFormation** to find the schemas for your data source connector, including configuration parameter descriptions and examples.
*Required*: Yes
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-qbusiness-datasource-description"></a>
A description for the data source connector.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-qbusiness-datasource-displayname"></a>
The name of the Amazon Q Business data source.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentEnrichmentConfiguration`  <a name="cfn-qbusiness-datasource-documentenrichmentconfiguration"></a>
Provides the configuration information for altering document metadata and content during the document ingestion process.
For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).
*Required*: No
*Type*: [DocumentEnrichmentConfiguration](aws-properties-qbusiness-datasource-documentenrichmentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexId`  <a name="cfn-qbusiness-datasource-indexid"></a>
The identifier of the index the data source is attached to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MediaExtractionConfiguration`  <a name="cfn-qbusiness-datasource-mediaextractionconfiguration"></a>
The configuration for extracting information from media in documents.
*Required*: No
*Type*: [MediaExtractionConfiguration](aws-properties-qbusiness-datasource-mediaextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-qbusiness-datasource-rolearn"></a>
The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. This field is required for all connector types except custom connectors, where it is optional.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SyncSchedule`  <a name="cfn-qbusiness-datasource-syncschedule"></a>
Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index. If you don't set a schedule, Amazon Q Business won't periodically update the index.
Specify a `cron-` format schedule string or an empty string to indicate that the index is updated on demand. You can't specify the `Schedule` parameter when the `Type` parameter is set to `CUSTOM`. If you do, you receive a `ValidationException` exception.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]*$`
*Maximum*: `998`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-qbusiness-datasource-tags"></a>
A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
*Required*: No
*Type*: Array of [Tag](aws-properties-qbusiness-datasource-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfiguration`  <a name="cfn-qbusiness-datasource-vpcconfiguration"></a>
Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source. For more information, see [Using Amazon VPC with Amazon Q Business connectors](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html).
*Required*: No
*Type*: [DataSourceVpcConfiguration](aws-properties-qbusiness-datasource-datasourcevpcconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-qbusiness-datasource-return-values"></a>

### Ref
<a name="aws-resource-qbusiness-datasource-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application ID, data source ID, and index ID. For example:

 `{"Ref": "ApplicationId|DataSourceId|IndexId"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-qbusiness-datasource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-qbusiness-datasource-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The Unix timestamp when the Amazon Q Business data source was created.

`DataSourceArn`  <a name="DataSourceArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of a data source in an Amazon Q Business application.

`DataSourceId`  <a name="DataSourceId-fn::getatt"></a>
The identifier of the Amazon Q Business data source.

`Status`  <a name="Status-fn::getatt"></a>
The status of the Amazon Q Business data source.

`Type`  <a name="Type-fn::getatt"></a>
The type of the Amazon Q Business data source.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The Unix timestamp when the Amazon Q Business data source was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
