---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_DeepHealthChecks.html
---

# DeepHealthChecks

The deep health check settings of a compute node group. Deep health checks test the graphics processing units (GPUs) of an instance each time it starts, including after a reboot, before it accepts jobs. Deep health checks with a profile other than `NONE` require instance types with NVIDIA GPUs.

## Contents
<a name="API_DeepHealthChecks_Contents"></a>

 ** onStart **   <a name="PCS-Type-DeepHealthChecks-onStart"></a>
The deep health check to run each time an instance starts, including after a reboot, before the compute node accepts jobs. If the check fails after a reboot, AWS PCS takes the same `repairAction` as at launch. For example, with `REPLACE`, AWS PCS replaces the instance instead of returning it to service. If the compute node group has scripts in the `nodeBootstrapped` stage of `nodeLifecycleActions`, the deep health check runs after those scripts. If a script fails and its `onError` setting terminates the compute node, the deep health check doesn't run. This value is required when you specify `deepHealthChecks`.
Type: [DeepHealthCheckOnStart](API_DeepHealthCheckOnStart.md) object
Required: No

## See Also
<a name="API_DeepHealthChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/DeepHealthChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/DeepHealthChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/DeepHealthChecks)
