---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateEvaluation.html
---

# CreateEvaluation
<a name="API_CreateEvaluation"></a>

Creates a new `Evaluation` of an `MLModel`. An `MLModel` is evaluated on a set of observations associated to a `DataSource`. Like a `DataSource` for an `MLModel`, the `DataSource` for an `Evaluation` contains values for the `Target Variable`. The `Evaluation` compares the predicted result for each observation to the actual outcome and provides a summary so that you know how effective the `MLModel` functions on the test data. Evaluation generates a relevant performance metric, such as BinaryAUC, RegressionRMSE or MulticlassAvgFScore based on the corresponding `MLModelType`: `BINARY`, `REGRESSION` or `MULTICLASS`.

 `CreateEvaluation` is an asynchronous operation. In response to `CreateEvaluation`, Amazon Machine Learning (Amazon ML) immediately returns and sets the evaluation status to `PENDING`. After the `Evaluation` is created and ready for use, Amazon ML sets the status to `COMPLETED`.

You can use the `GetEvaluation` operation to check progress of the evaluation during the creation operation.

## Request Syntax
<a name="API_CreateEvaluation_RequestSyntax"></a>

```
{
   "EvaluationDataSourceId": "{{string}}",
   "EvaluationId": "{{string}}",
   "EvaluationName": "{{string}}",
   "MLModelId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEvaluation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EvaluationDataSourceId](#API_CreateEvaluation_RequestSyntax) **   <a name="amazonml-CreateEvaluation-request-EvaluationDataSourceId"></a>
The ID of the `DataSource` for the evaluation. The schema of the `DataSource` must match the schema used to create the `MLModel`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [EvaluationId](#API_CreateEvaluation_RequestSyntax) **   <a name="amazonml-CreateEvaluation-request-EvaluationId"></a>
A user-supplied ID that uniquely identifies the `Evaluation`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [EvaluationName](#API_CreateEvaluation_RequestSyntax) **   <a name="amazonml-CreateEvaluation-request-EvaluationName"></a>
A user-supplied name or description of the `Evaluation`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [MLModelId](#API_CreateEvaluation_RequestSyntax) **   <a name="amazonml-CreateEvaluation-request-MLModelId"></a>
The ID of the `MLModel` to evaluate.
The schema used in creating the `MLModel` must match the schema of the `DataSource` used in the `Evaluation`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_CreateEvaluation_ResponseSyntax"></a>

```
{
   "EvaluationId": "string"
}
```

## Response Elements
<a name="API_CreateEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationId](#API_CreateEvaluation_ResponseSyntax) **   <a name="amazonml-CreateEvaluation-response-EvaluationId"></a>
The user-supplied ID that uniquely identifies the `Evaluation`. This value should be identical to the value of the `EvaluationId` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_CreateEvaluation_Errors"></a>

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
<a name="API_CreateEvaluation_Examples"></a>

### The following is a sample request and response of the CreateEvaluation operation:
<a name="API_CreateEvaluation_Example_1"></a>

This example illustrates one usage of CreateEvaluation.

#### Sample Request
<a name="API_CreateEvaluation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.CreateEvaluation
{
  "EvaluationId": "CreateEvaluation-pr-2014-09-12-15-14-04-924",
  "EvaluationName": "EXAMPLE",
  "MLModelId": "EXAMPLE-pr-2014-09-12-15-14-04-924",
  "EvaluationDataSourceId": "EXAMPLE-ev-ds-2014-09-12-15-14-04-411",
}
```

#### Sample Response
<a name="API_CreateEvaluation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"EvaluationId":"CreateEvaluation-pr-2014-09-12-15-14-04-924"}
```

## See Also
<a name="API_CreateEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/CreateEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/CreateEvaluation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
