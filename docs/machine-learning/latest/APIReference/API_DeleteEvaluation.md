---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteEvaluation.html
---

# DeleteEvaluation
<a name="API_DeleteEvaluation"></a>

Assigns the `DELETED` status to an `Evaluation`, rendering it unusable.

After invoking the `DeleteEvaluation` operation, you can use the `GetEvaluation` operation to verify that the status of the `Evaluation` changed to `DELETED`.

 **Caution:** The results of the `DeleteEvaluation` operation are irreversible.

## Request Syntax
<a name="API_DeleteEvaluation_RequestSyntax"></a>

```
{
   "EvaluationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEvaluation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EvaluationId](#API_DeleteEvaluation_RequestSyntax) **   <a name="amazonml-DeleteEvaluation-request-EvaluationId"></a>
A user-supplied ID that uniquely identifies the `Evaluation` to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteEvaluation_ResponseSyntax"></a>

```
{
   "EvaluationId": "string"
}
```

## Response Elements
<a name="API_DeleteEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationId](#API_DeleteEvaluation_ResponseSyntax) **   <a name="amazonml-DeleteEvaluation-response-EvaluationId"></a>
A user-supplied ID that uniquely identifies the `Evaluation`. This value should be identical to the value of the `EvaluationId` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_DeleteEvaluation_Errors"></a>

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
<a name="API_DeleteEvaluation_Examples"></a>

### The following is a sample request and response of the DeleteEvaluation operation.
<a name="API_DeleteEvaluation_Example_1"></a>

This example illustrates one usage of DeleteEvaluation.

#### Sample Request
<a name="API_DeleteEvaluation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.DeleteEvaluation
{"EvaluationId": "exampleEvaluationId"}
```

#### Sample Response
<a name="API_DeleteEvaluation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"EvaluationId":"exampleEvaluationId"}
```

## See Also
<a name="API_DeleteEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/DeleteEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/DeleteEvaluation)
