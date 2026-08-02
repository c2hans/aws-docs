---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationVpcConfiguration.html
---

# DeleteApplicationVpcConfiguration
<a name="API_DeleteApplicationVpcConfiguration"></a>

Removes a VPC configuration from a Managed Service for Apache Flink application.

## Request Syntax
<a name="API_DeleteApplicationVpcConfiguration_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "ConditionalToken": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "VpcConfigurationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteApplicationVpcConfiguration_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DeleteApplicationVpcConfiguration_RequestSyntax) **   <a name="APIReference-DeleteApplicationVpcConfiguration-request-ApplicationName"></a>
The name of an existing application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ConditionalToken](#API_DeleteApplicationVpcConfiguration_RequestSyntax) **   <a name="APIReference-DeleteApplicationVpcConfiguration-request-ConditionalToken"></a>
A value you use to implement strong concurrency for application updates. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`. You get the application's current `ConditionalToken` using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9-_+/=]+`
Required: No

 ** [CurrentApplicationVersionId](#API_DeleteApplicationVpcConfiguration_RequestSyntax) **   <a name="APIReference-DeleteApplicationVpcConfiguration-request-CurrentApplicationVersionId"></a>
The current application version ID. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`. You can retrieve the application version ID using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

 ** [VpcConfigurationId](#API_DeleteApplicationVpcConfiguration_RequestSyntax) **   <a name="APIReference-DeleteApplicationVpcConfiguration-request-VpcConfigurationId"></a>
The ID of the VPC configuration to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteApplicationVpcConfiguration_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number,
   "OperationId": "string"
}
```

## Response Elements
<a name="API_DeleteApplicationVpcConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_DeleteApplicationVpcConfiguration_ResponseSyntax) **   <a name="APIReference-DeleteApplicationVpcConfiguration-response-ApplicationARN"></a>
The ARN of the Managed Service for Apache Flink application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_DeleteApplicationVpcConfiguration_ResponseSyntax) **   <a name="APIReference-DeleteApplicationVpcConfiguration-response-ApplicationVersionId"></a>
The updated version ID of the application.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

 ** [OperationId](#API_DeleteApplicationVpcConfiguration_ResponseSyntax) **   <a name="APIReference-DeleteApplicationVpcConfiguration-response-OperationId"></a>
The operation ID that can be used to track the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_DeleteApplicationVpcConfiguration_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidApplicationConfigurationException **
The user-provided application configuration is not valid.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceInUseException **
The application is not available for this operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteApplicationVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationVpcConfiguration)
