---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuild.html
---

# StartBuild
<a name="API_StartBuild"></a>

Starts running a build with the settings defined in the project. These setting include: how to run a build, where to get the source code, which build environment to use, which build commands to run, and where to store the build output.

You can also start a build run by overriding some of the build settings in the project. The overrides only apply for that specific start build request. The settings in the project are unaltered.

## Request Syntax
<a name="API_StartBuild_RequestSyntax"></a>

```
{
   "artifactsOverride": {
      "artifactIdentifier": "{{string}}",
      "bucketOwnerAccess": "{{string}}",
      "encryptionDisabled": {{boolean}},
      "location": "{{string}}",
      "name": "{{string}}",
      "namespaceType": "{{string}}",
      "overrideArtifactName": {{boolean}},
      "packaging": "{{string}}",
      "path": "{{string}}",
      "type": "{{string}}"
   },
   "autoRetryLimitOverride": {{number}},
   "buildspecOverride": "{{string}}",
   "buildStatusConfigOverride": {
      "context": "{{string}}",
      "targetUrl": "{{string}}"
   },
   "cacheOverride": {
      "cacheNamespace": "{{string}}",
      "location": "{{string}}",
      "modes": [ "{{string}}" ],
      "type": "{{string}}"
   },
   "certificateOverride": "{{string}}",
   "computeTypeOverride": "{{string}}",
   "debugSessionEnabled": {{boolean}},
   "encryptionKeyOverride": "{{string}}",
   "environmentTypeOverride": "{{string}}",
   "environmentVariablesOverride": [
      {
         "name": "{{string}}",
         "type": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "fleetOverride": {
      "fleetArn": "{{string}}"
   },
   "gitCloneDepthOverride": {{number}},
   "gitSubmodulesConfigOverride": {
      "fetchSubmodules": {{boolean}}
   },
   "hostKernelOverride": "{{string}}",
   "idempotencyToken": "{{string}}",
   "imageOverride": "{{string}}",
   "imagePullCredentialsTypeOverride": "{{string}}",
   "insecureSslOverride": {{boolean}},
   "logsConfigOverride": {
      "cloudWatchLogs": {
         "groupName": "{{string}}",
         "status": "{{string}}",
         "streamName": "{{string}}"
      },
      "s3Logs": {
         "bucketOwnerAccess": "{{string}}",
         "encryptionDisabled": {{boolean}},
         "location": "{{string}}",
         "status": "{{string}}"
      }
   },
   "privilegedModeOverride": {{boolean}},
   "projectName": "{{string}}",
   "queuedTimeoutInMinutesOverride": {{number}},
   "registryCredentialOverride": {
      "credential": "{{string}}",
      "credentialProvider": "{{string}}"
   },
   "reportBuildStatusOverride": {{boolean}},
   "secondaryArtifactsOverride": [
      {
         "artifactIdentifier": "{{string}}",
         "bucketOwnerAccess": "{{string}}",
         "encryptionDisabled": {{boolean}},
         "location": "{{string}}",
         "name": "{{string}}",
         "namespaceType": "{{string}}",
         "overrideArtifactName": {{boolean}},
         "packaging": "{{string}}",
         "path": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "secondarySourcesOverride": [
      {
         "auth": {
            "resource": "{{string}}",
            "type": "{{string}}"
         },
         "buildspec": "{{string}}",
         "buildStatusConfig": {
            "context": "{{string}}",
            "targetUrl": "{{string}}"
         },
         "gitCloneDepth": {{number}},
         "gitSubmodulesConfig": {
            "fetchSubmodules": {{boolean}}
         },
         "insecureSsl": {{boolean}},
         "location": "{{string}}",
         "reportBuildStatus": {{boolean}},
         "sourceIdentifier": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "secondarySourcesVersionOverride": [
      {
         "sourceIdentifier": "{{string}}",
         "sourceVersion": "{{string}}"
      }
   ],
   "serviceRoleOverride": "{{string}}",
   "sourceAuthOverride": {
      "resource": "{{string}}",
      "type": "{{string}}"
   },
   "sourceLocationOverride": "{{string}}",
   "sourceTypeOverride": "{{string}}",
   "sourceVersion": "{{string}}",
   "timeoutInMinutesOverride": {{number}}
}
```

