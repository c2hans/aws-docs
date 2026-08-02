---
source_url: https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/plans.html
---

# Available Plans
<a name="plans"></a>

## CloudFront Flat-Rate Plans
<a name="cloudfront-plans"></a>

CloudFront Flat-Rate Plans combine global content delivery with AWS WAF, DDoS protection, Amazon Route 53 DNS, Amazon CloudWatch Logs ingestion, Amazon S3 storage credits, and serverless edge compute into a simple monthly price with no overage charges. Each plan includes predefined usage allowances for these integrated services.

### Plan Tiers
<a name="plan-tiers"></a>
+ Free ($0/month) - 1M requests, 100GB transfer
+ Pro ($15/month) - 10M requests, 50TB transfer
+ Business ($200/month) - 125M requests, 50TB transfer
+ Premium ($1,000/month) - 500M requests, 50TB transfer

### Usage Monitoring
<a name="usage-monitoring"></a>

You can monitor your CloudFront flat-rate plan usage through the CloudFront console. The console displays your usage percentage tracking against monthly allowances and days remaining in the current billing cycle. Email notifications are sent when you reach 50%, 80%, and 100% of your monthly allowance.

### Account Requirements
<a name="account-requirements"></a>

Free Tier accounts cannot use CloudFront Flat-Rate Plans.

### Service Code
<a name="service-code"></a>

 `CloudFrontPlans`

For technical details and feature specifications, see the [CloudFront documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html).
