---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteMlflowTrackingServer.html
---

# DeleteMlflowTrackingServer
<a name="API_DeleteMlflowTrackingServer"></a>

Deletes an MLflow Tracking Server. For more information, see [Clean up MLflow resources](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-cleanup.html.html).

## Request Syntax
<a name="API_DeleteMlflowTrackingServer_RequestSyntax"></a>

```
{
   "TrackingServerName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteMlflowTrackingServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrackingServerName](#API_DeleteMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-DeleteMlflowTrackingServer-request-TrackingServerName"></a>
The name of the the tracking server to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: Yes

## Response Syntax
<a name="API_DeleteMlflowTrackingServer_ResponseSyntax"></a>

```
{
   "TrackingServerArn": "string"
}
```

## Response Elements
<a name="API_DeleteMlflowTrackingServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrackingServerArn](#API_DeleteMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DeleteMlflowTrackingServer-response-TrackingServerArn"></a>
A `TrackingServerArn` object, the ARN of the tracking server that is deleted if successfully found.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-tracking-server/.*`

## Errors
<a name="API_DeleteMlflowTrackingServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteMlflowTrackingServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteMlflowTrackingServer)