## Request Parameters
<a name="API_StartBuild_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [projectName](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-projectName"></a>
The name of the AWS CodeBuild build project to start running a build.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [artifactsOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-artifactsOverride"></a>
Build output artifact settings that override, for this build only, the latest ones already defined in the build project.
Type: [ProjectArtifacts](API_ProjectArtifacts.md) object
Required: No

 ** [autoRetryLimitOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-autoRetryLimitOverride"></a>
The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry your build for up to 2 additional times.
Type: Integer
Required: No

 ** [buildspecOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-buildspecOverride"></a>
A buildspec file declaration that overrides the latest one defined in the build project, for this build only. The buildspec defined on the project is not changed.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml`). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage).
Since this property allows you to change the build commands that will run in the container, you should note that an IAM principal with the ability to call this API and set this parameter can override the default settings. Moreover, we encourage that you use a trustworthy buildspec location like a file in your source repository or a Amazon S3 bucket. Alternatively, you can restrict overrides to the buildspec by using a condition key: [Prevent unauthorized modifications to project buildspec](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html#action-context-keys-example-overridebuildspec.html).
Type: String
Required: No

 ** [buildStatusConfigOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-buildStatusConfigOverride"></a>
Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is `GITHUB`, `GITHUB_ENTERPRISE`, or `BITBUCKET`.
Type: [BuildStatusConfig](API_BuildStatusConfig.md) object
Required: No

 ** [cacheOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-cacheOverride"></a>
A ProjectCache object specified for this build that overrides the one defined in the build project.
Type: [ProjectCache](API_ProjectCache.md) object
Required: No

 ** [certificateOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-certificateOverride"></a>
The name of a certificate for this build that overrides the one specified in the build project.
Type: String
Required: No

 ** [computeTypeOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-computeTypeOverride"></a>
The name of a compute type for this build that overrides the one specified in the build project.
Type: String
Valid Values: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE | BUILD_GENERAL1_XLARGE | BUILD_GENERAL1_2XLARGE | BUILD_LAMBDA_1GB | BUILD_LAMBDA_2GB | BUILD_LAMBDA_4GB | BUILD_LAMBDA_8GB | BUILD_LAMBDA_10GB | ATTRIBUTE_BASED_COMPUTE | CUSTOM_INSTANCE_TYPE`
Required: No

 ** [debugSessionEnabled](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-debugSessionEnabled"></a>
Specifies if session debugging is enabled for this build. For more information, see [Viewing a running build in Session Manager](https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html).
Type: Boolean
Required: No

 ** [encryptionKeyOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-encryptionKeyOverride"></a>
The AWS Key Management Service customer master key (CMK) that overrides the one specified in the build project. The CMK key encrypts the build output artifacts.
 You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format `alias/<alias-name>`).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [environmentTypeOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-environmentTypeOverride"></a>
A container type for this build that overrides the one specified in the build project.
Type: String
Valid Values: `WINDOWS_CONTAINER | LINUX_CONTAINER | LINUX_GPU_CONTAINER | ARM_CONTAINER | WINDOWS_SERVER_2019_CONTAINER | WINDOWS_SERVER_2022_CONTAINER | LINUX_LAMBDA_CONTAINER | ARM_LAMBDA_CONTAINER | LINUX_EC2 | ARM_EC2 | WINDOWS_EC2 | MAC_ARM`
Required: No

 ** [environmentVariablesOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-environmentVariablesOverride"></a>
A set of environment variables that overrides, for this build only, the latest ones already defined in the build project.
Type: Array of [EnvironmentVariable](API_EnvironmentVariable.md) objects
Required: No

 ** [fleetOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-fleetOverride"></a>
A ProjectFleet object specified for this build that overrides the one defined in the build project.
Type: [ProjectFleet](API_ProjectFleet.md) object
Required: No

 ** [gitCloneDepthOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-gitCloneDepthOverride"></a>
The user-defined depth of history, with a minimum value of 0, that overrides, for this build only, any previous depth of history defined in the build project.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [gitSubmodulesConfigOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-gitSubmodulesConfigOverride"></a>
 Information about the Git submodules configuration for this build of an AWS CodeBuild build project.
Type: [GitSubmodulesConfig](API_GitSubmodulesConfig.md) object
Required: No

 ** [hostKernelOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-hostKernelOverride"></a>
The host operating system kernel for this build that overrides the one specified in the build project.
Type: String
Valid Values: `LINUX_KERNEL_4 | LINUX_KERNEL_6 | LINUX_KERNEL_LATEST`
Required: No

 ** [idempotencyToken](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-idempotencyToken"></a>
A unique, case sensitive identifier you provide to ensure the idempotency of the StartBuild request. The token is included in the StartBuild request and is valid for 5 minutes. If you repeat the StartBuild request with the same token, but change a parameter, AWS CodeBuild returns a parameter mismatch error.
Type: String
Required: No

 ** [imageOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-imageOverride"></a>
The name of an image for this build that overrides the one specified in the build project.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [imagePullCredentialsTypeOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-imagePullCredentialsTypeOverride"></a>
The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:
CODEBUILD
Specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild's service principal.
SERVICE\_ROLE
Specifies that AWS CodeBuild uses your build project's service role.
When using a cross-account or private registry image, you must use `SERVICE_ROLE` credentials. When using an AWS CodeBuild curated image, you must use `CODEBUILD` credentials.
Type: String
Valid Values: `CODEBUILD | SERVICE_ROLE`
Required: No

 ** [insecureSslOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-insecureSslOverride"></a>
Enable this flag to override the insecure SSL setting that is specified in the build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the build's source is GitHub Enterprise.
Type: Boolean
Required: No

 ** [logsConfigOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-logsConfigOverride"></a>
 Log settings for this build that override the log settings defined in the build project.
Type: [LogsConfig](API_LogsConfig.md) object
Required: No

 ** [privilegedModeOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-privilegedModeOverride"></a>
Enable this flag to override privileged mode in the build project.
Type: Boolean
Required: No

 ** [queuedTimeoutInMinutesOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-queuedTimeoutInMinutesOverride"></a>
 The number of minutes a build is allowed to be queued before it times out.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 480.
Required: No

 ** [registryCredentialOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-registryCredentialOverride"></a>
 The credentials for access to a private registry.
Type: [RegistryCredential](API_RegistryCredential.md) object
Required: No

 ** [reportBuildStatusOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-reportBuildStatusOverride"></a>
 Set to true to report to your source provider the status of a build's start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket, an `invalidInputException` is thrown.
To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) in the * AWS CodeBuild User Guide*.
 The status of a build triggered by a webhook is always reported to your source provider.
Type: Boolean
Required: No

 ** [secondaryArtifactsOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-secondaryArtifactsOverride"></a>
 An array of `ProjectArtifacts` objects.
Type: Array of [ProjectArtifacts](API_ProjectArtifacts.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [secondarySourcesOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-secondarySourcesOverride"></a>
 An array of `ProjectSource` objects.
Type: Array of [ProjectSource](API_ProjectSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [secondarySourcesVersionOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-secondarySourcesVersionOverride"></a>
 An array of `ProjectSourceVersion` objects that specify one or more versions of the project's secondary sources to be used for this build only.
Type: Array of [ProjectSourceVersion](API_ProjectSourceVersion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [serviceRoleOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-serviceRoleOverride"></a>
The name of a service role for this build that overrides the one specified in the build project.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [sourceAuthOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-sourceAuthOverride"></a>
An authorization type for this build that overrides the one defined in the build project. This override applies only if the build project's source is BitBucket, GitHub, GitLab, or GitLab Self Managed.
Type: [SourceAuth](API_SourceAuth.md) object
Required: No

 ** [sourceLocationOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-sourceLocationOverride"></a>
A location that overrides, for this build, the source location for the one defined in the build project.
Type: String
Required: No

 ** [sourceTypeOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-sourceTypeOverride"></a>
A source input type, for this build, that overrides the source input defined in the build project.
Type: String
Valid Values: `CODECOMMIT | CODEPIPELINE | GITHUB | GITLAB | GITLAB_SELF_MANAGED | S3 | BITBUCKET | GITHUB_ENTERPRISE | NO_SOURCE`
Required: No

 ** [sourceVersion](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-sourceVersion"></a>
The version of the build input to be built, for this build only. If not specified, the latest version is used. If specified, the contents depends on the source provider:
CodeCommit
The commit ID, branch, or Git tag to use.
GitHub
The commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25`). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
GitLab
The commit ID, branch, or Git tag to use.
Bitbucket
The commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
Amazon S3
The version ID of the object that represents the build input ZIP file to use.
If `sourceVersion` is specified at the project level, then this `sourceVersion` (at the build level) takes precedence.
For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the * AWS CodeBuild User Guide*.
Type: String
Required: No

 ** [timeoutInMinutesOverride](#API_StartBuild_RequestSyntax) **   <a name="CodeBuild-StartBuild-request-timeoutInMinutesOverride"></a>
The number of build timeout minutes, from 5 to 2160 (36 hours), that overrides, for this build only, the latest setting already defined in the build project.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 2160.
Required: No

## Response Syntax
<a name="API_StartBuild_ResponseSyntax"></a>

```
{
   "build": {
      "arn": "string",
      "artifacts": {
         "artifactIdentifier": "string",
         "bucketOwnerAccess": "string",
         "encryptionDisabled": boolean,
         "location": "string",
         "md5sum": "string",
         "overrideArtifactName": boolean,
         "sha256sum": "string"
      },
      "autoRetryConfig": {
         "autoRetryLimit": number,
         "autoRetryNumber": number,
         "nextAutoRetry": "string",
         "previousAutoRetry": "string"
      },
      "buildBatchArn": "string",
      "buildComplete": boolean,
      "buildNumber": number,
      "buildStatus": "string",
      "cache": {
         "cacheNamespace": "string",
         "location": "string",
         "modes": [ "string" ],
         "type": "string"
      },
      "currentPhase": "string",
      "debugSession": {
         "sessionEnabled": boolean,
         "sessionTarget": "string"
      },
      "encryptionKey": "string",
      "endTime": number,
      "environment": {
         "certificate": "string",
         "computeConfiguration": {
            "disk": number,
            "instanceType": "string",
            "machineType": "string",
            "memory": number,
            "vCpu": number
         },
         "computeType": "string",
         "dockerServer": {
            "computeType": "string",
            "securityGroupIds": [ "string" ],
            "status": {
               "message": "string",
               "status": "string"
            }
         },
         "environmentVariables": [
            {
               "name": "string",
               "type": "string",
               "value": "string"
            }
         ],
         "fleet": {
            "fleetArn": "string"
         },
         "hostKernel": "string",
         "image": "string",
         "imagePullCredentialsType": "string",
         "privilegedMode": boolean,
         "registryCredential": {
            "credential": "string",
            "credentialProvider": "string"
         },
         "type": "string"
      },
      "exportedEnvironmentVariables": [
         {
            "name": "string",
            "value": "string"
         }
      ],
      "fileSystemLocations": [
         {
            "identifier": "string",
            "location": "string",
            "mountOptions": "string",
            "mountPoint": "string",
            "type": "string"
         }
      ],
      "id": "string",
      "initiator": "string",
      "logs": {
         "cloudWatchLogs": {
            "groupName": "string",
            "status": "string",
            "streamName": "string"
         },
         "cloudWatchLogsArn": "string",
         "deepLink": "string",
         "groupName": "string",
         "s3DeepLink": "string",
         "s3Logs": {
            "bucketOwnerAccess": "string",
            "encryptionDisabled": boolean,
            "location": "string",
            "status": "string"
         },
         "s3LogsArn": "string",
         "streamName": "string"
      },
      "networkInterface": {
         "networkInterfaceId": "string",
         "subnetId": "string"
      },
      "phases": [
         {
            "contexts": [
               {
                  "message": "string",
                  "statusCode": "string"
               }
            ],
            "durationInSeconds": number,
            "endTime": number,
            "phaseStatus": "string",
            "phaseType": "string",
            "startTime": number
         }
      ],
      "projectName": "string",
      "queuedTimeoutInMinutes": number,
      "reportArns": [ "string" ],
      "resolvedSourceVersion": "string",
      "secondaryArtifacts": [
         {
            "artifactIdentifier": "string",
            "bucketOwnerAccess": "string",
            "encryptionDisabled": boolean,
            "location": "string",
            "md5sum": "string",
            "overrideArtifactName": boolean,
            "sha256sum": "string"
         }
      ],
      "secondarySources": [
         {
            "auth": {
               "resource": "string",
               "type": "string"
            },
            "buildspec": "string",
            "buildStatusConfig": {
               "context": "string",
               "targetUrl": "string"
            },
            "gitCloneDepth": number,
            "gitSubmodulesConfig": {
               "fetchSubmodules": boolean
            },
            "insecureSsl": boolean,
            "location": "string",
            "reportBuildStatus": boolean,
            "sourceIdentifier": "string",
            "type": "string"
         }
      ],
      "secondarySourceVersions": [
         {
            "sourceIdentifier": "string",
            "sourceVersion": "string"
         }
      ],
      "serviceRole": "string",
      "source": {
         "auth": {
            "resource": "string",
            "type": "string"
         },
         "buildspec": "string",
         "buildStatusConfig": {
            "context": "string",
            "targetUrl": "string"
         },
         "gitCloneDepth": number,
         "gitSubmodulesConfig": {
            "fetchSubmodules": boolean
         },
         "insecureSsl": boolean,
         "location": "string",
         "reportBuildStatus": boolean,
         "sourceIdentifier": "string",
         "type": "string"
      },
      "sourceVersion": "string",
      "startTime": number,
      "timeoutInMinutes": number,
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnets": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_StartBuild_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [build](#API_StartBuild_ResponseSyntax) **   <a name="CodeBuild-StartBuild-response-build"></a>
Information about the build to be run.
Type: [Build](API_Build.md) object

## Errors
<a name="API_StartBuild_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountLimitExceededException **
An AWS service limit was exceeded for the calling AWS account.
HTTP Status Code: 400

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_StartBuild_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/StartBuild)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/StartBuild)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
