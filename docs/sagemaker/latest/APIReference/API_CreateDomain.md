---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDomain.html
---

# CreateDomain
<a name="API_CreateDomain"></a>

Creates a `Domain`. A domain consists of an associated Amazon Elastic File System volume, a list of authorized users, and a variety of security, application, policy, and Amazon Virtual Private Cloud (VPC) configurations. Users within a domain can share notebook files and other artifacts with each other.

 **EFS storage**

When a domain is created, an EFS volume is created for use by all of the users within the domain. Each user receives a private home directory within the EFS volume for notebooks, Git repositories, and data files.

SageMaker AI uses the AWS Key Management Service (AWS KMS) to encrypt the EFS volume attached to the domain with an AWS managed key by default. For more control, you can specify a customer managed key. For more information, see [Protect Data at Rest Using Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest.html).

 **VPC configuration**

All traffic between the domain and the Amazon EFS volume is through the specified VPC and subnets. For other traffic, you can specify the `AppNetworkAccessType` parameter. `AppNetworkAccessType` corresponds to the network access type that you choose when you onboard to the domain. The following options are available:
+  `PublicInternetOnly` - Non-EFS traffic goes through a VPC managed by Amazon SageMaker AI, which allows internet access. This is the default value.
+  `VpcOnly` - All traffic is through the specified VPC and subnets. Internet access is disabled by default. To allow internet access, you must specify a NAT gateway.

  When internet access is disabled, you won't be able to run a Amazon SageMaker AI Studio notebook or to train or host models unless your VPC has an interface endpoint to the SageMaker AI API and runtime or a NAT gateway and your security groups allow outbound connections.

**Important**
NFS traffic over TCP on port 2049 needs to be allowed in both inbound and outbound rules in order to launch a Amazon SageMaker AI Studio app successfully.

For more information, see [Connect Amazon SageMaker AI Studio Notebooks to Resources in a VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html).

## Request Syntax
<a name="API_CreateDomain_RequestSyntax"></a>

```
{
   "AppNetworkAccessType": "{{string}}",
   "AppSecurityGroupManagement": "{{string}}",
   "AuthMode": "{{string}}",
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
   "DomainName": "{{string}}",
   "DomainSettings": {
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
      "RStudioServerProDomainSettings": {
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
   "HomeEfsFileSystemKmsKeyId": "{{string}}",
   "KmsKeyId": "{{string}}",
   "SubnetIds": [ "{{string}}" ],
   "TagPropagation": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppNetworkAccessType](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-AppNetworkAccessType"></a>
Specifies the VPC used for non-EFS traffic. The default value is `PublicInternetOnly`.
+  `PublicInternetOnly` - Non-EFS traffic is through a VPC managed by Amazon SageMaker AI, which allows direct internet access
+  `VpcOnly` - All traffic is through the specified VPC and subnets
Type: String
Valid Values: `PublicInternetOnly | VpcOnly`
Required: No

 ** [AppSecurityGroupManagement](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-AppSecurityGroupManagement"></a>
The entity that creates and manages the required security groups for inter-app communication in `VPCOnly` mode. Required when `CreateDomain.AppNetworkAccessType` is `VPCOnly` and `DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn` is provided. If setting up the domain for use with RStudio, this value must be set to `Service`.
Type: String
Valid Values: `Service | Customer`
Required: No

 ** [AuthMode](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-AuthMode"></a>
The mode of authentication that members use to access the domain.
Type: String
Valid Values: `SSO | IAM`
Required: Yes

 ** [DefaultSpaceSettings](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-DefaultSpaceSettings"></a>
The default settings for shared spaces that users create in the domain.
Type: [DefaultSpaceSettings](API_DefaultSpaceSettings.md) object
Required: No

 ** [DefaultUserSettings](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-DefaultUserSettings"></a>
The default settings to use to create a user profile when `UserSettings` isn't specified in the call to the `CreateUserProfile` API.
 `SecurityGroups` is aggregated when specified in both calls. For all other settings in `UserSettings`, the values specified in `CreateUserProfile` take precedence over those specified in `CreateDomain`.
Type: [UserSettings](API_UserSettings.md) object
Required: Yes

 ** [DomainName](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-DomainName"></a>
A name for the domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [DomainSettings](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-DomainSettings"></a>
A collection of `Domain` settings.
Type: [DomainSettings](API_DomainSettings.md) object
Required: No

 ** [HomeEfsFileSystemCreation](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-HomeEfsFileSystemCreation"></a>
Indicates whether to create a home EFS file system for the domain. Defaults to `Enabled`. Set to `Disabled` to skip EFS creation and reduce domain creation time. You can enable EFS later by calling `UpdateDomain`.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [HomeEfsFileSystemKmsKeyId](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-HomeEfsFileSystemKmsKeyId"></a>
 *This parameter has been deprecated.*
Use `KmsKeyId`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** [KmsKeyId](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-KmsKeyId"></a>
SageMaker AI uses AWS KMS to encrypt EFS and EBS volumes attached to the domain with an AWS managed key by default. For more control, specify a customer managed key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** [SubnetIds](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-SubnetIds"></a>
The VPC subnets that the domain uses for communication.
The field is optional when the `AppNetworkAccessType` parameter is set to `PublicInternetOnly` for domains created from Amazon SageMaker Unified Studio.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** [TagPropagation](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-TagPropagation"></a>
Indicates whether custom tag propagation is supported for the domain. Defaults to `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Tags](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-Tags"></a>
Tags to associated with the Domain. Each tag consists of a key and an optional value. Tag keys must be unique per resource. Tags are searchable using the `Search` API.
Tags that you specify for the Domain are also added to all Apps that the Domain launches.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [VpcId](#API_CreateDomain_RequestSyntax) **   <a name="sagemaker-CreateDomain-request-VpcId"></a>
The ID of the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.
The field is optional when the `AppNetworkAccessType` parameter is set to `PublicInternetOnly` for domains created from Amazon SageMaker Unified Studio.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

## Response Syntax
<a name="API_CreateDomain_ResponseSyntax"></a>

```
{
   "DomainArn": "string",
   "DomainId": "string",
   "Url": "string"
}
```

## Response Elements
<a name="API_CreateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainArn](#API_CreateDomain_ResponseSyntax) **   <a name="sagemaker-CreateDomain-response-DomainArn"></a>
The Amazon Resource Name (ARN) of the created domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:domain/.*`

 ** [DomainId](#API_CreateDomain_ResponseSyntax) **   <a name="sagemaker-CreateDomain-response-DomainId"></a>
The ID of the created domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`

 ** [Url](#API_CreateDomain_ResponseSyntax) **   <a name="sagemaker-CreateDomain-response-Url"></a>
The URL to the created domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_CreateDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateDomain)
