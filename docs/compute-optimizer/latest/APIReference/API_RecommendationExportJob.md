---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationExportJob.html
---

# RecommendationExportJob
<a name="API_RecommendationExportJob"></a>

Describes a recommendation export job.

Use the [DescribeRecommendationExportJobs](API_DescribeRecommendationExportJobs.md) action to view your recommendation export jobs.

Use the [ExportAutoScalingGroupRecommendations](API_ExportAutoScalingGroupRecommendations.md) or [ExportEC2InstanceRecommendations](API_ExportEC2InstanceRecommendations.md) actions to request an export of your recommendations.

## Contents
<a name="API_RecommendationExportJob_Contents"></a>

 ** creationTimestamp **   <a name="computeoptimizer-Type-RecommendationExportJob-creationTimestamp"></a>
The timestamp of when the export job was created.
Type: Timestamp
Required: No

 ** destination **   <a name="computeoptimizer-Type-RecommendationExportJob-destination"></a>
An object that describes the destination of the export file.
Type: [ExportDestination](API_ExportDestination.md) object
Required: No

 ** failureReason **   <a name="computeoptimizer-Type-RecommendationExportJob-failureReason"></a>
The reason for an export job failure.
Type: String
Required: No

 ** jobId **   <a name="computeoptimizer-Type-RecommendationExportJob-jobId"></a>
The identification number of the export job.
Type: String
Required: No

 ** lastUpdatedTimestamp **   <a name="computeoptimizer-Type-RecommendationExportJob-lastUpdatedTimestamp"></a>
The timestamp of when the export job was last updated.
Type: Timestamp
Required: No

 ** resourceType **   <a name="computeoptimizer-Type-RecommendationExportJob-resourceType"></a>
The resource type of the exported recommendations.
Type: String
Valid Values: `Ec2Instance | AutoScalingGroup | EbsVolume | LambdaFunction | NotApplicable | EcsService | License | RdsDBInstance | AuroraDBClusterStorage | Idle`
Required: No

 ** status **   <a name="computeoptimizer-Type-RecommendationExportJob-status"></a>
The status of the export job.
Type: String
Valid Values: `Queued | InProgress | Complete | Failed`
Required: No

## See Also
<a name="API_RecommendationExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RecommendationExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RecommendationExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RecommendationExportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
