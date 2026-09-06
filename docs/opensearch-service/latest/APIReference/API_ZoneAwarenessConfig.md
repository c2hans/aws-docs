---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ZoneAwarenessConfig.html
---

# ZoneAwarenessConfig
<a name="API_ZoneAwarenessConfig"></a>

The zone awareness configuration for an Amazon OpenSearch Service domain.

## Contents
<a name="API_ZoneAwarenessConfig_Contents"></a>

 ** AvailabilityZoneCount **   <a name="opensearchservice-Type-ZoneAwarenessConfig-AvailabilityZoneCount"></a>
If you enabled multiple Availability Zones, this value is the number of zones that you want the domain to use. Valid values are `2` and `3`. If your domain is provisioned within a VPC, this value be equal to number of subnets.
Type: Integer
Required: No

## See Also
<a name="API_ZoneAwarenessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ZoneAwarenessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ZoneAwarenessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ZoneAwarenessConfig)
