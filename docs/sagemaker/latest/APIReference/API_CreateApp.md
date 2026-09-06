---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateApp.html
---

# CreateApp
<a name="API_CreateApp"></a>

Creates a running app for the specified UserProfile. This operation is automatically invoked by Amazon SageMaker AI upon access to the associated Domain, and when new kernel configurations are selected by the user. A user may have multiple Apps active simultaneously.

## Request Syntax
<a name="API_CreateApp_RequestSyntax"></a>

```
{
   "AppName": "{{string}}",
   "AppType": "{{string}}",
   "DomainId": "{{string}}",
   "RecoveryMode": {{boolean}},
   "ResourceSpec": {
      "InstanceType": "{{string}}",
      "LifecycleConfigArn": "{{string}}",
      "SageMakerImageArn": "{{string}}",
      "SageMakerImageVersionAlias": "{{string}}",
      "SageMakerImageVersionArn": "{{string}}",
      "TrainingPlanArn": "{{string}}"
   },
   "SpaceName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UserProfileName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateApp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppName](#API_CreateApp_RequestSyntax) **   <a name="sagemaker-CreateApp-request-AppName"></a>
The name of the app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [AppType](#API_CreateApp_RequestSyntax) **   <a name="sagemaker-CreateApp-request-AppType"></a>
The type of app.
Type: String
Valid Values: `JupyterServer | KernelGateway | DetailedProfiler | TensorBoard | CodeEditor | JupyterLab | RStudioServerPro | RSessionGateway | Canvas`
Required: Yes

 ** [DomainId](#API_CreateApp_RequestSyntax) **   <a name="sagemaker-CreateApp-request-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [RecoveryMode](#API_CreateApp_RequestSyntax) **   <a name="sagemaker-CreateApp-request-RecoveryMode"></a>
 Indicates whether the application is launched in recovery mode.
Type: Boolean
Required: No

 ** [ResourceSpec](#API_CreateApp_RequestSyntax) **   <a name="sagemaker-CreateApp-request-ResourceSpec"></a>
The instance type and the Amazon Resource Name (ARN) of the SageMaker AI image created on the instance.
The value of `InstanceType` passed as part of the `ResourceSpec` in the `CreateApp` call overrides the value passed as part of the `ResourceSpec` configured for the user profile or the domain. If `InstanceType` is not specified in any of those three `ResourceSpec` values for a `KernelGateway` app, the `CreateApp` call fails with a request validation error.
Type: [ResourceSpec](API_ResourceSpec.md) object
Required: No

 ** [SpaceName](#API_CreateApp_RequestSyntax) **   <a name="sagemaker-CreateApp-request-SpaceName"></a>
The name of the space. If this value is not set, then `UserProfileName` must be set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [Tags](#API_CreateApp_RequestSyntax) **   <a name="sagemaker-CreateApp-request-Tags"></a>
Each tag consists of a key and an optional value. Tag keys must be unique per resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [UserProfileName](#API_CreateApp_RequestSyntax) **   <a name="sagemaker-CreateApp-request-UserProfileName"></a>
The user profile name. If this value is not set, then `SpaceName` must be set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## Response Syntax
<a name="API_CreateApp_ResponseSyntax"></a>

```
{
   "AppArn": "string"
}
```

## Response Elements
<a name="API_CreateApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppArn](#API_CreateApp_ResponseSyntax) **   <a name="sagemaker-CreateApp-response-AppArn"></a>
The Amazon Resource Name (ARN) of the app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:app/.*`

## Errors
<a name="API_CreateApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateApp)
