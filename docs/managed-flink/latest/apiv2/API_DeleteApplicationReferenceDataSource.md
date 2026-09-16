---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationReferenceDataSource.html
---

# DeleteApplicationReferenceDataSource
<a name="API_DeleteApplicationReferenceDataSource"></a>

Deletes a reference data source configuration from the specified SQL-based Kinesis Data Analytics application's configuration.

If the application is running, Kinesis Data Analytics immediately removes the in-application table that you created using the [AddApplicationReferenceDataSource](API_AddApplicationReferenceDataSource.md) operation.

## Request Syntax
<a name="API_DeleteApplicationReferenceDataSource_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "ReferenceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteApplicationReferenceDataSource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DeleteApplicationReferenceDataSource_RequestSyntax) **   <a name="APIReference-DeleteApplicationReferenceDataSource-request-ApplicationName"></a>
The name of an existing application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CurrentApplicationVersionId](#API_DeleteApplicationReferenceDataSource_RequestSyntax) **   <a name="APIReference-DeleteApplicationReferenceDataSource-request-CurrentApplicationVersionId"></a>
The current application version. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** [ReferenceId](#API_DeleteApplicationReferenceDataSource_RequestSyntax) **   <a name="APIReference-DeleteApplicationReferenceDataSource-request-ReferenceId"></a>
The ID of the reference data source. When you add a reference data source to your application using the [AddApplicationReferenceDataSource](API_AddApplicationReferenceDataSource.md), Kinesis Data Analytics assigns an ID. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the reference ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteApplicationReferenceDataSource_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number
}
```

## Response Elements
<a name="API_DeleteApplicationReferenceDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_DeleteApplicationReferenceDataSource_ResponseSyntax) **   <a name="APIReference-DeleteApplicationReferenceDataSource-response-ApplicationARN"></a>
The application Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_DeleteApplicationReferenceDataSource_ResponseSyntax) **   <a name="APIReference-DeleteApplicationReferenceDataSource-response-ApplicationVersionId"></a>
The updated version ID of the application.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

## Errors
<a name="API_DeleteApplicationReferenceDataSource_Errors"></a>

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
<a name="API_DeleteApplicationReferenceDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationReferenceDataSource)
