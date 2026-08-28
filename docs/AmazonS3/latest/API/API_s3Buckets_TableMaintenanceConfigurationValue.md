---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableMaintenanceConfigurationValue.html
---

# TableMaintenanceConfigurationValue
<a name="API_s3Buckets_TableMaintenanceConfigurationValue"></a>

The values that define a maintenance configuration for a table.

## Contents
<a name="API_s3Buckets_TableMaintenanceConfigurationValue_Contents"></a>

 ** settings **   <a name="AmazonS3-Type-s3Buckets_TableMaintenanceConfigurationValue-settings"></a>
Contains details about the settings for the maintenance configuration.
Type: [TableMaintenanceSettings](API_s3Buckets_TableMaintenanceSettings.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** status **   <a name="AmazonS3-Type-s3Buckets_TableMaintenanceConfigurationValue-status"></a>
The status of the maintenance configuration.
Type: String
Valid Values: `enabled | disabled`
Required: No

## See Also
<a name="API_s3Buckets_TableMaintenanceConfigurationValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableMaintenanceConfigurationValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableMaintenanceConfigurationValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableMaintenanceConfigurationValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
