---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateMlflowApp.html
---

# CreateMlflowApp
<a name="API_CreateMlflowApp"></a>

Creates an MLflow Tracking Server using a general purpose Amazon S3 bucket as the artifact store.

## Request Syntax
<a name="API_CreateMlflowApp_RequestSyntax"></a>

```
{
   "AccountDefaultStatus": "{{string}}",
   "ArtifactStoreUri": "{{string}}",
   "DefaultDomainIdList": [ "{{string}}" ],
   "KmsKeyId": "{{string}}",
   "ModelRegistrationMode": "{{string}}",
   "Name": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "WeeklyMaintenanceWindowStart": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateMlflowApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountDefaultStatus](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-AccountDefaultStatus"></a>
Indicates whether this MLflow app is the default for the entire account.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [ArtifactStoreUri](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-ArtifactStoreUri"></a>
The S3 URI for a general purpose bucket to use as the MLflow App artifact store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** [DefaultDomainIdList](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-DefaultDomainIdList"></a>
List of SageMaker domain IDs for which this MLflow App is used as the default.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: No

 ** [KmsKeyId](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-KmsKeyId"></a>
The ID of the AWS KMS key used to encrypt the data at rest associated with the MLflow App. If you don't specify a value, the MLflow App is not encrypted with a customer-managed key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** [ModelRegistrationMode](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-ModelRegistrationMode"></a>
Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to `AutoModelRegistrationEnabled`. To disable automatic model registration, set this value to `AutoModelRegistrationDisabled`. If not specified, `AutomaticModelRegistration` defaults to `AutoModelRegistrationDisabled`.
Type: String
Valid Values: `AutoModelRegistrationEnabled | AutoModelRegistrationDisabled`
Required: No

 ** [Name](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-Name"></a>
A string identifying the MLflow app name. This string is not part of the tracking server ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: Yes

 ** [RoleArn](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-RoleArn"></a>
The Amazon Resource Name (ARN) for an IAM role in your account that the MLflow App uses to access the artifact store in Amazon S3. The role should have the `AmazonS3FullAccess` permission.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-Tags"></a>
Tags consisting of key-value pairs used to manage metadata for the MLflow App.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [WeeklyMaintenanceWindowStart](#API_CreateMlflowApp_RequestSyntax) **   <a name="sagemaker-CreateMlflowApp-request-WeeklyMaintenanceWindowStart"></a>
The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. For example: TUE:03:30.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`
Required: No

## Response Syntax
<a name="API_CreateMlflowApp_ResponseSyntax"></a>

```
{
   "Arn": "string"
}
```

## Response Elements
<a name="API_CreateMlflowApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateMlflowApp_ResponseSyntax) **   <a name="sagemaker-CreateMlflowApp-response-Arn"></a>
The ARN of the MLflow App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-app/.*`

## Errors
<a name="API_CreateMlflowApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateMlflowApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateMlflowApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateMlflowApp)
