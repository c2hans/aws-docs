---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource
<a name="aws-resource-quicksight-datasource"></a>

Creates a data source.

## Syntax
<a name="aws-resource-quicksight-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-datasource-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::DataSource",
  "Properties" : {
      "[AlternateDataSourceParameters](#cfn-quicksight-datasource-alternatedatasourceparameters)" : {{[ DataSourceParameters, ... ]}},
      "[AwsAccountId](#cfn-quicksight-datasource-awsaccountid)" : {{String}},
      "[Credentials](#cfn-quicksight-datasource-credentials)" : {{DataSourceCredentials}},
      "[DataSourceId](#cfn-quicksight-datasource-datasourceid)" : {{String}},
      "[DataSourceParameters](#cfn-quicksight-datasource-datasourceparameters)" : {{DataSourceParameters}},
      "[ErrorInfo](#cfn-quicksight-datasource-errorinfo)" : {{DataSourceErrorInfo}},
      "[FolderArns](#cfn-quicksight-datasource-folderarns)" : {{[ String, ... ]}},
      "[Name](#cfn-quicksight-datasource-name)" : {{String}},
      "[Permissions](#cfn-quicksight-datasource-permissions)" : {{[ ResourcePermission, ... ]}},
      "[SslProperties](#cfn-quicksight-datasource-sslproperties)" : {{SslProperties}},
      "[Tags](#cfn-quicksight-datasource-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-quicksight-datasource-type)" : {{String}},
      "[VpcConnectionProperties](#cfn-quicksight-datasource-vpcconnectionproperties)" : {{VpcConnectionProperties}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-datasource-syntax.yaml"></a>

```
Type: AWS::QuickSight::DataSource
Properties:
  [AlternateDataSourceParameters](#cfn-quicksight-datasource-alternatedatasourceparameters): {{
    - DataSourceParameters}}
  [AwsAccountId](#cfn-quicksight-datasource-awsaccountid): {{String}}
  [Credentials](#cfn-quicksight-datasource-credentials): {{
    DataSourceCredentials}}
  [DataSourceId](#cfn-quicksight-datasource-datasourceid): {{String}}
  [DataSourceParameters](#cfn-quicksight-datasource-datasourceparameters): {{
    DataSourceParameters}}
  [ErrorInfo](#cfn-quicksight-datasource-errorinfo): {{
    DataSourceErrorInfo}}
  [FolderArns](#cfn-quicksight-datasource-folderarns): {{
    - String}}
  [Name](#cfn-quicksight-datasource-name): {{String}}
  [Permissions](#cfn-quicksight-datasource-permissions): {{
    - ResourcePermission}}
  [SslProperties](#cfn-quicksight-datasource-sslproperties): {{
    SslProperties}}
  [Tags](#cfn-quicksight-datasource-tags): {{
    - Tag}}
  [Type](#cfn-quicksight-datasource-type): {{String}}
  [VpcConnectionProperties](#cfn-quicksight-datasource-vpcconnectionproperties): {{
    VpcConnectionProperties}}
```

## Properties
<a name="aws-resource-quicksight-datasource-properties"></a>

`AlternateDataSourceParameters`  <a name="cfn-quicksight-datasource-alternatedatasourceparameters"></a>
A set of alternate data source parameters that you want to share for the credentials stored with this data source. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the `DataSourceParameters` structure that's in the request with the structures in the `AlternateDataSourceParameters` allow list. If the structures are an exact match, the request is allowed to use the credentials from this existing data source. If the `AlternateDataSourceParameters` list is null, the `Credentials` originally used with this `DataSourceParameters` are automatically allowed.
*Required*: No
*Type*: Array of [DataSourceParameters](aws-properties-quicksight-datasource-datasourceparameters.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsAccountId`  <a name="cfn-quicksight-datasource-awsaccountid"></a>
The AWS account ID.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Credentials`  <a name="cfn-quicksight-datasource-credentials"></a>
The credentials Amazon Quick Sight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.
*Required*: No
*Type*: [DataSourceCredentials](aws-properties-quicksight-datasource-datasourcecredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSourceId`  <a name="cfn-quicksight-datasource-datasourceid"></a>
An ID for the data source. This ID is unique per AWS Region for each AWS account.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSourceParameters`  <a name="cfn-quicksight-datasource-datasourceparameters"></a>
The parameters that Amazon Quick Sight uses to connect to your underlying source.
*Required*: No
*Type*: [DataSourceParameters](aws-properties-quicksight-datasource-datasourceparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ErrorInfo`  <a name="cfn-quicksight-datasource-errorinfo"></a>
Error information from the last update or the creation of the data source.
*Required*: No
*Type*: [DataSourceErrorInfo](aws-properties-quicksight-datasource-datasourceerrorinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FolderArns`  <a name="cfn-quicksight-datasource-folderarns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-datasource-name"></a>
A display name for the data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-datasource-permissions"></a>
A list of resource permissions on the data source.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-datasource-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslProperties`  <a name="cfn-quicksight-datasource-sslproperties"></a>
Secure Socket Layer (SSL) properties that apply when Amazon Quick Sight connects to your underlying source.
*Required*: No
*Type*: [SslProperties](aws-properties-quicksight-datasource-sslproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-datasource-tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-datasource-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-datasource-type"></a>
The type of the data source. To return a list of all data sources, use `ListDataSources`.
Use `AMAZON_ELASTICSEARCH` for Amazon OpenSearch Service.
*Required*: Yes
*Type*: String
*Allowed values*: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | AMAZON_OPENSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | DATABRICKS | DENODO | DREMIO | DYNAMODB | SAPHANA | DB2_AS400 | EXASOL | FILE | FULLY_MANAGED_KNOWLEDGE_BASE | GITHUB | INTERNATIONAL_DATA_CORPORATION | JIRA | MARIADB | MYSQL | ORACLE | POSTGRESQL | PRESTO | QBUSINESS | REDSHIFT | S3 | S3_TABLES | S3_KNOWLEDGE_BASE | SALESFORCE | SERVICENOW | SNOWFLAKE | SPARK | SPICE | SQLSERVER | TERADATA | TIMESTREAM | TWITTER | BIGQUERY | GOOGLE_ANALYTICS | TRINO | STARBURST | MONGO | MONGO_ATLAS | DOCUMENTDB | APPFLOW | IMPALA | GLUE | GOOGLE_DRIVE | CONFLUENCE | SHAREPOINT | ONE_DRIVE | WEB_CRAWLER | BOX | GOOGLESHEETS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConnectionProperties`  <a name="cfn-quicksight-datasource-vpcconnectionproperties"></a>
Use this parameter only when you want Amazon Quick Sight to use a VPC connection when connecting to your underlying source.
*Required*: No
*Type*: [VpcConnectionProperties](aws-properties-quicksight-datasource-vpcconnectionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-datasource-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-datasource-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-datasource-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the dataset.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time that this data source was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The last time that this data source was updated.

`Status`  <a name="Status-fn::getatt"></a>
The HTTP status of the request.
