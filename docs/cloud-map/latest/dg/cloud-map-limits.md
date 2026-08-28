---
source_url: https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html
---

# AWS Cloud Map service quotas
<a name="cloud-map-limits"></a>

AWS Cloud Map resources are subject to the following account-level service quotas. Each quota listed applies to each AWS Region where you create AWS Cloud Map resources.

| Name | Default | Adjustable | Description |
| --- | --- | --- | --- |
| Custom attributes per instance | Each supported Region: 30 | No | The maximum number of custom attributes that you can specify when you register an instance. |
| DiscoverInstances operation per account burst rate | Each supported Region: 2,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/AWSCloudMap/quotas/L-76CF203B)  | The maximum burst rate to call DiscoverInstances operation from a single account. |
| DiscoverInstances operation per account steady rate | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/AWSCloudMap/quotas/L-514A639A)  | The maximum steady rate to call DiscoverInstances operation from a single account. |
| DiscoverInstancesRevision operation per account rate | Each supported Region: 3,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/AWSCloudMap/quotas/L-0BA10AAE)  | The maximum rate to call DiscoverInstancesRevision operation from a single account. |
| Instances per namespace | Each supported Region: 2,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/AWSCloudMap/quotas/L-D95E8A57)  | The maximum number of service instances that you can register using the same namespace. |
| Instances per service | Each supported Region: 1,000 | No | The maximum number of instances that you can register in a Region using the same service. |
| Namespaces per Region | Each supported Region: 50 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/AWSCloudMap/quotas/L-0FE3F50E)  | The maximum number of namespaces that you can create per Region. |

**\*** When you create a namespace, we automatically create an Amazon Route 53 hosted zone. This hosted zone counts against the quota on the number of hosted zones that you can create with an AWS account. For more information, see [Quotas on hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-hosted-zones) in the *Amazon Route 53 Developer Guide*.

**\*\*** Increasing the instances for DNS namespaces for AWS Cloud Map requires an increase to the records per hosted zone Route 53 limit, which incurs additional charges.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
