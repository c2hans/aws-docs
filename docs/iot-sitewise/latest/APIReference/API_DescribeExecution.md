---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeExecution.html
---

# DescribeExecution
<a name="API_DescribeExecution"></a>

Retrieves information about the execution.

## Request Syntax
<a name="API_DescribeExecution_RequestSyntax"></a>

```
GET /executions/{{executionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionId](#API_DescribeExecution_RequestSyntax) **   <a name="iotsitewise-DescribeExecution-request-uri-executionId"></a>
The ID of the execution.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionType": "string",
   "executionDetails": {
      "string" : "string"
   },
   "executionEndTime": number,
   "executionEntityVersion": "string",
   "executionId": "string",
   "executionResult": {
      "string" : "string"
   },
   "executionStartTime": number,
   "executionStatus": {
      "state": "string"
   },
   "resolveTo": {
      "assetId": "string"
   },
   "targetResource": {
      "assetId": "string",
      "computationModelId": "string"
   },
   "targetResourceVersion": "string"
}
```

## Response Elements
<a name="API_DescribeExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionType](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-actionType"></a>
The type of action exectued.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [executionDetails](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-executionDetails"></a>
Provides detailed information about the execution of your anomaly detection models. This includes model metrics and training timestamps for both training and inference actions.
+  The training action (AWS/ANOMALY\_DETECTION\_TRAINING), includes performance metrics that help you compare different versions of your anomaly detection models. These metrics provide insights into the model's performance during the training process.
+  The inference action (AWS/ANOMALY\_DETECTION\_INFERENCE), includes information about the results of executing your anomaly detection models. This helps you understand the output of your models and assess their performance.
Type: String to string map
Key Pattern: `^[a-zA-Z0-9 _\-#$*!@]+$`
Value Pattern: `^[a-zA-Z0-9 _\-#$*!@]+$`

 ** [executionEndTime](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-executionEndTime"></a>
The time the process ended.
Type: Timestamp

 ** [executionEntityVersion](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-executionEntityVersion"></a>
Entity version used for the execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [executionId](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-executionId"></a>
The ID of the execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [executionResult](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-executionResult"></a>
The result of the execution.
Type: String to string map
Key Pattern: `^[a-zA-Z0-9 _\-#$*!@]+$`
Value Pattern: `^[a-zA-Z0-9 _\-#$*!@]+$`

 ** [executionStartTime](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-executionStartTime"></a>
The time the process started.
Type: Timestamp

 ** [executionStatus](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-executionStatus"></a>
The status of the execution process.
Type: [ExecutionStatus](API_ExecutionStatus.md) object

 ** [resolveTo](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-resolveTo"></a>
The detailed resource this execution resolves to.
Type: [ResolveTo](API_ResolveTo.md) object

 ** [targetResource](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-targetResource"></a>
The resource the action will be taken on. This can include asset-based resources and computation model resources.
Type: [TargetResource](API_TargetResource.md) object

 ** [targetResourceVersion](#API_DescribeExecution_ResponseSyntax) **   <a name="iotsitewise-DescribeExecution-response-targetResourceVersion"></a>
The version of the target resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

## Errors
<a name="API_DescribeExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeExecution)
