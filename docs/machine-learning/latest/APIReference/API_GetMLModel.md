---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetMLModel.html
---

# GetMLModel
<a name="API_GetMLModel"></a>

Returns an `MLModel` that includes detailed metadata, data source information, and the current status of the `MLModel`.

 `GetMLModel` provides results in normal or verbose format.

## Request Syntax
<a name="API_GetMLModel_RequestSyntax"></a>

```
{
   "MLModelId": "{{string}}",
   "Verbose": {{boolean}}
}
```

## Request Parameters
<a name="API_GetMLModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MLModelId](#API_GetMLModel_RequestSyntax) **   <a name="amazonml-GetMLModel-request-MLModelId"></a>
The ID assigned to the `MLModel` at creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Verbose](#API_GetMLModel_RequestSyntax) **   <a name="amazonml-GetMLModel-request-Verbose"></a>
Specifies whether the `GetMLModel` operation should return `Recipe`.
If true, `Recipe` is returned.
If false, `Recipe` is not returned.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetMLModel_ResponseSyntax"></a>

```
{
   "ComputeTime": number,
   "CreatedAt": number,
   "CreatedByIamUser": "string",
   "EndpointInfo": {
      "CreatedAt": number,
      "EndpointStatus": "string",
      "EndpointUrl": "string",
      "PeakRequestsPerSecond": number
   },
   "FinishedAt": number,
   "InputDataLocationS3": "string",
   "LastUpdatedAt": number,
   "LogUri": "string",
   "Message": "string",
   "MLModelId": "string",
   "MLModelType": "string",
   "Name": "string",
   "Recipe": "string",
   "Schema": "string",
   "ScoreThreshold": number,
   "ScoreThresholdLastUpdatedAt": number,
   "SizeInBytes": number,
   "StartedAt": number,
   "Status": "string",
   "TrainingDataSourceId": "string",
   "TrainingParameters": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetMLModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComputeTime](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-ComputeTime"></a>
The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the `MLModel`, normalized and scaled on computation resources. `ComputeTime` is only available if the `MLModel` is in the `COMPLETED` state.
Type: Long

 ** [CreatedAt](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-CreatedAt"></a>
The time that the `MLModel` was created. The time is expressed in epoch time.
Type: Timestamp

 ** [CreatedByIamUser](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-CreatedByIamUser"></a>
The AWS user account from which the `MLModel` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
Type: String
Pattern: `arn:aws:iam::[0-9]+:((user/.+)|(root))`

 ** [EndpointInfo](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-EndpointInfo"></a>
The current endpoint of the `MLModel`
Type: [RealtimeEndpointInfo](API_RealtimeEndpointInfo.md) object

 ** [FinishedAt](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-FinishedAt"></a>
The epoch time when Amazon Machine Learning marked the `MLModel` as `COMPLETED` or `FAILED`. `FinishedAt` is only available when the `MLModel` is in the `COMPLETED` or `FAILED` state.
Type: Timestamp

 ** [InputDataLocationS3](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-InputDataLocationS3"></a>
The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`

 ** [LastUpdatedAt](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-LastUpdatedAt"></a>
The time of the most recent edit to the `MLModel`. The time is expressed in epoch time.
Type: Timestamp

 ** [LogUri](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-LogUri"></a>
A link to the file that contains logs of the `CreateMLModel` operation.
Type: String

 ** [Message](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-Message"></a>
A description of the most recent details about accessing the `MLModel`.
Type: String
Length Constraints: Maximum length of 10240.

 ** [MLModelId](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-MLModelId"></a>
The MLModel ID, which is same as the `MLModelId` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [MLModelType](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-MLModelType"></a>
Identifies the `MLModel` category. The following are the available types:
+ REGRESSION -- Produces a numeric result. For example, "What price should a house be listed at?"
+ BINARY -- Produces one of two possible results. For example, "Is this an e-commerce website?"
+ MULTICLASS -- Produces one of several possible results. For example, "Is this a HIGH, LOW or MEDIUM risk trade?"
Type: String
Valid Values: `REGRESSION | BINARY | MULTICLASS`

 ** [Name](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-Name"></a>
A user-supplied name or description of the `MLModel`.
Type: String
Length Constraints: Maximum length of 1024.

 ** [Recipe](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-Recipe"></a>
The recipe to use when training the `MLModel`. The `Recipe` provides detailed information about the observation data to use during training, and manipulations to perform on the observation data during training.
 **Note:** This parameter is provided as part of the verbose format.
Type: String
Length Constraints: Maximum length of 131071.

 ** [Schema](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-Schema"></a>
The schema used by all of the data files referenced by the `DataSource`.
 **Note:** This parameter is provided as part of the verbose format.
Type: String
Length Constraints: Maximum length of 131071.

 ** [ScoreThreshold](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-ScoreThreshold"></a>
The scoring threshold is used in binary classification `MLModel` models. It marks the boundary between a positive prediction and a negative prediction.
Output values greater than or equal to the threshold receive a positive result from the MLModel, such as `true`. Output values less than the threshold receive a negative response from the MLModel, such as `false`.
Type: Float

 ** [ScoreThresholdLastUpdatedAt](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-ScoreThresholdLastUpdatedAt"></a>
The time of the most recent edit to the `ScoreThreshold`. The time is expressed in epoch time.
Type: Timestamp

 ** [SizeInBytes](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-SizeInBytes"></a>
Long integer type that is a 64-bit signed number.
Type: Long

 ** [StartedAt](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-StartedAt"></a>
The epoch time when Amazon Machine Learning marked the `MLModel` as `INPROGRESS`. `StartedAt` isn't available if the `MLModel` is in the `PENDING` state.
Type: Timestamp

 ** [Status](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-Status"></a>
The current status of the `MLModel`. This element can have one of the following values:
+  `PENDING` - Amazon Machine Learning (Amazon ML) submitted a request to describe a `MLModel`.
+  `INPROGRESS` - The request is processing.
+  `FAILED` - The request did not run to completion. The ML model isn't usable.
+  `COMPLETED` - The request completed successfully.
+  `DELETED` - The `MLModel` is marked as deleted. It isn't usable.
Type: String
Valid Values: `PENDING | INPROGRESS | FAILED | COMPLETED | DELETED`

 ** [TrainingDataSourceId](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-TrainingDataSourceId"></a>
The ID of the training `DataSource`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [TrainingParameters](#API_GetMLModel_ResponseSyntax) **   <a name="amazonml-GetMLModel-response-TrainingParameters"></a>
A list of the training parameters in the `MLModel`. The list is implemented as a map of key-value pairs.
The following is the current set of training parameters:
+  `sgd.maxMLModelSizeInBytes` - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.

   The value is an integer that ranges from `100000` to `2147483648`. The default value is `33554432`.
+  `sgd.maxPasses` - The number of times that the training process traverses the observations to build the `MLModel`. The value is an integer that ranges from `1` to `100`. The default value is `10`.
+  `sgd.shuffleType` - Whether Amazon ML shuffles the training data. Shuffling data improves a model's ability to find the optimal solution for a variety of data types. The valid values are `auto` and `none`. The default value is `none`. We strongly recommend that you shuffle your data.
+  `sgd.l1RegularizationAmount` - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

  The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is to not use L1 normalization. This parameter can't be used when `L2` is specified. Use this parameter sparingly.
+  `sgd.l2RegularizationAmount` - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as `1.0E-08`.

  The value is a double that ranges from `0` to `MAX_DOUBLE`. The default is to not use L2 normalization. This parameter can't be used when `L1` is specified. Use this parameter sparingly.
Type: String to string map

## Errors
<a name="API_GetMLModel_Errors"></a>

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
<a name="API_GetMLModel_Examples"></a>

### The following is a sample request and response of the GetMLModel operation.
<a name="API_GetMLModel_Example_1"></a>

This example illustrates one usage of GetMLModel.

#### Sample Request
<a name="API_GetMLModel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: machinelearning.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonML_20141212.GetMLModel
{"MLModelId": "EXAMPLE-pr-2014-09-12-15-14-04-924", "Verbose": true}
```

#### Sample Response
<a name="API_GetMLModel_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "CreatedAt":1410560408.264,
  "CreatedByIamUser":"arn:aws:iam::<awsAccountId>:user/user",
  "HasCalibration":false,
  "LastUpdatedAt":1410560416.338,
  "LogUri": "https://s3bucket/locationToLogs/logname.tar.gz",
  "Name":"Name-ml-model",
  "Algorithm": "sgd",
  "MLModelId":"ml-model",
  "EndpointInfo": {
    "CreatedAt": 1424378682.266,
   "EndpointStatus": "READY",
   "EndpointUrl": "<realtime endpoint from Amazon Machine Learning for ml-model>",
   "PeakRequestsPerSecond": 200}
  "MLModelType":"BINARY",
  "Recipe":"{
    \"groups\": {},
    \n\"assignments\": {},
    \n\"dependencies\": {},
    \n\"outputs\": [\n    \"'x'\"\n]
  }\n",
  "Schema": "{
  \"version\":\"1.0\",
  \"rowId\":null,
  \"rowWeight\":null,
  \"targetAttributeName\":\"y\",
  \"dataFormat\":\"CSV\",
  \"dataFileContainsHeader\":false,
  \"attributes\":[{\"attributeName\":\"age\",
  \"attributeType\":\"NUMERIC\"},
  {\"attributeName\":\"job\",
  \"attributeType\":\"CATEGORICAL\"},
  {\"attributeName\":\"contact\",
  \"attributeType\":\"CATEGORICAL\"},
  {\"attributeName\":\"month\",
  \"attributeType\":\"CATEGORICAL\"},
  {\"attributeName\":\"day_of_week\",
  \"attributeType\":\"CATEGORICAL\"},
  {\"attributeName\":\"duration\",
  \"attributeType\":\"NUMERIC\"},
  {\"attributeName\":\"poutcome\",
  \"attributeType\":\"CATEGORICAL\"},
  {\"attributeName\":\"nr_employed\",
  \"attributeType\":\"NUMERIC\"},
  {\"attributeName\":\"y\",
  \"attributeType\":\"BINARY\"}],
  \"excludedAttributeNames\":[]}"
  "SizeInBytes": 400374,
  "Status":"COMPLETED",
  "ComputeTime":"185200",
  "FinishedAt":1410560416.338,
  "StartedAt":1410560409.264,
  "TrainingDataSourceId":"EXAMPLE-tr-ds-2014-09-12-15-14-04-989",
  "TrainingParameters":{
      "algorithm":"sgd",
      "sgd.l1":"0.0",
      "sgd.l2":"0.0",
      "sgd.likelihood":"logreg",
      "sgd.passes":"1"
  }
}
```

## See Also
<a name="API_GetMLModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/machinelearning-2014-12-12/GetMLModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/GetMLModel)
