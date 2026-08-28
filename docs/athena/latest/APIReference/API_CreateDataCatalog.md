---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateDataCatalog.html
---

# CreateDataCatalog
<a name="API_CreateDataCatalog"></a>

Creates (registers) a data catalog with the specified name and properties. Catalogs created are visible to all users of the same AWS account.

For a `FEDERATED` catalog, this API operation creates the following resources.
+ CFN Stack Name with a maximum length of 128 characters and prefix `athenafederatedcatalog-CATALOG_NAME_SANITIZED` with length 23 characters.
+ Lambda Function Name with a maximum length of 64 characters and prefix `athenafederatedcatalog_CATALOG_NAME_SANITIZED` with length 23 characters.
+ Glue Connection Name with a maximum length of 255 characters and a prefix `athenafederatedcatalog_CATALOG_NAME_SANITIZED` with length 23 characters.

## Request Syntax
<a name="API_CreateDataCatalog_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Parameters": {
      "{{string}}" : "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDataCatalog_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateDataCatalog_RequestSyntax) **   <a name="athena-CreateDataCatalog-request-Description"></a>
A description of the data catalog to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Name](#API_CreateDataCatalog_RequestSyntax) **   <a name="athena-CreateDataCatalog-request-Name"></a>
The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.
For `FEDERATED` type the catalog name has following considerations and limits:
+ The catalog name allows special characters such as `_ , @ , \ , - `. These characters are replaced with a hyphen (-) when creating the CFN Stack Name and with an underscore (\_) when creating the Lambda Function and Glue Connection Name.
+ The catalog name has a theoretical limit of 128 characters. However, since we use it to create other resources that allow less characters and we prepend a prefix to it, the actual catalog name limit for `FEDERATED` catalog is 64 - 23 = 41 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Parameters](#API_CreateDataCatalog_RequestSyntax) **   <a name="athena-CreateDataCatalog-request-Parameters"></a>
Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type.
+ For the `HIVE` data catalog type, use the following syntax. The `metadata-function` parameter is required. `The sdk-version` parameter is optional and defaults to the currently supported version.

   `metadata-function=lambda_arn, sdk-version=version_number `
+ For the `LAMBDA` data catalog type, use one of the following sets of required parameters, but not both.
  + If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.

     `metadata-function=lambda_arn, record-function=lambda_arn `
  +  If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.

     `function=lambda_arn `
+ The `GLUE` type takes a catalog ID parameter and is required. The ` catalog_id ` is the account ID of the AWS account to which the AWS Glue Data Catalog belongs.

   `catalog-id=catalog_id `
  + The `GLUE` data catalog type also applies to the default `AwsDataCatalog` that already exists in your account, of which you can have only one and cannot modify.
+ The `FEDERATED` data catalog type uses one of the following parameters, but not both. Use `connection-arn` for an existing AWS Glue connection. Use `connection-type` and `connection-properties` to specify the configuration setting for a new connection.
  +  `connection-arn:<glue_connection_arn_to_reuse> `
  +  `lambda-role-arn` (optional): The execution role to use for the Lambda function. If not provided, one is created.
  +  `connection-type:MYSQL|REDSHIFT|...., connection-properties:"<json_string>"`

    For * `<json_string>` *, use escaped JSON text, as in the following example.

     `"{\"spill_bucket\":\"my_spill\",\"spill_prefix\":\"athena-spill\",\"host\":\"abc12345.snowflakecomputing.com\",\"port\":\"1234\",\"warehouse\":\"DEV_WH\",\"database\":\"TEST\",\"schema\":\"PUBLIC\",\"SecretArn\":\"arn:aws:secretsmanager:ap-south-1:111122223333:secret:snowflake-XHb67j\"}"`
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 51200.
Required: No

 ** [Tags](#API_CreateDataCatalog_RequestSyntax) **   <a name="athena-CreateDataCatalog-request-Tags"></a>
A list of comma separated tags to add to the data catalog that is created. All the resources that are created by the `CreateDataCatalog` API operation with `FEDERATED` type will have the tag `federated_athena_datacatalog="true"`. This includes the CFN Stack, Glue Connection, Athena DataCatalog, and all the resources created as part of the CFN Stack (Lambda Function, IAM policies/roles).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [Type](#API_CreateDataCatalog_RequestSyntax) **   <a name="athena-CreateDataCatalog-request-Type"></a>
The type of data catalog to create: `LAMBDA` for a federated catalog, `GLUE` for an AWS Glue Data Catalog, and `HIVE` for an external Apache Hive metastore. `FEDERATED` is a federated catalog for which Athena creates the connection and the Lambda function for you based on the parameters that you pass.
For `FEDERATED` type, we do not support IAM identity center.
Type: String
Valid Values: `LAMBDA | GLUE | HIVE | FEDERATED`
Required: Yes

## Response Syntax
<a name="API_CreateDataCatalog_ResponseSyntax"></a>

```
{
   "DataCatalog": {
      "ConnectionType": "string",
      "Description": "string",
      "Error": "string",
      "Name": "string",
      "Parameters": {
         "string" : "string"
      },
      "Status": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_CreateDataCatalog_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataCatalog](#API_CreateDataCatalog_ResponseSyntax) **   <a name="athena-CreateDataCatalog-response-DataCatalog"></a>
Contains information about a data catalog in an AWS account.
In the Athena console, data catalogs are listed as "data sources" on the **Data sources** page under the **Data source name** column.
Type: [DataCatalog](API_DataCatalog.md) object

## Errors
<a name="API_CreateDataCatalog_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataCatalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateDataCatalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CreateDataCatalog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
