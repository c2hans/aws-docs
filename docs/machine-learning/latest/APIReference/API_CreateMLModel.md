---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateMLModel.html
---

# CreateMLModel
<a name="API_CreateMLModel"></a>

Creates a new `MLModel` using the `DataSource` and the recipe as information sources.

An `MLModel` is nearly immutable. Users can update only the `MLModelName` and the `ScoreThreshold` in an `MLModel` without creating a new `MLModel`.

 `CreateMLModel` is an asynchronous operation. In response to `CreateMLModel`, Amazon Machine Learning (Amazon ML) immediately returns and sets the `MLModel` status to `PENDING`. After the `MLModel` has been created and ready is for use, Amazon ML sets the status to `COMPLETED`.

You can use the `GetMLModel` operation to check the progress of the `MLModel` during the creation operation.

 `CreateMLModel` requires a `DataSource` with computed statistics, which can be created by setting `ComputeStatistics` to `true` in `CreateDataSourceFromRDS`, `CreateDataSourceFromS3`, or `CreateDataSourceFromRedshift` operations.

## Request Syntax
<a name="API_CreateMLModel_RequestSyntax"></a>

```
{
   "MLModelId": "{{string}}",
   "MLModelName": "{{string}}",
   "MLModelType": "{{string}}",
   "Parameters": {
      "{{string}}" : "{{string}}"
   },
   "Recipe": "{{string}}",
   "RecipeUri": "{{string}}",
   "TrainingDataSourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateMLModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MLModelId](#API_CreateMLModel_RequestSyntax) **   <a name="amazonml-CreateMLModel-request-MLModelId"></a>
A user-supplied ID that uniquely identifies the `MLModel`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [MLModelName](#API_CreateMLModel_RequestSyntax) **   <a name="amazonml-CreateMLModel-request-MLModelName"></a>
A user-supplied name or description of the `MLModel`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** [MLModelType](#API_CreateMLModel_RequestSyntax) **   <a name="amazonml-CreateMLModel-request-MLModelType"></a>
The category of supervised learning that this `MLModel` will address. Choose from the following types:
+ Choose `REGRESSION` if the `MLModel` will be used to predict a numeric value.
+ Choose `BINARY` if the `MLModel` result has two possible values.
+ Choose `MULTICLASS` if the `MLModel` result has a limited number of values.
 For more information, see the [Amazon Machine Learning Developer Guide](https://docs.aws.amazon.com/machine-learning/latest/dg).
Type: String
Valid Values: `REGRESSION | BINARY | MULTICLASS`
Required: Yes

 ** [Parameters](#API_CreateMLModel_RequestSyntax) **   <a name="amazonml-CreateMLModel-request-Parameters"></a>
A list of the training parameters in the `MLModel`. The list is implemented as a map of key-value pairs.
The following is the current set of training parameters:
+  `sgd.maxMLModelSizeInBytes` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.

   The value is an integer that ranges from `100000` to `2147483648`. The default value is `33554432`.
+  `sgd.maxPasses` - The number of times that the training process traverses the observations to build the `MLModel`. The value is an integer that ranges from `1` to `100`. The default value is `10`.
+  `sgd.shuffleType` - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are `auto` and `none`. The default value is `none`. We strongly recommend that you shuffle your data.
+  `sgd.l1RegularizationAmount` - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

  The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is to not use L1 normalization. This parameter can't be used when `L2` is specified. Use this parameter sparingly.
+  `sgd.l2RegularizationAmount` - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

  The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is to not use L2 normalization. This parameter can't be used when `L1` is specified. Use this parameter sparingly.
Type: String to string map
Required: No

 ** [Recipe](#API_CreateMLModel_RequestSyntax) **   <a name="amazonml-CreateMLModel-request-Recipe"></a>
The data recipe for creating the `MLModel`. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.
Type: String
Length Constraints: Maximum length of 131071.
Required: No

 ** [RecipeUri](#API_CreateMLModel_RequestSyntax) **   <a name="amazonml-CreateMLModel-request-RecipeUri"></a>
The Amazon Simple Storage Service (Amazon S3) location and file name that contains the `MLModel` recipe. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: No

 ** [TrainingDataSourceId](#API_CreateMLModel_RequestSyntax) **   <a name="amazonml-CreateMLModel-request-TrainingDataSourceId"></a>
The `DataSource` that points to the training data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_CreateMLModel_ResponseSyntax"></a>

```
{
   "MLModelId": "string"
}
```

## Response Elements
<a name="API_CreateMLModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MLModelId](#API_CreateMLModel_ResponseSyntax) **   <a name="amazonml-CreateMLModel-response-MLModelId"></a>
A user-supplied ID that uniquely identifies the `MLModel`. This value should be identical to the value of the `MLModelId` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_CreateMLModel_Errors"></a>

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
<a name="API_CreateMLModel_Examples"></a>

### The following is a sample request and response of the CreateMLModel operation.
<a name="API_CreateMLModel_Example_1"></a>

This example illustrates one usage of CreateMLModel.

#### Sample Request
<a name="API_CreateMLModel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.CreateMLModel
{
  "MLModelId": "exampleModelId",
  "MLModelName": "EXAMPLE",
  "MLModelType": "BINARY",
  "TrainingDataSourceId": "17SdAv6WC6r5vACAxF7U",
  "RecipeUri": "s3://eml-test-EXAMPLE/data.recipe.json"
}
```

#### Sample Response
<a name="API_CreateMLModel_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{"MLModelId":"exampleModelId"}
```

## See Also
<a name="API_CreateMLModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/CreateMLModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/CreateMLModel)
