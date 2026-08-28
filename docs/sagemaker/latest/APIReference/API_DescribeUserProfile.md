---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeUserProfile.html
---

# DescribeUserProfile
<a name="API_DescribeUserProfile"></a>

Describes a user profile. For more information, see `CreateUserProfile`.

## Request Syntax
<a name="API_DescribeUserProfile_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "UserProfileName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUserProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_DescribeUserProfile_RequestSyntax) **   <a name="sagemaker-DescribeUserProfile-request-DomainId"></a>
The domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [UserProfileName](#API_DescribeUserProfile_RequestSyntax) **   <a name="sagemaker-DescribeUserProfile-request-UserProfileName"></a>
The user profile name. This value is not case sensitive.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeUserProfile_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "DomainId": "string",
   "FailureReason": "string",
   "HomeEfsFileSystemUid": "string",
   "LastModifiedTime": number,
   "SingleSignOnUserIdentifier": "string",
   "SingleSignOnUserValue": "string",
   "Status": "string",
   "UserProfileArn": "string",
   "UserProfileName": "string",
   "UserSettings": {
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
   }
}
```

## Response Elements
<a name="API_DescribeUserProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-CreationTime"></a>
The creation time.
Type: Timestamp

 ** [DomainId](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-DomainId"></a>
The ID of the domain that contains the profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`

 ** [FailureReason](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-FailureReason"></a>
The failure reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [HomeEfsFileSystemUid](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-HomeEfsFileSystemUid"></a>
The ID of the user's profile in the Amazon Elastic File System volume.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `\d+`

 ** [LastModifiedTime](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-LastModifiedTime"></a>
The last modified time.
Type: Timestamp

 ** [SingleSignOnUserIdentifier](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-SingleSignOnUserIdentifier"></a>
The IAM Identity Center user identifier.
Type: String
Pattern: `UserName`

 ** [SingleSignOnUserValue](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-SingleSignOnUserValue"></a>
The IAM Identity Center user value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [Status](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-Status"></a>
The status.
Type: String
Valid Values: `Deleting | Failed | InService | Pending | Updating | Update_Failed | Delete_Failed`

 ** [UserProfileArn](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-UserProfileArn"></a>
The user profile Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:user-profile/.*`

 ** [UserProfileName](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-UserProfileName"></a>
The user profile name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [UserSettings](#API_DescribeUserProfile_ResponseSyntax) **   <a name="sagemaker-DescribeUserProfile-response-UserSettings"></a>
A collection of settings.
Type: [UserSettings](API_UserSettings.md) object

## Errors
<a name="API_DescribeUserProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeUserProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeUserProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeUserProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
