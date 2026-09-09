---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeMlflowApp.html
---

# DescribeMlflowApp
<a name="API_DescribeMlflowApp"></a>

Returns information about an MLflow App.

## Request Syntax
<a name="API_DescribeMlflowApp_RequestSyntax"></a>

```
{
   "Arn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMlflowApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arn](#API_DescribeMlflowApp_RequestSyntax) **   <a name="sagemaker-DescribeMlflowApp-request-Arn"></a>
The ARN of the MLflow App for which to get information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-app/.*`
Required: Yes

## Response Syntax
<a name="API_DescribeMlflowApp_ResponseSyntax"></a>

```
{
   "AccountDefaultStatus": "string",
   "Arn": "string",
   "ArtifactStoreUri": "string",
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
   "DefaultDomainIdList": [ "string" ],
   "KmsKeyId": "string",
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
   "MaintenanceStatus": "string",
   "MlflowVersion": "string",
   "ModelRegistrationMode": "string",
   "Name": "string",
   "RoleArn": "string",
   "Status": "string",
   "WeeklyMaintenanceWindowStart": "string"
}
```

## Response Elements
<a name="API_DescribeMlflowApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountDefaultStatus](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-AccountDefaultStatus"></a>
Indicates whether this MLflow app is the default for the entire account.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [Arn](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-Arn"></a>
The ARN of the MLflow App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-app/.*`

 ** [ArtifactStoreUri](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-ArtifactStoreUri"></a>
The S3 URI of the general purpose bucket used as the MLflow App artifact store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`

 ** [CreatedBy](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [DefaultDomainIdList](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-DefaultDomainIdList"></a>
List of SageMaker Domain IDs for which this MLflow App is the default.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`

 ** [KmsKeyId](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-KmsKeyId"></a>
The ID of the AWS KMS key used to encrypt the data at rest associated with the MLflow App. This field is absent if the MLflow App is not encrypted with a customer-managed key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`

 ** [LastModifiedBy](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [MaintenanceStatus](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-MaintenanceStatus"></a>
Current maintenance status of the MLflow App.
Type: String
Valid Values: `MaintenanceInProgress | MaintenanceComplete | MaintenanceFailed`

 ** [MlflowVersion](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-MlflowVersion"></a>
The MLflow version used.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `[0-9]*.[0-9]*.[0-9]*`

 ** [ModelRegistrationMode](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-ModelRegistrationMode"></a>
Whether automatic registration of new MLflow models to the SageMaker Model Registry is enabled.
Type: String
Valid Values: `AutoModelRegistrationEnabled | AutoModelRegistrationDisabled`

 ** [Name](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-Name"></a>
The name of the MLflow App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`

 ** [RoleArn](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-RoleArn"></a>
The Amazon Resource Name (ARN) for an IAM role in your account that the MLflow App uses to access the artifact store in Amazon S3.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [Status](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-Status"></a>
The current creation status of the described MLflow App.
Type: String
Valid Values: `Creating | Created | CreateFailed | Updating | Updated | UpdateFailed | Deleting | DeleteFailed | Deleted`

 ** [WeeklyMaintenanceWindowStart](#API_DescribeMlflowApp_ResponseSyntax) **   <a name="sagemaker-DescribeMlflowApp-response-WeeklyMaintenanceWindowStart"></a>
The day and time of the week when weekly maintenance occurs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9.
Pattern: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`

## Errors
<a name="API_DescribeMlflowApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeMlflowApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeMlflowApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeMlflowApp)
