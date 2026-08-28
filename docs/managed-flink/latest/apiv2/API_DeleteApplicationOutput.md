---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationOutput.html
---

# DeleteApplicationOutput
<a name="API_DeleteApplicationOutput"></a>

Deletes the output destination configuration from your SQL-based Kinesis Data Analytics application's configuration. Kinesis Data Analytics will no longer write data from the corresponding in-application stream to the external output destination.

## Request Syntax
<a name="API_DeleteApplicationOutput_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "OutputId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteApplicationOutput_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_DeleteApplicationOutput_RequestSyntax) **   <a name="APIReference-DeleteApplicationOutput-request-ApplicationName"></a>
The application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CurrentApplicationVersionId](#API_DeleteApplicationOutput_RequestSyntax) **   <a name="APIReference-DeleteApplicationOutput-request-CurrentApplicationVersionId"></a>
The application version. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** [OutputId](#API_DeleteApplicationOutput_RequestSyntax) **   <a name="APIReference-DeleteApplicationOutput-request-OutputId"></a>
The ID of the configuration to delete. Each output configuration that is added to the application (either when the application is created or later) using the [AddApplicationOutput](API_AddApplicationOutput.md) operation has a unique ID. You need to provide the ID to uniquely identify the output configuration that you want to delete from the application configuration. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the specific `OutputId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteApplicationOutput_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number
}
```

## Response Elements
<a name="API_DeleteApplicationOutput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_DeleteApplicationOutput_ResponseSyntax) **   <a name="APIReference-DeleteApplicationOutput-response-ApplicationARN"></a>
The application Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_DeleteApplicationOutput_ResponseSyntax) **   <a name="APIReference-DeleteApplicationOutput-response-ApplicationVersionId"></a>
The current application version ID.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

## Errors
<a name="API_DeleteApplicationOutput_Errors"></a>

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
<a name="API_DeleteApplicationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DeleteApplicationOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
