---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RegionalConfiguration.html
---

# RegionalConfiguration
<a name="API_RegionalConfiguration"></a>

A list of the replication groups

## Contents
<a name="API_RegionalConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ReplicationGroupId **
The name of the secondary cluster
Type: String
Required: Yes

 ** ReplicationGroupRegion **
The Amazon region where the cluster is stored
Type: String
Required: Yes

 ** ReshardingConfiguration.ReshardingConfiguration.N **
A list of `PreferredAvailabilityZones` objects that specifies the configuration of a node group in the resharded cluster.
Type: Array of [ReshardingConfiguration](API_ReshardingConfiguration.md) objects
Required: Yes

## See Also
<a name="API_RegionalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/RegionalConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/RegionalConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/RegionalConfiguration)
