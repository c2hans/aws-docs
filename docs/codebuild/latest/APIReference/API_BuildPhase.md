---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html
---

# BuildPhase
<a name="API_BuildPhase"></a>

Information about a stage for a build.

## Contents
<a name="API_BuildPhase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** contexts **   <a name="CodeBuild-Type-BuildPhase-contexts"></a>
Additional information about a build phase, especially to help troubleshoot a failed build.
Type: Array of [PhaseContext](API_PhaseContext.md) objects
Required: No

 ** durationInSeconds **   <a name="CodeBuild-Type-BuildPhase-durationInSeconds"></a>
How long, in seconds, between the starting and ending times of the build's phase.
Type: Long
Required: No

 ** endTime **   <a name="CodeBuild-Type-BuildPhase-endTime"></a>
When the build phase ended, expressed in Unix time format.
Type: Timestamp
Required: No

 ** phaseStatus **   <a name="CodeBuild-Type-BuildPhase-phaseStatus"></a>
The current status of the build phase. Valid values include:
FAILED
The build phase failed.
FAULT
The build phase faulted.
IN\_PROGRESS
The build phase is still in progress.
STOPPED
The build phase stopped.
SUCCEEDED
The build phase succeeded.
TIMED\_OUT
The build phase timed out.
Type: String
Valid Values: `SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`
Required: No

 ** phaseType **   <a name="CodeBuild-Type-BuildPhase-phaseType"></a>
The name of the build phase. Valid values include:
BUILD
Core build activities typically occur in this build phase.
COMPLETED
The build has been completed.
DOWNLOAD\_SOURCE
Source code is being downloaded in this build phase.
FINALIZING
The build process is completing in this build phase.
INSTALL
Installation activities typically occur in this build phase.
POST\_BUILD
Post-build activities typically occur in this build phase.
PRE\_BUILD
Pre-build activities typically occur in this build phase.
PROVISIONING
The build environment is being set up.
QUEUED
The build has been submitted and is queued behind other submitted builds.
SUBMITTED
The build has been submitted.
UPLOAD\_ARTIFACTS
Build output artifacts are being uploaded to the output location.
Type: String
Valid Values: `SUBMITTED | QUEUED | PROVISIONING | DOWNLOAD_SOURCE | INSTALL | PRE_BUILD | BUILD | POST_BUILD | UPLOAD_ARTIFACTS | FINALIZING | COMPLETED`
Required: No

 ** startTime **   <a name="CodeBuild-Type-BuildPhase-startTime"></a>
When the build phase started, expressed in Unix time format.
Type: Timestamp
Required: No

## See Also
<a name="API_BuildPhase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BuildPhase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BuildPhase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BuildPhase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
