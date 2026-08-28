---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateEvaluation.html
---

# UpdateEvaluation
<a name="API_UpdateEvaluation"></a>

Updates the `EvaluationName` of an `Evaluation`.

You can use the `GetEvaluation` operation to view the contents of the updated data element.

## Request Syntax
<a name="API_UpdateEvaluation_RequestSyntax"></a>

```
{
   "EvaluationId": "{{string}}",
   "EvaluationName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEvaluation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EvaluationId](#API_UpdateEvaluation_RequestSyntax) **   <a name="amazonml-UpdateEvaluation-request-EvaluationId"></a>
The ID assigned to the `Evaluation` during creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [EvaluationName](#API_UpdateEvaluation_RequestSyntax) **   <a name="amazonml-UpdateEvaluation-request-EvaluationName"></a>
A new user-supplied name or description of the `Evaluation` that will replace the current content.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: Yes

## Response Syntax
<a name="API_UpdateEvaluation_ResponseSyntax"></a>

```
{
   "EvaluationId": "string"
}
```

## Response Elements
<a name="API_UpdateEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationId](#API_UpdateEvaluation_ResponseSyntax) **   <a name="amazonml-UpdateEvaluation-response-EvaluationId"></a>
The ID assigned to the `Evaluation` during creation. This value should be identical to the value of the `Evaluation` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_UpdateEvaluation_Errors"></a>

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
<a name="API_UpdateEvaluation_Examples"></a>

### The following is a sample request and response of the UpdateEvaluation operation.
<a name="API_UpdateEvaluation_Example_1"></a>

This example illustrates one usage of UpdateEvaluation.

#### Sample Request
<a name="API_UpdateEvaluation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.UpdateEvaluation
{
  "EvaluationId": "ev-exampleEvaluationId",
  "EvaluationName": "ev-exampleEvaluationName"
}
```

#### Sample Response
<a name="API_UpdateEvaluation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"EvaluationId": "ev-exampleEvaluationId"}
```

## See Also
<a name="API_UpdateEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/UpdateEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/UpdateEvaluation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
