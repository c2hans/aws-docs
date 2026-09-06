---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportEBSVolumeRecommendations.html
---

# ExportEBSVolumeRecommendations
<a name="API_ExportEBSVolumeRecommendations"></a>

Exports optimization recommendations for Amazon EBS volumes.

Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (JSON) (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see [Exporting Recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html) in the *Compute Optimizer User Guide*.

You can have only one Amazon EBS volume export job in progress per AWS Region.

## Request Syntax
<a name="API_ExportEBSVolumeRecommendations_RequestSyntax"></a>

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
   "s3DestinationConfig": {
      "bucket": "{{string}}",
      "keyPrefix": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ExportEBSVolumeRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_ExportEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportEBSVolumeRecommendations-request-accountIds"></a>
The IDs of the AWS accounts for which to export Amazon EBS volume recommendations.
If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.
This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.
Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.
You can specify multiple account IDs per request.
Type: Array of strings
Required: No

 ** [fieldsToExport](#API_ExportEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportEBSVolumeRecommendations-request-fieldsToExport"></a>
The recommendations data to include in the export file. For more information about the fields that can be exported, see [Exported files](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files) in the *Compute Optimizer User Guide*.
Type: Array of strings
Valid Values: `AccountId | VolumeArn | Finding | UtilizationMetricsVolumeReadOpsPerSecondMaximum | UtilizationMetricsVolumeWriteOpsPerSecondMaximum | UtilizationMetricsVolumeReadBytesPerSecondMaximum | UtilizationMetricsVolumeWriteBytesPerSecondMaximum | UtilizationMetricsVolumeIOPSExceededMaximum | UtilizationMetricsVolumeThroughputExceededMaximum | LookbackPeriodInDays | CurrentConfigurationVolumeType | CurrentConfigurationVolumeBaselineIOPS | CurrentConfigurationVolumeBaselineThroughput | CurrentConfigurationVolumeBurstIOPS | CurrentConfigurationVolumeBurstThroughput | CurrentConfigurationVolumeSize | CurrentMonthlyPrice | RecommendationOptionsConfigurationVolumeType | RecommendationOptionsConfigurationVolumeBaselineIOPS | RecommendationOptionsConfigurationVolumeBaselineThroughput | RecommendationOptionsConfigurationVolumeBurstIOPS | RecommendationOptionsConfigurationVolumeBurstThroughput | RecommendationOptionsConfigurationVolumeSize | RecommendationOptionsMonthlyPrice | RecommendationOptionsPerformanceRisk | LastRefreshTimestamp | CurrentPerformanceRisk | RecommendationOptionsSavingsOpportunityPercentage | RecommendationOptionsEstimatedMonthlySavingsCurrency | RecommendationOptionsEstimatedMonthlySavingsValue | Tags | RootVolume | CurrentConfigurationRootVolume | EffectiveRecommendationPreferencesSavingsEstimationMode | RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage | RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts | RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts | EffectiveRecommendationPreferencesLookBackPeriod`
Required: No

 ** [fileFormat](#API_ExportEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportEBSVolumeRecommendations-request-fileFormat"></a>
The format of the export file.
The only export file format currently supported is `Csv`.
Type: String
Valid Values: `Csv`
Required: No

 ** [filters](#API_ExportEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportEBSVolumeRecommendations-request-filters"></a>
An array of objects to specify a filter that exports a more specific set of Amazon EBS volume recommendations.
Type: Array of [EBSFilter](API_EBSFilter.md) objects
Required: No

 ** [includeMemberAccounts](#API_ExportEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportEBSVolumeRecommendations-request-includeMemberAccounts"></a>
Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.
The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see [Compute Optimizer and AWS Organizations trusted access](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access) in the * AWS Compute Optimizer User Guide*.
Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.
This parameter cannot be specified together with the account IDs parameter. The parameters are mutually exclusive.
Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.
Type: Boolean
Required: No

 ** [s3DestinationConfig](#API_ExportEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-ExportEBSVolumeRecommendations-request-s3DestinationConfig"></a>
Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for a recommendations export job.
You must create the destination Amazon S3 bucket for your recommendations export before you create the export job. Compute Optimizer does not create the S3 bucket for you. After you create the S3 bucket, ensure that it has the required permission policy to allow Compute Optimizer to write the export file to it. If you plan to specify an object prefix when you create the export job, you must include the object prefix in the policy that you add to the S3 bucket. For more information, see [Amazon S3 Bucket Policy for Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html) in the *Compute Optimizer User Guide*.
Type: [S3DestinationConfig](API_S3DestinationConfig.md) object
Required: Yes

## Response Syntax
<a name="API_ExportEBSVolumeRecommendations_ResponseSyntax"></a>

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
<a name="API_ExportEBSVolumeRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_ExportEBSVolumeRecommendations_ResponseSyntax) **   <a name="computeoptimizer-ExportEBSVolumeRecommendations-response-jobId"></a>
The identification number of the export job.
Use the [DescribeRecommendationExportJobs](API_DescribeRecommendationExportJobs.md) action, and specify the job ID to view the status of an export job.
Type: String

 ** [s3Destination](#API_ExportEBSVolumeRecommendations_ResponseSyntax) **   <a name="computeoptimizer-ExportEBSVolumeRecommendations-response-s3Destination"></a>
Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a recommendations export file, and its associated metadata file.
Type: [S3Destination](API_S3Destination.md) object

## Errors
<a name="API_ExportEBSVolumeRecommendations_Errors"></a>

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
<a name="API_ExportEBSVolumeRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ExportEBSVolumeRecommendations)
