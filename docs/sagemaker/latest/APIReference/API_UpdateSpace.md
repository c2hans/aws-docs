---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateSpace.html
---

# UpdateSpace
<a name="API_UpdateSpace"></a>

Updates the settings of a space.

**Note**
You can't edit the app type of a space in the `SpaceSettings`.

## Request Syntax
<a name="API_UpdateSpace_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "SpaceDisplayName": "{{string}}",
   "SpaceName": "{{string}}",
   "SpaceSettings": {
      "AppType": "{{string}}",
      "CodeEditorAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": {{number}}
            }
         },
         "DefaultResourceSpec": {
            "InstanceType": "{{string}}",
            "LifecycleConfigArn": "{{string}}",
            "SageMakerImageArn": "{{string}}",
            "SageMakerImageVersionAlias": "{{string}}",
            "SageMakerImageVersionArn": "{{string}}",
            "TrainingPlanArn": "{{string}}"
         }
      },
      "CustomFileSystems": [
         { ... }
      ],
      "JupyterLabAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": {{number}}
            }
         },
         "CodeRepositories": [
            {
               "RepositoryUrl": "{{string}}"
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "{{string}}",
            "LifecycleConfigArn": "{{string}}",
            "SageMakerImageArn": "{{string}}",
            "SageMakerImageVersionAlias": "{{string}}",
            "SageMakerImageVersionArn": "{{string}}",
            "TrainingPlanArn": "{{string}}"
         }
      },
      "JupyterServerAppSettings": {
         "CodeRepositories": [
            {
               "RepositoryUrl": "{{string}}"
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "{{string}}",
            "LifecycleConfigArn": "{{string}}",
            "SageMakerImageArn": "{{string}}",
            "SageMakerImageVersionAlias": "{{string}}",
            "SageMakerImageVersionArn": "{{string}}",
            "TrainingPlanArn": "{{string}}"
         },
         "LifecycleConfigArns": [ "{{string}}" ]
      },
      "KernelGatewayAppSettings": {
         "CustomImages": [
            {
               "AppImageConfigName": "{{string}}",
               "ImageName": "{{string}}",
               "ImageVersionNumber": {{number}}
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "{{string}}",
            "LifecycleConfigArn": "{{string}}",
            "SageMakerImageArn": "{{string}}",
            "SageMakerImageVersionAlias": "{{string}}",
            "SageMakerImageVersionArn": "{{string}}",
            "TrainingPlanArn": "{{string}}"
         },
         "LifecycleConfigArns": [ "{{string}}" ]
      },
      "RemoteAccess": "{{string}}",
      "SpaceManagedResources": "{{string}}",
      "SpaceStorageSettings": {
         "EbsStorageSettings": {
            "EbsVolumeSizeInGb": {{number}}
         }
      }
   }
}
```

## Request Parameters
<a name="API_UpdateSpace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_UpdateSpace_RequestSyntax) **   <a name="sagemaker-UpdateSpace-request-DomainId"></a>
The ID of the associated domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [SpaceDisplayName](#API_UpdateSpace_RequestSyntax) **   <a name="sagemaker-UpdateSpace-request-SpaceDisplayName"></a>
The name of the space that appears in the Amazon SageMaker Studio UI.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`
Required: No

 ** [SpaceName](#API_UpdateSpace_RequestSyntax) **   <a name="sagemaker-UpdateSpace-request-SpaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [SpaceSettings](#API_UpdateSpace_RequestSyntax) **   <a name="sagemaker-UpdateSpace-request-SpaceSettings"></a>
A collection of space settings.
Type: [SpaceSettings](API_SpaceSettings.md) object
Required: No

## Response Syntax
<a name="API_UpdateSpace_ResponseSyntax"></a>

```
{
   "SpaceArn": "string"
}
```

## Response Elements
<a name="API_UpdateSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SpaceArn](#API_UpdateSpace_ResponseSyntax) **   <a name="sagemaker-UpdateSpace-response-SpaceArn"></a>
The space's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:space/.*`

## Errors
<a name="API_UpdateSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateSpace)
