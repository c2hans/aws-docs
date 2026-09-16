---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationInputProcessingConfiguration.html
---

# AddApplicationInputProcessingConfiguration
<a name="API_AddApplicationInputProcessingConfiguration"></a>

Adds an [InputProcessingConfiguration](API_InputProcessingConfiguration.md) to a SQL-based Kinesis Data Analytics application. An input processor pre-processes records on the input stream before the application's SQL code executes. Currently, the only input processor available is [Amazon Lambda](https://docs.aws.amazon.com/lambda/).

## Request Syntax
<a name="API_AddApplicationInputProcessingConfiguration_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "InputId": "{{string}}",
   "InputProcessingConfiguration": {
      "InputLambdaProcessor": {
         "ResourceARN": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_AddApplicationInputProcessingConfiguration_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_AddApplicationInputProcessingConfiguration_RequestSyntax) **   <a name="APIReference-AddApplicationInputProcessingConfiguration-request-ApplicationName"></a>
The name of the application to which you want to add the input processing configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CurrentApplicationVersionId](#API_AddApplicationInputProcessingConfiguration_RequestSyntax) **   <a name="APIReference-AddApplicationInputProcessingConfiguration-request-CurrentApplicationVersionId"></a>
The version of the application to which you want to add the input processing configuration. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** [InputId](#API_AddApplicationInputProcessingConfiguration_RequestSyntax) **   <a name="APIReference-AddApplicationInputProcessingConfiguration-request-InputId"></a>
The ID of the input configuration to add the input processing configuration to. You can get a list of the input IDs for an application using the [DescribeApplication](API_DescribeApplication.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [InputProcessingConfiguration](#API_AddApplicationInputProcessingConfiguration_RequestSyntax) **   <a name="APIReference-AddApplicationInputProcessingConfiguration-request-InputProcessingConfiguration"></a>
The [InputProcessingConfiguration](API_InputProcessingConfiguration.md) to add to the application.
Type: [InputProcessingConfiguration](API_InputProcessingConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_AddApplicationInputProcessingConfiguration_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number,
   "InputId": "string",
   "InputProcessingConfigurationDescription": {
      "InputLambdaProcessorDescription": {
         "ResourceARN": "string",
         "RoleARN": "string"
      }
   }
}
```

## Response Elements
<a name="API_AddApplicationInputProcessingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_AddApplicationInputProcessingConfiguration_ResponseSyntax) **   <a name="APIReference-AddApplicationInputProcessingConfiguration-response-ApplicationARN"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_AddApplicationInputProcessingConfiguration_ResponseSyntax) **   <a name="APIReference-AddApplicationInputProcessingConfiguration-response-ApplicationVersionId"></a>
Provides the current application version.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

 ** [InputId](#API_AddApplicationInputProcessingConfiguration_ResponseSyntax) **   <a name="APIReference-AddApplicationInputProcessingConfiguration-response-InputId"></a>
The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [InputProcessingConfigurationDescription](#API_AddApplicationInputProcessingConfiguration_ResponseSyntax) **   <a name="APIReference-AddApplicationInputProcessingConfiguration-response-InputProcessingConfigurationDescription"></a>
The description of the preprocessor that executes on records in this input before the application's code is run.
Type: [InputProcessingConfigurationDescription](API_InputProcessingConfigurationDescription.md) object

## Errors
<a name="API_AddApplicationInputProcessingConfiguration_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
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
<a name="API_AddApplicationInputProcessingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/AddApplicationInputProcessingConfiguration)
