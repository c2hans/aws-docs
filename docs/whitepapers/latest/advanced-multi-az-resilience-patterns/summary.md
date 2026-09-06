---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/summary.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Summary
<a name="summary"></a>

 This section described three approaches to help identify single Availability Zone impairments. Each approach should be used together to provide a holistic view of your workload’s health.

The CloudWatch composite alarm approach allows you to find problems where the skew in availability isn’t statistically significant, say availabilities of 98% (the impaired Availability Zone), 100%, and 99.99%, that isn’t caused by a single, shared resource.

Outlier detection will help detect single Availability Zone impairments where you have uncorrelated errors happening in multiple Availability Zones that all surpass your alarm threshold.

Finally, identifying degradation of a single instance zonal resource helps discover when an Availability Zone impairment affects a resource that is shared across Availability Zones.

The resulting alarms from each one of these patterns can be combined into a CloudWatch composite alarm hierarchy to discover when single Availability Zone impairments occur and have impact to the availability or latency of your workload.
