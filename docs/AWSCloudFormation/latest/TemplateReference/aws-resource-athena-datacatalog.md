---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-athena-datacatalog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::DataCatalog
<a name="aws-resource-athena-datacatalog"></a>

The AWS::Athena::DataCatalog resource specifies an Amazon Athena data catalog, which contains a name, description, type, parameters, and tags. For more information, see [DataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_DataCatalog.html) in the *Amazon Athena API Reference*.

## Syntax
<a name="aws-resource-athena-datacatalog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-athena-datacatalog-syntax.json"></a>

```
{
  "Type" : "AWS::Athena::DataCatalog",
  "Properties" : {
      "[ConnectionType](#cfn-athena-datacatalog-connectiontype)" : {{String}},
      "[Description](#cfn-athena-datacatalog-description)" : {{String}},
      "[Error](#cfn-athena-datacatalog-error)" : {{String}},
      "[Name](#cfn-athena-datacatalog-name)" : {{String}},
      "[Parameters](#cfn-athena-datacatalog-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Status](#cfn-athena-datacatalog-status)" : {{String}},
      "[Tags](#cfn-athena-datacatalog-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-athena-datacatalog-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-athena-datacatalog-syntax.yaml"></a>

```
Type: AWS::Athena::DataCatalog
Properties:
  [ConnectionType](#cfn-athena-datacatalog-connectiontype): {{String}}
  [Description](#cfn-athena-datacatalog-description): {{String}}
  [Error](#cfn-athena-datacatalog-error): {{String}}
  [Name](#cfn-athena-datacatalog-name): {{String}}
  [Parameters](#cfn-athena-datacatalog-parameters): {{
    {{Key}}: {{Value}}}}
  [Status](#cfn-athena-datacatalog-status): {{String}}
  [Tags](#cfn-athena-datacatalog-tags): {{
    - Tag}}
  [Type](#cfn-athena-datacatalog-type): {{String}}
```

## Properties
<a name="aws-resource-athena-datacatalog-properties"></a>

`ConnectionType`  <a name="cfn-athena-datacatalog-connectiontype"></a>
The type of connection for a `FEDERATED` data catalog (for example, `REDSHIFT`, `MYSQL`, or `SQLSERVER`). For information about individual connectors, see [Available data source connectors](https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html).
*Required*: No
*Type*: String
*Allowed values*: `DYNAMODB | MYSQL | POSTGRESQL | REDSHIFT | ORACLE | SYNAPSE | SQLSERVER | DB2 | OPENSEARCH | BIGQUERY | GOOGLECLOUDSTORAGE | HBASE | DOCUMENTDB | CMDB | TPCDS | TIMESTREAM | SAPHANA | SNOWFLAKE | DATALAKEGEN2 | DB2AS400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-athena-datacatalog-description"></a>
A description of the data catalog.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Error`  <a name="cfn-athena-datacatalog-error"></a>
Text of the error that occurred during data catalog creation or deletion.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-athena-datacatalog-name"></a>
The name of the data catalog. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-athena-datacatalog-parameters"></a>
Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type.
+ For the `HIVE` data catalog type, use the following syntax. The `metadata-function` parameter is required. `The sdk-version` parameter is optional and defaults to the currently supported version.

   `metadata-function=lambda_arn, sdk-version=version_number`
+ For the `LAMBDA` data catalog type, use one of the following sets of required parameters, but not both.
  + If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.

     `metadata-function=lambda_arn, record-function=lambda_arn`
  +  If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.

     `function=lambda_arn`
+ The `GLUE` type takes a catalog ID parameter and is required. The ` catalog_id ` is the account ID of the AWS account to which the AWS Glue Data Catalog belongs.

   `catalog-id=catalog_id`
  + The `GLUE` data catalog type also applies to the default `AwsDataCatalog` that already exists in your account, of which you can have only one and cannot modify.
+ The `FEDERATED` data catalog type uses one of the following parameters, but not both. Use `connection-arn` for an existing AWS Glue connection. Use `connection-type` and `connection-properties` to specify the configuration setting for a new connection.
  +  `connection-arn:<glue_connection_arn_to_reuse>`
  + `lambda-role-arn` (optional): The execution role to use for the Lambda function. If not provided, one is created.
  +  `connection-type:MYSQL|REDSHIFT|...., connection-properties:"<json_string>"`

    For * `<json_string>` *, use escaped JSON text, as in the following example.

     `"{\"spill_bucket\":\"my_spill\",\"spill_prefix\":\"athena-spill\",\"host\":\"abc12345.snowflakecomputing.com\",\"port\":\"1234\",\"warehouse\":\"DEV_WH\",\"database\":\"TEST\",\"schema\":\"PUBLIC\",\"SecretArn\":\"arn:aws:secretsmanager:ap-south-1:111122223333:secret:snowflake-XHb67j\"}"`
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-athena-datacatalog-status"></a>
The status of the creation or deletion of the data catalog.
+ The `LAMBDA`, `GLUE`, and `HIVE` data catalog types are created synchronously. Their status is either `CREATE_COMPLETE` or `CREATE_FAILED`.
+ The `FEDERATED` data catalog type is created asynchronously.
Data catalog creation status:
+ `CREATE_IN_PROGRESS`: Federated data catalog creation in progress.
+ `CREATE_COMPLETE`: Data catalog creation complete.
+ `CREATE_FAILED`: Data catalog could not be created.
+ `CREATE_FAILED_CLEANUP_IN_PROGRESS`: Federated data catalog creation failed and is being removed.
+ `CREATE_FAILED_CLEANUP_COMPLETE`: Federated data catalog creation failed and was removed.
+ `CREATE_FAILED_CLEANUP_FAILED`: Federated data catalog creation failed but could not be removed.
Data catalog deletion status:
+ `DELETE_IN_PROGRESS`: Federated data catalog deletion in progress.
+ `DELETE_COMPLETE`: Federated data catalog deleted.
+ `DELETE_FAILED`: Federated data catalog could not be deleted.
*Required*: No
*Type*: String
*Allowed values*: `CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | CREATE_FAILED_CLEANUP_IN_PROGRESS | CREATE_FAILED_CLEANUP_COMPLETE | CREATE_FAILED_CLEANUP_FAILED | DELETE_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-athena-datacatalog-tags"></a>
The tags (key-value pairs) to associate with this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-athena-datacatalog-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-athena-datacatalog-type"></a>
The type of data catalog: `LAMBDA` for a federated catalog, `GLUE` for AWS Glue Catalog, or `HIVE` for an external hive metastore.
*Required*: Yes
*Type*: String
*Allowed values*: `LAMBDA | GLUE | HIVE | FEDERATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-athena-datacatalog-return-values"></a>

### Ref
<a name="aws-resource-athena-datacatalog-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the data catalog.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-athena-datacatalog--examples"></a>

### Create an Athena data catalog
<a name="aws-resource-athena-datacatalog--examples--Create_an_Athena_data_catalog"></a>

The following example template creates a custom Hive data catalog in Athena.

#### JSON
<a name="aws-resource-athena-datacatalog--examples--Create_an_Athena_data_catalog--json"></a>

```
{
    "Resources":{
        "MyAthenaDataCatalog":{
            "Type":"AWS::Athena::DataCatalog",
            "Properties":{
                "Name":"MyCustomDataCatalog",
                "Type":"HIVE",
                "Description":"Custom Hive Catalog Description",
                "Tags":[
                    {
                        "Key":"key1",
                        "Value":"value1"
                    },
                    {
                        "Key":"key2",
                        "Value":"value2"
                    }
                ],
                "Parameters":{
                    "metadata-function":"arn:aws:lambda:us-west-2:111122223333:function:lambdaname"
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-athena-datacatalog--examples--Create_an_Athena_data_catalog--yaml"></a>

```
Resources:
  MyAthenaDataCatalog:
    Type: AWS::Athena::DataCatalog
    Properties:
      Name: MyCustomDataCatalog
      Type: HIVE
      Description: Custom Hive Catalog Description
      Tags:
        - Key: "key1"
          Value: "value1"
        - Key: "key2"
          Value: "value2"
      Parameters:
        metadata-function: "arn:aws:lambda:us-west-2:111122223333:function:lambdaname"
```
