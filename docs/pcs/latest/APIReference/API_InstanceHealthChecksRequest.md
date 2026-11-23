---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_InstanceHealthChecksRequest.html
---

# InstanceHealthChecksRequest

The instance health check settings to configure on a compute node group when you create it. Specify `healthMonitoring`, `deepHealthChecks`, or both. You can't specify an empty object (`{}`).

## Contents
<a name="API_InstanceHealthChecksRequest_Contents"></a>

 ** deepHealthChecks **   <a name="PCS-Type-InstanceHealthChecksRequest-deepHealthChecks"></a>
The deep health check settings. Deep health checks test the graphics processing units (GPUs) of an instance each time it starts, including after a reboot, before it accepts jobs. If you specify this object, it can't be empty.
Type: [DeepHealthChecks](API_DeepHealthChecks.md) object
Required: No

 ** healthMonitoring **   <a name="PCS-Type-InstanceHealthChecksRequest-healthMonitoring"></a>
The health monitoring settings. Health monitoring continuously checks running instances for hardware and software faults. If you specify this object, it can't be empty.
Type: [HealthMonitoring](API_HealthMonitoring.md) object
Required: No

## See Also
<a name="API_InstanceHealthChecksRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/InstanceHealthChecksRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/InstanceHealthChecksRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/InstanceHealthChecksRequest)
