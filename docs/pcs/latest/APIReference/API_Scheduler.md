---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_Scheduler.html
---

# Scheduler
<a name="API_Scheduler"></a>

The cluster management and job scheduling software associated with the cluster.

## Contents
<a name="API_Scheduler_Contents"></a>

 ** type **   <a name="PCS-Type-Scheduler-type"></a>
The software AWS PCS uses to manage cluster scaling and job scheduling.
Type: String
Valid Values: `SLURM`
Required: Yes

 ** version **   <a name="PCS-Type-Scheduler-version"></a>
The version of the specified scheduling software that AWS PCS uses to manage cluster scaling and job scheduling. You can update this version using the `UpdateCluster` API action. For more information, see [Updating the scheduler version on a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html) and [Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions.html) in the * AWS PCS User Guide*.
Valid Values: `23.11 | 24.05 | 24.11 | 25.05 | 25.11`
Type: String
Required: Yes

## See Also
<a name="API_Scheduler_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/Scheduler)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/Scheduler)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/Scheduler)
