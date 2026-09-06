---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Project.html
---

# Project
<a name="API_Project"></a>

Information about a build project.

## Contents
<a name="API_Project_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-Project-arn"></a>
The Amazon Resource Name (ARN) of the build project.
Type: String
Required: No

 ** artifacts **   <a name="CodeBuild-Type-Project-artifacts"></a>
Information about the build output artifacts for the build project.
Type: [ProjectArtifacts](API_ProjectArtifacts.md) object
Required: No

 ** autoRetryLimit **   <a name="CodeBuild-Type-Project-autoRetryLimit"></a>
The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry your build for up to 2 additional times.
Type: Integer
Required: No

 ** badge **   <a name="CodeBuild-Type-Project-badge"></a>
Information about the build badge for the build project.
Type: [ProjectBadge](API_ProjectBadge.md) object
Required: No

 ** buildBatchConfig **   <a name="CodeBuild-Type-Project-buildBatchConfig"></a>
A [ProjectBuildBatchConfig](API_ProjectBuildBatchConfig.md) object that defines the batch build options for the project.
Type: [ProjectBuildBatchConfig](API_ProjectBuildBatchConfig.md) object
Required: No

 ** cache **   <a name="CodeBuild-Type-Project-cache"></a>
Information about the cache for the build project.
Type: [ProjectCache](API_ProjectCache.md) object
Required: No

 ** concurrentBuildLimit **   <a name="CodeBuild-Type-Project-concurrentBuildLimit"></a>
The maximum number of concurrent builds that are allowed for this project.
New builds are only started if the current number of builds is less than or equal to this limit. If the current build count meets this limit, new builds are throttled and are not run.
Type: Integer
Required: No

 ** created **   <a name="CodeBuild-Type-Project-created"></a>
When the build project was created, expressed in Unix time format.
Type: Timestamp
Required: No

 ** description **   <a name="CodeBuild-Type-Project-description"></a>
A description that makes the build project easy to identify.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** encryptionKey **   <a name="CodeBuild-Type-Project-encryptionKey"></a>
The AWS Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format `alias/<alias-name>`). If you don't specify a value, CodeBuild uses the managed CMK for Amazon Simple Storage Service (Amazon S3).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** environment **   <a name="CodeBuild-Type-Project-environment"></a>
Information about the build environment for this build project.
Type: [ProjectEnvironment](API_ProjectEnvironment.md) object
Required: No

 ** fileSystemLocations **   <a name="CodeBuild-Type-Project-fileSystemLocations"></a>
 An array of `ProjectFileSystemLocation` objects for a CodeBuild build project. A `ProjectFileSystemLocation` object specifies the `identifier`, `location`, `mountOptions`, `mountPoint`, and `type` of a file system created using Amazon Elastic File System.
Type: Array of [ProjectFileSystemLocation](API_ProjectFileSystemLocation.md) objects
Required: No

 ** lastModified **   <a name="CodeBuild-Type-Project-lastModified"></a>
When the build project's settings were last modified, expressed in Unix time format.
Type: Timestamp
Required: No

 ** logsConfig **   <a name="CodeBuild-Type-Project-logsConfig"></a>
Information about logs for the build project. A project can create logs in CloudWatch Logs, an S3 bucket, or both.
Type: [LogsConfig](API_LogsConfig.md) object
Required: No

 ** name **   <a name="CodeBuild-Type-Project-name"></a>
The name of the build project.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 150.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{1,149}`
Required: No

 ** projectVisibility **   <a name="CodeBuild-Type-Project-projectVisibility"></a>
Specifies the visibility of the project's builds. Possible values are:
PUBLIC\_READ
The project builds are visible to the public.
PRIVATE
The project builds are not visible to the public.
Type: String
Valid Values: `PUBLIC_READ | PRIVATE`
Required: No

 ** publicProjectAlias **   <a name="CodeBuild-Type-Project-publicProjectAlias"></a>
Contains the project identifier used with the public build APIs.
For more information, see [Public build](https://docs.aws.amazon.com/codebuild/latest/userguide/public-build.html).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** queuedTimeoutInMinutes **   <a name="CodeBuild-Type-Project-queuedTimeoutInMinutes"></a>
The number of minutes a build is allowed to be queued before it times out.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 480.
Required: No

 ** resourceAccessRole **   <a name="CodeBuild-Type-Project-resourceAccessRole"></a>
The ARN of the IAM role that enables CodeBuild to access the CloudWatch Logs and Amazon S3 artifacts for the project's builds.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** secondaryArtifacts **   <a name="CodeBuild-Type-Project-secondaryArtifacts"></a>
An array of `ProjectArtifacts` objects.
Type: Array of [ProjectArtifacts](API_ProjectArtifacts.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** secondarySources **   <a name="CodeBuild-Type-Project-secondarySources"></a>
An array of `ProjectSource` objects.
Type: Array of [ProjectSource](API_ProjectSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** secondarySourceVersions **   <a name="CodeBuild-Type-Project-secondarySourceVersions"></a>
An array of `ProjectSourceVersion` objects. If `secondarySourceVersions` is specified at the build level, then they take over these `secondarySourceVersions` (at the project level).
Type: Array of [ProjectSourceVersion](API_ProjectSourceVersion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** serviceRole **   <a name="CodeBuild-Type-Project-serviceRole"></a>
The ARN of the IAM role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** source **   <a name="CodeBuild-Type-Project-source"></a>
Information about the build input source code for this build project.
Type: [ProjectSource](API_ProjectSource.md) object
Required: No

 ** sourceVersion **   <a name="CodeBuild-Type-Project-sourceVersion"></a>
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

 ** tags **   <a name="CodeBuild-Type-Project-tags"></a>
A list of tag key and value pairs associated with this build project.
These tags are available for use by AWS services that support AWS CodeBuild build project tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** timeoutInMinutes **   <a name="CodeBuild-Type-Project-timeoutInMinutes"></a>
How long, in minutes, from 5 to 2160 (36 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 2160.
Required: No

 ** vpcConfig **   <a name="CodeBuild-Type-Project-vpcConfig"></a>
Information about the VPC configuration that AWS CodeBuild accesses.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

 ** webhook **   <a name="CodeBuild-Type-Project-webhook"></a>
Information about a webhook that connects repository events to a build project in AWS CodeBuild.
Type: [Webhook](API_Webhook.md) object
Required: No

## See Also
<a name="API_Project_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/Project)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/Project)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/Project)
