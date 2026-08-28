---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_QueueSnapshotCapacityUsage.html
---

# QueueSnapshotCapacityUsage
<a name="API_QueueSnapshotCapacityUsage"></a>

The configured capacity usage for a job queue snapshot, including the unit of measure and quantity of resources being used.

## Contents
<a name="API_QueueSnapshotCapacityUsage_Contents"></a>

 ** capacityUnit **   <a name="Batch-Type-QueueSnapshotCapacityUsage-capacityUnit"></a>
The unit of measure for the capacity usage. For compute jobs, this is `VCPU` for Amazon EC2 and `cpu` for Amazon EKS. For service jobs, this is the instance type.
Type: String
Required: No

 ** quantity **   <a name="Batch-Type-QueueSnapshotCapacityUsage-quantity"></a>
The quantity of capacity being used in the queue snapshot, measured in the units specified by `capacityUnit`.
Type: Double
Required: No

## See Also
<a name="API_QueueSnapshotCapacityUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QueueSnapshotCapacityUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QueueSnapshotCapacityUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QueueSnapshotCapacityUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
