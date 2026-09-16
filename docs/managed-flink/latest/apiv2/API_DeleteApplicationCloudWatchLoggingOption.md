---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html
---

# DeleteApplicationCloudWatchLoggingOption
<a name="API_DeleteApplicationCloudWatchLoggingOption"></a>

Deletes an Amazon CloudWatch log stream from an SQL-based Kinesis Data Analytics application.

## Request Syntax
<a name="API_DeleteApplicationCloudWatchLoggingOption_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CloudWatchLoggingOptionId": "{{string}}",
   "ConditionalToken": "{{string}}",
   "CurrentApplicationVersionId": {{number}}
}
```

## Request Parameters
<a name="API_DeleteApplicationCloudWatchLoggingOption_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DeleteApplicationCloudWatchLoggingOption_RequestSyntax) **   <a name="APIReference-DeleteApplicationCloudWatchLoggingOption-request-ApplicationName"></a>
The application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CloudWatchLoggingOptionId](#API_DeleteApplicationCloudWatchLoggingOption_RequestSyntax) **   <a name="APIReference-DeleteApplicationCloudWatchLoggingOption-request-CloudWatchLoggingOptionId"></a>
The `CloudWatchLoggingOptionId` of the Amazon CloudWatch logging option to delete. You can get the `CloudWatchLoggingOptionId` by using the [DescribeApplication](API_DescribeApplication.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [ConditionalToken](#API_DeleteApplicationCloudWatchLoggingOption_RequestSyntax) **   <a name="APIReference-DeleteApplicationCloudWatchLoggingOption-request-ConditionalToken"></a>
A value you use to implement strong concurrency for application updates. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`. You get the application's current `ConditionalToken` using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9-_+/=]+`
Required: No

 ** [CurrentApplicationVersionId](#API_DeleteApplicationCloudWatchLoggingOption_RequestSyntax) **   <a name="APIReference-DeleteApplicationCloudWatchLoggingOption-request-CurrentApplicationVersionId"></a>
The version ID of the application. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`. You can retrieve the application version ID using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

## Response Syntax
<a name="API_DeleteApplicationCloudWatchLoggingOption_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number,
   "CloudWatchLoggingOptionDescriptions": [
      {
         "CloudWatchLoggingOptionId": "string",
         "LogStreamARN": "string",
         "RoleARN": "string"
      }
   ],
   "OperationId": "string"
}
```

## Response Elements
<a name="API_DeleteApplicationCloudWatchLoggingOption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_DeleteApplicationCloudWatchLoggingOption_ResponseSyntax) **   <a name="APIReference-DeleteApplicationCloudWatchLoggingOption-response-ApplicationARN"></a>
The application's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_DeleteApplicationCloudWatchLoggingOption_ResponseSyntax) **   <a name="APIReference-DeleteApplicationCloudWatchLoggingOption-response-ApplicationVersionId"></a>
The version ID of the application. Kinesis Data Analytics updates the `ApplicationVersionId` each time you change the CloudWatch logging options.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

 ** [CloudWatchLoggingOptionDescriptions](#API_DeleteApplicationCloudWatchLoggingOption_ResponseSyntax) **   <a name="APIReference-DeleteApplicationCloudWatchLoggingOption-response-CloudWatchLoggingOptionDescriptions"></a>
The descriptions of the remaining CloudWatch logging options for the application.
Type: Array of [CloudWatchLoggingOptionDescription](API_CloudWatchLoggingOptionDescription.md) objects

 ** [OperationId](#API_DeleteApplicationCloudWatchLoggingOption_ResponseSyntax) **   <a name="APIReference-DeleteApplicationCloudWatchLoggingOption-response-OperationId"></a>
The operation ID that can be used to track the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_DeleteApplicationCloudWatchLoggingOption_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidApplicationConfigurationException **
The user-provided application configuration is not valid.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request JSON is not valid for the operation.
HTTP Status Code: 400

 ** ResourceInUseException **
The application is not available for this operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteApplicationCloudWatchLoggingOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationCloudWatchLoggingOption)
