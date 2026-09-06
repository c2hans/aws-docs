---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportRDSDatabaseRecommendations.html
---

# ExportRDSDatabaseRecommendations
<a name="API_ExportRDSDatabaseRecommendations"></a>

 Export optimization recommendations for your Amazon Aurora and Amazon Relational Database Service (Amazon RDS) databases.

Recommendations are exported in a comma-separated values (CSV) file, and its metadata in a JavaScript Object Notation (JSON) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see [Exporting Recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html) in the *Compute Optimizer User Guide*.

You can have only one Amazon Aurora or RDS export job in progress per AWS Region.

## Request Syntax
<a name="API_ExportRDSDatabaseRecommendations_RequestSyntax"></a>

```
{
   "accountIds": [ "{{string}}" ],
   "fieldsToExport": [ "{{string}}" ],
   "fileFormat": "{{string}}",
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "includeMemberAccounts": {{boolean}},
   "recommendationPreferences": {
      "cpuVendorArchitectures": [ "{{string}}" ]
   },
   "s3DestinationConfig": {
      "bucket": "{{string}}",
      "keyPrefix": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ExportRDSDatabaseRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_ExportRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-request-accountIds"></a>
 The AWS account IDs for the export Amazon Aurora and RDS database recommendations.
If your account is the management account or the delegated administrator of an organization, use this parameter to specify the member account you want to export recommendations to.
This parameter can't be specified together with the include member accounts parameter. The parameters are mutually exclusive.
If this parameter or the include member accounts parameter is omitted, the recommendations for member accounts aren't included in the export.
You can specify multiple account IDs per request.
Type: Array of strings
Required: No

 ** [fieldsToExport](#API_ExportRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-request-fieldsToExport"></a>
The recommendations data to include in the export file. For more information about the fields that can be exported, see [Exported files](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files) in the *Compute Optimizer User Guide*.
Type: Array of strings
Valid Values: `ResourceArn | AccountId | Engine | EngineVersion | Idle | MultiAZDBInstance | ClusterWriter | CurrentDBInstanceClass | CurrentStorageConfigurationStorageType | CurrentStorageConfigurationAllocatedStorage | CurrentStorageConfigurationMaxAllocatedStorage | CurrentStorageConfigurationIOPS | CurrentStorageConfigurationStorageThroughput | CurrentStorageEstimatedMonthlyVolumeIOPsCostVariation | CurrentInstanceOnDemandHourlyPrice | CurrentStorageOnDemandMonthlyPrice | LookbackPeriodInDays | CurrentStorageEstimatedClusterInstanceOnDemandMonthlyCost | CurrentStorageEstimatedClusterStorageOnDemandMonthlyCost | CurrentStorageEstimatedClusterStorageIOOnDemandMonthlyCost | CurrentInstancePerformanceRisk | UtilizationMetricsCpuMaximum | UtilizationMetricsMemoryMaximum | UtilizationMetricsEBSVolumeStorageSpaceUtilizationMaximum | UtilizationMetricsNetworkReceiveThroughputMaximum | UtilizationMetricsNetworkTransmitThroughputMaximum | UtilizationMetricsEBSVolumeReadIOPSMaximum | UtilizationMetricsEBSVolumeWriteIOPSMaximum | UtilizationMetricsEBSVolumeReadThroughputMaximum | UtilizationMetricsEBSVolumeWriteThroughputMaximum | UtilizationMetricsDatabaseConnectionsMaximum | UtilizationMetricsStorageNetworkReceiveThroughputMaximum | UtilizationMetricsStorageNetworkTransmitThroughputMaximum | UtilizationMetricsAuroraMemoryHealthStateMaximum | UtilizationMetricsAuroraMemoryNumDeclinedSqlTotalMaximum | UtilizationMetricsAuroraMemoryNumKillConnTotalMaximum | UtilizationMetricsAuroraMemoryNumKillQueryTotalMaximum | UtilizationMetricsReadIOPSEphemeralStorageMaximum | UtilizationMetricsWriteIOPSEphemeralStorageMaximum | UtilizationMetricsVolumeBytesUsedAverage | UtilizationMetricsVolumeReadIOPsAverage | UtilizationMetricsVolumeWriteIOPsAverage | InstanceFinding | InstanceFindingReasonCodes | StorageFinding | StorageFindingReasonCodes | InstanceRecommendationOptionsDBInstanceClass | InstanceRecommendationOptionsRank | InstanceRecommendationOptionsPerformanceRisk | InstanceRecommendationOptionsProjectedUtilizationMetricsCpuMaximum | StorageRecommendationOptionsStorageType | StorageRecommendationOptionsAllocatedStorage | StorageRecommendationOptionsMaxAllocatedStorage | StorageRecommendationOptionsIOPS | StorageRecommendationOptionsStorageThroughput | StorageRecommendationOptionsRank | StorageRecommendationOptionsEstimatedMonthlyVolumeIOPsCostVariation | InstanceRecommendationOptionsInstanceOnDemandHourlyPrice | InstanceRecommendationOptionsSavingsOpportunityPercentage | InstanceRecommendationOptionsEstimatedMonthlySavingsCurrency | InstanceRecommendationOptionsEstimatedMonthlySavingsValue | InstanceRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage | InstanceRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts | InstanceRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts | StorageRecommendationOptionsOnDemandMonthlyPrice | StorageRecommendationOptionsEstimatedClusterInstanceOnDemandMonthlyCost | StorageRecommendationOptionsEstimatedClusterStorageOnDemandMonthlyCost | StorageRecommendationOptionsEstimatedClusterStorageIOOnDemandMonthlyCost | StorageRecommendationOptionsSavingsOpportunityPercentage | StorageRecommendationOptionsEstimatedMonthlySavingsCurrency | StorageRecommendationOptionsEstimatedMonthlySavingsValue | StorageRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage | StorageRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts | StorageRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts | EffectiveRecommendationPreferencesCpuVendorArchitectures | EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics | EffectiveRecommendationPreferencesLookBackPeriod | EffectiveRecommendationPreferencesSavingsEstimationMode | LastRefreshTimestamp | Tags | DBClusterIdentifier | PromotionTier`
Required: No

 ** [fileFormat](#API_ExportRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-request-fileFormat"></a>
 The format of the export file.
The CSV file is the only export file format currently supported.
Type: String
Valid Values: `Csv`
Required: No

 ** [filters](#API_ExportRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-request-filters"></a>
 An array of objects to specify a filter that exports a more specific set of Amazon Aurora and RDS recommendations.
Type: Array of [RDSDBRecommendationFilter](API_RDSDBRecommendationFilter.md) objects
Required: No

 ** [includeMemberAccounts](#API_ExportRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-request-includeMemberAccounts"></a>
If your account is the management account or the delegated administrator of an organization, this parameter indicates whether to include recommendations for resources in all member accounts of the organization.
The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see [Compute Optimizer and AWS Organizations trusted access](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access) in the * AWS Compute Optimizer User Guide*.
If this parameter is omitted, recommendations for member accounts of the organization aren't included in the export file.
If this parameter or the account ID parameter is omitted, recommendations for member accounts aren't included in the export.
Type: Boolean
Required: No

 ** [recommendationPreferences](#API_ExportRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-request-recommendationPreferences"></a>
Describes the recommendation preferences to return in the response of a [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md), [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md), [GetEC2RecommendationProjectedMetrics](API_GetEC2RecommendationProjectedMetrics.md), [GetRDSDatabaseRecommendations](API_GetRDSDatabaseRecommendations.md), and [GetRDSDatabaseRecommendationProjectedMetrics](API_GetRDSDatabaseRecommendationProjectedMetrics.md) request.
Type: [RecommendationPreferences](API_RecommendationPreferences.md) object
Required: No

 ** [s3DestinationConfig](#API_ExportRDSDatabaseRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-request-s3DestinationConfig"></a>
Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for a recommendations export job.
You must create the destination Amazon S3 bucket for your recommendations export before you create the export job. Compute Optimizer does not create the S3 bucket for you. After you create the S3 bucket, ensure that it has the required permission policy to allow Compute Optimizer to write the export file to it. If you plan to specify an object prefix when you create the export job, you must include the object prefix in the policy that you add to the S3 bucket. For more information, see [Amazon S3 Bucket Policy for Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html) in the *Compute Optimizer User Guide*.
Type: [S3DestinationConfig](API_S3DestinationConfig.md) object
Required: Yes

## Response Syntax
<a name="API_ExportRDSDatabaseRecommendations_ResponseSyntax"></a>

```
{
   "jobId": "string",
   "s3Destination": {
      "bucket": "string",
      "key": "string",
      "metadataKey": "string"
   }
}
```

## Response Elements
<a name="API_ExportRDSDatabaseRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_ExportRDSDatabaseRecommendations_ResponseSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-response-jobId"></a>
 The identification number of the export job.
To view the status of an export job, use the [DescribeRecommendationExportJobs](API_DescribeRecommendationExportJobs.md) action and specify the job ID.
Type: String

 ** [s3Destination](#API_ExportRDSDatabaseRecommendations_ResponseSyntax) **   <a name="computeoptimizer-ExportRDSDatabaseRecommendations-response-s3Destination"></a>
Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a recommendations export file, and its associated metadata file.
Type: [S3Destination](API_S3Destination.md) object

## Errors
<a name="API_ExportRDSDatabaseRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal error has occurred. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value supplied for the input parameter is out of range or not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The request exceeds a limit of the service.
HTTP Status Code: 400

 ** MissingAuthenticationToken **
The request must contain either a valid (registered) AWS access key ID or X.509 certificate.
HTTP Status Code: 400

 ** OptInRequiredException **
The account is not opted in to AWS Compute Optimizer.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the server.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_ExportRDSDatabaseRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ExportRDSDatabaseRecommendations)
