---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRouter.html
---

# CreateInferenceRouter

Creates an inference router. An inference router is a Regional SageMaker AI resource that sends each inference request to one of the endpoints or inference components that you list for a routing target. These destinations can be in any AWS account, and in any AWS Region in the same partition as the router.

The router's status is `Creating` until it's ready to use. SageMaker AI checks that each endpoint is a real-time or asynchronous endpoint, as the routing target requires, and rejects one of the wrong type. It checks endpoints in other accounts with your credentials, so the endpoint policy must allow `sagemaker:DescribeEndpoint`. SageMaker AI accepts an endpoint that it can't check, for example one that doesn't exist. Requests to it fail if it's the wrong type or doesn't exist. To see the status of each destination, call [DescribeInferenceRouter](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceRouter.html) and see the `RoutingStatus` of each destination.

To invoke the router, use `InvokeInferenceRouter` or `InvokeInferenceRouterAsync`. For information about inference routers, see [Route requests across Regions with inference routers](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router.html).

## Request Syntax
<a name="API_CreateInferenceRouter_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
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
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateInferenceRouter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateInferenceRouter_RequestSyntax) **   <a name="sagemaker-CreateInferenceRouter-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you reuse a client token, use the same request parameters. Otherwise, the request fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [InferenceRouterName](#API_CreateInferenceRouter_RequestSyntax) **   <a name="sagemaker-CreateInferenceRouter-request-InferenceRouterName"></a>
The name of the inference router. The name must be unique within your account in the current AWS Region. The name is case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [RoutingTargets](#API_CreateInferenceRouter_RequestSyntax) **   <a name="sagemaker-CreateInferenceRouter-request-RoutingTargets"></a>
The routing targets of the inference router. Each routing target is a model that callers name when they invoke the router, and the destinations that serve it.
Type: Array of [RoutingTarget](API_RoutingTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** [Tags](#API_CreateInferenceRouter_RequestSyntax) **   <a name="sagemaker-CreateInferenceRouter-request-Tags"></a>
A list of key-value pairs to apply to the inference router. For information about tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateInferenceRouter_ResponseSyntax"></a>

```
{
   "InferenceRouterArn": "string"
}
```

## Response Elements
<a name="API_CreateInferenceRouter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceRouterArn](#API_CreateInferenceRouter_ResponseSyntax) **   <a name="sagemaker-CreateInferenceRouter-response-InferenceRouterArn"></a>
The Amazon Resource Name (ARN) of the inference router.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:sagemaker:[a-z0-9-]+:[0-9]{12}:inference-router/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateInferenceRouter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceAlreadyExists **
The resource that you are trying to create already exists. Use a different resource name, or delete the existing resource before retrying.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateInferenceRouter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateInferenceRouter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateInferenceRouter)
