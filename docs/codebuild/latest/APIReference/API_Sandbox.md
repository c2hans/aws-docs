---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Sandbox.html
---

# Sandbox
<a name="API_Sandbox"></a>

Contains sandbox information.

## Contents
<a name="API_Sandbox_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-Sandbox-arn"></a>
The ARN of the sandbox.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** currentSession **   <a name="CodeBuild-Type-Sandbox-currentSession"></a>
The current session for the sandbox.
Type: [SandboxSession](API_SandboxSession.md) object
Required: No

 ** encryptionKey **   <a name="CodeBuild-Type-Sandbox-encryptionKey"></a>
The AWS Key Management Service customer master key (CMK) to be used for encrypting the sandbox output artifacts.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** endTime **   <a name="CodeBuild-Type-Sandbox-endTime"></a>
When the sandbox process ended, expressed in Unix time format.
Type: Timestamp
Required: No

 ** environment **   <a name="CodeBuild-Type-Sandbox-environment"></a>
Information about the build environment of the build project.
Type: [ProjectEnvironment](API_ProjectEnvironment.md) object
Required: No

 ** fileSystemLocations **   <a name="CodeBuild-Type-Sandbox-fileSystemLocations"></a>
 An array of `ProjectFileSystemLocation` objects for a CodeBuild build project. A `ProjectFileSystemLocation` object specifies the `identifier`, `location`, `mountOptions`, `mountPoint`, and `type` of a file system created using Amazon Elastic File System.
Type: Array of [ProjectFileSystemLocation](API_ProjectFileSystemLocation.md) objects
Required: No

 ** id **   <a name="CodeBuild-Type-Sandbox-id"></a>
The ID of the sandbox.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** logConfig **   <a name="CodeBuild-Type-Sandbox-logConfig"></a>
 Information about logs for a build project. These can be logs in CloudWatch Logs, built in a specified S3 bucket, or both.
Type: [LogsConfig](API_LogsConfig.md) object
Required: No

 ** projectName **   <a name="CodeBuild-Type-Sandbox-projectName"></a>
The AWS CodeBuild project name.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** queuedTimeoutInMinutes **   <a name="CodeBuild-Type-Sandbox-queuedTimeoutInMinutes"></a>
The number of minutes a sandbox is allowed to be queued before it times out.
Type: Integer
Required: No

 ** requestTime **   <a name="CodeBuild-Type-Sandbox-requestTime"></a>
When the sandbox process was initially requested, expressed in Unix time format.
Type: Timestamp
Required: No

 ** secondarySources **   <a name="CodeBuild-Type-Sandbox-secondarySources"></a>
 An array of `ProjectSource` objects.
Type: Array of [ProjectSource](API_ProjectSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** secondarySourceVersions **   <a name="CodeBuild-Type-Sandbox-secondarySourceVersions"></a>
 An array of `ProjectSourceVersion` objects.
Type: Array of [ProjectSourceVersion](API_ProjectSourceVersion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Required: No

 ** serviceRole **   <a name="CodeBuild-Type-Sandbox-serviceRole"></a>
The name of a service role used for this sandbox.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** source **   <a name="CodeBuild-Type-Sandbox-source"></a>
Information about the build input source code for the build project.
Type: [ProjectSource](API_ProjectSource.md) object
Required: No

 ** sourceVersion **   <a name="CodeBuild-Type-Sandbox-sourceVersion"></a>
Any version identifier for the version of the sandbox to be built.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** startTime **   <a name="CodeBuild-Type-Sandbox-startTime"></a>
When the sandbox process started, expressed in Unix time format.
Type: Timestamp
Required: No

 ** status **   <a name="CodeBuild-Type-Sandbox-status"></a>
The status of the sandbox.
Type: String
Required: No

 ** timeoutInMinutes **   <a name="CodeBuild-Type-Sandbox-timeoutInMinutes"></a>
How long, in minutes, from 5 to 2160 (36 hours), for AWS CodeBuild to wait before timing out this sandbox if it does not get marked as completed.
Type: Integer
Required: No

 ** vpcConfig **   <a name="CodeBuild-Type-Sandbox-vpcConfig"></a>
Information about the VPC configuration that AWS CodeBuild accesses.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_Sandbox_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/Sandbox)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/Sandbox)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/Sandbox)
