---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMlflowApp.html
---

# UpdateMlflowApp
<a name="API_UpdateMlflowApp"></a>

Updates an MLflow App.

## Request Syntax
<a name="API_UpdateMlflowApp_RequestSyntax"></a>

```
{
   "AccountDefaultStatus": "{{string}}",
   "Arn": "{{string}}",
   "ArtifactStoreUri": "{{string}}",
   "DefaultDomainIdList": [ "{{string}}" ],
   "ModelRegistrationMode": "{{string}}",
   "Name": "{{string}}",
   "WeeklyMaintenanceWindowStart": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMlflowApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountDefaultStatus](#API_UpdateMlflowApp_RequestSyntax) **   <a name="sagemaker-UpdateMlflowApp-request-AccountDefaultStatus"></a>
Indicates whether this this MLflow App is the default for the account.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Arn](#API_UpdateMlflowApp_RequestSyntax) **   <a name="sagemaker-UpdateMlflowApp-request-Arn"></a>
The ARN of the MLflow App to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-app/.*`
Required: Yes

 ** [ArtifactStoreUri](#API_UpdateMlflowApp_RequestSyntax) **   <a name="sagemaker-UpdateMlflowApp-request-ArtifactStoreUri"></a>
The new S3 URI for the general purpose bucket to use as the artifact store for the MLflow App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** [DefaultDomainIdList](#API_UpdateMlflowApp_RequestSyntax) **   <a name="sagemaker-UpdateMlflowApp-request-DefaultDomainIdList"></a>
List of SageMaker Domain IDs for which this MLflow App is the default.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: No

 ** [ModelRegistrationMode](#API_UpdateMlflowApp_RequestSyntax) **   <a name="sagemaker-UpdateMlflowApp-request-ModelRegistrationMode"></a>
Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to `AutoModelRegistrationEnabled`. To disable automatic model registration, set this value to `AutoModelRegistrationDisabled`. If not specified, `AutomaticModelRegistration` defaults to `AutoModelRegistrationEnabled`
Type: String
Valid Values: `AutoModelRegistrationEnabled | AutoModelRegistrationDisabled`
Required: No

 ** [Name](#API_UpdateMlflowApp_RequestSyntax) **   <a name="sagemaker-UpdateMlflowApp-request-Name"></a>
The name of the MLflow App to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** [WeeklyMaintenanceWindowStart](#API_UpdateMlflowApp_RequestSyntax) **   <a name="sagemaker-UpdateMlflowApp-request-WeeklyMaintenanceWindowStart"></a>
The new weekly maintenance window start day and time to update. The maintenance window day and time should be in Coordinated Universal Time (UTC) 24-hour standard time. For example: TUE:03:30.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`
Required: No

## Response Syntax
<a name="API_UpdateMlflowApp_ResponseSyntax"></a>

```
{
   "Arn": "string"
}
```

## Response Elements
<a name="API_UpdateMlflowApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateMlflowApp_ResponseSyntax) **   <a name="sagemaker-UpdateMlflowApp-response-Arn"></a>
The ARN of the updated MLflow App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-app/.*`

## Errors
<a name="API_UpdateMlflowApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMlflowApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateMlflowApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateMlflowApp)
