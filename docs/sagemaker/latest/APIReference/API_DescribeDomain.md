---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeDomain.html
---

# DescribeDomain
<a name="API_DescribeDomain"></a>

The description of the domain.

## Request Syntax
<a name="API_DescribeDomain_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_DescribeDomain_RequestSyntax) **   <a name="sagemaker-DescribeDomain-request-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

## Response Syntax
<a name="API_DescribeDomain_ResponseSyntax"></a>

```
{
   "AppNetworkAccessType": "string",
   "AppSecurityGroupManagement": "string",
   "AuthMode": "string",
   "CreationTime": number,
   "DefaultSpaceSettings": {
      "CustomFileSystemConfigs": [
         { ... }
      ],
      "CustomPosixUserConfig": {
         "Gid": number,
         "Uid": number
      },
      "ExecutionRole": "string",
      "JupyterLabAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": number,
               "LifecycleManagement": "string",
               "MaxIdleTimeoutInMinutes": number,
               "MinIdleTimeoutInMinutes": number
            }
         },
         "BuiltInLifecycleConfigArn": "string",
         "CodeRepositories": [
            {
               "RepositoryUrl": "string"
            }
         ],
         "CustomImages": [
            {
               "AppImageConfigName": "string",
               "ImageName": "string",
               "ImageVersionNumber": number
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "EmrSettings": {
            "AssumableRoleArns": [ "string" ],
            "ExecutionRoleArns": [ "string" ]
         },
         "LifecycleConfigArns": [ "string" ]
      },
      "JupyterServerAppSettings": {
         "CodeRepositories": [
            {
               "RepositoryUrl": "string"
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "LifecycleConfigArns": [ "string" ]
      },
      "KernelGatewayAppSettings": {
         "CustomImages": [
            {
               "AppImageConfigName": "string",
               "ImageName": "string",
               "ImageVersionNumber": number
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "LifecycleConfigArns": [ "string" ]
      },
      "SecurityGroups": [ "string" ],
      "SpaceStorageSettings": {
         "DefaultEbsStorageSettings": {
            "DefaultEbsVolumeSizeInGb": number,
            "MaximumEbsVolumeSizeInGb": number
         }
      }
   },
   "DefaultUserSettings": {
      "AutoMountHomeEFS": "string",
      "CanvasAppSettings": {
         "DirectDeploySettings": {
            "Status": "string"
         },
         "EmrServerlessSettings": {
            "ExecutionRoleArn": "string",
            "Status": "string"
         },
         "GenerativeAiSettings": {
            "AmazonBedrockRoleArn": "string"
         },
         "IdentityProviderOAuthSettings": [
            {
               "DataSourceName": "string",
               "SecretArn": "string",
               "Status": "string"
            }
         ],
         "KendraSettings": {
            "Status": "string"
         },
         "ModelRegisterSettings": {
            "CrossAccountModelRegisterRoleArn": "string",
            "Status": "string"
         },
         "TimeSeriesForecastingSettings": {
            "AmazonForecastRoleArn": "string",
            "Status": "string"
         },
         "WorkspaceSettings": {
            "S3ArtifactPath": "string",
            "S3KmsKeyId": "string"
         }
      },
      "CodeEditorAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": number,
               "LifecycleManagement": "string",
               "MaxIdleTimeoutInMinutes": number,
               "MinIdleTimeoutInMinutes": number
            }
         },
         "BuiltInLifecycleConfigArn": "string",
         "CustomImages": [
            {
               "AppImageConfigName": "string",
               "ImageName": "string",
               "ImageVersionNumber": number
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "LifecycleConfigArns": [ "string" ]
      },
      "CustomFileSystemConfigs": [
         { ... }
      ],
      "CustomPosixUserConfig": {
         "Gid": number,
         "Uid": number
      },
      "DefaultLandingUri": "string",
      "ExecutionRole": "string",
      "JupyterLabAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": number,
               "LifecycleManagement": "string",
               "MaxIdleTimeoutInMinutes": number,
               "MinIdleTimeoutInMinutes": number
            }
         },
         "BuiltInLifecycleConfigArn": "string",
         "CodeRepositories": [
            {
               "RepositoryUrl": "string"
            }
         ],
         "CustomImages": [
            {
               "AppImageConfigName": "string",
               "ImageName": "string",
               "ImageVersionNumber": number
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "EmrSettings": {
            "AssumableRoleArns": [ "string" ],
            "ExecutionRoleArns": [ "string" ]
         },
         "LifecycleConfigArns": [ "string" ]
      },
      "JupyterServerAppSettings": {
         "CodeRepositories": [
            {
               "RepositoryUrl": "string"
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "LifecycleConfigArns": [ "string" ]
      },
      "KernelGatewayAppSettings": {
         "CustomImages": [
            {
               "AppImageConfigName": "string",
               "ImageName": "string",
               "ImageVersionNumber": number
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "LifecycleConfigArns": [ "string" ]
      },
      "RSessionAppSettings": {
         "CustomImages": [
            {
               "AppImageConfigName": "string",
               "ImageName": "string",
               "ImageVersionNumber": number
            }
         ],
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         }
      },
      "RStudioServerProAppSettings": {
         "AccessStatus": "string",
         "UserGroup": "string"
      },
      "SecurityGroups": [ "string" ],
      "SharingSettings": {
         "NotebookOutputOption": "string",
         "S3KmsKeyId": "string",
         "S3OutputPath": "string"
      },
      "SpaceStorageSettings": {
         "DefaultEbsStorageSettings": {
            "DefaultEbsVolumeSizeInGb": number,
            "MaximumEbsVolumeSizeInGb": number
         }
      },
      "StudioWebPortal": "string",
      "StudioWebPortalSettings": {
         "ExecutionRoleSessionNameMode": "string",
         "HiddenAppTypes": [ "string" ],
         "HiddenInstanceTypes": [ "string" ],
         "HiddenMlTools": [ "string" ],
         "HiddenSageMakerImageVersionAliases": [
            {
               "SageMakerImageName": "string",
               "VersionAliases": [ "string" ]
            }
         ]
      },
      "TensorBoardAppSettings": {
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         }
      }
   },
   "DomainArn": "string",
   "DomainId": "string",
   "DomainName": "string",
   "DomainSettings": {
      "AmazonQSettings": {
         "QProfileArn": "string",
         "Status": "string"
      },
      "DockerSettings": {
         "EnableDockerAccess": "string",
         "RootlessDocker": "string",
         "VpcOnlyTrustedAccounts": [ "string" ]
      },
      "ExecutionRoleIdentityConfig": "string",
      "IpAddressType": "string",
      "RStudioServerProDomainSettings": {
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "DomainExecutionRoleArn": "string",
         "RStudioConnectUrl": "string",
         "RStudioPackageManagerUrl": "string"
      },
      "SecurityGroupIds": [ "string" ],
      "TrustedIdentityPropagationSettings": {
         "Status": "string"
      },
      "UnifiedStudioSettings": {
         "DomainAccountId": "string",
         "DomainId": "string",
         "DomainRegion": "string",
         "EnvironmentId": "string",
         "ProjectId": "string",
         "ProjectS3Path": "string",
         "SingleSignOnApplicationArn": "string",
         "StudioWebPortalAccess": "string"
      }
   },
   "FailureReason": "string",
   "HomeEfsFileSystemCreation": "string",
   "HomeEfsFileSystemId": "string",
   "HomeEfsFileSystemKmsKeyId": "string",
   "KmsKeyId": "string",
   "LastModifiedTime": number,
   "SecurityGroupIdForDomainBoundary": "string",
   "SingleSignOnApplicationArn": "string",
   "SingleSignOnManagedApplicationInstanceId": "string",
   "Status": "string",
   "SubnetIds": [ "string" ],
   "TagPropagation": "string",
   "Url": "string",
   "VpcId": "string"
}
```

