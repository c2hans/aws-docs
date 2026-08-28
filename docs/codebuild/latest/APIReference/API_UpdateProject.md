---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateProject.html
---

# UpdateProject
<a name="API_UpdateProject"></a>

Changes the settings of a build project.

## Request Syntax
<a name="API_UpdateProject_RequestSyntax"></a>

```
{
   "artifacts": {
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
   "autoRetryLimit": {{number}},
   "badgeEnabled": {{boolean}},
   "buildBatchConfig": {
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
   "cache": {
      "cacheNamespace": "{{string}}",
      "location": "{{string}}",
      "modes": [ "{{string}}" ],
      "type": "{{string}}"
   },
   "concurrentBuildLimit": {{number}},
   "description": "{{string}}",
   "encryptionKey": "{{string}}",
   "environment": {
      "certificate": "{{string}}",
      "computeConfiguration": {
         "disk": {{number}},
         "instanceType": "{{string}}",
         "machineType": "{{string}}",
         "memory": {{number}},
         "vCpu": {{number}}
      },
      "computeType": "{{string}}",
      "dockerServer": {
         "computeType": "{{string}}",
         "securityGroupIds": [ "{{string}}" ],
         "status": {
            "message": "{{string}}",
            "status": "{{string}}"
         }
      },
      "environmentVariables": [
         {
            "name": "{{string}}",
            "type": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "fleet": {
         "fleetArn": "{{string}}"
      },
      "hostKernel": "{{string}}",
      "image": "{{string}}",
      "imagePullCredentialsType": "{{string}}",
      "privilegedMode": {{boolean}},
      "registryCredential": {
         "credential": "{{string}}",
         "credentialProvider": "{{string}}"
      },
      "type": "{{string}}"
   },
   "fileSystemLocations": [
      {
         "identifier": "{{string}}",
         "location": "{{string}}",
         "mountOptions": "{{string}}",
         "mountPoint": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "logsConfig": {
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
   "name": "{{string}}",
   "queuedTimeoutInMinutes": {{number}},
   "secondaryArtifacts": [
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
   "secondarySources": [
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
   "secondarySourceVersions": [
      {
         "sourceIdentifier": "{{string}}",
         "sourceVersion": "{{string}}"
      }
   ],
   "serviceRole": "{{string}}",
   "source": {
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
   },
   "sourceVersion": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "timeoutInMinutes": {{number}},
   "vpcConfig": {
      "securityGroupIds": [ "{{string}}" ],
      "subnets": [ "{{string}}" ],
      "vpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [name](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-name"></a>
The name of the build project.
You cannot change a build project's name.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [artifacts](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-artifacts"></a>
Information to be changed about the build output artifacts for the build project.
Type: [ProjectArtifacts](API_ProjectArtifacts.md) object
Required: No

 ** [autoRetryLimit](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-autoRetryLimit"></a>
The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry your build for up to 2 additional times.
Type: Integer
Required: No

 ** [badgeEnabled](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-badgeEnabled"></a>
Set this to true to generate a publicly accessible URL for your project's build badge.
Type: Boolean
Required: No

 ** [buildBatchConfig](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-buildBatchConfig"></a>
Contains configuration information about a batch build project.
Type: [ProjectBuildBatchConfig](API_ProjectBuildBatchConfig.md) object
Required: No

 ** [cache](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-cache"></a>
Stores recently used information so that it can be quickly accessed at a later time.
Type: [ProjectCache](API_ProjectCache.md) object
Required: No

 ** [concurrentBuildLimit](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-concurrentBuildLimit"></a>
The maximum number of concurrent builds that are allowed for this project.
New builds are only started if the current number of builds is less than or equal to this limit. If the current build count meets this limit, new builds are throttled and are not run.
To remove this limit, set this value to -1.
Type: Integer
Required: No

 ** [description](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-description"></a>
A new or replacement description of the build project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [encryptionKey](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-encryptionKey"></a>
The AWS Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.
 You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format `alias/<alias-name>`).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [environment](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-environment"></a>
Information to be changed about the build environment for the build project.
Type: [ProjectEnvironment](API_ProjectEnvironment.md) object
Required: No

 ** [fileSystemLocations](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-fileSystemLocations"></a>
 An array of `ProjectFileSystemLocation` objects for a CodeBuild build project. A `ProjectFileSystemLocation` object specifies the `identifier`, `location`, `mountOptions`, `mountPoint`, and `type` of a file system created using Amazon Elastic File System.
Type: Array of [ProjectFileSystemLocation](API_ProjectFileSystemLocation.md) objects
Required: No

 ** [logsConfig](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-logsConfig"></a>
 Information about logs for the build project. A project can create logs in CloudWatch Logs, logs in an S3 bucket, or both.
Type: [LogsConfig](API_LogsConfig.md) object
Required: No

 ** [queuedTimeoutInMinutes](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-queuedTimeoutInMinutes"></a>
 The number of minutes a build is allowed to be queued before it times out.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 480.
Required: No

 ** [secondaryArtifacts](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-secondaryArtifacts"></a>
 An array of `ProjectArtifact` objects.
Type: Array of [ProjectArtifacts](API_ProjectArtifacts.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [secondarySources](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-secondarySources"></a>
 An array of `ProjectSource` objects.
Type: Array of [ProjectSource](API_ProjectSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [secondarySourceVersions](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-secondarySourceVersions"></a>
 An array of `ProjectSourceVersion` objects. If `secondarySourceVersions` is specified at the build level, then they take over these `secondarySourceVersions` (at the project level).
Type: Array of [ProjectSourceVersion](API_ProjectSourceVersion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** [serviceRole](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-serviceRole"></a>
The replacement ARN of the IAM role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [source](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-source"></a>
Information to be changed about the build input source code for the build project.
Type: [ProjectSource](API_ProjectSource.md) object
Required: No

 ** [sourceVersion](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-sourceVersion"></a>
 A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:
+ For CodeCommit: the commit ID, branch, or Git tag to use.
+ For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25`). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
+ For GitLab: the commit ID, branch, or Git tag to use.
+ For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
+ For Amazon S3: the version ID of the object that represents the build input ZIP file to use.
 If `sourceVersion` is specified at the build level, then that version takes precedence over this `sourceVersion` (at the project level).
 For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the * AWS CodeBuild User Guide*.
