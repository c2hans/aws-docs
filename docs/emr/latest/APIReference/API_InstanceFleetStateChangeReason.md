---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_InstanceFleetStateChangeReason.html
---

# InstanceFleetStateChangeReason
<a name="API_InstanceFleetStateChangeReason"></a>

Provides status change reason details for the instance fleet.

**Note**
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceFleetStateChangeReason_Contents"></a>

 ** Code **   <a name="EMR-Type-InstanceFleetStateChangeReason-Code"></a>
A code corresponding to the reason the state change occurred.
Type: String
Valid Values: `INTERNAL_ERROR | VALIDATION_ERROR | INSTANCE_FAILURE | CLUSTER_TERMINATED`
Required: No

 ** Message **   <a name="EMR-Type-InstanceFleetStateChangeReason-Message"></a>
An explanatory message.
Type: String
Required: No

## See Also
<a name="API_InstanceFleetStateChangeReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetStateChangeReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetStateChangeReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetStateChangeReason)
