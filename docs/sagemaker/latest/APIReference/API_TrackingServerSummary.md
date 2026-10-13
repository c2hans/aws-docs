---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrackingServerSummary.html
---

# TrackingServerSummary
<a name="API_TrackingServerSummary"></a>

The summary of the tracking server to list.

## Contents
<a name="API_TrackingServerSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-TrackingServerSummary-CreationTime"></a>
The creation time of a listed tracking server.
Type: Timestamp
Required: No

 ** IsActive **   <a name="sagemaker-Type-TrackingServerSummary-IsActive"></a>
The activity status of a listed tracking server.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-TrackingServerSummary-LastModifiedTime"></a>
The last modified time of a listed tracking server.
Type: Timestamp
Required: No

 ** MlflowVersion **   <a name="sagemaker-Type-TrackingServerSummary-MlflowVersion"></a>
The MLflow version used for a listed tracking server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `[0-9]*.[0-9]*.[0-9]*`
Required: No

 ** TrackingServerArn **   <a name="sagemaker-Type-TrackingServerSummary-TrackingServerArn"></a>
The ARN of a listed tracking server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-tracking-server/.*`
Required: No

 ** TrackingServerName **   <a name="sagemaker-Type-TrackingServerSummary-TrackingServerName"></a>
The name of a listed tracking server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** TrackingServerStatus **   <a name="sagemaker-Type-TrackingServerSummary-TrackingServerStatus"></a>
The creation status of a listed tracking server.
Type: String
Valid Values: `Creating | Created | CreateFailed | Updating | Updated | UpdateFailed | Deleting | DeleteFailed | Stopping | Stopped | StopFailed | Starting | Started | StartFailed | MaintenanceInProgress | MaintenanceComplete | MaintenanceFailed`
Required: No

## See Also
<a name="API_TrackingServerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrackingServerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrackingServerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrackingServerSummary)
