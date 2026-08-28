---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuildBatch.html
---

# StartBuildBatch
<a name="API_StartBuildBatch"></a>

Starts a batch build for a project.

## Request Syntax
<a name="API_StartBuildBatch_RequestSyntax"></a>

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
   "buildBatchConfigOverride": {
      "batchReportMode": "{{string}}",
      "combineArtifacts": {{boolean}},
      "restrictions": {
         "computeTypesAllowed": [ "{{string}}" ],
         "fleetsAllowed": [ "{{string}}" ],
         "maximumBuildsAllowed": {{number}}
      },
      "serviceRole": "{{string}}",
      "timeoutInMins": {{number}}
   },
   "buildspecOverride": "{{string}}",
   "buildTimeoutInMinutesOverride": {{number}},
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
   "gitCloneDepthOverride": {{number}},
   "gitSubmodulesConfigOverride": {
      "fetchSubmodules": {{boolean}}
   },
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
   "reportBuildBatchStatusOverride": {{boolean}},
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
   "sourceVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_StartBuildBatch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [projectName](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-projectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [artifactsOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-artifactsOverride"></a>
An array of `ProjectArtifacts` objects that contains information about the build output artifact overrides for the build project.
Type: [ProjectArtifacts](API_ProjectArtifacts.md) object
Required: No

 ** [buildBatchConfigOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-buildBatchConfigOverride"></a>
A `BuildBatchConfigOverride` object that contains batch build configuration overrides.
Type: [ProjectBuildBatchConfig](API_ProjectBuildBatchConfig.md) object
Required: No

 ** [buildspecOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-buildspecOverride"></a>
A buildspec file declaration that overrides, for this build only, the latest one already defined in the build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml`). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage).
Type: String
Required: No

 ** [buildTimeoutInMinutesOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-buildTimeoutInMinutesOverride"></a>
Overrides the build timeout specified in the batch build project.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 2160.
Required: No

 ** [cacheOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-cacheOverride"></a>
A `ProjectCache` object that specifies cache overrides.
Type: [ProjectCache](API_ProjectCache.md) object
Required: No

 ** [certificateOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-certificateOverride"></a>
The name of a certificate for this batch build that overrides the one specified in the batch build project.
Type: String
Required: No

 ** [computeTypeOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-computeTypeOverride"></a>
The name of a compute type for this batch build that overrides the one specified in the batch build project.
Type: String
Valid Values: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE | BUILD_GENERAL1_XLARGE | BUILD_GENERAL1_2XLARGE | BUILD_LAMBDA_1GB | BUILD_LAMBDA_2GB | BUILD_LAMBDA_4GB | BUILD_LAMBDA_8GB | BUILD_LAMBDA_10GB | ATTRIBUTE_BASED_COMPUTE | CUSTOM_INSTANCE_TYPE`
Required: No

 ** [debugSessionEnabled](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-debugSessionEnabled"></a>
Specifies if session debugging is enabled for this batch build. For more information, see [Viewing a running build in Session Manager](https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html). Batch session debugging is not supported for matrix batch builds.
Type: Boolean
Required: No

 ** [encryptionKeyOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-encryptionKeyOverride"></a>
The AWS Key Management Service customer master key (CMK) that overrides the one specified in the batch build project. The CMK key encrypts the build output artifacts.
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format `alias/<alias-name>`).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [environmentTypeOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-environmentTypeOverride"></a>
A container type for this batch build that overrides the one specified in the batch build project.
Type: String
Valid Values: `WINDOWS_CONTAINER | LINUX_CONTAINER | LINUX_GPU_CONTAINER | ARM_CONTAINER | WINDOWS_SERVER_2019_CONTAINER | WINDOWS_SERVER_2022_CONTAINER | LINUX_LAMBDA_CONTAINER | ARM_LAMBDA_CONTAINER | LINUX_EC2 | ARM_EC2 | WINDOWS_EC2 | MAC_ARM`
Required: No

 ** [environmentVariablesOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-environmentVariablesOverride"></a>
An array of `EnvironmentVariable` objects that override, or add to, the environment variables defined in the batch build project.
Type: Array of [EnvironmentVariable](API_EnvironmentVariable.md) objects
Required: No

 ** [gitCloneDepthOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-gitCloneDepthOverride"></a>
The user-defined depth of history, with a minimum value of 0, that overrides, for this batch build only, any previous depth of history defined in the batch build project.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [gitSubmodulesConfigOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-gitSubmodulesConfigOverride"></a>
A `GitSubmodulesConfig` object that overrides the Git submodules configuration for this batch build.
Type: [GitSubmodulesConfig](API_GitSubmodulesConfig.md) object
Required: No

 ** [idempotencyToken](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-idempotencyToken"></a>
A unique, case sensitive identifier you provide to ensure the idempotency of the `StartBuildBatch` request. The token is included in the `StartBuildBatch` request and is valid for five minutes. If you repeat the `StartBuildBatch` request with the same token, but change a parameter, AWS CodeBuild returns a parameter mismatch error.
Type: String
Required: No

 ** [imageOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-imageOverride"></a>
The name of an image for this batch build that overrides the one specified in the batch build project.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [imagePullCredentialsTypeOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-imagePullCredentialsTypeOverride"></a>
The type of credentials AWS CodeBuild uses to pull images in your batch build. There are two valid values:
CODEBUILD
Specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild's service principal.
SERVICE\_ROLE
Specifies that AWS CodeBuild uses your build project's service role.
When using a cross-account or private registry image, you must use `SERVICE_ROLE` credentials. When using an AWS CodeBuild curated image, you must use `CODEBUILD` credentials.
Type: String
Valid Values: `CODEBUILD | SERVICE_ROLE`
Required: No

 ** [insecureSslOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-insecureSslOverride"></a>
Enable this flag to override the insecure SSL setting that is specified in the batch build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the build's source is GitHub Enterprise.
Type: Boolean
Required: No

 ** [logsConfigOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-logsConfigOverride"></a>
A `LogsConfig` object that override the log settings defined in the batch build project.
Type: [LogsConfig](API_LogsConfig.md) object
Required: No

 ** [privilegedModeOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-privilegedModeOverride"></a>
Enable this flag to override privileged mode in the batch build project.
Type: Boolean
Required: No

 ** [queuedTimeoutInMinutesOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-queuedTimeoutInMinutesOverride"></a>
The number of minutes a batch build is allowed to be queued before it times out.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 480.
Required: No

 ** [registryCredentialOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-registryCredentialOverride"></a>
A `RegistryCredential` object that overrides credentials for access to a private registry.
Type: [RegistryCredential](API_RegistryCredential.md) object
Required: No

 ** [reportBuildBatchStatusOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-reportBuildBatchStatusOverride"></a>
Set to `true` to report to your source provider the status of a batch build's start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, or Bitbucket, an `invalidInputException` is thrown.
The status of a build triggered by a webhook is always reported to your source provider.
Type: Boolean
Required: No

 ** [secondaryArtifactsOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-secondaryArtifactsOverride"></a>
An array of `ProjectArtifacts` objects that override the secondary artifacts defined in the batch build project.
Type: Array of [ProjectArtifacts](API_ProjectArtifacts.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [secondarySourcesOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-secondarySourcesOverride"></a>
An array of `ProjectSource` objects that override the secondary sources defined in the batch build project.
Type: Array of [ProjectSource](API_ProjectSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [secondarySourcesVersionOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-secondarySourcesVersionOverride"></a>
An array of `ProjectSourceVersion` objects that override the secondary source versions in the batch build project.
Type: Array of [ProjectSourceVersion](API_ProjectSourceVersion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [serviceRoleOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-serviceRoleOverride"></a>
The name of a service role for this batch build that overrides the one specified in the batch build project.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [sourceAuthOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-sourceAuthOverride"></a>
A `SourceAuth` object that overrides the one defined in the batch build project. This override applies only if the build project's source is BitBucket or GitHub.
Type: [SourceAuth](API_SourceAuth.md) object
Required: No

 ** [sourceLocationOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-sourceLocationOverride"></a>
A location that overrides, for this batch build, the source location defined in the batch build project.
Type: String
Required: No

 ** [sourceTypeOverride](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-sourceTypeOverride"></a>
The source input type that overrides the source input defined in the batch build project.
Type: String
Valid Values: `CODECOMMIT | CODEPIPELINE | GITHUB | GITLAB | GITLAB_SELF_MANAGED | S3 | BITBUCKET | GITHUB_ENTERPRISE | NO_SOURCE`
Required: No

 ** [sourceVersion](#API_StartBuildBatch_RequestSyntax) **   <a name="CodeBuild-StartBuildBatch-request-sourceVersion"></a>
The version of the batch build input to be built, for this build only. If not specified, the latest version is used. If specified, the contents depends on the source provider:
CodeCommit
The commit ID, branch, or Git tag to use.
GitHub
The commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25`). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
Bitbucket
The commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
Amazon S3
The version ID of the object that represents the build input ZIP file to use.
If `sourceVersion` is specified at the project level, then this `sourceVersion` (at the build level) takes precedence.
For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the * AWS CodeBuild User Guide*.
Type: String
Required: No

## Response Syntax
<a name="API_StartBuildBatch_ResponseSyntax"></a>

```
{
   "buildBatch": {
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
      "buildBatchConfig": {
         "batchReportMode": "string",
         "combineArtifacts": boolean,
         "restrictions": {
            "computeTypesAllowed": [ "string" ],
            "fleetsAllowed": [ "string" ],
            "maximumBuildsAllowed": number
         },
         "serviceRole": "string",
         "timeoutInMins": number
      },
      "buildBatchNumber": number,
      "buildBatchStatus": "string",
      "buildGroups": [
         {
            "currentBuildSummary": {
               "arn": "string",
               "buildStatus": "string",
               "primaryArtifact": {
                  "identifier": "string",
                  "location": "string",
                  "type": "string"
               },
               "requestedOn": number,
               "secondaryArtifacts": [
                  {
                     "identifier": "string",
                     "location": "string",
                     "type": "string"
                  }
               ]
            },
            "dependsOn": [ "string" ],
            "identifier": "string",
            "ignoreFailure": boolean,
            "priorBuildSummaryList": [
               {
                  "arn": "string",
                  "buildStatus": "string",
                  "primaryArtifact": {
                     "identifier": "string",
                     "location": "string",
                     "type": "string"
                  },
                  "requestedOn": number,
                  "secondaryArtifacts": [
                     {
                        "identifier": "string",
                        "location": "string",
                        "type": "string"
                     }
                  ]
               }
            ]
         }
      ],
      "buildTimeoutInMinutes": number,
      "cache": {
         "cacheNamespace": "string",
         "location": "string",
         "modes": [ "string" ],
         "type": "string"
      },
      "complete": boolean,
      "currentPhase": "string",
      "debugSessionEnabled": boolean,
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
      "logConfig": {
         "cloudWatchLogs": {
            "groupName": "string",
            "status": "string",
            "streamName": "string"
         },
         "s3Logs": {
            "bucketOwnerAccess": "string",
            "encryptionDisabled": boolean,
            "location": "string",
            "status": "string"
         }
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
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnets": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_StartBuildBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buildBatch](#API_StartBuildBatch_ResponseSyntax) **   <a name="CodeBuild-StartBuildBatch-response-buildBatch"></a>
A `BuildBatch` object that contains information about the batch build.
Type: [BuildBatch](API_BuildBatch.md) object

## Errors
<a name="API_StartBuildBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_StartBuildBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/StartBuildBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/StartBuildBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
