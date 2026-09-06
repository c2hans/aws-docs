---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_SnapshotSchedule.html
---

# SnapshotSchedule
<a name="API_SnapshotSchedule"></a>

Describes a snapshot schedule. You can set a regular interval for creating snapshots of a cluster. You can also schedule snapshots for specific dates.

## Contents
<a name="API_SnapshotSchedule_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AssociatedClusterCount **
The number of clusters associated with the schedule.
Type: Integer
Required: No

 ** AssociatedClusters.ClusterAssociatedToSchedule.N **
A list of clusters associated with the schedule. A maximum of 100 clusters is returned.
Type: Array of [ClusterAssociatedToSchedule](API_ClusterAssociatedToSchedule.md) objects
Required: No

 ** NextInvocations.SnapshotTime.N **

Type: Array of timestamps
Required: No

 ** ScheduleDefinitions.ScheduleDefinition.N **
A list of ScheduleDefinitions.
Type: Array of strings
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ScheduleDescription **
The description of the schedule.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ScheduleIdentifier **
A unique identifier for the schedule.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Tags.Tag.N **
An optional set of tags describing the schedule.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_SnapshotSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/SnapshotSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/SnapshotSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/SnapshotSchedule)
