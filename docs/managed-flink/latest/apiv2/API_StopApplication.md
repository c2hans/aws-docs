---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StopApplication.html
---

# StopApplication
<a name="API_StopApplication"></a>

Stops the application from processing data. You can stop an application only if it is in the running status, unless you set the `Force` parameter to `true`.

You can use the [DescribeApplication](API_DescribeApplication.md) operation to find the application status.

Managed Service for Apache Flink takes a snapshot when the application is stopped, unless `Force` is set to `true`.

## Request Syntax
<a name="API_StopApplication_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "Force": {{boolean}}
}
```

## Request Parameters
<a name="API_StopApplication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_StopApplication_RequestSyntax) **   <a name="APIReference-StopApplication-request-ApplicationName"></a>
The name of the running application to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Force](#API_StopApplication_RequestSyntax) **   <a name="APIReference-StopApplication-request-Force"></a>
Set to `true` to force the application to stop. If you set `Force` to `true`, Managed Service for Apache Flink stops the application without taking a snapshot.
Force-stopping your application may lead to data loss or duplication. To prevent data loss or duplicate processing of data during application restarts, we recommend you to take frequent snapshots of your application.
You can only force stop a Managed Service for Apache Flink application. You can't force stop a SQL-based Kinesis Data Analytics application.
The application must be in the `STARTING`, `UPDATING`, `STOPPING`, `AUTOSCALING`, or `RUNNING` status.
Type: Boolean
Required: No

## Response Syntax
<a name="API_StopApplication_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_StopApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_StopApplication_ResponseSyntax) **   <a name="APIReference-StopApplication-response-OperationId"></a>
The operation ID that can be used to track the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_StopApplication_Errors"></a>

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
<a name="API_StopApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/StopApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/StopApplication)
