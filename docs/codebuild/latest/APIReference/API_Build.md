---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Build.html
---

# Build
<a name="API_Build"></a>

Information about a build.

## Contents
<a name="API_Build_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-Build-arn"></a>
The Amazon Resource Name (ARN) of the build.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** artifacts **   <a name="CodeBuild-Type-Build-artifacts"></a>
Information about the output artifacts for the build.
Type: [BuildArtifacts](API_BuildArtifacts.md) object
Required: No

 ** autoRetryConfig **   <a name="CodeBuild-Type-Build-autoRetryConfig"></a>
Information about the auto-retry configuration for the build.
Type: [AutoRetryConfig](API_AutoRetryConfig.md) object
Required: No

 ** buildBatchArn **   <a name="CodeBuild-Type-Build-buildBatchArn"></a>
The ARN of the batch build that this build is a member of, if applicable.
Type: String
Required: No

 ** buildComplete **   <a name="CodeBuild-Type-Build-buildComplete"></a>
Whether the build is complete. True if complete; otherwise, false.
Type: Boolean
Required: No

 ** buildNumber **   <a name="CodeBuild-Type-Build-buildNumber"></a>
The number of the build. For each project, the `buildNumber` of its first build is `1`. The `buildNumber` of each subsequent build is incremented by `1`. If a build is deleted, the `buildNumber` of other builds does not change.
Type: Long
Required: No

 ** buildStatus **   <a name="CodeBuild-Type-Build-buildStatus"></a>
The current status of the build. Valid values include:
+  `FAILED`: The build failed.
+  `FAULT`: The build faulted.
+  `IN_PROGRESS`: The build is still in progress.
+  `STOPPED`: The build stopped.
+  `SUCCEEDED`: The build succeeded.
+  `TIMED_OUT`: The build timed out.
Type: String
Valid Values: `SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`
Required: No

 ** cache **   <a name="CodeBuild-Type-Build-cache"></a>
Information about the cache for the build.
Type: [ProjectCache](API_ProjectCache.md) object
Required: No

 ** currentPhase **   <a name="CodeBuild-Type-Build-currentPhase"></a>
The current build phase.
Type: String
Required: No

 ** debugSession **   <a name="CodeBuild-Type-Build-debugSession"></a>
Contains information about the debug session for this build.
Type: [DebugSession](API_DebugSession.md) object
Required: No

 ** encryptionKey **   <a name="CodeBuild-Type-Build-encryptionKey"></a>
The AWS Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.
 You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format `alias/<alias-name>`).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** endTime **   <a name="CodeBuild-Type-Build-endTime"></a>
When the build process ended, expressed in Unix time format.
Type: Timestamp
Required: No

 ** environment **   <a name="CodeBuild-Type-Build-environment"></a>
Information about the build environment for this build.
Type: [ProjectEnvironment](API_ProjectEnvironment.md) object
Required: No

 ** exportedEnvironmentVariables **   <a name="CodeBuild-Type-Build-exportedEnvironmentVariables"></a>
A list of exported environment variables for this build.
Exported environment variables are used in conjunction with CodePipeline to export environment variables from the current build stage to subsequent stages in the pipeline. For more information, see [Working with variables](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-variables.html) in the *CodePipeline User Guide*.
Type: Array of [ExportedEnvironmentVariable](API_ExportedEnvironmentVariable.md) objects
Required: No

 ** fileSystemLocations **   <a name="CodeBuild-Type-Build-fileSystemLocations"></a>
 An array of `ProjectFileSystemLocation` objects for a CodeBuild build project. A `ProjectFileSystemLocation` object specifies the `identifier`, `location`, `mountOptions`, `mountPoint`, and `type` of a file system created using Amazon Elastic File System.
Type: Array of [ProjectFileSystemLocation](API_ProjectFileSystemLocation.md) objects
Required: No

 ** id **   <a name="CodeBuild-Type-Build-id"></a>
