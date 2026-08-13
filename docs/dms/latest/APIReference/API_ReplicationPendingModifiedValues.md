---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationPendingModifiedValues.html
---

# ReplicationPendingModifiedValues
<a name="API_ReplicationPendingModifiedValues"></a>

Provides information about the values of pending modifications to a replication instance. This data type is an object of the [`ReplicationInstance`](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationInstance.html) user-defined data type.

## Contents
<a name="API_ReplicationPendingModifiedValues_Contents"></a>

 ** AllocatedStorage **   <a name="DMS-Type-ReplicationPendingModifiedValues-AllocatedStorage"></a>
The amount of storage (in gigabytes) that is allocated for the replication instance.
Type: Integer
Required: No

 ** EngineVersion **   <a name="DMS-Type-ReplicationPendingModifiedValues-EngineVersion"></a>
The engine version number of the replication instance.
Type: String
Required: No

 ** MultiAZ **   <a name="DMS-Type-ReplicationPendingModifiedValues-MultiAZ"></a>
 Specifies whether the replication instance is a Multi-AZ deployment. You can't set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to `true`.
Type: Boolean
Required: No

 ** NetworkType **   <a name="DMS-Type-ReplicationPendingModifiedValues-NetworkType"></a>
The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.
Type: String
Required: No

 ** ReplicationInstanceClass **   <a name="DMS-Type-ReplicationPendingModifiedValues-ReplicationInstanceClass"></a>
The compute and memory capacity of the replication instance as defined for the specified replication instance class.
For more information on the settings and capacities for the available replication instance classes, see [ Selecting the right AWS DMS replication instance for your migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth).
Type: String
Length Constraints: Maximum length of 30.
Required: No

## See Also
<a name="API_ReplicationPendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationPendingModifiedValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationPendingModifiedValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationPendingModifiedValues)
