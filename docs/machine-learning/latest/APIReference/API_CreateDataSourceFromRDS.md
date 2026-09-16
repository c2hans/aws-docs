---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromRDS.html
---

# CreateDataSourceFromRDS
<a name="API_CreateDataSourceFromRDS"></a>

Creates a `DataSource` object from an [ Amazon Relational Database Service](http://aws.amazon.com/rds/) (Amazon RDS). A `DataSource` references data that can be used to perform `CreateMLModel`, `CreateEvaluation`, or `CreateBatchPrediction` operations.

 `CreateDataSourceFromRDS` is an asynchronous operation. In response to `CreateDataSourceFromRDS`, Amazon Machine Learning (Amazon ML) immediately returns and sets the `DataSource` status to `PENDING`. After the `DataSource` is created and ready for use, Amazon ML sets the `Status` parameter to `COMPLETED`. `DataSource` in the `COMPLETED` or `PENDING` state can be used only to perform `>CreateMLModel`>, `CreateEvaluation`, or `CreateBatchPrediction` operations.

 If Amazon ML cannot accept the input source, it sets the `Status` parameter to `FAILED` and includes an error message in the `Message` attribute of the `GetDataSource` operation response.

## Request Syntax
<a name="API_CreateDataSourceFromRDS_RequestSyntax"></a>

```
{
   "ComputeStatistics": {{boolean}},
   "DataSourceId": "{{string}}",
   "DataSourceName": "{{string}}",
   "RDSData": {
      "DatabaseCredentials": {
         "Password": "{{string}}",
         "Username": "{{string}}"
      },
      "DatabaseInformation": {
         "DatabaseName": "{{string}}",
         "InstanceIdentifier": "{{string}}"
      },
      "DataRearrangement": "{{string}}",
      "DataSchema": "{{string}}",
      "DataSchemaUri": "{{string}}",
      "ResourceRole": "{{string}}",
      "S3StagingLocation": "{{string}}",
      "SecurityGroupIds": [ "{{string}}" ],
      "SelectSqlQuery": "{{string}}",
      "ServiceRole": "{{string}}",
      "SubnetId": "{{string}}"
   },
   "RoleARN": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDataSourceFromRDS_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComputeStatistics](#API_CreateDataSourceFromRDS_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRDS-request-ComputeStatistics"></a>
The compute statistics for a `DataSource`. The statistics are generated from the observation data referenced by a `DataSource`. Amazon ML uses the statistics internally during `MLModel` training. This parameter must be set to `true` if the ``DataSource`` needs to be used for `MLModel` training.
Type: Boolean
Required: No

 ** [DataSourceId](#API_CreateDataSourceFromRDS_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRDS-request-DataSourceId"></a>
A user-supplied ID that uniquely identifies the `DataSource`. Typically, an Amazon Resource Number (ARN) becomes the ID for a `DataSource`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [DataSourceName](#API_CreateDataSourceFromRDS_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRDS-request-DataSourceName"></a>
A user-supplied name or description of the `DataSource`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [RDSData](#API_CreateDataSourceFromRDS_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRDS-request-RDSData"></a>
The data specification of an Amazon RDS `DataSource`:
+ DatabaseInformation -
  +  `DatabaseName` - The name of the Amazon RDS database.
  +  `InstanceIdentifier ` - A unique identifier for the Amazon RDS database instance.
+ DatabaseCredentials - AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon RDS database.
+ ResourceRole - A role (DataPipelineDefaultResourceRole) assumed by an EC2 instance to carry out the copy task from Amazon RDS to Amazon Simple Storage Service (Amazon S3). For more information, see [Role templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.
+ ServiceRole - A role (DataPipelineDefaultRole) assumed by the AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see [Role templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.
+ SecurityInfo - The security information to use to access an RDS DB instance. You need to set up appropriate ingress rules for the security entity IDs provided to allow access to the Amazon RDS instance. Specify a [`SubnetId`, `SecurityGroupIds`] pair for a VPC-based RDS DB instance.
+ SelectSqlQuery - A query that is used to retrieve the observation data for the `Datasource`.
+ S3StagingLocation - The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using `SelectSqlQuery` is stored in this location.
+ DataSchemaUri - The Amazon S3 location of the `DataSchema`.
+ DataSchema - A JSON string representing the schema. This is not required if `DataSchemaUri` is specified.
+ DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the `Datasource`.

   Sample - ` "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"`
Type: [RDSDataSpec](API_RDSDataSpec.md) object
Required: Yes

 ** [RoleARN](#API_CreateDataSourceFromRDS_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRDS-request-RoleARN"></a>
The role that Amazon ML assumes on behalf of the user to create and activate a data pipeline in the user's account and copy data using the `SelectSqlQuery` query from Amazon RDS to Amazon S3.

Type: String
Length Constraints: Minimum length of 1. Maximum length of 110.
Required: Yes

## Response Syntax
<a name="API_CreateDataSourceFromRDS_ResponseSyntax"></a>

```
{
   "DataSourceId": "string"
}
```

## Response Elements
<a name="API_CreateDataSourceFromRDS_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSourceId](#API_CreateDataSourceFromRDS_ResponseSyntax) **   <a name="amazonml-CreateDataSourceFromRDS-response-DataSourceId"></a>
A user-supplied ID that uniquely identifies the datasource. This value should be identical to the value of the `DataSourceID` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_CreateDataSourceFromRDS_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
A second request to use or change an object was not allowed. This can result from retrying a request using a parameter that was not present in the original request.
HTTP Status Code: 400

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

## Examples
<a name="API_CreateDataSourceFromRDS_Examples"></a>

### The following is a sample HTTP request and response of the CreateDataSourceFromRDS operation.
<a name="API_CreateDataSourceFromRDS_Example_1"></a>

This example illustrates one usage of CreateDataSourceFromRDS.

#### Sample Request
<a name="API_CreateDataSourceFromRDS_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.CreateDataSourceFromRDS
{
  "DataSourceId": "ml-rds-data-source-demo",
  "DataSourceName": "ml-rds-data-source-demo",
  "RDSData":
  {
    "DatabaseInformation":
    {
      "InstanceIdentifier": "demo",
      "DatabaseName": "demo"
    },
    "SelectSqlQuery": "select feature1, feature2, feature3, ...., featureN from RDS_DEMO_TABLE;",
    "DatabaseCredentials":
    {
      "Username": "demo_user",
      "Password": "demo_password"
    },
    "S3StagingLocation": "s3://mldemo/data/",
    "DataSchemaUri": "s3://mldemo/schema/mldemo.csv.schema",
    "ResourceRole": "DataPipelineDefaultResourceRole",
    "ServiceRole": "DataPipelineDefaultRole",
    "SubnetId": "subnet-XXXX",
    "SecurityGroupIds":
      ["sg-XXXXXX", "sg-XXXXXX"]
  },
  "RoleARN": "arn:aws:iam::<awsAccountId>:role/<roleToAssume>"
}
```

#### Sample Response
<a name="API_CreateDataSourceFromRDS_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "DataSourceId":"ml-rds-data-source-demo"
}
```

## See Also
<a name="API_CreateDataSourceFromRDS_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/CreateDataSourceFromRDS)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/CreateDataSourceFromRDS)