The unique ID for the build.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** initiator **   <a name="CodeBuild-Type-Build-initiator"></a>
The entity that started the build. Valid values include:
+ If CodePipeline started the build, the pipeline's name (for example, `codepipeline/my-demo-pipeline`).
+ If a user started the build, the user's name (for example, `MyUserName`).
+ If the Jenkins plugin for AWS CodeBuild started the build, the string `CodeBuild-Jenkins-Plugin`.
Type: String
Required: No

 ** logs **   <a name="CodeBuild-Type-Build-logs"></a>
Information about the build's logs in CloudWatch Logs.
Type: [LogsLocation](API_LogsLocation.md) object
Required: No

 ** networkInterface **   <a name="CodeBuild-Type-Build-networkInterface"></a>
Describes a network interface.
Type: [NetworkInterface](API_NetworkInterface.md) object
Required: No

 ** phases **   <a name="CodeBuild-Type-Build-phases"></a>
Information about all previous build phases that are complete and information about any current build phase that is not yet complete.
Type: Array of [BuildPhase](API_BuildPhase.md) objects
Required: No

 ** projectName **   <a name="CodeBuild-Type-Build-projectName"></a>
The name of the AWS CodeBuild project.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** queuedTimeoutInMinutes **   <a name="CodeBuild-Type-Build-queuedTimeoutInMinutes"></a>
 The number of minutes a build is allowed to be queued before it times out.
Type: Integer
Required: No

 ** reportArns **   <a name="CodeBuild-Type-Build-reportArns"></a>
 An array of the ARNs associated with this build's reports.
Type: Array of strings
Required: No

 ** resolvedSourceVersion **   <a name="CodeBuild-Type-Build-resolvedSourceVersion"></a>
 An identifier for the version of this build's source code.
+  For CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
+  For CodePipeline, the source revision provided by CodePipeline.
+  For Amazon S3, this does not apply.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** secondaryArtifacts **   <a name="CodeBuild-Type-Build-secondaryArtifacts"></a>
 An array of `ProjectArtifacts` objects.
Type: Array of [BuildArtifacts](API_BuildArtifacts.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** secondarySources **   <a name="CodeBuild-Type-Build-secondarySources"></a>
 An array of `ProjectSource` objects.
Type: Array of [ProjectSource](API_ProjectSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** secondarySourceVersions **   <a name="CodeBuild-Type-Build-secondarySourceVersions"></a>
 An array of `ProjectSourceVersion` objects. Each `ProjectSourceVersion` must be one of:
+ For CodeCommit: the commit ID, branch, or Git tag to use.
+ For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example, `pr/25`). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
+ For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
+ For Amazon S3: the version ID of the object that represents the build input ZIP file to use.
Type: Array of [ProjectSourceVersion](API_ProjectSourceVersion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** serviceRole **   <a name="CodeBuild-Type-Build-serviceRole"></a>
The name of a service role used for this build.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** source **   <a name="CodeBuild-Type-Build-source"></a>
Information about the source code to be built.
Type: [ProjectSource](API_ProjectSource.md) object
Required: No

 ** sourceVersion **   <a name="CodeBuild-Type-Build-sourceVersion"></a>
Any version identifier for the version of the source code to be built. If `sourceVersion` is specified at the project level, then this `sourceVersion` (at the build level) takes precedence.
 For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the * AWS CodeBuild User Guide*.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** startTime **   <a name="CodeBuild-Type-Build-startTime"></a>
When the build process started, expressed in Unix time format.
Type: Timestamp
Required: No

 ** timeoutInMinutes **   <a name="CodeBuild-Type-Build-timeoutInMinutes"></a>
How long, in minutes, from 5 to 2160 (36 hours), for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.
Type: Integer
Required: No

 ** vpcConfig **   <a name="CodeBuild-Type-Build-vpcConfig"></a>
If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_Build_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/Build)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/Build)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/Build)
