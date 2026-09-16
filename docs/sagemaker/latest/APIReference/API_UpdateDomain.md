---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateDomain.html
---

# UpdateDomain
<a name="API_UpdateDomain"></a>

Updates the default settings for new user profiles in the domain.

## Request Syntax
<a name="API_UpdateDomain_RequestSyntax"></a>

```
{
   "AppNetworkAccessType": "{{string}}",
   "AppSecurityGroupManagement": "{{string}}",
   "DefaultSpaceSettings": {
      "CustomFileSystemConfigs": [
         { ... }
      ],
      "CustomPosixUserConfig": {
         "Gid": {{number}},
         "Uid": {{number}}
      },
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
      "SecurityGroups": [ "{{string}}" ],
      "SpaceStorageSettings": {
         "DefaultEbsStorageSettings": {
            "DefaultEbsVolumeSizeInGb": {{number}},
            "MaximumEbsVolumeSizeInGb": {{number}}
         }
      }
   },
   "DefaultUserSettings": {
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
   },
   "DomainId": "{{string}}",
   "DomainSettingsForUpdate": {
      "AmazonQSettings": {
         "QProfileArn": "{{string}}",
         "Status": "{{string}}"
      },
      "DockerSettings": {
         "EnableDockerAccess": "{{string}}",
         "RootlessDocker": "{{string}}",
         "VpcOnlyTrustedAccounts": [ "{{string}}" ]
      },
      "ExecutionRoleIdentityConfig": "{{string}}",
      "IpAddressType": "{{string}}",
      "RStudioServerProDomainSettingsForUpdate": {
         "DefaultResourceSpec": {
            "InstanceType": "{{string}}",
            "LifecycleConfigArn": "{{string}}",
            "SageMakerImageArn": "{{string}}",
            "SageMakerImageVersionAlias": "{{string}}",
            "SageMakerImageVersionArn": "{{string}}",
            "TrainingPlanArn": "{{string}}"
         },
         "DomainExecutionRoleArn": "{{string}}",
         "RStudioConnectUrl": "{{string}}",
         "RStudioPackageManagerUrl": "{{string}}"
      },
      "SecurityGroupIds": [ "{{string}}" ],
      "TrustedIdentityPropagationSettings": {
         "Status": "{{string}}"
      },
      "UnifiedStudioSettings": {
         "DomainAccountId": "{{string}}",
         "DomainId": "{{string}}",
         "DomainRegion": "{{string}}",
         "EnvironmentId": "{{string}}",
         "ProjectId": "{{string}}",
         "ProjectS3Path": "{{string}}",
         "SingleSignOnApplicationArn": "{{string}}",
         "StudioWebPortalAccess": "{{string}}"
      }
   },
   "HomeEfsFileSystemCreation": "{{string}}",
   "SubnetIds": [ "{{string}}" ],
   "TagPropagation": "{{string}}",
   "VpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppNetworkAccessType](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-AppNetworkAccessType"></a>
Specifies the VPC used for non-EFS traffic.
+  `PublicInternetOnly` - Non-EFS traffic is through a VPC managed by Amazon SageMaker AI, which allows direct internet access.
+  `VpcOnly` - All Studio traffic is through the specified VPC and subnets.
This configuration can only be modified if there are no apps in the `InService`, `Pending`, or `Deleting` state. The configuration cannot be updated if `DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn` is already set or `DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn` is provided as part of the same request.
Type: String
Valid Values: `PublicInternetOnly | VpcOnly`
Required: No

 ** [AppSecurityGroupManagement](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-AppSecurityGroupManagement"></a>
The entity that creates and manages the required security groups for inter-app communication in `VPCOnly` mode. Required when `CreateDomain.AppNetworkAccessType` is `VPCOnly` and `DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn` is provided. If setting up the domain for use with RStudio, this value must be set to `Service`.
Type: String
Valid Values: `Service | Customer`
Required: No

 ** [DefaultSpaceSettings](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-DefaultSpaceSettings"></a>
The default settings for shared spaces that users create in the domain.
Type: [DefaultSpaceSettings](API_DefaultSpaceSettings.md) object
Required: No

 ** [DefaultUserSettings](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-DefaultUserSettings"></a>
A collection of settings.
Type: [UserSettings](API_UserSettings.md) object
Required: No

 ** [DomainId](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-DomainId"></a>
The ID of the domain to be updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [DomainSettingsForUpdate](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-DomainSettingsForUpdate"></a>
A collection of `DomainSettings` configuration values to update.
Type: [DomainSettingsForUpdate](API_DomainSettingsForUpdate.md) object
Required: No

 ** [HomeEfsFileSystemCreation](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-HomeEfsFileSystemCreation"></a>
Indicates whether to create a home EFS file system for the domain. You can change from `Disabled` to `Enabled` to provision EFS on demand, but you cannot change from `Enabled` to `Disabled`.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [SubnetIds](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-SubnetIds"></a>
The VPC subnets that Studio uses for communication.
If removing subnets, ensure there are no apps in the `InService`, `Pending`, or `Deleting` state.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** [TagPropagation](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-TagPropagation"></a>
Indicates whether custom tag propagation is supported for the domain. Defaults to `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [VpcId](#API_UpdateDomain_RequestSyntax) **   <a name="sagemaker-UpdateDomain-request-VpcId"></a>
The identifier for the VPC used by the domain for network communication. Use this field only when adding VPC configuration to a SageMaker AI domain used in Amazon SageMaker Unified Studio that was created without VPC settings. SageMaker AI doesn't automatically apply VPC updates to existing applications. Stop and restart your applications to apply the changes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

## Response Syntax
<a name="API_UpdateDomain_ResponseSyntax"></a>

```
{
   "DomainArn": "string"
}
```

## Response Elements
<a name="API_UpdateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainArn](#API_UpdateDomain_ResponseSyntax) **   <a name="sagemaker-UpdateDomain-response-DomainArn"></a>
The Amazon Resource Name (ARN) of the domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:domain/.*`

## Errors
<a name="API_UpdateDomain_Errors"></a>

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
<a name="API_UpdateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateDomain)
