---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeMlflowTrackingServer.html
---

# DescribeMlflowTrackingServer
<a name="API_DescribeMlflowTrackingServer"></a>

Returns information about an MLflow Tracking Server.

## Request Syntax
<a name="API_DescribeMlflowTrackingServer_RequestSyntax"></a>

```
{
   "TrackingServerName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMlflowTrackingServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrackingServerName](#API_DescribeMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-request-TrackingServerName"></a>
The name of the MLflow Tracking Server to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: Yes

## Response Syntax
<a name="API_DescribeMlflowTrackingServer_ResponseSyntax"></a>

```
{
   "ArtifactStoreUri": "string",
   "AutomaticModelRegistration": boolean,
   "CreatedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "CreationTime": number,
   "IsActive": "string",
   "LastModifiedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "LastModifiedTime": number,
   "MlflowVersion": "string",
   "RoleArn": "string",
   "S3BucketOwnerAccountId": "string",
   "S3BucketOwnerVerification": boolean,
   "TrackingServerArn": "string",
   "TrackingServerMaintenanceStatus": "string",
   "TrackingServerName": "string",
   "TrackingServerSize": "string",
   "TrackingServerStatus": "string",
   "TrackingServerUrl": "string",
   "WeeklyMaintenanceWindowStart": "string"
}
```

## Response Elements
<a name="API_DescribeMlflowTrackingServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArtifactStoreUri](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-ArtifactStoreUri"></a>
The S3 URI of the general purpose bucket used as the MLflow Tracking Server artifact store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`

 ** [AutomaticModelRegistration](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-AutomaticModelRegistration"></a>
Whether automatic registration of new MLflow models to the SageMaker Model Registry is enabled.
Type: Boolean

 ** [CreatedBy](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-CreationTime"></a>
The timestamp of when the described MLflow Tracking Server was created.
Type: Timestamp

 ** [IsActive](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-IsActive"></a>
Whether the described MLflow Tracking Server is currently active.
Type: String
Valid Values: `Active | Inactive`

 ** [LastModifiedBy](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-LastModifiedTime"></a>
The timestamp of when the described MLflow Tracking Server was last modified.
Type: Timestamp

 ** [MlflowVersion](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-MlflowVersion"></a>
The MLflow version used for the described tracking server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `[0-9]*.[0-9]*.[0-9]*`

 ** [RoleArn](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-RoleArn"></a>
The Amazon Resource Name (ARN) for an IAM role in your account that the described MLflow Tracking Server uses to access the artifact store in Amazon S3.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [S3BucketOwnerAccountId](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-S3BucketOwnerAccountId"></a>
Expected AWS account ID that owns the Amazon S3 bucket for artifact storage.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`

 ** [S3BucketOwnerVerification](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-S3BucketOwnerVerification"></a>
Whether Amazon S3 Bucket Ownership checks are enabled whenever the tracking server interacts with Amazon Amazon S3.
Type: Boolean

 ** [TrackingServerArn](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-TrackingServerArn"></a>
The ARN of the described tracking server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-tracking-server/.*`

 ** [TrackingServerMaintenanceStatus](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-TrackingServerMaintenanceStatus"></a>
 The current maintenance status of the described MLflow Tracking Server.
Type: String
Valid Values: `MaintenanceInProgress | MaintenanceComplete | MaintenanceFailed`

 ** [TrackingServerName](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-TrackingServerName"></a>
The name of the described tracking server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`

 ** [TrackingServerSize](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-TrackingServerSize"></a>
The size of the described tracking server.
Type: String
Valid Values: `Small | Medium | Large`

 ** [TrackingServerStatus](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-TrackingServerStatus"></a>
The current creation status of the described MLflow Tracking Server.
Type: String
Valid Values: `Creating | Created | CreateFailed | Updating | Updated | UpdateFailed | Deleting | DeleteFailed | Stopping | Stopped | StopFailed | Starting | Started | StartFailed | MaintenanceInProgress | MaintenanceComplete | MaintenanceFailed`

 ** [TrackingServerUrl](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-TrackingServerUrl"></a>
The URL to connect to the MLflow user interface for the described tracking server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [WeeklyMaintenanceWindowStart](#API_DescribeMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowTrackingServer-response-WeeklyMaintenanceWindowStart"></a>
The day and time of the week when weekly maintenance occurs on the described tracking server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`

## Errors
<a name="API_DescribeMlflowTrackingServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeMlflowTrackingServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeMlflowTrackingServer)
