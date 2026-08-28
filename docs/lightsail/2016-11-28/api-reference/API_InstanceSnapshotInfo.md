---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstanceSnapshotInfo.html
---

# InstanceSnapshotInfo
<a name="API_InstanceSnapshotInfo"></a>

Describes an instance snapshot.

## Contents
<a name="API_InstanceSnapshotInfo_Contents"></a>

 ** fromBlueprintId **   <a name="Lightsail-Type-InstanceSnapshotInfo-fromBlueprintId"></a>
The blueprint ID from which the source instance (`amazon_linux_2023`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** fromBundleId **   <a name="Lightsail-Type-InstanceSnapshotInfo-fromBundleId"></a>
The bundle ID from which the source instance was created (`micro_x_x`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** fromDiskInfo **   <a name="Lightsail-Type-InstanceSnapshotInfo-fromDiskInfo"></a>
A list of objects describing the disks that were attached to the source instance.
Type: Array of [DiskInfo](API_DiskInfo.md) objects
Required: No

## See Also
<a name="API_InstanceSnapshotInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstanceSnapshotInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstanceSnapshotInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstanceSnapshotInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
