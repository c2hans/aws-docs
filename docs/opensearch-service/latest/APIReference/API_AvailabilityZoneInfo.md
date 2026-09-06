---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AvailabilityZoneInfo.html
---

# AvailabilityZoneInfo
<a name="API_AvailabilityZoneInfo"></a>

Information about an Availability Zone on a domain.

## Contents
<a name="API_AvailabilityZoneInfo_Contents"></a>

 ** AvailabilityZoneName **   <a name="opensearchservice-Type-AvailabilityZoneInfo-AvailabilityZoneName"></a>
The name of the Availability Zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Required: No

 ** AvailableDataNodeCount **   <a name="opensearchservice-Type-AvailabilityZoneInfo-AvailableDataNodeCount"></a>
The number of data nodes active in the Availability Zone.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`
Required: No

 ** ConfiguredDataNodeCount **   <a name="opensearchservice-Type-AvailabilityZoneInfo-ConfiguredDataNodeCount"></a>
The total number of data nodes configured in the Availability Zone.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`
Required: No

 ** TotalShards **   <a name="opensearchservice-Type-AvailabilityZoneInfo-TotalShards"></a>
The total number of primary and replica shards in the Availability Zone.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`
Required: No

 ** TotalUnAssignedShards **   <a name="opensearchservice-Type-AvailabilityZoneInfo-TotalUnAssignedShards"></a>
The total number of primary and replica shards that aren't allocated to any of the nodes in the Availability Zone.
Type: String
Pattern: `^((\d+)|(NotAvailable))$`
Required: No

 ** ZoneStatus **   <a name="opensearchservice-Type-AvailabilityZoneInfo-ZoneStatus"></a>
The current state of the Availability Zone. Current options are `Active` and `StandBy`.
+  `Active` - Data nodes in the Availability Zone are in use.
+  `StandBy` - Data nodes in the Availability Zone are in a standby state.
+  `NotAvailable` - Unable to retrieve information.
Type: String
Valid Values: `Active | StandBy | NotAvailable`
Required: No

## See Also
<a name="API_AvailabilityZoneInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AvailabilityZoneInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AvailabilityZoneInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AvailabilityZoneInfo)
