---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildSummary.html
---

# BuildSummary
<a name="API_BuildSummary"></a>

Contains summary information about a batch build group.

## Contents
<a name="API_BuildSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-BuildSummary-arn"></a>
The batch build ARN.
Type: String
Required: No

 ** buildStatus **   <a name="CodeBuild-Type-BuildSummary-buildStatus"></a>
The status of the build group.
FAILED
The build group failed.
FAULT
The build group faulted.
IN\_PROGRESS
The build group is still in progress.
STOPPED
The build group stopped.
SUCCEEDED
The build group succeeded.
TIMED\_OUT
The build group timed out.
Type: String
Valid Values: `SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`
Required: No

 ** primaryArtifact **   <a name="CodeBuild-Type-BuildSummary-primaryArtifact"></a>
A `ResolvedArtifact` object that represents the primary build artifacts for the build group.
Type: [ResolvedArtifact](API_ResolvedArtifact.md) object
Required: No

 ** requestedOn **   <a name="CodeBuild-Type-BuildSummary-requestedOn"></a>
When the build was started, expressed in Unix time format.
Type: Timestamp
Required: No

 ** secondaryArtifacts **   <a name="CodeBuild-Type-BuildSummary-secondaryArtifacts"></a>
An array of `ResolvedArtifact` objects that represents the secondary build artifacts for the build group.
Type: Array of [ResolvedArtifact](API_ResolvedArtifact.md) objects
Required: No

## See Also
<a name="API_BuildSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BuildSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BuildSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BuildSummary)