## Response Elements
<a name="API_DescribeDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppNetworkAccessType](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-AppNetworkAccessType"></a>
Specifies the VPC used for non-EFS traffic. The default value is `PublicInternetOnly`.
+  `PublicInternetOnly` - Non-EFS traffic is through a VPC managed by Amazon SageMaker AI, which allows direct internet access
+  `VpcOnly` - All traffic is through the specified VPC and subnets
Type: String
Valid Values: `PublicInternetOnly | VpcOnly`

 ** [AppSecurityGroupManagement](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-AppSecurityGroupManagement"></a>
The entity that creates and manages the required security groups for inter-app communication in `VPCOnly` mode. Required when `CreateDomain.AppNetworkAccessType` is `VPCOnly` and `DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn` is provided.
Type: String
Valid Values: `Service | Customer`

 ** [AuthMode](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-AuthMode"></a>
The domain's authentication mode.
Type: String
Valid Values: `SSO | IAM`

 ** [CreationTime](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-CreationTime"></a>
The creation time.
Type: Timestamp

 ** [DefaultSpaceSettings](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-DefaultSpaceSettings"></a>
The default settings for shared spaces that users create in the domain.
Type: [DefaultSpaceSettings](API_DefaultSpaceSettings.md) object

 ** [DefaultUserSettings](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-DefaultUserSettings"></a>
Settings which are applied to UserProfiles in this domain if settings are not explicitly specified in a given UserProfile.
Type: [UserSettings](API_UserSettings.md) object

 ** [DomainArn](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-DomainArn"></a>
The domain's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:domain/.*`

 ** [DomainId](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`

 ** [DomainName](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-DomainName"></a>
The domain name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [DomainSettings](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-DomainSettings"></a>
A collection of `Domain` settings.
Type: [DomainSettings](API_DomainSettings.md) object

 ** [FailureReason](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-FailureReason"></a>
The failure reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [HomeEfsFileSystemCreation](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-HomeEfsFileSystemCreation"></a>
Indicates whether a home EFS file system is created for the domain.
Type: String
Valid Values: `Enabled | Disabled`

 ** [HomeEfsFileSystemId](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-HomeEfsFileSystemId"></a>
The ID of the Amazon Elastic File System managed by this Domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [HomeEfsFileSystemKmsKeyId](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-HomeEfsFileSystemKmsKeyId"></a>
 *This parameter has been deprecated.*
Use `KmsKeyId`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`

 ** [KmsKeyId](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-KmsKeyId"></a>
The AWS KMS customer managed key used to encrypt the EFS volume attached to the domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`

 ** [LastModifiedTime](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-LastModifiedTime"></a>
The last modified time.
Type: Timestamp

 ** [SecurityGroupIdForDomainBoundary](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-SecurityGroupIdForDomainBoundary"></a>
The ID of the security group that authorizes traffic between the `RSessionGateway` apps and the `RStudioServerPro` app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`

 ** [SingleSignOnApplicationArn](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-SingleSignOnApplicationArn"></a>
The ARN of the application managed by SageMaker AI in IAM Identity Center. This value is only returned for domains created after October 1, 2023.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::[0-9]+:application\/[a-zA-Z0-9-_.]+\/apl-[a-zA-Z0-9]+`

 ** [SingleSignOnManagedApplicationInstanceId](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-SingleSignOnManagedApplicationInstanceId"></a>
The IAM Identity Center managed application instance ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [Status](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-Status"></a>
The status.
Type: String
Valid Values: `Deleting | Failed | InService | Pending | Updating | Update_Failed | Delete_Failed`

 ** [SubnetIds](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-SubnetIds"></a>
The VPC subnets that the domain uses for communication.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`

 ** [TagPropagation](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-TagPropagation"></a>
Indicates whether custom tag propagation is supported for the domain.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [Url](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-Url"></a>
The domain's URL.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [VpcId](#API_DescribeDomain_ResponseSyntax) **   <a name="sagemaker-DescribeDomain-response-VpcId"></a>
The ID of the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`

## Errors
<a name="API_DescribeDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeDomain)
