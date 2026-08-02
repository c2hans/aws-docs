---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html
---

# BuildBatchPhase
<a name="API_BuildBatchPhase"></a>

Contains information about a stage for a batch build.

## Contents
<a name="API_BuildBatchPhase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** contexts **   <a name="CodeBuild-Type-BuildBatchPhase-contexts"></a>
Additional information about the batch build phase. Especially to help troubleshoot a failed batch build.
Type: Array of [PhaseContext](API_PhaseContext.md) objects
Required: No

 ** durationInSeconds **   <a name="CodeBuild-Type-BuildBatchPhase-durationInSeconds"></a>
How long, in seconds, between the starting and ending times of the batch build's phase.
Type: Long
Required: No

 ** endTime **   <a name="CodeBuild-Type-BuildBatchPhase-endTime"></a>
When the batch build phase ended, expressed in Unix time format.
Type: Timestamp
Required: No

 ** phaseStatus **   <a name="CodeBuild-Type-BuildBatchPhase-phaseStatus"></a>
The current status of the batch build phase. Valid values include:
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

 ** phaseType **   <a name="CodeBuild-Type-BuildBatchPhase-phaseType"></a>
The name of the batch build phase. Valid values include:
COMBINE\_ARTIFACTS
Build output artifacts are being combined and uploaded to the output location.
DOWNLOAD\_BATCHSPEC
The batch build specification is being downloaded.
FAILED
One or more of the builds failed.
IN\_PROGRESS
The batch build is in progress.
STOPPED
The batch build was stopped.
SUBMITTED
The btach build has been submitted.
SUCCEEDED
The batch build succeeded.
Type: String
Valid Values: `SUBMITTED | DOWNLOAD_BATCHSPEC | IN_PROGRESS | COMBINE_ARTIFACTS | SUCCEEDED | FAILED | STOPPED`
Required: No

 ** startTime **   <a name="CodeBuild-Type-BuildBatchPhase-startTime"></a>
When the batch build phase started, expressed in Unix time format.
Type: Timestamp
Required: No

## See Also
<a name="API_BuildBatchPhase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BuildBatchPhase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BuildBatchPhase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BuildBatchPhase)
