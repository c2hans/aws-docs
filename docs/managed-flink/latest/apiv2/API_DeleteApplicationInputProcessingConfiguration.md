---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationInputProcessingConfiguration.html
---

# DeleteApplicationInputProcessingConfiguration
<a name="API_DeleteApplicationInputProcessingConfiguration"></a>

Deletes an [InputProcessingConfiguration](API_InputProcessingConfiguration.md) from an input.

## Request Syntax
<a name="API_DeleteApplicationInputProcessingConfiguration_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "InputId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteApplicationInputProcessingConfiguration_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax) **   <a name="APIReference-DeleteApplicationInputProcessingConfiguration-request-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CurrentApplicationVersionId](#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax) **   <a name="APIReference-DeleteApplicationInputProcessingConfiguration-request-CurrentApplicationVersionId"></a>
The application version. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** [InputId](#API_DeleteApplicationInputProcessingConfiguration_RequestSyntax) **   <a name="APIReference-DeleteApplicationInputProcessingConfiguration-request-InputId"></a>
The ID of the input configuration from which to delete the input processing configuration. You can get a list of the input IDs for an application by using the [DescribeApplication](API_DescribeApplication.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteApplicationInputProcessingConfiguration_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number
}
```

## Response Elements
<a name="API_DeleteApplicationInputProcessingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_DeleteApplicationInputProcessingConfiguration_ResponseSyntax) **   <a name="APIReference-DeleteApplicationInputProcessingConfiguration-response-ApplicationARN"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_DeleteApplicationInputProcessingConfiguration_ResponseSyntax) **   <a name="APIReference-DeleteApplicationInputProcessingConfiguration-response-ApplicationVersionId"></a>
The current application version ID.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

## Errors
<a name="API_DeleteApplicationInputProcessingConfiguration_Errors"></a>

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
<a name="API_DeleteApplicationInputProcessingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationInputProcessingConfiguration)
