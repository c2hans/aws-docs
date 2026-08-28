---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsGuardDutyDetectorDataSourcesDetails.html
---

# AwsGuardDutyDetectorDataSourcesDetails
<a name="API_AwsGuardDutyDetectorDataSourcesDetails"></a>

 Describes which data sources are activated for the detector.

## Contents
<a name="API_AwsGuardDutyDetectorDataSourcesDetails_Contents"></a>

 ** CloudTrail **   <a name="securityhub-Type-AwsGuardDutyDetectorDataSourcesDetails-CloudTrail"></a>
 An object that contains information on the status of CloudTrail as a data source for the detector.
Type: [AwsGuardDutyDetectorDataSourcesCloudTrailDetails](API_AwsGuardDutyDetectorDataSourcesCloudTrailDetails.md) object
Required: No

 ** DnsLogs **   <a name="securityhub-Type-AwsGuardDutyDetectorDataSourcesDetails-DnsLogs"></a>
 An object that contains information on the status of DNS logs as a data source for the detector.
Type: [AwsGuardDutyDetectorDataSourcesDnsLogsDetails](API_AwsGuardDutyDetectorDataSourcesDnsLogsDetails.md) object
Required: No

 ** FlowLogs **   <a name="securityhub-Type-AwsGuardDutyDetectorDataSourcesDetails-FlowLogs"></a>
 An object that contains information on the status of VPC Flow Logs as a data source for the detector.
Type: [AwsGuardDutyDetectorDataSourcesFlowLogsDetails](API_AwsGuardDutyDetectorDataSourcesFlowLogsDetails.md) object
Required: No

 ** Kubernetes **   <a name="securityhub-Type-AwsGuardDutyDetectorDataSourcesDetails-Kubernetes"></a>
 An object that contains information on the status of Kubernetes data sources for the detector.
Type: [AwsGuardDutyDetectorDataSourcesKubernetesDetails](API_AwsGuardDutyDetectorDataSourcesKubernetesDetails.md) object
Required: No

 ** MalwareProtection **   <a name="securityhub-Type-AwsGuardDutyDetectorDataSourcesDetails-MalwareProtection"></a>
 An object that contains information on the status of Malware Protection as a data source for the detector.
Type: [AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails](API_AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails.md) object
Required: No

 ** S3Logs **   <a name="securityhub-Type-AwsGuardDutyDetectorDataSourcesDetails-S3Logs"></a>
 An object that contains information on the status of S3 Data event logs as a data source for the detector.
Type: [AwsGuardDutyDetectorDataSourcesS3LogsDetails](API_AwsGuardDutyDetectorDataSourcesS3LogsDetails.md) object
Required: No

## See Also
<a name="API_AwsGuardDutyDetectorDataSourcesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsGuardDutyDetectorDataSourcesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsGuardDutyDetectorDataSourcesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsGuardDutyDetectorDataSourcesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
