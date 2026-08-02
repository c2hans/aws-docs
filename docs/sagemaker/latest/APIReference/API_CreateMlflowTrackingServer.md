---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateMlflowTrackingServer.html
---

# CreateMlflowTrackingServer
<a name="API_CreateMlflowTrackingServer"></a>

Creates an MLflow Tracking Server using a general purpose Amazon S3 bucket as the artifact store. For more information, see [Create an MLflow Tracking Server](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html).

## Request Syntax
<a name="API_CreateMlflowTrackingServer_RequestSyntax"></a>

```
{
   "ArtifactStoreUri": "{{string}}",
   "AutomaticModelRegistration": {{boolean}},
   "MlflowVersion": "{{string}}",
   "RoleArn": "{{string}}",
   "S3BucketOwnerAccountId": "{{string}}",
   "S3BucketOwnerVerification": {{boolean}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrackingServerName": "{{string}}",
   "TrackingServerSize": "{{string}}",
   "WeeklyMaintenanceWindowStart": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateMlflowTrackingServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArtifactStoreUri](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-ArtifactStoreUri"></a>
The S3 URI for a general purpose bucket to use as the MLflow Tracking Server artifact store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** [AutomaticModelRegistration](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-AutomaticModelRegistration"></a>
Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to `True`. To disable automatic model registration, set this value to `False`. If not specified, `AutomaticModelRegistration` defaults to `False`.
Type: Boolean
Required: No

 ** [MlflowVersion](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-MlflowVersion"></a>
The version of MLflow that the tracking server uses. To see which MLflow versions are available to use, see [How it works](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html#mlflow-create-tracking-server-how-it-works).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `[0-9]*.[0-9]*.[0-9]*`
Required: No

 ** [RoleArn](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-RoleArn"></a>
The Amazon Resource Name (ARN) for an IAM role in your account that the MLflow Tracking Server uses to access the artifact store in Amazon S3. The role should have `AmazonS3FullAccess` permissions. For more information on IAM permissions for tracking server creation, see [Set up IAM permissions for MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server-iam.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [S3BucketOwnerAccountId](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-S3BucketOwnerAccountId"></a>
Expected AWS account ID that owns the Amazon S3 bucket for artifact storage. Defaults to caller's account ID if not provided.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** [S3BucketOwnerVerification](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-S3BucketOwnerVerification"></a>
Enable Amazon S3 Ownership checks when interacting with Amazon S3 buckets from a SageMaker Managed MLflow Tracking Server. Defaults to `True` if not provided.
Type: Boolean
Required: No

 ** [Tags](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-Tags"></a>
Tags consisting of key-value pairs used to manage metadata for the tracking server.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TrackingServerName](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-TrackingServerName"></a>
A unique string identifying the tracking server name. This string is part of the tracking server ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: Yes

 ** [TrackingServerSize](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-TrackingServerSize"></a>
The size of the tracking server you want to create. You can choose between `"Small"`, `"Medium"`, and `"Large"`. The default MLflow Tracking Server configuration size is `"Small"`. You can choose a size depending on the projected use of the tracking server such as the volume of data logged, number of users, and frequency of use.
We recommend using a small tracking server for teams of up to 25 users, a medium tracking server for teams of up to 50 users, and a large tracking server for teams of up to 100 users.
Type: String
Valid Values: `Small | Medium | Large`
Required: No

 ** [WeeklyMaintenanceWindowStart](#API_CreateMlflowTrackingServer_RequestSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-request-WeeklyMaintenanceWindowStart"></a>
The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. For example: TUE:03:30.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`
Required: No

## Response Syntax
<a name="API_CreateMlflowTrackingServer_ResponseSyntax"></a>

```
{
   "TrackingServerArn": "string"
}
```

## Response Elements
<a name="API_CreateMlflowTrackingServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrackingServerArn](#API_CreateMlflowTrackingServer_ResponseSyntax) **   <a name="sagemaker-CreateMlflowTrackingServer-response-TrackingServerArn"></a>
The ARN of the tracking server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-tracking-server/.*`

## Errors
<a name="API_CreateMlflowTrackingServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateMlflowTrackingServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateMlflowTrackingServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateMlflowTrackingServer)
