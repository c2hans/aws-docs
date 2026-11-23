---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_InstanceHealthChecks.html
---

# InstanceHealthChecks

The instance health check settings of a compute node group. Instance health checks detect faults on instances in the compute node group and respond with the repair action that you choose.

## Contents
<a name="API_InstanceHealthChecks_Contents"></a>

 ** deepHealthChecks **   <a name="PCS-Type-InstanceHealthChecks-deepHealthChecks"></a>
The deep health check settings. Deep health checks test the graphics processing units (GPUs) of an instance each time it starts, including after a reboot, before it accepts jobs.
Type: [DeepHealthChecks](API_DeepHealthChecks.md) object
Required: No

 ** healthMonitoring **   <a name="PCS-Type-InstanceHealthChecks-healthMonitoring"></a>
The health monitoring settings. Health monitoring continuously checks running instances for hardware and software faults.
Type: [HealthMonitoring](API_HealthMonitoring.md) object
Required: No

## See Also
<a name="API_InstanceHealthChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/InstanceHealthChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/InstanceHealthChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/InstanceHealthChecks)
