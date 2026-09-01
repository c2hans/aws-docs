---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-architecture-costs.html
---

# ECS architecture costs
<a name="ecs-architecture-costs"></a>

The ECS architecture has higher baseline costs due to always-running infrastructure but provides better performance and advanced features. Costs scale with the selected t-shirt size and auto-scaling configuration.

## ECS architecture cost summary
<a name="ecs-cost-table"></a>

Dynamic Image Transformation for Amazon CloudFront uses CloudFront’s pay-as-you-go pricing model by default. However, if you expect your monthly usage on your distribution to be below 50TB of data transfer and 500M image requests, you can optimize costs by switching to CloudFront’s Business or Premium fixed-pricing tiers after deployment.

To switch to these tiers after deployment, navigate to the CloudFront console, select your CloudFront distribution, under the Billing section choose "Switch to a plan" and select one of the available fixed pricing plans.

The pricing estimates below reflect costs when using the fixed-pricing tiers.

For detailed CloudFront pricing information, including pay-as-you-go rates and fixed-pricing tier benefits, visit the [CloudFront Pricing page](https://aws.amazon.com/cloudfront/pricing/).

## ECS architecture cost breakdown
<a name="ecs-architecture-cost-breakdown"></a>

The following table provides sample cost breakdowns for different ECS deployment sizes in the US East (N. Virginia) Region for one month.

## Assumptions
<a name="assumptions"></a>
+ 90% cache hit rate
+ Average image size: 45 KB
+ ALB configuration is Small, Medium and Large for the corresponding workloads
+ Actual cost might vary based on burst traffic patterns

| AWS Service | 10M images served(Small deployment size) | 125M images served(Medium deployment size) | 500M images served(Large deployment size) |
| --- | --- | --- | --- |
| Amazon CloudFront | $200 | $200 | $1000 |
| AWS ECS | $72.08 | $216.24 | $576.64 |
| Application Load Balancer | $16.79 | $22.27 | $34.30 |
| CloudWatch Logs | $1.15 | $19.17 | $75.67 |
|  **Total**  |  **$290.02**  |  **$457.68**  |  **$1686.61**  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
