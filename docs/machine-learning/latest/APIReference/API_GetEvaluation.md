---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetEvaluation.html
---

# GetEvaluation
<a name="API_GetEvaluation"></a>

Returns an `Evaluation` that includes metadata as well as the current status of the `Evaluation`.

## Request Syntax
<a name="API_GetEvaluation_RequestSyntax"></a>

```
{
   "EvaluationId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEvaluation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EvaluationId](#API_GetEvaluation_RequestSyntax) **   <a name="amazonml-GetEvaluation-request-EvaluationId"></a>
The ID of the `Evaluation` to retrieve. The evaluation of each `MLModel` is recorded and cataloged. The ID provides the means to access the information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_GetEvaluation_ResponseSyntax"></a>

```
{
   "ComputeTime": number,
   "CreatedAt": number,
   "CreatedByIamUser": "string",
   "EvaluationDataSourceId": "string",
   "EvaluationId": "string",
   "FinishedAt": number,
   "InputDataLocationS3": "string",
   "LastUpdatedAt": number,
   "LogUri": "string",
   "Message": "string",
   "MLModelId": "string",
   "Name": "string",
   "PerformanceMetrics": {
      "Properties": {
         "string" : "string"
      }
   },
   "StartedAt": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_GetEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComputeTime](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-ComputeTime"></a>
The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the `Evaluation`, normalized and scaled on computation resources. `ComputeTime` is only available if the `Evaluation` is in the `COMPLETED` state.
Type: Long

 ** [CreatedAt](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-CreatedAt"></a>
The time that the `Evaluation` was created. The time is expressed in epoch time.
Type: Timestamp

 ** [CreatedByIamUser](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-CreatedByIamUser"></a>
The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
Type: String
Pattern: `arn:aws:iam::[0-9]+:((user/.+)|(root))`

 ** [EvaluationDataSourceId](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-EvaluationDataSourceId"></a>
The `DataSource` used for this evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [EvaluationId](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-EvaluationId"></a>
The evaluation ID which is same as the `EvaluationId` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [FinishedAt](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-FinishedAt"></a>
The epoch time when Amazon Machine Learning marked the `Evaluation` as `COMPLETED` or `FAILED`. `FinishedAt` is only available when the `Evaluation` is in the `COMPLETED` or `FAILED` state.
Type: Timestamp

 ** [InputDataLocationS3](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-InputDataLocationS3"></a>
The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`

 ** [LastUpdatedAt](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-LastUpdatedAt"></a>
The time of the most recent edit to the `Evaluation`. The time is expressed in epoch time.
Type: Timestamp

 ** [LogUri](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-LogUri"></a>
A link to the file that contains logs of the `CreateEvaluation` operation.
Type: String

 ** [Message](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-Message"></a>
A description of the most recent details about evaluating the `MLModel`.
Type: String
Length Constraints: Maximum length of 10240.

 ** [MLModelId](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-MLModelId"></a>
The ID of the `MLModel` that was the focus of the evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [Name](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-Name"></a>
A user-supplied name or description of the `Evaluation`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`

 ** [PerformanceMetrics](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-PerformanceMetrics"></a>
Measurements of how well the `MLModel` performed using observations referenced by the `DataSource`. One of the following metric is returned based on the type of the `MLModel`:
+ BinaryAUC: A binary `MLModel` uses the Area Under the Curve (AUC) technique to measure performance.
+ RegressionRMSE: A regression `MLModel` uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.
+ MulticlassAvgFScore: A multiclass `MLModel` uses the F1 score technique to measure performance.
 For more information about performance metrics, please see the [Amazon Machine Learning Developer Guide](https://docs.aws.amazon.com/machine-learning/latest/dg).
Type: [PerformanceMetrics](API_PerformanceMetrics.md) object

 ** [StartedAt](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-StartedAt"></a>
The epoch time when Amazon Machine Learning marked the `Evaluation` as `INPROGRESS`. `StartedAt` isn't available if the `Evaluation` is in the `PENDING` state.
Type: Timestamp

 ** [Status](#API_GetEvaluation_ResponseSyntax) **   <a name="amazonml-GetEvaluation-response-Status"></a>
The status of the evaluation. This element can have one of the following values:
+  `PENDING` - Amazon Machine Language (Amazon ML) submitted a request to evaluate an `MLModel`.
+  `INPROGRESS` - The evaluation is underway.
+  `FAILED` - The request to evaluate an `MLModel` did not run to completion. It is not usable.
+  `COMPLETED` - The evaluation process completed successfully.
+  `DELETED` - The `Evaluation` is marked as deleted. It is not usable.
Type: String
Valid Values: `PENDING | INPROGRESS | FAILED | COMPLETED | DELETED`

## Errors
<a name="API_GetEvaluation_Errors"></a>

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
<a name="API_GetEvaluation_Examples"></a>

### The following is a sample request and response of the GetEvaluation operation.
<a name="API_GetEvaluation_Example_1"></a>

This example illustrates one usage of GetEvaluation.

#### Sample Request
<a name="API_GetEvaluation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.GetEvaluation
{"EvaluationId": "ev-2014-09-12-15-14-04-924"}
```

#### Sample Response
<a name="API_GetEvaluation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "CreatedAt":1410560805.669,
  "CreatedByIamUser":"arn:aws:iam::<awsAccountId>:user/user",
  "EvaluationDataSourceId":"EXAMPLE-ev-ds-2014-09-12-15-14-04-411",
  "EvaluationId":"ev-2014-09-12-15-14-04-924",
  "InputDataLocationS3": "s3://eml-test-EXAMPLE/example.csv",
  "LastUpdatedAt":1410560805.669,
  "LogUri": "https://s3bucket/locationToLogs/logname.tar.gz",
  "Name":"EXAMPLE",
  "PerformanceMetrics":{"Properties":{}},
  "MLModelId":"EXAMPLE-pr-2014-09-12-15-14-04-924",
  "Status":"COMPLETED",
  "ComputeTime":"185200",
  "FinishedAt":1410560805.669,
  "StartedAt":1410560805.669
}
```

## See Also
<a name="API_GetEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/GetEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/GetEvaluation)
