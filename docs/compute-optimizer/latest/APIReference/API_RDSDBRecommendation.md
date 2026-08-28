---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDBRecommendation.html
---

# RDSDBRecommendation
<a name="API_RDSDBRecommendation"></a>

 Describes an Amazon Aurora and RDS database recommendation.

## Contents
<a name="API_RDSDBRecommendation_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-RDSDBRecommendation-accountId"></a>
 The AWS account ID of the Amazon Aurora or RDS database.
Type: String
Required: No

 ** currentDBInstanceClass **   <a name="computeoptimizer-Type-RDSDBRecommendation-currentDBInstanceClass"></a>
 The DB instance class of the current Aurora or RDS DB instance.
Type: String
Required: No

 ** currentInstancePerformanceRisk **   <a name="computeoptimizer-Type-RDSDBRecommendation-currentInstancePerformanceRisk"></a>
The performance risk for the current DB instance.
Type: String
Valid Values: `VeryLow | Low | Medium | High`
Required: No

 ** currentStorageConfiguration **   <a name="computeoptimizer-Type-RDSDBRecommendation-currentStorageConfiguration"></a>
 The configuration of the current DB storage.
Type: [DBStorageConfiguration](API_DBStorageConfiguration.md) object
Required: No

 ** currentStorageEstimatedMonthlyVolumeIOPsCostVariation **   <a name="computeoptimizer-Type-RDSDBRecommendation-currentStorageEstimatedMonthlyVolumeIOPsCostVariation"></a>
 The level of variation in monthly I/O costs for the current DB storage configuration.
Type: String
Valid Values: `None | Low | Medium | High`
Required: No

 ** dbClusterIdentifier **   <a name="computeoptimizer-Type-RDSDBRecommendation-dbClusterIdentifier"></a>
The identifier for DB cluster.
Type: String
Required: No

 ** effectiveRecommendationPreferences **   <a name="computeoptimizer-Type-RDSDBRecommendation-effectiveRecommendationPreferences"></a>
 Describes the effective recommendation preferences for DB instances.
Type: [RDSEffectiveRecommendationPreferences](API_RDSEffectiveRecommendationPreferences.md) object
Required: No

 ** engine **   <a name="computeoptimizer-Type-RDSDBRecommendation-engine"></a>
 The engine of the DB instance.
Type: String
Required: No

 ** engineVersion **   <a name="computeoptimizer-Type-RDSDBRecommendation-engineVersion"></a>
 The database engine version.
Type: String
Required: No

 ** idle **   <a name="computeoptimizer-Type-RDSDBRecommendation-idle"></a>
 This indicates if the DB instance is idle or not.
Type: String
Valid Values: `True | False`
Required: No

 ** instanceFinding **   <a name="computeoptimizer-Type-RDSDBRecommendation-instanceFinding"></a>
 The finding classification of an Amazon Aurora and RDS DB instance.
For more information about finding classifications, see [ Finding classifications for Aurora and RDS databases](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html#rds-recommendations-findings) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `Optimized | Underprovisioned | Overprovisioned`
Required: No

 ** instanceFindingReasonCodes **   <a name="computeoptimizer-Type-RDSDBRecommendation-instanceFindingReasonCodes"></a>
 The reason for the finding classification of a DB instance.
Type: Array of strings
Valid Values: `CPUOverprovisioned | NetworkBandwidthOverprovisioned | EBSIOPSOverprovisioned | EBSIOPSUnderprovisioned | EBSThroughputOverprovisioned | CPUUnderprovisioned | NetworkBandwidthUnderprovisioned | EBSThroughputUnderprovisioned | NewGenerationDBInstanceClassAvailable | NewEngineVersionAvailable | DBClusterWriterUnderprovisioned | MemoryUnderprovisioned | InstanceStorageReadIOPSUnderprovisioned | InstanceStorageWriteIOPSUnderprovisioned`
Required: No

 ** instanceRecommendationOptions **   <a name="computeoptimizer-Type-RDSDBRecommendation-instanceRecommendationOptions"></a>
 An array of objects that describe the recommendation options for the RDS DB instance.
Type: Array of [RDSDBInstanceRecommendationOption](API_RDSDBInstanceRecommendationOption.md) objects
Required: No

 ** lastRefreshTimestamp **   <a name="computeoptimizer-Type-RDSDBRecommendation-lastRefreshTimestamp"></a>
 The timestamp of when the DB instance recommendation was last generated.
Type: Timestamp
Required: No

 ** lookbackPeriodInDays **   <a name="computeoptimizer-Type-RDSDBRecommendation-lookbackPeriodInDays"></a>
 The number of days the DB instance utilization metrics were analyzed.
Type: Double
Required: No

 ** promotionTier **   <a name="computeoptimizer-Type-RDSDBRecommendation-promotionTier"></a>
The promotion tier for the Aurora instance.
Type: Integer
Required: No

 ** resourceArn **   <a name="computeoptimizer-Type-RDSDBRecommendation-resourceArn"></a>
 The ARN of the current Amazon Aurora or RDS database.
 The following is the format of the ARN:
 `arn:aws:rds:{region}:{accountId}:db:{resourceName}`
Type: String
Required: No

 ** storageFinding **   <a name="computeoptimizer-Type-RDSDBRecommendation-storageFinding"></a>
 The finding classification of Amazon RDS DB instance storage.
For more information about finding classifications, see [ Finding classifications for Aurora and RDS databases](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html#rds-recommendations-findings) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `Optimized | Underprovisioned | Overprovisioned | NotOptimized`
Required: No

 ** storageFindingReasonCodes **   <a name="computeoptimizer-Type-RDSDBRecommendation-storageFindingReasonCodes"></a>
 The reason for the finding classification of RDS DB instance storage.
Type: Array of strings
Valid Values: `EBSVolumeAllocatedStorageUnderprovisioned | EBSVolumeThroughputUnderprovisioned | EBSVolumeIOPSOverprovisioned | EBSVolumeThroughputOverprovisioned | NewGenerationStorageTypeAvailable | DBClusterStorageOptionAvailable | DBClusterStorageSavingsAvailable`
Required: No

 ** storageRecommendationOptions **   <a name="computeoptimizer-Type-RDSDBRecommendation-storageRecommendationOptions"></a>
 An array of objects that describe the recommendation options for DB instance storage.
Type: Array of [RDSDBStorageRecommendationOption](API_RDSDBStorageRecommendationOption.md) objects
Required: No

 ** tags **   <a name="computeoptimizer-Type-RDSDBRecommendation-tags"></a>
 A list of tags assigned to your DB instance recommendations.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** utilizationMetrics **   <a name="computeoptimizer-Type-RDSDBRecommendation-utilizationMetrics"></a>
 An array of objects that describe the utilization metrics of the DB instance.
Type: Array of [RDSDBUtilizationMetric](API_RDSDBUtilizationMetric.md) objects
Required: No

## See Also
<a name="API_RDSDBRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RDSDBRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RDSDBRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RDSDBRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
