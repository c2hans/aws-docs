---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetBatchPrediction.html
---

# GetBatchPrediction
<a name="API_GetBatchPrediction"></a>

Returns a `BatchPrediction` that includes detailed metadata, status, and data file information for a `Batch Prediction` request.

## Request Syntax
<a name="API_GetBatchPrediction_RequestSyntax"></a>

```
{
   "BatchPredictionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetBatchPrediction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BatchPredictionId](#API_GetBatchPrediction_RequestSyntax) **   <a name="amazonml-GetBatchPrediction-request-BatchPredictionId"></a>
An ID assigned to the `BatchPrediction` at creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_GetBatchPrediction_ResponseSyntax"></a>

```
{
   "BatchPredictionDataSourceId": "string",
   "BatchPredictionId": "string",
   "ComputeTime": number,
   "CreatedAt": number,
   "CreatedByIamUser": "string",
   "FinishedAt": number,
   "InputDataLocationS3": "string",
   "InvalidRecordCount": number,
   "LastUpdatedAt": number,
   "LogUri": "string",
   "Message": "string",
   "MLModelId": "string",
   "Name": "string",
   "OutputUri": "string",
   "StartedAt": number,
   "Status": "string",
   "TotalRecordCount": number
}
```

## Response Elements
<a name="API_GetBatchPrediction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BatchPredictionDataSourceId](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-BatchPredictionDataSourceId"></a>
The ID of the `DataSource` that was used to create the `BatchPrediction`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [BatchPredictionId](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-BatchPredictionId"></a>
An ID assigned to the `BatchPrediction` at creation. This value should be identical to the value of the `BatchPredictionID` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [ComputeTime](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-ComputeTime"></a>
The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the `BatchPrediction`, normalized and scaled on computation resources. `ComputeTime` is only available if the `BatchPrediction` is in the `COMPLETED` state.
Type: Long

 ** [CreatedAt](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-CreatedAt"></a>
The time when the `BatchPrediction` was created. The time is expressed in epoch time.
Type: Timestamp

 ** [CreatedByIamUser](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-CreatedByIamUser"></a>
The AWS user account that invoked the `BatchPrediction`. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
Type: String
Pattern: `arn:aws:iam::[0-9]+:((user/.+)|(root))`

 ** [FinishedAt](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-FinishedAt"></a>
The epoch time when Amazon Machine Learning marked the `BatchPrediction` as `COMPLETED` or `FAILED`. `FinishedAt` is only available when the `BatchPrediction` is in the `COMPLETED` or `FAILED` state.
Type: Timestamp

 ** [InputDataLocationS3](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-InputDataLocationS3"></a>
The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`

 ** [InvalidRecordCount](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-InvalidRecordCount"></a>
The number of invalid records that Amazon Machine Learning saw while processing the `BatchPrediction`.
Type: Long

 ** [LastUpdatedAt](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-LastUpdatedAt"></a>
The time of the most recent edit to `BatchPrediction`. The time is expressed in epoch time.
Type: Timestamp

 ** [LogUri](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-LogUri"></a>
A link to the file that contains logs of the `CreateBatchPrediction` operation.
Type: String

 ** [Message](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-Message"></a>
A description of the most recent details about processing the batch prediction request.
Type: String
Length Constraints: Maximum length of 10240.

 ** [MLModelId](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-MLModelId"></a>
The ID of the `MLModel` that generated predictions for the `BatchPrediction` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [Name](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-Name"></a>
A user-supplied name or description of the `BatchPrediction`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`

 ** [OutputUri](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-OutputUri"></a>
The location of an Amazon S3 bucket or directory to receive the operation results.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`

 ** [StartedAt](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-StartedAt"></a>
The epoch time when Amazon Machine Learning marked the `BatchPrediction` as `INPROGRESS`. `StartedAt` isn't available if the `BatchPrediction` is in the `PENDING` state.
Type: Timestamp

 ** [Status](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-Status"></a>
The status of the `BatchPrediction`, which can be one of the following values:
+  `PENDING` - Amazon Machine Learning (Amazon ML) submitted a request to generate batch predictions.
+  `INPROGRESS` - The batch predictions are in progress.
+  `FAILED` - The request to perform a batch prediction did not run to completion. It is not usable.
+  `COMPLETED` - The batch prediction process completed successfully.
+  `DELETED` - The `BatchPrediction` is marked as deleted. It is not usable.
Type: String
Valid Values: `PENDING | INPROGRESS | FAILED | COMPLETED | DELETED`

 ** [TotalRecordCount](#API_GetBatchPrediction_ResponseSyntax) **   <a name="amazonml-GetBatchPrediction-response-TotalRecordCount"></a>
The number of total records that Amazon Machine Learning saw while processing the `BatchPrediction`.
Type: Long

## Errors
<a name="API_GetBatchPrediction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource cannot be located.
HTTP Status Code: 400

## Examples
<a name="API_GetBatchPrediction_Examples"></a>

### The following is a sample request and response of the GetBatchPrediction operation.
<a name="API_GetBatchPrediction_Example_1"></a>

This example illustrates one usage of GetBatchPrediction.

#### Sample Request
<a name="API_GetBatchPrediction_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.GetBatchPrediction
{"BatchPredictionId": "EXAMPLE-bp-2014-09-12-15-14-04-156"}
```

#### Sample Response
<a name="API_GetBatchPrediction_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "BatchPredictionDataSourceId":"EXAMPLE-tr-ds-2014-09-12-15-14-04-989",
  "BatchPredictionId":"EXAMPLE-bp-2014-09-12-15-14-04-156",
  "CreatedAt":1410560632.327,
  "CreatedByIamUser":"arn:aws:iam::<awsAccountId>:user/user",
  "InputDataLocationS3": "s3://eml-test-EXAMPLE/example.csv",
  "LastUpdatedAt":1410560632.327,
  "LogUri": "https://s3bucket/locationToLogs/logname.tar.gz",
  "Name":"EXAMPLE",
  "OutputUri":"s3://eml-test-EXAMPLE/test-outputs/EXAMPLE-bp-2014-09-12-15-14-04-156/results",
  "MLModelId":"EXAMPLE-pr-2014-09-12-15-14-04-924",
  "Status":"COMPLETED",
  "ComputeTime":"185200",
  "FinishedAt":1410560632.327,
  "StartedAt":1410560632.327,
  "TotalRecordCount":"21154",
  "InvalidRecordCount":"0"
}
```

## See Also
<a name="API_GetBatchPrediction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/GetBatchPrediction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/GetBatchPrediction)
