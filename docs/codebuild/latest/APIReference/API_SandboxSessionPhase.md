---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SandboxSessionPhase.html
---

# SandboxSessionPhase
<a name="API_SandboxSessionPhase"></a>

Contains information about the sandbox phase.

## Contents
<a name="API_SandboxSessionPhase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** contexts **   <a name="CodeBuild-Type-SandboxSessionPhase-contexts"></a>
 An array of `PhaseContext` objects.
Type: Array of [PhaseContext](API_PhaseContext.md) objects
Required: No

 ** durationInSeconds **   <a name="CodeBuild-Type-SandboxSessionPhase-durationInSeconds"></a>
How long, in seconds, between the starting and ending times of the sandbox's phase.
Type: Long
Required: No

 ** endTime **   <a name="CodeBuild-Type-SandboxSessionPhase-endTime"></a>
When the sandbox phase ended, expressed in Unix time format.
Type: Timestamp
Required: No

 ** phaseStatus **   <a name="CodeBuild-Type-SandboxSessionPhase-phaseStatus"></a>
The current status of the sandbox phase. Valid values include:
FAILED
The sandbox phase failed.
FAULT
The sandbox phase faulted.
IN\_PROGRESS
The sandbox phase is still in progress.
STOPPED
The sandbox phase stopped.
SUCCEEDED
The sandbox phase succeeded.
TIMED\_OUT
The sandbox phase timed out.
Type: String
Valid Values: `SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`
Required: No

 ** phaseType **   <a name="CodeBuild-Type-SandboxSessionPhase-phaseType"></a>
The name of the sandbox phase.
Type: String
Required: No

 ** startTime **   <a name="CodeBuild-Type-SandboxSessionPhase-startTime"></a>
When the sandbox phase started, expressed in Unix time format.
Type: Timestamp
Required: No

## See Also
<a name="API_SandboxSessionPhase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/SandboxSessionPhase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/SandboxSessionPhase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/SandboxSessionPhase)
