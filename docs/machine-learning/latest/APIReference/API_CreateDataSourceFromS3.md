---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromS3.html
---

# CreateDataSourceFromS3
<a name="API_CreateDataSourceFromS3"></a>

Creates a `DataSource` object. A `DataSource` references data that can be used to perform `CreateMLModel`, `CreateEvaluation`, or `CreateBatchPrediction` operations.

 `CreateDataSourceFromS3` is an asynchronous operation. In response to `CreateDataSourceFromS3`, Amazon Machine Learning (Amazon ML) immediately returns and sets the `DataSource` status to `PENDING`. After the `DataSource` has been created and is ready for use, Amazon ML sets the `Status` parameter to `COMPLETED`. `DataSource` in the `COMPLETED` or `PENDING` state can be used to perform only `CreateMLModel`, `CreateEvaluation` or `CreateBatchPrediction` operations.

 If Amazon ML can't accept the input source, it sets the `Status` parameter to `FAILED` and includes an error message in the `Message` attribute of the `GetDataSource` operation response.

The observation data used in a `DataSource` should be ready to use; that is, it should have a consistent structure, and missing data values should be kept to a minimum. The observation data must reside in one or more .csv files in an Amazon Simple Storage Service (Amazon S3) location, along with a schema that describes the data items by name and type. The same schema must be used for all of the data files referenced by the `DataSource`.

After the `DataSource` has been created, it's ready to use in evaluations and batch predictions. If you plan to use the `DataSource` to train an `MLModel`, the `DataSource` also needs a recipe. A recipe describes how each input variable will be used in training an `MLModel`. Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.

## Request Syntax
<a name="API_CreateDataSourceFromS3_RequestSyntax"></a>

```
{
   "ComputeStatistics": {{boolean}},
   "DataSourceId": "{{string}}",
   "DataSourceName": "{{string}}",
   "DataSpec": {
      "DataLocationS3": "{{string}}",
      "DataRearrangement": "{{string}}",
      "DataSchema": "{{string}}",
      "DataSchemaLocationS3": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateDataSourceFromS3_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComputeStatistics](#API_CreateDataSourceFromS3_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromS3-request-ComputeStatistics"></a>
The compute statistics for a `DataSource`. The statistics are generated from the observation data referenced by a `DataSource`. Amazon ML uses the statistics internally during `MLModel` training. This parameter must be set to `true` if the ``DataSource`` needs to be used for `MLModel` training.
Type: Boolean
Required: No

 ** [DataSourceId](#API_CreateDataSourceFromS3_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromS3-request-DataSourceId"></a>
A user-supplied identifier that uniquely identifies the `DataSource`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [DataSourceName](#API_CreateDataSourceFromS3_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromS3-request-DataSourceName"></a>
A user-supplied name or description of the `DataSource`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [DataSpec](#API_CreateDataSourceFromS3_RequestSyntax) **   <a name="amazonml-CreateDataSourceFromS3-request-DataSpec"></a>
The data specification of a `DataSource`:
+ DataLocationS3 - The Amazon S3 location of the observation data.
+ DataSchemaLocationS3 - The Amazon S3 location of the `DataSchema`.
+ DataSchema - A JSON string representing the schema. This is not required if `DataSchemaUri` is specified.
+ DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the `Datasource`.

   Sample - ` "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"`
Type: [S3DataSpec](API_S3DataSpec.md) object
Required: Yes

## Response Syntax
<a name="API_CreateDataSourceFromS3_ResponseSyntax"></a>

```
{
   "DataSourceId": "string"
}
```

## Response Elements
<a name="API_CreateDataSourceFromS3_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSourceId](#API_CreateDataSourceFromS3_ResponseSyntax) **   <a name="amazonml-CreateDataSourceFromS3-response-DataSourceId"></a>
A user-supplied ID that uniquely identifies the `DataSource`. This value should be identical to the value of the `DataSourceID` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_CreateDataSourceFromS3_Errors"></a>

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
<a name="API_CreateDataSourceFromS3_Examples"></a>

### The following is a sample request and response of the CreateDataSourceFromS3 operation.
<a name="API_CreateDataSourceFromS3_Example_1"></a>

This example illustrates one usage of CreateDataSourceFromS3.

#### Sample Request
<a name="API_CreateDataSourceFromS3_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.CreateDataSourceFromS3
{
  "DataSourceId": "exampleDataSourceId",
  "DataSourceName": "exampleDataSourceName",
  "DataSpec":
  {
    "DataLocationS3": "s3://eml-test-EXAMPLE/data.csv",
    "DataSchemaLocationS3": "s3://eml-test-EXAMPLE/data.csv.schema",
    "DataRearrangement": "{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"
  }
}
```

#### Sample Response
<a name="API_CreateDataSourceFromS3_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"DataSourceId":"exampleDataSourceId"}
```

## See Also
<a name="API_CreateDataSourceFromS3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/CreateDataSourceFromS3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/CreateDataSourceFromS3)
