---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationMaintenanceConfigurationDescription.html
---

# ApplicationMaintenanceConfigurationDescription
<a name="API_ApplicationMaintenanceConfigurationDescription"></a>

The details of the maintenance configuration for the application.

## Contents
<a name="API_ApplicationMaintenanceConfigurationDescription_Contents"></a>

 ** ApplicationMaintenanceWindowEndTime **   <a name="APIReference-Type-ApplicationMaintenanceConfigurationDescription-ApplicationMaintenanceWindowEndTime"></a>
The end time for the maintenance window.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `([01][0-9]|2[0-3]):[0-5][0-9]`
Required: Yes

 ** ApplicationMaintenanceWindowStartTime **   <a name="APIReference-Type-ApplicationMaintenanceConfigurationDescription-ApplicationMaintenanceWindowStartTime"></a>
The start time for the maintenance window.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `([01][0-9]|2[0-3]):[0-5][0-9]`
Required: Yes

## See Also
<a name="API_ApplicationMaintenanceConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationMaintenanceConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationMaintenanceConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationMaintenanceConfigurationDescription)
