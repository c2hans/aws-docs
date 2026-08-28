---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_S3OutputConfigurations.html
---

# S3OutputConfigurations
<a name="API_DataExports_S3OutputConfigurations"></a>

The compression type, file format, and overwrite preference for the data export.

## Contents
<a name="API_DataExports_S3OutputConfigurations_Contents"></a>

 ** Compression **   <a name="awscostmanagement-Type-DataExports_S3OutputConfigurations-Compression"></a>
The compression type for the data export.
Type: String
Valid Values: `GZIP | PARQUET | ZIP`
Required: Yes

 ** Format **   <a name="awscostmanagement-Type-DataExports_S3OutputConfigurations-Format"></a>
The file format for the data export.
Type: String
Valid Values: `TEXT_OR_CSV | PARQUET`
Required: Yes

 ** OutputType **   <a name="awscostmanagement-Type-DataExports_S3OutputConfigurations-OutputType"></a>
The output type for the data export.
Type: String
Valid Values: `CUSTOM | ATHENA | REDSHIFT`
Required: Yes

 ** Overwrite **   <a name="awscostmanagement-Type-DataExports_S3OutputConfigurations-Overwrite"></a>
The rule to follow when generating a version of the data export file. You have the choice to overwrite the previous version or to be delivered in addition to the previous versions. Overwriting exports can save on Amazon S3 storage costs. Creating new export versions allows you to track the changes in cost and usage data over time.
Type: String
Valid Values: `CREATE_NEW_REPORT | OVERWRITE_REPORT`
Required: Yes

## See Also
<a name="API_DataExports_S3OutputConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/S3OutputConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/S3OutputConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/S3OutputConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