Type: String
Required: No

 ** [tags](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-tags"></a>
An updated list of tag key and value pairs associated with this build project.
These tags are available for use by AWS services that support AWS CodeBuild build project tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [timeoutInMinutes](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-timeoutInMinutes"></a>
The replacement value in minutes, from 5 to 2160 (36 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 2160.
Required: No

 ** [vpcConfig](#API_UpdateProject_RequestSyntax) **   <a name="CodeBuild-UpdateProject-request-vpcConfig"></a>
VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateProject_ResponseSyntax"></a>

```
{
   "project": {
      "arn": "string",
      "artifacts": {
         "artifactIdentifier": "string",
         "bucketOwnerAccess": "string",
         "encryptionDisabled": boolean,
         "location": "string",
         "name": "string",
         "namespaceType": "string",
         "overrideArtifactName": boolean,
         "packaging": "string",
         "path": "string",
         "type": "string"
      },
      "autoRetryLimit": number,
      "badge": {
         "badgeEnabled": boolean,
         "badgeRequestUrl": "string"
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
      "cache": {
         "cacheNamespace": "string",
         "location": "string",
         "modes": [ "string" ],
         "type": "string"
      },
      "concurrentBuildLimit": number,
      "created": number,
      "description": "string",
      "encryptionKey": "string",
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
      "lastModified": number,
      "logsConfig": {
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
      "name": "string",
      "projectVisibility": "string",
      "publicProjectAlias": "string",
      "queuedTimeoutInMinutes": number,
      "resourceAccessRole": "string",
      "secondaryArtifacts": [
         {
            "artifactIdentifier": "string",
            "bucketOwnerAccess": "string",
            "encryptionDisabled": boolean,
            "location": "string",
            "name": "string",
            "namespaceType": "string",
            "overrideArtifactName": boolean,
            "packaging": "string",
            "path": "string",
            "type": "string"
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
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "timeoutInMinutes": number,
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnets": [ "string" ],
         "vpcId": "string"
      },
      "webhook": {
         "branchFilter": "string",
         "buildType": "string",
         "filterGroups": [
            [
               {
                  "excludeMatchedPattern": boolean,
                  "pattern": "string",
                  "type": "string"
               }
            ]
         ],
         "lastModifiedSecret": number,
         "manualCreation": boolean,
         "payloadUrl": "string",
         "pullRequestBuildPolicy": {
            "approverRoles": [ "string" ],
            "requiresCommentApproval": "string"
         },
         "scopeConfiguration": {
            "domain": "string",
            "name": "string",
            "scope": "string"
         },
         "secret": "string",
         "status": "string",
         "statusMessage": "string",
         "url": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [project](#API_UpdateProject_ResponseSyntax) **   <a name="CodeBuild-UpdateProject-response-project"></a>
Information about the build project that was changed.
Type: [Project](API_Project.md) object

## Errors
<a name="API_UpdateProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/UpdateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/UpdateProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
