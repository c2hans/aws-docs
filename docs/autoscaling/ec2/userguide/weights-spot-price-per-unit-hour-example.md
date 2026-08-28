---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/weights-spot-price-per-unit-hour-example.html
---

# Spot price per unit hour example
<a name="weights-spot-price-per-unit-hour-example"></a>

The following table compares the hourly price for Spot Instances in different Availability Zones in US East (Northern Virginia) with the price for On-Demand Instances in the same Region. The prices shown are example pricing and not current pricing. These are your costs per *instance* hour.

**Example: Spot pricing per instance hour**

| Instance type | us-east-1a | us-east-1b | us-east-1c | On-Demand pricing |
| --- | --- | --- | --- | --- |
| c5.2xlarge  | $0.180 | $0.191 | $0.170 | $0.34  |
| c5.4xlarge | $0.341 | $0.361 | $0.318 | $0.68 |
| c5.12xlarge  | $0.779 | $0.777  | $0.777  | $2.04 |
| c5.18xlarge  | $1.207 | $1.475 | $1.357 | $3.06 |
| c5.24xlarge | $1.555 | $1.555 | $1.555 | $4.08 |

With instance weights, you can evaluate your costs based on what you use per *unit* hour. You can determine the price per unit hour by dividing your price for an instance type by the number of units that it represents. For On-Demand Instances, the price per unit hour is the same when deploying one instance type as it is when deploying a different size of the same instance type. In contrast, however, the Spot price per unit hour varies by Spot pool.

The following example shows how the Spot price per unit hour calculation works with instance weights. For ease of calculation, let's say you want to launch Spot Instances only in `us-east-1a`. The per unit hour price is captured in the following table.

**Example: Spot Price per unit hour**

| Instance type | us-east-1a | Instance weight | Price per unit hour  |
| --- | --- | --- | --- |
| c5.2xlarge  | $0.180 | 2 | $0.090 |
| c5.4xlarge | $0.341 | 4 | $0.085 |
| c5.12xlarge  | $0.779 | 12 | $0.065 |
| c5.18xlarge  | $1.207 | 18 | $0.067 |
| c5.24xlarge | $1.555 | 24 | $0.065 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
