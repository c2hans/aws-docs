---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDatabaseProjectedMetric.html
---

# RDSDatabaseProjectedMetric
<a name="API_RDSDatabaseProjectedMetric"></a>

 Describes the projected metrics of an Amazon Aurora and RDS database recommendation option.

 To determine the performance difference between your current Amazon Aurora and RDS database and the recommended option, compare the metric data of your service against its projected metric data.

## Contents
<a name="API_RDSDatabaseProjectedMetric_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-RDSDatabaseProjectedMetric-name"></a>
 The name of the projected metric.
Type: String
Valid Values: `CPU | Memory | EBSVolumeStorageSpaceUtilization | NetworkReceiveThroughput | NetworkTransmitThroughput | EBSVolumeReadIOPS | EBSVolumeWriteIOPS | EBSVolumeReadThroughput | EBSVolumeWriteThroughput | DatabaseConnections | StorageNetworkReceiveThroughput | StorageNetworkTransmitThroughput | AuroraMemoryHealthState | AuroraMemoryNumDeclinedSql | AuroraMemoryNumKillConnTotal | AuroraMemoryNumKillQueryTotal | ReadIOPSEphemeralStorage | WriteIOPSEphemeralStorage | VolumeReadIOPs | VolumeBytesUsed | VolumeWriteIOPs`
Required: No

 ** timestamps **   <a name="computeoptimizer-Type-RDSDatabaseProjectedMetric-timestamps"></a>
 The timestamps of the projected metric.
Type: Array of timestamps
Required: No

 ** values **   <a name="computeoptimizer-Type-RDSDatabaseProjectedMetric-values"></a>
 The values for the projected metric.
Type: Array of doubles
Required: No

## See Also
<a name="API_RDSDatabaseProjectedMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RDSDatabaseProjectedMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RDSDatabaseProjectedMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RDSDatabaseProjectedMetric)
