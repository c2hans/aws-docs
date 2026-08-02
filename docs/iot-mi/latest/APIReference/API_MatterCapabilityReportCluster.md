---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_MatterCapabilityReportCluster.html
---

# MatterCapabilityReportCluster
<a name="API_MatterCapabilityReportCluster"></a>

Capability used in Matter capability report.

## Contents
<a name="API_MatterCapabilityReportCluster_Contents"></a>

 ** id **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-id"></a>
The id of the AWS Matter capability report cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: Yes

 ** revision **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-revision"></a>
The id of the revision for the AWS Matter capability report.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

 ** attributes **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-attributes"></a>
The attributes of the AWS Matter capability report.
Type: Array of [MatterCapabilityReportAttribute](API_MatterCapabilityReportAttribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** commands **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-commands"></a>
The commands used with the AWS Matter capability report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: No

 ** events **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-events"></a>
The events used with the AWS Matter capability report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: No

 ** fabricIndex **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-fabricIndex"></a>
The fabric index for the AWS Matter capability report.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 4096.
Required: No

 ** featureMap **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-featureMap"></a>
32 bit-map used to indicate which features a cluster supports.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** generatedCommands **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-generatedCommands"></a>
Matter clusters used in capability report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: No

 ** name **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-name"></a>
The capability name used in the AWS Matter capability report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/a-zA-Z0-9\._ -]+`
Required: No

 ** publicId **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-publicId"></a>
The id of the schema version.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+@(\d+\.\d+(\.\d+)?|\$latest)`
Required: No

 ** specVersion **   <a name="managedintegrations-Type-MatterCapabilityReportCluster-specVersion"></a>
The spec version used in the AWS Matter capability report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\d+\.\d+`
Required: No

## See Also
<a name="API_MatterCapabilityReportCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/MatterCapabilityReportCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/MatterCapabilityReportCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/MatterCapabilityReportCluster)
