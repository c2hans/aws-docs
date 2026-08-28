---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ReportDefinition.html
---

# ReportDefinition
<a name="API_cur_ReportDefinition"></a>

The definition of AWS Cost and Usage Report. You can specify the report name, time unit, report format, compression format, S3 bucket, additional artifacts, and schema elements in the definition.

## Contents
<a name="API_cur_ReportDefinition_Contents"></a>

 ** AdditionalSchemaElements **   <a name="awscostmanagement-Type-cur_ReportDefinition-AdditionalSchemaElements"></a>
A list of strings that indicate additional content that AWS includes in the report, such as individual resource IDs.
Type: Array of strings
Valid Values: `RESOURCES | SPLIT_COST_ALLOCATION_DATA | MANUAL_DISCOUNT_COMPATIBILITY`
Required: Yes

 ** Compression **   <a name="awscostmanagement-Type-cur_ReportDefinition-Compression"></a>
The compression format that AWS uses for the report.
If you choose `Parquet` for the `Compression`, you must also specify `Parquet` for the `Format` parameter.
If you choose `ZIP` or `GZIP` for the `Compression`, you must specify `textORcsv` for the `Format` parameter.
Type: String
Valid Values: `ZIP | GZIP | Parquet`
Required: Yes

 ** Format **   <a name="awscostmanagement-Type-cur_ReportDefinition-Format"></a>
The format that AWS saves the report in.
If you choose `Parquet` for the `Format`, you must also specify `Parquet` for the `Compression` parameter.
If you choose `textORcsv` for the `Format`, you must specify `ZIP` or `GZIP` for the `Compression` parameter.
Type: String
Valid Values: `textORcsv | Parquet`
Required: Yes

 ** ReportName **   <a name="awscostmanagement-Type-cur_ReportDefinition-ReportName"></a>
The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[0-9A-Za-z!\-_.*\'()]+`
Required: Yes

 ** S3Bucket **   <a name="awscostmanagement-Type-cur_ReportDefinition-S3Bucket"></a>
The S3 bucket where AWS delivers the report. The S3 bucket must be owned by the AWS account that was used to create the report.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[A-Za-z0-9_\.\-]+`
Required: Yes

 ** S3Prefix **   <a name="awscostmanagement-Type-cur_ReportDefinition-S3Prefix"></a>
The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[0-9A-Za-z!\-_.*\'()/]*`
Required: Yes

 ** S3Region **   <a name="awscostmanagement-Type-cur_ReportDefinition-S3Region"></a>
The region of the S3 bucket that AWS delivers the report into.
Type: String
Valid Values: `af-south-1 | ap-east-1 | ap-south-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-northeast-1 | ap-northeast-2 | ap-northeast-3 | ca-central-1 | eu-central-1 | eu-central-2 | eu-west-1 | eu-west-2 | eu-west-3 | eu-north-1 | eu-south-1 | eu-south-2 | me-central-1 | me-south-1 | sa-east-1 | us-east-1 | us-east-2 | us-west-1 | us-west-2 | cn-north-1 | cn-northwest-1`
Required: Yes

 ** TimeUnit **   <a name="awscostmanagement-Type-cur_ReportDefinition-TimeUnit"></a>
The length of time covered by the report.
Type: String
Valid Values: `HOURLY | DAILY | MONTHLY`
Required: Yes

 ** AdditionalArtifacts **   <a name="awscostmanagement-Type-cur_ReportDefinition-AdditionalArtifacts"></a>
A list of manifests that you want AWS to create for this report.
Type: Array of strings
Valid Values: `REDSHIFT | QUICKSIGHT | ATHENA`
Required: No

 ** BillingViewArn **   <a name="awscostmanagement-Type-cur_ReportDefinition-BillingViewArn"></a>
 The Amazon resource name of the billing view. The `BillingViewArn` is needed to create AWS Cost and Usage Report for each billing group maintained in the AWS Billing Conductor service. The `BillingViewArn` for a billing group can be constructed as: `arn:aws:billing::payer-account-id:billingview/billing-group-primary-account-id` or retrieved by calling the [ListBillingViews](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListBillingViews.html) API.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `(arn:aws(-cn)?:billing::[0-9]{12}:billingview/)?[a-zA-Z0-9_\+=\.\-@].{1,30}`
Required: No

 ** RefreshClosedReports **   <a name="awscostmanagement-Type-cur_ReportDefinition-RefreshClosedReports"></a>
Whether you want AWS to update your reports after they have been finalized if AWS detects charges related to previous months. These charges can include refunds, credits, or support fees.
Type: Boolean
Required: No

 ** ReportStatus **   <a name="awscostmanagement-Type-cur_ReportDefinition-ReportStatus"></a>
The status of the report.
Type: [ReportStatus](API_cur_ReportStatus.md) object
Required: No

 ** ReportVersioning **   <a name="awscostmanagement-Type-cur_ReportDefinition-ReportVersioning"></a>
Whether you want AWS to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
Type: String
Valid Values: `CREATE_NEW_REPORT | OVERWRITE_REPORT`
Required: No

## See Also
<a name="API_cur_ReportDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cur-2017-01-06/ReportDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cur-2017-01-06/ReportDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cur-2017-01-06/ReportDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
