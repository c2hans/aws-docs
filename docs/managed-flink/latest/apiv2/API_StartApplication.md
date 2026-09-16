---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StartApplication.html
---

# StartApplication
<a name="API_StartApplication"></a>

Starts the specified Managed Service for Apache Flink application. After creating an application, you must exclusively call this operation to start your application.

## Request Syntax
<a name="API_StartApplication_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "RunConfiguration": {
      "ApplicationRestoreConfiguration": {
         "ApplicationRestoreType": "{{string}}",
         "SnapshotName": "{{string}}"
      },
      "FlinkRunConfiguration": {
         "AllowNonRestoredState": {{boolean}}
      },
      "SqlRunConfigurations": [
         {
            "InputId": "{{string}}",
            "InputStartingPositionConfiguration": {
               "InputStartingPosition": "{{string}}"
            }
         }
      ]
   }
}
```

## Request Parameters
<a name="API_StartApplication_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_StartApplication_RequestSyntax) **   <a name="APIReference-StartApplication-request-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [RunConfiguration](#API_StartApplication_RequestSyntax) **   <a name="APIReference-StartApplication-request-RunConfiguration"></a>
Identifies the run configuration (start parameters) of a Managed Service for Apache Flink application.
Type: [RunConfiguration](API_RunConfiguration.md) object
Required: No

## Response Syntax
<a name="API_StartApplication_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_StartApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_StartApplication_ResponseSyntax) **   <a name="APIReference-StartApplication-response-OperationId"></a>
The operation ID that can be used to track the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_StartApplication_Errors"></a>

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
<a name="API_StartApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/StartApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/StartApplication)
