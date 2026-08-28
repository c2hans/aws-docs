---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/protecting-your-origin-bp1-bp5.html
---

# Protecting your origin (BP1, BP5)
<a name="protecting-your-origin-bp1-bp5"></a>

 When using [Amazon CloudFront](https://aws.amazon.com/cloudfront/) with an origin inside your VPC, it's crucial to ensure that only your CloudFront distribution can forward requests to your origin. AWS provides several approaches to implement this security control, with CloudFront VPC origins being the newest and recommended solution.

 CloudFront VPC origins enables you to keep your applications in private subnets without internet access while restricting access to only your CloudFront distributions. This feature allows CloudFront to deliver content directly from applications hosted in VPC private subnets, supporting [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)s (ALB), [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/)s (NLB), and EC2 instances. This approach eliminates the need for public origins and creates a single, secure entry point to your web applications while maintaining the performance and scale benefits of CloudFront. There is no additional cost for using VPC origins with CloudFront.

 To learn more, see [CloudFront VPC origins](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html).

 For origins using Amazon S3, [AWS Elemental](https://aws.amazon.com/media-services/elemental/), or Lambda function URLs, Origin Access Control (OAC) remains the recommended managed solution to secure these origins.

 There are a number of alternative approaches for cases when you're not using VPC Origins yet, see [Restrict access to Application Load Balancers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html) for more information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
