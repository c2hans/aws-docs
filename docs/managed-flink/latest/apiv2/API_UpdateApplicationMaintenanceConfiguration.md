---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplicationMaintenanceConfiguration.html
---

# UpdateApplicationMaintenanceConfiguration
<a name="API_UpdateApplicationMaintenanceConfiguration"></a>

Updates the maintenance configuration of the Managed Service for Apache Flink application.

You can invoke this operation on an application that is in one of the two following states: `READY` or `RUNNING`. If you invoke it when the application is in a state other than these two states, it throws a `ResourceInUseException`. The service makes use of the updated configuration the next time it schedules maintenance for the application. If you invoke this operation after the service schedules maintenance, the service will apply the configuration update the next time it schedules maintenance for the application. This means that you might not see the maintenance configuration update applied to the maintenance process that follows a successful invocation of this operation, but to the following maintenance process instead.

To see the current maintenance configuration of your application, invoke the [DescribeApplication](API_DescribeApplication.md) operation.

For information about application maintenance, see [Managed Service for Apache Flink for Apache Flink Maintenance](https://docs.aws.amazon.com/kinesisanalytics/latest/java/maintenance.html).

**Note**
This operation is supported only for Managed Service for Apache Flink.

## Request Syntax
<a name="API_UpdateApplicationMaintenanceConfiguration_RequestSyntax"></a>

```
{
   "ApplicationMaintenanceConfigurationUpdate": {
      "ApplicationMaintenanceWindowStartTimeUpdate": "{{string}}"
   },
   "ApplicationName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApplicationMaintenanceConfiguration_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationMaintenanceConfigurationUpdate](#API_UpdateApplicationMaintenanceConfiguration_RequestSyntax) **   <a name="APIReference-UpdateApplicationMaintenanceConfiguration-request-ApplicationMaintenanceConfigurationUpdate"></a>
Describes the application maintenance configuration update.
Type: [ApplicationMaintenanceConfigurationUpdate](API_ApplicationMaintenanceConfigurationUpdate.md) object
Required: Yes

 ** [ApplicationName](#API_UpdateApplicationMaintenanceConfiguration_RequestSyntax) **   <a name="APIReference-UpdateApplicationMaintenanceConfiguration-request-ApplicationName"></a>
The name of the application for which you want to update the maintenance configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateApplicationMaintenanceConfiguration_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationMaintenanceConfigurationDescription": {
      "ApplicationMaintenanceWindowEndTime": "string",
      "ApplicationMaintenanceWindowStartTime": "string"
   }
}
```

## Response Elements
<a name="API_UpdateApplicationMaintenanceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_UpdateApplicationMaintenanceConfiguration_ResponseSyntax) **   <a name="APIReference-UpdateApplicationMaintenanceConfiguration-response-ApplicationARN"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationMaintenanceConfigurationDescription](#API_UpdateApplicationMaintenanceConfiguration_ResponseSyntax) **   <a name="APIReference-UpdateApplicationMaintenanceConfiguration-response-ApplicationMaintenanceConfigurationDescription"></a>
The application maintenance configuration description after the update.
Type: [ApplicationMaintenanceConfigurationDescription](API_ApplicationMaintenanceConfigurationDescription.md) object

## Errors
<a name="API_UpdateApplicationMaintenanceConfiguration_Errors"></a>

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
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

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateApplicationMaintenanceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/UpdateApplicationMaintenanceConfiguration)
