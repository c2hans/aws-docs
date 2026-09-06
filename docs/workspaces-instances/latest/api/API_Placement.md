---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_Placement.html
---

# Placement
<a name="API_Placement"></a>

Defines instance placement configuration for WorkSpace Instance.

## Contents
<a name="API_Placement_Contents"></a>

 ** Affinity **   <a name="workspacesinstances-Type-Placement-Affinity"></a>
Specifies host affinity for dedicated instances.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** AvailabilityZone **   <a name="workspacesinstances-Type-Placement-AvailabilityZone"></a>
Identifies the specific AWS availability zone.
Type: String
Pattern: `[a-z]{2}-[a-z]+-\d(?:[a-z]|-[a-z]+-\d[a-z])`
Required: No

 ** GroupId **   <a name="workspacesinstances-Type-Placement-GroupId"></a>
Unique identifier for placement group.
Type: String
Pattern: `pg-[0-9a-zA-Z]{1,63}`
Required: No

 ** GroupName **   <a name="workspacesinstances-Type-Placement-GroupName"></a>
Name of the placement group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** HostId **   <a name="workspacesinstances-Type-Placement-HostId"></a>
Identifies the specific dedicated host.
Type: String
Pattern: `h-[0-9a-zA-Z]{1,63}`
Required: No

 ** HostResourceGroupArn **   <a name="workspacesinstances-Type-Placement-HostResourceGroupArn"></a>
ARN of the host resource group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** PartitionNumber **   <a name="workspacesinstances-Type-Placement-PartitionNumber"></a>
Specifies partition number for partition placement groups.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Tenancy **   <a name="workspacesinstances-Type-Placement-Tenancy"></a>
Defines instance tenancy configuration.
Type: String
Valid Values: `default | dedicated | host`
Required: No

## See Also
<a name="API_Placement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/Placement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/Placement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/Placement)
