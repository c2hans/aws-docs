---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateUserProfile.html
---

# UpdateUserProfile
<a name="API_UpdateUserProfile"></a>

Updates a user profile.

## Request Syntax
<a name="API_UpdateUserProfile_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "UserProfileName": "{{string}}",
   "UserSettings": {
      "AutoMountHomeEFS": "{{string}}",
      "CanvasAppSettings": {
         "DirectDeploySettings": {
            "Status": "{{string}}"
         },
         "EmrServerlessSettings": {
            "ExecutionRoleArn": "{{string}}",
            "Status": "{{string}}"
         },
         "GenerativeAiSettings": {
            "AmazonBedrockRoleArn": "{{string}}"
         },
         "IdentityProviderOAuthSettings": [
            {
               "DataSourceName": "{{string}}",
               "SecretArn": "{{string}}",
               "Status": "{{string}}"
            }
         ],
         "KendraSettings": {
            "Status": "{{string}}"
         },
         "ModelRegisterSettings": {
            "CrossAccountModelRegisterRoleArn": "{{string}}",
            "Status": "{{string}}"
         },
         "TimeSeriesForecastingSettings": {
            "AmazonForecastRoleArn": "{{string}}",
            "Status": "{{string}}"
         },
         "WorkspaceSettings": {
            "S3ArtifactPath": "{{string}}",
            "S3KmsKeyId": "{{string}}"
         }
      },
      "CodeEditorAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": {{number}},
               "LifecycleManagement": "{{string}}",
               "MaxIdleTimeoutInMinutes": {{number}},
               "MinIdleTimeoutInMinutes": {{number}}
            }
         },
         "BuiltInLifecycleConfigArn": "{{string}}",
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
      "CustomFileSystemConfigs": [
         { ... }
      ],
      "CustomPosixUserConfig": {
         "Gid": {{number}},
         "Uid": {{number}}
      },
      "DefaultLandingUri": "{{string}}",
      "ExecutionRole": "{{string}}",
      "JupyterLabAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": {{number}},
               "LifecycleManagement": "{{string}}",
               "MaxIdleTimeoutInMinutes": {{number}},
               "MinIdleTimeoutInMinutes": {{number}}
            }
         },
         "BuiltInLifecycleConfigArn": "{{string}}",
         "CodeRepositories": [
            {
               "RepositoryUrl": "{{string}}"
            }
         ],
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
         "EmrSettings": {
            "AssumableRoleArns": [ "{{string}}" ],
            "ExecutionRoleArns": [ "{{string}}" ]
         },
         "LifecycleConfigArns": [ "{{string}}" ]
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
      "RSessionAppSettings": {
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
         }
      },
      "RStudioServerProAppSettings": {
         "AccessStatus": "{{string}}",
         "UserGroup": "{{string}}"
      },
      "SecurityGroups": [ "{{string}}" ],
      "SharingSettings": {
         "NotebookOutputOption": "{{string}}",
         "S3KmsKeyId": "{{string}}",
         "S3OutputPath": "{{string}}"
      },
      "SpaceStorageSettings": {
         "DefaultEbsStorageSettings": {
            "DefaultEbsVolumeSizeInGb": {{number}},
            "MaximumEbsVolumeSizeInGb": {{number}}
         }
      },
      "StudioWebPortal": "{{string}}",
      "StudioWebPortalSettings": {
         "ExecutionRoleSessionNameMode": "{{string}}",
         "HiddenAppTypes": [ "{{string}}" ],
         "HiddenInstanceTypes": [ "{{string}}" ],
         "HiddenMlTools": [ "{{string}}" ],
         "HiddenSageMakerImageVersionAliases": [
            {
               "SageMakerImageName": "{{string}}",
               "VersionAliases": [ "{{string}}" ]
            }
         ]
      },
      "TensorBoardAppSettings": {
         "DefaultResourceSpec": {
            "InstanceType": "{{string}}",
            "LifecycleConfigArn": "{{string}}",
            "SageMakerImageArn": "{{string}}",
            "SageMakerImageVersionAlias": "{{string}}",
            "SageMakerImageVersionArn": "{{string}}",
            "TrainingPlanArn": "{{string}}"
         }
      }
   }
}
```

## Request Parameters
<a name="API_UpdateUserProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_UpdateUserProfile_RequestSyntax) **   <a name="sagemaker-UpdateUserProfile-request-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [UserProfileName](#API_UpdateUserProfile_RequestSyntax) **   <a name="sagemaker-UpdateUserProfile-request-UserProfileName"></a>
The user profile name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [UserSettings](#API_UpdateUserProfile_RequestSyntax) **   <a name="sagemaker-UpdateUserProfile-request-UserSettings"></a>
A collection of settings.
Type: [UserSettings](API_UserSettings.md) object
Required: No

## Response Syntax
<a name="API_UpdateUserProfile_ResponseSyntax"></a>

```
{
   "UserProfileArn": "string"
}
```

## Response Elements
<a name="API_UpdateUserProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserProfileArn](#API_UpdateUserProfile_ResponseSyntax) **   <a name="sagemaker-UpdateUserProfile-response-UserProfileArn"></a>
The user profile Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:user-profile/.*`

## Errors
<a name="API_UpdateUserProfile_Errors"></a>

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
<a name="API_UpdateUserProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateUserProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateUserProfile)
