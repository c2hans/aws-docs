---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromRedshift.html
---

# CreateDataSourceFromRedshift
<a name="API_CreateDataSourceFromRedshift"></a>

Creates a `DataSource` from a database hosted on an Amazon Redshift cluster. A `DataSource` references data that can be used to perform either `CreateMLModel`, `CreateEvaluation`, or `CreateBatchPrediction` operations.

 `CreateDataSourceFromRedshift` is an asynchronous operation. In response to `CreateDataSourceFromRedshift`, Amazon Machine Learning (Amazon ML) immediately returns and sets the `DataSource` status to `PENDING`. After the `DataSource` is created and ready for use, Amazon ML sets the `Status` parameter to `COMPLETED`. `DataSource` in `COMPLETED` or `PENDING` states can be used to perform only `CreateMLModel`, `CreateEvaluation`, or `CreateBatchPrediction` operations.

 If Amazon ML can't accept the input source, it sets the `Status` parameter to `FAILED` and includes an error message in the `Message` attribute of the `GetDataSource` operation response.

The observations should be contained in the database hosted on an Amazon Redshift cluster and should be specified by a `SelectSqlQuery` query. Amazon ML executes an `Unload` command in Amazon Redshift to transfer the result set of the `SelectSqlQuery` query to `S3StagingLocation`.

After the `DataSource` has been created, it's ready for use in evaluations and batch predictions. If you plan to use the `DataSource` to train an `MLModel`, the `DataSource` also requires a recipe. A recipe describes how each input variable will be used in training an `MLModel`. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.

You can't change an existing datasource, but you can copy and modify the settings from an existing Amazon Redshift datasource to create a new datasource. To do so, call `GetDataSource` for an existing datasource and copy the values to a `CreateDataSource` call. Change the settings that you want to change and make sure that all required fields have the appropriate values.

## Request Syntax
<a name="API_CreateDataSourceFromRedshift_RequestSyntax"></a>

```
{
   "ComputeStatistics": {{boolean}},
   "DataSourceId": "{{string}}",
   "DataSourceName": "{{string}}",
   "DataSpec": {
      "DatabaseCredentials": {
         "Password": "{{string}}",
         "Username": "{{string}}"
      },
      "DatabaseInformation": {
         "ClusterIdentifier": "{{string}}",
         "DatabaseName": "{{string}}"
      },
      "DataRearrangement": "{{string}}",
      "DataSchema": "{{string}}",
      "DataSchemaUri": "{{string}}",
      "S3StagingLocation": "{{string}}",
      "SelectSqlQuery": "{{string}}"
   },
   "RoleARN": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDataSourceFromRedshift_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComputeStatistics](#API_CreateDataSourceFromRedshift_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRedshift-request-ComputeStatistics"></a>
The compute statistics for a `DataSource`. The statistics are generated from the observation data referenced by a `DataSource`. Amazon ML uses the statistics internally during `MLModel` training. This parameter must be set to `true` if the `DataSource` needs to be used for `MLModel` training.
Type: Boolean
Required: No

 ** [DataSourceId](#API_CreateDataSourceFromRedshift_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRedshift-request-DataSourceId"></a>
A user-supplied ID that uniquely identifies the `DataSource`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [DataSourceName](#API_CreateDataSourceFromRedshift_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRedshift-request-DataSourceName"></a>
A user-supplied name or description of the `DataSource`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [DataSpec](#API_CreateDataSourceFromRedshift_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRedshift-request-DataSpec"></a>
The data specification of an Amazon Redshift `DataSource`:
+ DatabaseInformation -
  +  `DatabaseName` - The name of the Amazon Redshift database.
  +  ` ClusterIdentifier` - The unique ID for the Amazon Redshift cluster.
+ DatabaseCredentials - The AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon Redshift database.
+ SelectSqlQuery - The query that is used to retrieve the observation data for the `Datasource`.
+ S3StagingLocation - The Amazon Simple Storage Service (Amazon S3) location for staging Amazon Redshift data. The data retrieved from Amazon Redshift using the `SelectSqlQuery` query is stored in this location.
+ DataSchemaUri - The Amazon S3 location of the `DataSchema`.
+ DataSchema - A JSON string representing the schema. This is not required if `DataSchemaUri` is specified.
+ DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the `DataSource`.

   Sample - ` "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"`
Type: [RedshiftDataSpec](API_RedshiftDataSpec.md) object
Required: Yes

 ** [RoleARN](#API_CreateDataSourceFromRedshift_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromRedshift-request-RoleARN"></a>
A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the role on behalf of the user to create the following:
+ A security group to allow Amazon ML to execute the `SelectSqlQuery` query on an Amazon Redshift cluster
+ An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the `S3StagingLocation`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 110.
Required: Yes

## Response Syntax
<a name="API_CreateDataSourceFromRedshift_ResponseSyntax"></a>

```
{
   "DataSourceId": "string"
}
```

## Response Elements
<a name="API_CreateDataSourceFromRedshift_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSourceId](#API_CreateDataSourceFromRedshift_ResponseSyntax) **   <a name="amazonml-CreateDataSourceFromRedshift-response-DataSourceId"></a>
A user-supplied ID that uniquely identifies the datasource. This value should be identical to the value of the `DataSourceID` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_CreateDataSourceFromRedshift_Errors"></a>

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
<a name="API_CreateDataSourceFromRedshift_Examples"></a>

### The following is a sample request and response of the CreateDataSourceFromRedshift operation.
<a name="API_CreateDataSourceFromRedshift_Example_1"></a>

This example illustrates one usage of CreateDataSourceFromRedshift.

#### Sample Request
<a name="API_CreateDataSourceFromRedshift_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.CreateDataSourceFromRedshift
{
  "DataSourceId": "ds-exampleDatasourceId",
  "DataSourceName": "exampleDatasourceName",
  "DataSpec":
  {
    "DatabaseInformation":
    {
      "DatabaseName": "dev",
      "ClusterIdentifier": "test-cluster-1234"
    },
    "SelectSqlQuery": "select * from table",
    "DatabaseCredentials":
    {
      "Username": "foo",
      "Password": "foo"
    },
   "S3StagingLocation": "s3://bucketName/",
   "DataSchemaUri": "s3://bucketName/locationToUri/example.schema.json"},
   "RoleARN": "arn:aws:iam::<awsAccountId>:role/username"
  }
}
```

#### Sample Response
<a name="API_CreateDataSourceFromRedshift_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"DataSourceId": "ds-exampleDatasourceId"}
```

## See Also
<a name="API_CreateDataSourceFromRedshift_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/CreateDataSourceFromRedshift)
