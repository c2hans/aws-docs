---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html
---

# Amazon WorkSpaces Applications Service Quotas
<a name="limits"></a>

WorkSpaces Applications provides different resources that you can use. WorkSpaces Applications resources include stacks, fleets, images, and image builders. When you create your Amazon Web Services account, we set default quotas (also referred to as limits) on the number of resources that you can create, and on the number of users who can use the WorkSpaces Applications service.

To request a quota increase, you can use the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/). For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

The following table lists the default quotas for each WorkSpaces Applications resource and for users in the WorkSpaces Applications user pool. The actual quotas for your account could be higher or lower, depending on when you created your account.

**Note**
Graphics Pro instances are no longer available after 10/31/2025 due to End of Life of hardware supporting Graphics Pro instance types. WorkSpaces Applications does not accept limit increase requests for Graphics Pro instances.
Graphics Design instances will no longer be available from AWS after 12/31/2025 due to End of Life of hardware supporting Graphics Design instance types. WorkSpaces Applications does not accept limit increase requests for Graphics Design instances.

| Name | Default | Adjustable |
| --- | --- | --- |
| Stacks | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appstream2/quotas/L-A8B8B901) |
| Fleets | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appstream2/quotas/L-3FEADC0C) |
| Compute-optimized fleet instances \* |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Graphics fleet instances \* |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Memory-optimized fleet instances \* |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Standard fleet instances \* |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| General purpose fleet instances\* |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Compute optimize fleet instances\* |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Memory optimize fleet instances\* |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Accelerated fleet instances\* |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Image builders (total) | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appstream2/quotas/L-DE32F884) |
| Images | 10 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appstream2/quotas/L-E1182CCA) |
| Compute-optimized image builder instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Graphics image builder instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Memory-optimized image builder instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Standard image builder instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| General purpose image builder instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Compute optimize image builder instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Memory optimize image builder instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Accelerated image builder instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| BYOL Standard fleet instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| BYOL Compute-optimized fleet instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| BYOL Memory-optimized fleet instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| BYOL Graphics fleet instances |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| BYOL Standard Image Builders |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| BYOL Compute-optimized Image Builders |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| BYOL Memory-optimized Image Builders |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| BYOL Graphics Image Builders |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |
| Number of AWS accounts an image can be shared with | 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appstream2/quotas/L-99A44980) |
| Concurrent image copies per destination Region | 2 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appstream2/quotas/L-60244546) |
| Concurrent image updates | 5 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appstream2/quotas/L-9B6418E0) |
| Users in the user pool | 50 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appstream2/quotas/L-6A8C9986) |
| Max concurrent sessions for Elastic fleets | [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)Windows Server 2019[See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html) | Yes |
|  App block builders (total) | 10 | Yes |
|  Max number of app block builders |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)  | Yes |

\* WorkSpaces Applications instance type and size quotas are per AWS account per AWS Region. If you have multiple fleets in the same Region that use the same instance type and size, the total number of instances in all fleets in that Region must be less than or equal to the applicable quota. To determine which instance types are available in which Regions or Availability Zones, see *Pricing by AWS Region – Always-On, On-Demand, app block builders, and image builder instances* in [WorkSpaces Applications Pricing](https://aws.amazon.com/appstream2/pricing/).

For fleets that have **Default Internet Access** enabled, the quota is 100 fleet instances. If your deployment must support more than 100 concurrent users, use the [NAT gateway configuration](managing-network-internet-NAT-gateway.md) instead. For more information about enabling internet access for a fleet, see [Internet Access](internet-access.md).
