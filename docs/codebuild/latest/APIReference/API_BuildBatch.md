---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatch.html
---

# BuildBatch
<a name="API_BuildBatch"></a>

Contains information about a batch build.

## Contents
<a name="API_BuildBatch_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-BuildBatch-arn"></a>
The ARN of the batch build.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** artifacts **   <a name="CodeBuild-Type-BuildBatch-artifacts"></a>
A `BuildArtifacts` object the defines the build artifacts for this batch build.
Type: [BuildArtifacts](API_BuildArtifacts.md) object
Required: No

 ** buildBatchConfig **   <a name="CodeBuild-Type-BuildBatch-buildBatchConfig"></a>
Contains configuration information about a batch build project.
Type: [ProjectBuildBatchConfig](API_ProjectBuildBatchConfig.md) object
Required: No

 ** buildBatchNumber **   <a name="CodeBuild-Type-BuildBatch-buildBatchNumber"></a>
The number of the batch build. For each project, the `buildBatchNumber` of its first batch build is `1`. The `buildBatchNumber` of each subsequent batch build is incremented by `1`. If a batch build is deleted, the `buildBatchNumber` of other batch builds does not change.
Type: Long
Required: No

 ** buildBatchStatus **   <a name="CodeBuild-Type-BuildBatch-buildBatchStatus"></a>
The status of the batch build.
Type: String
Valid Values: `SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`
Required: No

 ** buildGroups **   <a name="CodeBuild-Type-BuildBatch-buildGroups"></a>
An array of `BuildGroup` objects that define the build groups for the batch build.
Type: Array of [BuildGroup](API_BuildGroup.md) objects
Required: No

 ** buildTimeoutInMinutes **   <a name="CodeBuild-Type-BuildBatch-buildTimeoutInMinutes"></a>
Specifies the maximum amount of time, in minutes, that the build in a batch must be completed in.
Type: Integer
Required: No

 ** cache **   <a name="CodeBuild-Type-BuildBatch-cache"></a>
Information about the cache for the build project.
Type: [ProjectCache](API_ProjectCache.md) object
Required: No

 ** complete **   <a name="CodeBuild-Type-BuildBatch-complete"></a>
Indicates if the batch build is complete.
Type: Boolean
Required: No

 ** currentPhase **   <a name="CodeBuild-Type-BuildBatch-currentPhase"></a>
The current phase of the batch build.
Type: String
Required: No

 ** debugSessionEnabled **   <a name="CodeBuild-Type-BuildBatch-debugSessionEnabled"></a>
Specifies if session debugging is enabled for this batch build. For more information, see [Viewing a running build in Session Manager](https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html). Batch session debugging is not supported for matrix batch builds.
Type: Boolean
Required: No

 ** encryptionKey **   <a name="CodeBuild-Type-BuildBatch-encryptionKey"></a>
The AWS Key Management Service customer master key (CMK) to be used for encrypting the batch build output artifacts.
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format `alias/<alias-name>`).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** endTime **   <a name="CodeBuild-Type-BuildBatch-endTime"></a>
The date and time that the batch build ended.
Type: Timestamp
Required: No

 ** environment **   <a name="CodeBuild-Type-BuildBatch-environment"></a>
Information about the build environment of the build project.
Type: [ProjectEnvironment](API_ProjectEnvironment.md) object
Required: No

 ** fileSystemLocations **   <a name="CodeBuild-Type-BuildBatch-fileSystemLocations"></a>
An array of `ProjectFileSystemLocation` objects for the batch build project. A `ProjectFileSystemLocation` object specifies the `identifier`, `location`, `mountOptions`, `mountPoint`, and `type` of a file system created using Amazon Elastic File System.
Type: Array of [ProjectFileSystemLocation](API_ProjectFileSystemLocation.md) objects
Required: No

 ** id **   <a name="CodeBuild-Type-BuildBatch-id"></a>
The identifier of the batch build.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** initiator **   <a name="CodeBuild-Type-BuildBatch-initiator"></a>
The entity that started the batch build. Valid values include:
+ If CodePipeline started the build, the pipeline's name (for example, `codepipeline/my-demo-pipeline`).
+ If a user started the build, the user's name.
+ If the Jenkins plugin for AWS CodeBuild started the build, the string `CodeBuild-Jenkins-Plugin`.
Type: String
Required: No

 ** logConfig **   <a name="CodeBuild-Type-BuildBatch-logConfig"></a>
 Information about logs for a build project. These can be logs in CloudWatch Logs, built in a specified S3 bucket, or both.
Type: [LogsConfig](API_LogsConfig.md) object
Required: No

 ** phases **   <a name="CodeBuild-Type-BuildBatch-phases"></a>
An array of `BuildBatchPhase` objects the specify the phases of the batch build.
Type: Array of [BuildBatchPhase](API_BuildBatchPhase.md) objects
Required: No

 ** projectName **   <a name="CodeBuild-Type-BuildBatch-projectName"></a>
The name of the batch build project.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** queuedTimeoutInMinutes **   <a name="CodeBuild-Type-BuildBatch-queuedTimeoutInMinutes"></a>
Specifies the amount of time, in minutes, that the batch build is allowed to be queued before it times out.
Type: Integer
Required: No

 ** reportArns **   <a name="CodeBuild-Type-BuildBatch-reportArns"></a>
An array that contains the ARNs of reports created by merging reports from builds associated with this batch build.
Type: Array of strings
Required: No

 ** resolvedSourceVersion **   <a name="CodeBuild-Type-BuildBatch-resolvedSourceVersion"></a>
The identifier of the resolved version of this batch build's source code.
+ For CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
+ For CodePipeline, the source revision provided by CodePipeline.
+ For Amazon S3, this does not apply.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** secondaryArtifacts **   <a name="CodeBuild-Type-BuildBatch-secondaryArtifacts"></a>
An array of `BuildArtifacts` objects the define the build artifacts for this batch build.
Type: Array of [BuildArtifacts](API_BuildArtifacts.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** secondarySources **   <a name="CodeBuild-Type-BuildBatch-secondarySources"></a>
An array of `ProjectSource` objects that define the sources for the batch build.
Type: Array of [ProjectSource](API_ProjectSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** secondarySourceVersions **   <a name="CodeBuild-Type-BuildBatch-secondarySourceVersions"></a>
An array of `ProjectSourceVersion` objects. Each `ProjectSourceVersion` must be one of:
+ For CodeCommit: the commit ID, branch, or Git tag to use.
+ For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example, `pr/25`). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
+ For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.
+ For Amazon S3: the version ID of the object that represents the build input ZIP file to use.
Type: Array of [ProjectSourceVersion](API_ProjectSourceVersion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** serviceRole **   <a name="CodeBuild-Type-BuildBatch-serviceRole"></a>
The name of a service role used for builds in the batch.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** source **   <a name="CodeBuild-Type-BuildBatch-source"></a>
Information about the build input source code for the build project.
Type: [ProjectSource](API_ProjectSource.md) object
Required: No

 ** sourceVersion **   <a name="CodeBuild-Type-BuildBatch-sourceVersion"></a>
The identifier of the version of the source code to be built.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** startTime **   <a name="CodeBuild-Type-BuildBatch-startTime"></a>
The date and time that the batch build started.
Type: Timestamp
Required: No

 ** vpcConfig **   <a name="CodeBuild-Type-BuildBatch-vpcConfig"></a>
Information about the VPC configuration that AWS CodeBuild accesses.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_BuildBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BuildBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BuildBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BuildBatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
