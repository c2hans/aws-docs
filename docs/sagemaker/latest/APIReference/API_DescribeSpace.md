---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeSpace.html
---

# DescribeSpace
<a name="API_DescribeSpace"></a>

Describes the space.

## Request Syntax
<a name="API_DescribeSpace_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "SpaceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSpace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_DescribeSpace_RequestSyntax) **   <a name="sagemaker-DescribeSpace-request-DomainId"></a>
The ID of the associated domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: Yes

 ** [SpaceName](#API_DescribeSpace_RequestSyntax) **   <a name="sagemaker-DescribeSpace-request-SpaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeSpace_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "DomainId": "string",
   "FailureReason": "string",
   "HomeEfsFileSystemUid": "string",
   "LastModifiedTime": number,
   "OwnershipSettings": {
      "OwnerUserProfileName": "string"
   },
   "SpaceArn": "string",
   "SpaceDisplayName": "string",
   "SpaceName": "string",
   "SpaceSettings": {
      "AppType": "string",
      "CodeEditorAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": number
            }
         },
         "DefaultResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         }
      },
      "CustomFileSystems": [
         { ... }
      ],
      "JupyterLabAppSettings": {
         "AppLifecycleManagement": {
            "IdleSettings": {
               "IdleTimeoutInMinutes": number
            }
         },
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
         }
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
      "RemoteAccess": "string",
      "SpaceManagedResources": "string",
      "SpaceStorageSettings": {
         "EbsStorageSettings": {
            "EbsVolumeSizeInGb": number
         }
      }
   },
   "SpaceSharingSettings": {
      "SharingType": "string"
   },
   "Status": "string",
   "Url": "string"
}
```

## Response Elements
<a name="API_DescribeSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-CreationTime"></a>
The creation time.
Type: Timestamp

 ** [DomainId](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-DomainId"></a>
The ID of the associated domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`

 ** [FailureReason](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-FailureReason"></a>
The failure reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [HomeEfsFileSystemUid](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-HomeEfsFileSystemUid"></a>
The ID of the space's profile in the Amazon EFS volume.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Pattern: `\d+`

 ** [LastModifiedTime](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-LastModifiedTime"></a>
The last modified time.
Type: Timestamp

 ** [OwnershipSettings](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-OwnershipSettings"></a>
The collection of ownership settings for a space.
Type: [OwnershipSettings](API_OwnershipSettings.md) object

 ** [SpaceArn](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-SpaceArn"></a>
The space's Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:space/.*`

 ** [SpaceDisplayName](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-SpaceDisplayName"></a>
The name of the space that appears in the Amazon SageMaker Studio UI.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!\s*$).+`

 ** [SpaceName](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-SpaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [SpaceSettings](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-SpaceSettings"></a>
A collection of space settings.
Type: [SpaceSettings](API_SpaceSettings.md) object

 ** [SpaceSharingSettings](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-SpaceSharingSettings"></a>
The collection of space sharing settings for a space.
Type: [SpaceSharingSettings](API_SpaceSharingSettings.md) object

 ** [Status](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-Status"></a>
The status.
Type: String
Valid Values: `Deleting | Failed | InService | Pending | Updating | Update_Failed | Delete_Failed`

 ** [Url](#API_DescribeSpace_ResponseSyntax) **   <a name="sagemaker-DescribeSpace-response-Url"></a>
Returns the URL of the space. If the space is created with AWS IAM Identity Center (Successor to AWS Single Sign-On) authentication, users can navigate to the URL after appending the respective redirect parameter for the application type to be federated through AWS IAM Identity Center.
The following application types are supported:
+ Studio Classic: `&redirect=JupyterServer`
+ JupyterLab: `&redirect=JupyterLab`
+ Code Editor, based on Code-OSS, Visual Studio Code - Open Source: `&redirect=CodeEditor`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_DescribeSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeSpace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
