---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateBatchPrediction.html
---

# CreateBatchPrediction
<a name="API_CreateBatchPrediction"></a>

Generates predictions for a group of observations. The observations to process exist in one or more data files referenced by a `DataSource`. This operation creates a new `BatchPrediction`, and uses an `MLModel` and the data files referenced by the `DataSource` as information sources.

 `CreateBatchPrediction` is an asynchronous operation. In response to `CreateBatchPrediction`, Amazon Machine Learning (Amazon ML) immediately returns and sets the `BatchPrediction` status to `PENDING`. After the `BatchPrediction` completes, Amazon ML sets the status to `COMPLETED`.

You can poll for status updates by using the [GetBatchPrediction](API_GetBatchPrediction.md) operation and checking the `Status` parameter of the result. After the `COMPLETED` status appears, the results are available in the location specified by the `OutputUri` parameter.

## Request Syntax
<a name="API_CreateBatchPrediction_RequestSyntax"></a>

```
{
   "BatchPredictionDataSourceId": "{{string}}",
   "BatchPredictionId": "{{string}}",
   "BatchPredictionName": "{{string}}",
   "MLModelId": "{{string}}",
   "OutputUri": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateBatchPrediction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BatchPredictionDataSourceId](#API_CreateBatchPrediction_RequestSyntax) **   <a name="amazonml-CreateBatchPrediction-request-BatchPredictionDataSourceId"></a>
The ID of the `DataSource` that points to the group of observations to predict.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [BatchPredictionId](#API_CreateBatchPrediction_RequestSyntax) **   <a name="amazonml-CreateBatchPrediction-request-BatchPredictionId"></a>
A user-supplied ID that uniquely identifies the `BatchPrediction`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [BatchPredictionName](#API_CreateBatchPrediction_RequestSyntax) **   <a name="amazonml-CreateBatchPrediction-request-BatchPredictionName"></a>
A user-supplied name or description of the `BatchPrediction`. `BatchPredictionName` can only use the UTF-8 character set.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [MLModelId](#API_CreateBatchPrediction_RequestSyntax) **   <a name="amazonml-CreateBatchPrediction-request-MLModelId"></a>
The ID of the `MLModel` that will generate predictions for the group of observations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [OutputUri](#API_CreateBatchPrediction_RequestSyntax) **   <a name="amazonml-CreateBatchPrediction-request-OutputUri"></a>
The location of an Amazon Simple Storage Service (Amazon S3) bucket or directory to store the batch prediction results. The following substrings are not allowed in the `s3 key` portion of the `outputURI` field: ':', '//', '/./', '/../'.
Amazon ML needs permissions to store and retrieve the logs on your behalf. For information about how to set permissions, see the [Amazon Machine Learning Developer Guide](https://docs.aws.amazon.com/machine-learning/latest/dg).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: Yes

## Response Syntax
<a name="API_CreateBatchPrediction_ResponseSyntax"></a>

```
{
   "BatchPredictionId": "string"
}
```

## Response Elements
<a name="API_CreateBatchPrediction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BatchPredictionId](#API_CreateBatchPrediction_ResponseSyntax) **   <a name="amazonml-CreateBatchPrediction-response-BatchPredictionId"></a>
A user-supplied ID that uniquely identifies the `BatchPrediction`. This value is identical to the value of the `BatchPredictionId` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_CreateBatchPrediction_Errors"></a>

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
<a name="API_CreateBatchPrediction_Examples"></a>

### The following is a sample request and response of the BatchPrediction operation.
<a name="API_CreateBatchPrediction_Example_1"></a>

This example illustrates one usage of CreateBatchPrediction.

#### Sample Request
<a name="API_CreateBatchPrediction_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.CreateBatchPrediction
{
  "BatchPredictionId": "EXAMPLE-bp-2014-09-12-15-14-04-156",
  "BatchPredictionName": "EXAMPLE",
  "MLModelId": "EXAMPLE-pr-2014-09-12-15-14-04-924",
  "BatchPredictionDataSourceId": "EXAMPLE-tr-ds-2014-09-12-15-14-04-989",
  "OutputUri": "s3://eml-test-EXAMPLE/test-outputs/EXAMPLE-bp-2014-09-12-15-14-04-156/results"
}
```

#### Sample Response
<a name="API_CreateBatchPrediction_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"BatchPredictionId":"EXAMPLE-bp-2014-09-12-15-14-04-156"}
```

## See Also
<a name="API_CreateBatchPrediction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/CreateBatchPrediction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/CreateBatchPrediction)
