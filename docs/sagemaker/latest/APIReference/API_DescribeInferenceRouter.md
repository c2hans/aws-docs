---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceRouter.html
---

# DescribeInferenceRouter
<a name="API_DescribeInferenceRouter"></a>

Returns information about an inference router, including the routing status of each destination.

SageMaker AI checks each destination with your permissions when you call this operation, so callers with different permissions can see a different `RoutingStatus`. To get the router's tags, use [ListTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTags.html).

## Request Syntax
<a name="API_DescribeInferenceRouter_RequestSyntax"></a>

```
{
   "InferenceRouterName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInferenceRouter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InferenceRouterName](#API_DescribeInferenceRouter_RequestSyntax) **   <a name="sagemaker-DescribeInferenceRouter-request-InferenceRouterName"></a>
The name of the inference router to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeInferenceRouter_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "InferenceRouterArn": "string",
   "InferenceRouterName": "string",
   "LastModifiedTime": number,
   "RoutingTargets": [
      {
         "AsyncInferenceConfig": {
            "ClientConfig": {
               "MaxTimeInBacklogSeconds": number
            },
            "OutputConfig": {
               "KmsKeyId": "string",
               "NotificationConfig": {
                  "ErrorTopic": "string",
                  "SuccessTopic": "string"
               },
               "S3FailurePath": "string",
               "S3OutputPath": "string"
            }
         },
         "Destinations": [
            {
               "ResourceArn": "string",
               "RoutingStatus": "string"
            }
         ],
         "Name": "string",
         "RoutingPreference": "string"
      }
   ],
   "Status": "string",
   "StatusReason": "string"
}
```

## Response Elements
<a name="API_DescribeInferenceRouter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRouter-response-CreationTime"></a>
The date and time that the inference router was created.
Type: Timestamp

 ** [InferenceRouterArn](#API_DescribeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRouter-response-InferenceRouterArn"></a>
The Amazon Resource Name (ARN) of the inference router.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:sagemaker:[a-z0-9-]+:[0-9]{12}:inference-router/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [InferenceRouterName](#API_DescribeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRouter-response-InferenceRouterName"></a>
The name of the inference router.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [LastModifiedTime](#API_DescribeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRouter-response-LastModifiedTime"></a>
The date and time that the inference router was last updated.
Type: Timestamp

 ** [RoutingTargets](#API_DescribeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRouter-response-RoutingTargets"></a>
The routing targets of the inference router. Each destination includes its `RoutingStatus`. You can send these routing targets back in an `UpdateInferenceRouter` request without changes.
Type: Array of [RoutingTarget](API_RoutingTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [Status](#API_DescribeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRouter-response-Status"></a>
The status of the inference router.
Type: String
Valid Values: `InService | Creating | Updating | Failed | Deleting`

 ** [StatusReason](#API_DescribeInferenceRouter_ResponseSyntax) **   <a name="sagemaker-DescribeInferenceRouter-response-StatusReason"></a>
If the status is `Failed`, the reason that the inference router failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_DescribeInferenceRouter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeInferenceRouter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeInferenceRouter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeInferenceRouter)
