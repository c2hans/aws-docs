---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeApp.html
---

# DescribeApp
<a name="API_DescribeApp"></a>

Describes the app.

## Request Syntax
<a name="API_DescribeApp_RequestSyntax"></a>

```
{
   "AppName": "{{string}}",
   "AppType": "{{string}}",
   "DomainId": "{{string}}",
   "SpaceName": "{{string}}",
   "UserProfileName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppName](#API_DescribeApp_RequestSyntax) **   <a name="sagemaker-DescribeApp-request-AppName"></a>
The name of the app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [AppType](#API_DescribeApp_RequestSyntax) **   <a name="sagemaker-DescribeApp-request-AppType"></a>
The type of app.
Type: String
Valid Values: `JupyterServer | KernelGateway`
Required: Yes

 ** [DomainId](#API_DescribeApp_RequestSyntax) **   <a name="sagemaker-DescribeApp-request-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [SpaceName](#API_DescribeApp_RequestSyntax) **   <a name="sagemaker-DescribeApp-request-SpaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [UserProfileName](#API_DescribeApp_RequestSyntax) **   <a name="sagemaker-DescribeApp-request-UserProfileName"></a>
The user profile name. If this value is not set, then `SpaceName` must be set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## Response Syntax
<a name="API_DescribeApp_ResponseSyntax"></a>

```
{
   "AppArn": "string",
   "AppName": "string",
   "AppType": "string",
   "BuiltInLifecycleConfigArn": "string",
   "DomainId": "string",
   "EffectiveTrustedIdentityPropagationStatus": "string",
   "FailureReason": "string",
   "RecoveryMode": boolean,
   "ResourceSpec": {
      "InstanceType": "string",
      "LifecycleConfigArn": "string",
      "SageMakerImageArn": "string",
      "SageMakerImageVersionAlias": "string",
      "SageMakerImageVersionArn": "string",
      "TrainingPlanArn": "string"
   },
   "SpaceName": "string",
   "Status": "string",
   "UserProfileName": "string"
}
```

## Response Elements
<a name="API_DescribeApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppArn](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-AppArn"></a>
The Amazon Resource Name (ARN) of the app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:app/.*`

 ** [AppName](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-AppName"></a>
The name of the app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [AppType](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-AppType"></a>
The type of app.
Type: String
Valid Values: `JupyterServer | KernelGateway`

 ** [BuiltInLifecycleConfigArn](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-BuiltInLifecycleConfigArn"></a>
The lifecycle configuration that runs before the default lifecycle configuration
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`

 ** [DomainId](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`

 ** [EffectiveTrustedIdentityPropagationStatus](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-EffectiveTrustedIdentityPropagationStatus"></a>
The effective status of Trusted Identity Propagation (TIP) for this application. When enabled, user identities from IAM Identity Center are being propagated through the application to TIP enabled AWS services. When disabled, standard IAM role-based access is used.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [FailureReason](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-FailureReason"></a>
The failure reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [RecoveryMode](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-RecoveryMode"></a>
 Indicates whether the application is launched in recovery mode.
Type: Boolean

 ** [ResourceSpec](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-ResourceSpec"></a>
The instance type and the Amazon Resource Name (ARN) of the SageMaker AI image created on the instance.
Type: [ResourceSpec](API_ResourceSpec.md) object

 ** [SpaceName](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-SpaceName"></a>
The name of the space. If this value is not set, then `UserProfileName` must be set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [Status](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-Status"></a>
The status.
Type: String
Valid Values: `Deleted | Deleting | Failed | InService | Pending`

 ** [UserProfileName](#API_DescribeApp_ResponseSyntax) **   <a name="sagemaker-DescribeApp-response-UserProfileName"></a>
The user profile name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_DescribeApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeApp)
