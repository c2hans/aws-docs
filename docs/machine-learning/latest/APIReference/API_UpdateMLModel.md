---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateMLModel.html
---

# UpdateMLModel
<a name="API_UpdateMLModel"></a>

Updates the `MLModelName` and the `ScoreThreshold` of an `MLModel`.

You can use the `GetMLModel` operation to view the contents of the updated data element.

## Request Syntax
<a name="API_UpdateMLModel_RequestSyntax"></a>

```
{
   "MLModelId": "{{string}}",
   "MLModelName": "{{string}}",
   "ScoreThreshold": {{number}}
}
```

## Request Parameters
<a name="API_UpdateMLModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MLModelId](#API_UpdateMLModel_RequestSyntax) **   <a name="amazonml-UpdateMLModel-request-MLModelId"></a>
The ID assigned to the `MLModel` during creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [MLModelName](#API_UpdateMLModel_RequestSyntax) **   <a name="amazonml-UpdateMLModel-request-MLModelName"></a>
A user-supplied name or description of the `MLModel`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [ScoreThreshold](#API_UpdateMLModel_RequestSyntax) **   <a name="amazonml-UpdateMLModel-request-ScoreThreshold"></a>
The `ScoreThreshold` used in binary classification `MLModel` that marks the boundary between a positive prediction and a negative prediction.
Output values greater than or equal to the `ScoreThreshold` receive a positive result from the `MLModel`, such as `true`. Output values less than the `ScoreThreshold` receive a negative response from the `MLModel`, such as `false`.
Type: Float
Required: No

## Response Syntax
<a name="API_UpdateMLModel_ResponseSyntax"></a>

```
{
   "MLModelId": "string"
}
```

## Response Elements
<a name="API_UpdateMLModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MLModelId](#API_UpdateMLModel_ResponseSyntax) **   <a name="amazonml-UpdateMLModel-response-MLModelId"></a>
The ID assigned to the `MLModel` during creation. This value should be identical to the value of the `MLModelID` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_UpdateMLModel_Errors"></a>

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
<a name="API_UpdateMLModel_Examples"></a>

### The following is a sample request and response of the UpdateMLModel operation.
<a name="API_UpdateMLModel_Example_1"></a>

This example illustrates one usage of UpdateMLModel.

#### Sample Request
<a name="API_UpdateMLModel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.UpdateMLModel
{
  "MLModelId": "ml-exampleModelId",
  "MLModelName": "ml-exampleModelName",
  "ScoreThreshold": 0.8
}
```

#### Sample Response
<a name="API_UpdateMLModel_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"MLModelId": "pr-exampleModelId"}
```

## See Also
<a name="API_UpdateMLModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/UpdateMLModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/UpdateMLModel)
