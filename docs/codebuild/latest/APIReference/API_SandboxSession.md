---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SandboxSession.html
---

# SandboxSession
<a name="API_SandboxSession"></a>

Contains information about the sandbox session.

## Contents
<a name="API_SandboxSession_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** currentPhase **   <a name="CodeBuild-Type-SandboxSession-currentPhase"></a>
The current phase for the sandbox.
Type: String
Required: No

 ** endTime **   <a name="CodeBuild-Type-SandboxSession-endTime"></a>
When the sandbox session ended, expressed in Unix time format.
Type: Timestamp
Required: No

 ** id **   <a name="CodeBuild-Type-SandboxSession-id"></a>
The ID of the sandbox session.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** logs **   <a name="CodeBuild-Type-SandboxSession-logs"></a>
Information about build logs in CloudWatch Logs.
Type: [LogsLocation](API_LogsLocation.md) object
Required: No

 ** networkInterface **   <a name="CodeBuild-Type-SandboxSession-networkInterface"></a>
Describes a network interface.
Type: [NetworkInterface](API_NetworkInterface.md) object
Required: No

 ** phases **   <a name="CodeBuild-Type-SandboxSession-phases"></a>
 An array of `SandboxSessionPhase` objects.
Type: Array of [SandboxSessionPhase](API_SandboxSessionPhase.md) objects
Required: No

 ** resolvedSourceVersion **   <a name="CodeBuild-Type-SandboxSession-resolvedSourceVersion"></a>
An identifier for the version of this sandbox's source code.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** startTime **   <a name="CodeBuild-Type-SandboxSession-startTime"></a>
When the sandbox session started, expressed in Unix time format.
Type: Timestamp
Required: No

 ** status **   <a name="CodeBuild-Type-SandboxSession-status"></a>
The status of the sandbox session.
Type: String
Required: No

## See Also
<a name="API_SandboxSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/SandboxSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/SandboxSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/SandboxSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
