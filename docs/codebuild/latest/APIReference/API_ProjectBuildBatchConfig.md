---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectBuildBatchConfig.html
---

# ProjectBuildBatchConfig
<a name="API_ProjectBuildBatchConfig"></a>

Contains configuration information about a batch build project.

## Contents
<a name="API_ProjectBuildBatchConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** batchReportMode **   <a name="CodeBuild-Type-ProjectBuildBatchConfig-batchReportMode"></a>
Specifies how build status reports are sent to the source provider for the batch build. This property is only used when the source provider for your project is Bitbucket, GitHub, or GitHub Enterprise, and your project is configured to report build statuses to the source provider.
REPORT\_AGGREGATED\_BATCH
(Default) Aggregate all of the build statuses into a single status report.
REPORT\_INDIVIDUAL\_BUILDS
Send a separate status report for each individual build.
Type: String
Valid Values: `REPORT_INDIVIDUAL_BUILDS | REPORT_AGGREGATED_BATCH`
Required: No

 ** combineArtifacts **   <a name="CodeBuild-Type-ProjectBuildBatchConfig-combineArtifacts"></a>
Specifies if the build artifacts for the batch build should be combined into a single artifact location.
Type: Boolean
Required: No

 ** restrictions **   <a name="CodeBuild-Type-ProjectBuildBatchConfig-restrictions"></a>
A `BatchRestrictions` object that specifies the restrictions for the batch build.
Type: [BatchRestrictions](API_BatchRestrictions.md) object
Required: No

 ** serviceRole **   <a name="CodeBuild-Type-ProjectBuildBatchConfig-serviceRole"></a>
Specifies the service role ARN for the batch build project.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** timeoutInMins **   <a name="CodeBuild-Type-ProjectBuildBatchConfig-timeoutInMins"></a>
Specifies the maximum amount of time, in minutes, that the batch build must be completed in.
Type: Integer
Required: No

## See Also
<a name="API_ProjectBuildBatchConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ProjectBuildBatchConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ProjectBuildBatchConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ProjectBuildBatchConfig)
