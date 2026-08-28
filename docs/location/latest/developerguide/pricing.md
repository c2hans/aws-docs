---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/pricing.html
---

# Pricing model
<a name="pricing"></a>

Amazon Location Service requires no up-front commitment and no minimum fee. You're only charged for what you use. Amazon Location offers a free trial for the first three months of usage (usage quota apply). Location data is billed based on each request your application makes to the service. Beyond the Amazon Location Service free trial, you pay for the requests your application makes to the service. For more pricing information, visit our [pricing page](https://aws.amazon.com/location/pricing/).

**Pricing Buckets**

Each API may offer multiple features at different price points and the price may vary based on features you requested through request parameters.

For example, for `CalculateRoutes`, you'll be charged at **Core** price bucket when using `Car`, `Pedestrian`, or `Truck` mode. You'll be charged at **Advanced** price bucket when using other travel modes, such as `Scooter` mode. You'll be charged at **Premium** price bucket when you request for Toll Cost calculation.

The specific pricing bucket you'll be charged for will be returned in the `PricingBucket` response field. To review the pricing for each API and feature, see the Amazon Location Service [pricing page](https://aws.amazon.com/location/pricing/) for details on API feature, request parameters, and corresponding pricing. For more information, see the following topics:
+ [Maps pricing](maps-pricing.md)
+ [Places pricing](places-pricing.md)
+ [Routes pricing](routes-pricing.md)
+ [Geofences pricing](geofence-price.md)
+ [Trackers pricing](trackers-pricing.md)
+ [Jobs pricing](jobs-pricing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
