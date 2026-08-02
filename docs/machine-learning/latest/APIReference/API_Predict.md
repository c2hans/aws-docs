---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Predict.html
---

# Predict
<a name="API_Predict"></a>

Generates a prediction for the observation using the specified `ML Model`.

 **Note:** Not all response parameters will be populated. Whether a response parameter is populated depends on the type of model requested.

## Request Syntax
<a name="API_Predict_RequestSyntax"></a>

```
{
   "MLModelId": "{{string}}",
   "PredictEndpoint": "{{string}}",
   "Record": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_Predict_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MLModelId](#API_Predict_RequestSyntax) **   <a name="amazonml-Predict-request-MLModelId"></a>
A unique identifier of the `MLModel`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [PredictEndpoint](#API_Predict_RequestSyntax) **   <a name="amazonml-Predict-request-PredictEndpoint"></a>
The predicted endpoint for the input.
Type: String
Required: Yes

 ** [Record](#API_Predict_RequestSyntax) **   <a name="amazonml-Predict-request-Record"></a>
A map of variable name-value pairs that represent an observation.
Type: String to string map
Required: Yes

## Response Syntax
<a name="API_Predict_ResponseSyntax"></a>

```
{
   "Prediction": {
      "details": {
         "string" : "string"
      },
      "predictedLabel": "string",
      "predictedScores": {
         "string" : number
      },
      "predictedValue": number
   }
}
```

## Response Elements
<a name="API_Predict_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Prediction](#API_Predict_ResponseSyntax) **   <a name="amazonml-Predict-response-Prediction"></a>
The output from a `Predict` operation:
+  `Details` - Contains the following attributes: `DetailsAttributes.PREDICTIVE_MODEL_TYPE - REGRESSION | BINARY | MULTICLASS` `DetailsAttributes.ALGORITHM - SGD`
+  `PredictedLabel` - Present for either a `BINARY` or `MULTICLASS` `MLModel` request.
+  `PredictedScores` - Contains the raw classification score corresponding to each label.
+  `PredictedValue` - Present for a `REGRESSION` `MLModel` request.
Type: [Prediction](API_Prediction.md) object

## Errors
<a name="API_Predict_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An error on the server occurred when trying to process a request.
HTTP Status Code: 500

 ** InvalidInputException **
An error on the client occurred. Typically, the cause is an invalid input value.
HTTP Status Code: 400

 ** LimitExceededException **
The subscriber exceeded the maximum number of operations. This exception can occur when listing objects such as `DataSource`.
HTTP Status Code: 400

 ** PredictorNotMountedException **
The exception is thrown when a predict request is made to an unmounted `MLModel`.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A specified resource cannot be located.
HTTP Status Code: 400

## Examples
<a name="API_Predict_Examples"></a>

### The following is a sample request and response of the Predict operation.
<a name="API_Predict_Example_1"></a>

This example illustrates one usage of Predict.

#### Sample Request
<a name="API_Predict_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: <hostname from the GetMLModel response EndpointUrl object>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.Predict
{"MLModelId" : "exampleMLModelId",
 "Record" : {
   "ExampleData" : "exampleValue"
 },
 "PredictEndpoint" : "<realtime endpoint from Amazon Machine Learning for exampleMLModelId>"
}
```

#### Sample Response
<a name="API_Predict_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"PredictedLabel" : "0"
 "PredictedScores" : {
   "0" : "0.446588516"
 },
 "Details" : {
   "PredictiveModelType" : "BINARY",
   "Algorithm" : "SGD"
 }
}
```

## See Also
<a name="API_Predict_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/Predict)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/Predict)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/Predict)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/Predict)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/Predict)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/Predict)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/Predict)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/Predict)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/Predict)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/Predict)
