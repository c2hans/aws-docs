---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplication.html
---

# DeleteApplication
<a name="API_DeleteApplication"></a>

Deletes the specified application. Managed Service for Apache Flink halts application execution and deletes the application.

## Request Syntax
<a name="API_DeleteApplication_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CreateTimestamp": {{number}}
}
```

## Request Parameters
<a name="API_DeleteApplication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DeleteApplication_RequestSyntax) **   <a name="APIReference-DeleteApplication-request-ApplicationName"></a>
The name of the application to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CreateTimestamp](#API_DeleteApplication_RequestSyntax) **   <a name="APIReference-DeleteApplication-request-CreateTimestamp"></a>
Use the `DescribeApplication` operation to get this value.
Type: Timestamp
Required: Yes

## Response Elements
<a name="API_DeleteApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteApplication_Errors"></a>

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
<a name="API_DeleteApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DeleteApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DeleteApplication)
