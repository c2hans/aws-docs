---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterDeferredMaintenanceWindow.html
---

# AwsRedshiftClusterDeferredMaintenanceWindow
<a name="API_AwsRedshiftClusterDeferredMaintenanceWindow"></a>

A time windows during which maintenance was deferred for an Amazon Redshift cluster.

## Contents
<a name="API_AwsRedshiftClusterDeferredMaintenanceWindow_Contents"></a>

 ** DeferMaintenanceEndTime **   <a name="securityhub-Type-AwsRedshiftClusterDeferredMaintenanceWindow-DeferMaintenanceEndTime"></a>
The end of the time window for which maintenance was deferred.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeferMaintenanceIdentifier **   <a name="securityhub-Type-AwsRedshiftClusterDeferredMaintenanceWindow-DeferMaintenanceIdentifier"></a>
The identifier of the maintenance window.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeferMaintenanceStartTime **   <a name="securityhub-Type-AwsRedshiftClusterDeferredMaintenanceWindow-DeferMaintenanceStartTime"></a>
The start of the time window for which maintenance was deferred.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRedshiftClusterDeferredMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterDeferredMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterDeferredMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterDeferredMaintenanceWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
