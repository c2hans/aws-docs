---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMlflowTrackingServer.html
---

# UpdateMlflowTrackingServer
<a name="API_UpdateMlflowTrackingServer"></a>

Updates properties of an existing MLflow Tracking Server.

## Request Syntax
<a name="API_UpdateMlflowTrackingServer_RequestSyntax"></a>

```
{
   "ArtifactStoreUri": "{{string}}",
   "AutomaticModelRegistration": {{boolean}},
   "S3BucketOwnerAccountId": "{{string}}",
   "S3BucketOwnerVerification": {{boolean}},
   "TrackingServerName": "{{string}}",
   "TrackingServerSize": "{{string}}",
   "WeeklyMaintenanceWindowStart": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMlflowTrackingServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArtifactStoreUri](#API_UpdateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-UpdateMlflowTrackingServer-request-ArtifactStoreUri"></a>
The new S3 URI for the general purpose bucket to use as the artifact store for the MLflow Tracking Server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** [AutomaticModelRegistration](#API_UpdateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-UpdateMlflowTrackingServer-request-AutomaticModelRegistration"></a>
Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to `True`. To disable automatic model registration, set this value to `False`. If not specified, `AutomaticModelRegistration` defaults to `False`
Type: Boolean
Required: No

 ** [S3BucketOwnerAccountId](#API_UpdateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-UpdateMlflowTrackingServer-request-S3BucketOwnerAccountId"></a>
The new expected AWS account ID that owns the Amazon S3 bucket for artifact storage.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** [S3BucketOwnerVerification](#API_UpdateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-UpdateMlflowTrackingServer-request-S3BucketOwnerVerification"></a>
Whether to enable or disable Amazon S3 Bucket Owenrship Verifaction whenever the MLflow Tracking Server interacts with Amazon Amazon S3.
Type: Boolean
Required: No

 ** [TrackingServerName](#API_UpdateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-UpdateMlflowTrackingServer-request-TrackingServerName"></a>
The name of the MLflow Tracking Server to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: Yes

 ** [TrackingServerSize](#API_UpdateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-UpdateMlflowTrackingServer-request-TrackingServerSize"></a>
The new size for the MLflow Tracking Server.
Type: String
Valid Values: `Small | Medium | Large`
Required: No

 ** [WeeklyMaintenanceWindowStart](#API_UpdateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-UpdateMlflowTrackingServer-request-WeeklyMaintenanceWindowStart"></a>
The new weekly maintenance window start day and time to update. The maintenance window day and time should be in Coordinated Universal Time (UTC) 24-hour standard time. For example: TUE:03:30.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`
Required: No

## Response Syntax
<a name="API_UpdateMlflowTrackingServer_ResponseSyntax"></a>

```
{
   "TrackingServerArn": "string"
}
```

## Response Elements
<a name="API_UpdateMlflowTrackingServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrackingServerArn](#API_UpdateMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-UpdateMlflowTrackingServer-response-TrackingServerArn"></a>
The ARN of the updated MLflow Tracking Server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-tracking-server/.*`

## Errors
<a name="API_UpdateMlflowTrackingServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMlflowTrackingServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateMlflowTrackingServer)
