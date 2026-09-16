---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html
---

# AddApplicationCloudWatchLoggingOption
<a name="API_AddApplicationCloudWatchLoggingOption"></a>

Adds an Amazon CloudWatch log stream to monitor application configuration errors.

## Request Syntax
<a name="API_AddApplicationCloudWatchLoggingOption_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CloudWatchLoggingOption": {
      "LogStreamARN": "{{string}}"
   },
   "ConditionalToken": "{{string}}",
   "CurrentApplicationVersionId": {{number}}
}
```

## Request Parameters
<a name="API_AddApplicationCloudWatchLoggingOption_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_AddApplicationCloudWatchLoggingOption_RequestSyntax) **   <a name="APIReference-AddApplicationCloudWatchLoggingOption-request-ApplicationName"></a>
The Kinesis Data Analytics application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CloudWatchLoggingOption](#API_AddApplicationCloudWatchLoggingOption_RequestSyntax) **   <a name="APIReference-AddApplicationCloudWatchLoggingOption-request-CloudWatchLoggingOption"></a>
Provides the Amazon CloudWatch log stream Amazon Resource Name (ARN).
Type: [CloudWatchLoggingOption](API_CloudWatchLoggingOption.md) object
Required: Yes

 ** [ConditionalToken](#API_AddApplicationCloudWatchLoggingOption_RequestSyntax) **   <a name="APIReference-AddApplicationCloudWatchLoggingOption-request-ConditionalToken"></a>
A value you use to implement strong concurrency for application updates. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`. You get the application's current `ConditionalToken` using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9-_+/=]+`
Required: No

 ** [CurrentApplicationVersionId](#API_AddApplicationCloudWatchLoggingOption_RequestSyntax) **   <a name="APIReference-AddApplicationCloudWatchLoggingOption-request-CurrentApplicationVersionId"></a>
The version ID of the SQL-based Kinesis Data Analytics application. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken`.You can retrieve the application version ID using [DescribeApplication](API_DescribeApplication.md). For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId`.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

## Response Syntax
<a name="API_AddApplicationCloudWatchLoggingOption_ResponseSyntax"></a>

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
<a name="API_AddApplicationCloudWatchLoggingOption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_AddApplicationCloudWatchLoggingOption_ResponseSyntax) **   <a name="APIReference-AddApplicationCloudWatchLoggingOption-response-ApplicationARN"></a>
The application's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_AddApplicationCloudWatchLoggingOption_ResponseSyntax) **   <a name="APIReference-AddApplicationCloudWatchLoggingOption-response-ApplicationVersionId"></a>
The new version ID of the SQL-based Kinesis Data Analytics application. Kinesis Data Analytics updates the `ApplicationVersionId` each time you change the CloudWatch logging options.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

 ** [CloudWatchLoggingOptionDescriptions](#API_AddApplicationCloudWatchLoggingOption_ResponseSyntax) **   <a name="APIReference-AddApplicationCloudWatchLoggingOption-response-CloudWatchLoggingOptionDescriptions"></a>
The descriptions of the current CloudWatch logging options for the SQL-based Kinesis Data Analytics application.
Type: Array of [CloudWatchLoggingOptionDescription](API_CloudWatchLoggingOptionDescription.md) objects

 ** [OperationId](#API_AddApplicationCloudWatchLoggingOption_ResponseSyntax) **   <a name="APIReference-AddApplicationCloudWatchLoggingOption-response-OperationId"></a>
The operation ID that can be used to track the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_AddApplicationCloudWatchLoggingOption_Errors"></a>

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
<a name="API_AddApplicationCloudWatchLoggingOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/AddApplicationCloudWatchLoggingOption)
