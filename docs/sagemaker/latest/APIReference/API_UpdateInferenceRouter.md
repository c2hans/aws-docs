---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateInferenceRouter.html
---

# UpdateInferenceRouter
<a name="API_UpdateInferenceRouter"></a>

Updates the routing targets of an inference router. The routing targets that you specify replace all of the router's existing routing targets. To change one routing target, call [DescribeInferenceRouter](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceRouter.html), edit the routing targets, and send all of them.

The update is applied in full or not at all, and each request uses either the previous configuration or the new one. Updates typically take effect within about 2 minutes.

If the router is being created, updated, or deleted, or another request changes it at the same time, you get a `ConflictException`. Describe the router, and then send your update again.

## Request Syntax
<a name="API_UpdateInferenceRouter_RequestSyntax"></a>

```
{
   "InferenceRouterName": "{{string}}",
   "RoutingTargets": [
      {
         "AsyncInferenceConfig": {
            "ClientConfig": {
               "MaxTimeInBacklogSeconds": {{number}}
            },
            "OutputConfig": {
               "KmsKeyId": "{{string}}",
               "NotificationConfig": {
                  "ErrorTopic": "{{string}}",
                  "SuccessTopic": "{{string}}"
               },
               "S3FailurePath": "{{string}}",
               "S3OutputPath": "{{string}}"
            }
         },
         "Destinations": [
            {
               "ResourceArn": "{{string}}",
               "RoutingStatus": "{{string}}"
            }
         ],
         "Name": "{{string}}",
         "RoutingPreference": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateInferenceRouter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InferenceRouterName](#API_UpdateInferenceRouter_RequestSyntax) **   <a name="sagemaker-UpdateInferenceRouter-request-InferenceRouterName"></a>
The name of the inference router to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [RoutingTargets](#API_UpdateInferenceRouter_RequestSyntax) **   <a name="sagemaker-UpdateInferenceRouter-request-RoutingTargets"></a>
The complete list of routing targets for the inference router. To remove the last routing target, delete the router.
Type: Array of [RoutingTarget](API_RoutingTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_UpdateInferenceRouter_ResponseSyntax"></a>

```
{
   "InferenceRouterArn": "string"
}
```

## Response Elements
<a name="API_UpdateInferenceRouter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceRouterArn](#API_UpdateInferenceRouter_ResponseSyntax) **   <a name="sagemaker-UpdateInferenceRouter-response-InferenceRouterArn"></a>
The Amazon Resource Name (ARN) of the inference router.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:sagemaker:[a-z0-9-]+:[0-9]{12}:inference-router/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_UpdateInferenceRouter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateInferenceRouter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateInferenceRouter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateInferenceRouter)
