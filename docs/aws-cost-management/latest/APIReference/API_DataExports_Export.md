---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_Export.html
---

# Export
<a name="API_DataExports_Export"></a>

The details that are available for an export.

## Contents
<a name="API_DataExports_Export_Contents"></a>

 ** DataQuery **   <a name="awscostmanagement-Type-DataExports_Export-DataQuery"></a>
The data query for this specific data export.
Type: [DataQuery](API_DataExports_DataQuery.md) object
Required: Yes

 ** DestinationConfigurations **   <a name="awscostmanagement-Type-DataExports_Export-DestinationConfigurations"></a>
The destination configuration for this specific data export.
Type: [DestinationConfigurations](API_DataExports_DestinationConfigurations.md) object
Required: Yes

 ** Name **   <a name="awscostmanagement-Type-DataExports_Export-Name"></a>
The name of this specific data export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9A-Za-z\-_]+`
Required: Yes

 ** RefreshCadence **   <a name="awscostmanagement-Type-DataExports_Export-RefreshCadence"></a>
The cadence for AWS to update the export in your S3 bucket.
Type: [RefreshCadence](API_DataExports_RefreshCadence.md) object
Required: Yes

 ** Description **   <a name="awscostmanagement-Type-DataExports_Export-Description"></a>
The description for this specific data export.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ExportArn **   <a name="awscostmanagement-Type-DataExports_Export-ExportArn"></a>
The Amazon Resource Name (ARN) for this export.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: No

## See Also
<a name="API_DataExports_Export_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/Export)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/Export)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/Export)
