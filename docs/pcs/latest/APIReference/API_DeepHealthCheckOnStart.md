---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_DeepHealthCheckOnStart.html
---

# DeepHealthCheckOnStart

The deep health check that runs each time an instance starts, including after a reboot, before the compute node accepts jobs.

## Contents
<a name="API_DeepHealthCheckOnStart_Contents"></a>

 ** profile **   <a name="PCS-Type-DeepHealthCheckOnStart-profile"></a>
The deep health check profile to run. Each profile other than `NONE` runs NVIDIA Data Center GPU Manager (DCGM) diagnostics. More thorough profiles run more tests and add more time to instance launch. A profile other than `NONE` requires instance types with NVIDIA GPUs. This value is required when you specify `onStart`. There is no default value. Valid values:
+  `NONE` – Turns off the deep health check. You can't specify `repairAction` with this profile.
+  `QUICK` – Runs basic GPU tests (DCGM diagnostics level 1). This profile adds the least time to instance launch.
+  `MEDIUM` – Runs extended GPU tests (DCGM diagnostics level 2).
+  `LONG` – Runs GPU stress and diagnostic tests (DCGM diagnostics level 3). This profile adds the most time to instance launch.
Type: String
Valid Values: `NONE | QUICK | MEDIUM | LONG`
Required: No

 ** repairAction **   <a name="PCS-Type-DeepHealthCheckOnStart-repairAction"></a>
The action that AWS PCS takes when an instance fails the deep health check. You can't specify this value when `profile` is `NONE`. If you don't specify this value and `profile` isn't `NONE`, AWS PCS uses `AUTO`. `GetComputeNodeGroup` doesn't return a `repairAction` that you didn't specify. Valid values:
+  `AUTO` – AWS PCS chooses the repair action based on the fault.
+  `REPLACE` – Replaces the instance before it accepts jobs.
+  `ISOLATE` – Stops new jobs on the instance and keeps the instance running until you investigate.
+  `NONE` – Records the fault in Slurm and leaves the instance available for jobs.
Type: String
Valid Values: `AUTO | REPLACE | ISOLATE | NONE`
Required: No

## See Also
<a name="API_DeepHealthCheckOnStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/DeepHealthCheckOnStart)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/DeepHealthCheckOnStart)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/DeepHealthCheckOnStart)
