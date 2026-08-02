---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateUserProfile.html
---

# CreateUserProfile
<a name="API_CreateUserProfile"></a>

Creates a user profile. A user profile represents a single user within a domain, and is the main way to reference a "person" for the purposes of sharing, reporting, and other user-oriented features. This entity is created when a user onboards to a domain. If an administrator invites a person by email or imports them from IAM Identity Center, a user profile is automatically created. A user profile is the primary holder of settings for an individual user and has a reference to the user's private Amazon Elastic File System home directory.

## Request Syntax
<a name="API_CreateUserProfile_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "SingleSignOnUserIdentifier": "{{string}}",
   "SingleSignOnUserValue": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
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
<a name="API_CreateUserProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_CreateUserProfile_RequestSyntax) **   <a name="sagemaker-CreateUserProfile-request-DomainId"></a>
The ID of the associated Domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [SingleSignOnUserIdentifier](#API_CreateUserProfile_RequestSyntax) **   <a name="sagemaker-CreateUserProfile-request-SingleSignOnUserIdentifier"></a>
A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is IAM Identity Center, this field is required. If the Domain's AuthMode is not IAM Identity Center, this field cannot be specified.
Type: String
Pattern: `UserName`
Required: No

 ** [SingleSignOnUserValue](#API_CreateUserProfile_RequestSyntax) **   <a name="sagemaker-CreateUserProfile-request-SingleSignOnUserValue"></a>
The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is IAM Identity Center, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not IAM Identity Center, this field cannot be specified.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Tags](#API_CreateUserProfile_RequestSyntax) **   <a name="sagemaker-CreateUserProfile-request-Tags"></a>
Each tag consists of a key and an optional value. Tag keys must be unique per resource.
Tags that you specify for the User Profile are also added to all Apps that the User Profile launches.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [UserProfileName](#API_CreateUserProfile_RequestSyntax) **   <a name="sagemaker-CreateUserProfile-request-UserProfileName"></a>
A name for the UserProfile. This value is not case sensitive.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [UserSettings](#API_CreateUserProfile_RequestSyntax) **   <a name="sagemaker-CreateUserProfile-request-UserSettings"></a>
A collection of settings.
Type: [UserSettings](API_UserSettings.md) object
Required: No

## Response Syntax
<a name="API_CreateUserProfile_ResponseSyntax"></a>

```
{
   "UserProfileArn": "string"
}
```

## Response Elements
<a name="API_CreateUserProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserProfileArn](#API_CreateUserProfile_ResponseSyntax) **   <a name="sagemaker-CreateUserProfile-response-UserProfileArn"></a>
The user profile Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:user-profile/.*`

## Errors
<a name="API_CreateUserProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateUserProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateUserProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateUserProfile)
