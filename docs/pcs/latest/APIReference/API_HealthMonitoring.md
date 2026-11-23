---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_HealthMonitoring.html
---

# HealthMonitoring

The health monitoring settings of a compute node group. Health monitoring continuously checks running instances for hardware and software faults.

## Contents
<a name="API_HealthMonitoring_Contents"></a>

 ** mode **   <a name="PCS-Type-HealthMonitoring-mode"></a>
The health monitoring mode. This value is required when you specify `healthMonitoring`. There is no default value. Valid values:
+  `NONE` – Turns off health monitoring. You can't specify `repairAction` with this mode.
+  `STANDARD` – Continuously checks running instances for hardware and software faults.
Type: String
Valid Values: `NONE | STANDARD`
Required: No

 ** repairAction **   <a name="PCS-Type-HealthMonitoring-repairAction"></a>
The action that AWS PCS takes when health monitoring finds a fault on an instance. You can't specify this value when `mode` is `NONE`. If you don't specify this value and `mode` isn't `NONE`, AWS PCS uses `AUTO`. `GetComputeNodeGroup` doesn't return a `repairAction` that you didn't specify. Valid values:
+  `AUTO` – AWS PCS chooses the repair action based on the fault.
+  `REPLACE` – Replaces the instance after running jobs finish.
+  `ISOLATE` – Stops new jobs on the instance and keeps the instance running until you investigate.
+  `NONE` – Records the fault in Slurm and leaves the instance available for jobs.
Type: String
Valid Values: `AUTO | REPLACE | ISOLATE | NONE`
Required: No

## See Also
<a name="API_HealthMonitoring_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/HealthMonitoring)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/HealthMonitoring)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/HealthMonitoring)
