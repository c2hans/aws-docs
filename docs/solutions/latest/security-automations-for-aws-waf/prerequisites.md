---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

This solution is designed to work with web applications deployed with CloudFront or an ALB. If you don’t already have one of these resources configured, complete the applicable tasks before you launch this solution.

## Configure a CloudFront distribution
<a name="configure-a-cloudfront-distribution"></a>

Complete the following steps to configure a CloudFront distribution for your web application’s static and dynamic content. Refer to the [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) for detailed instructions.

1. Create a CloudFront web application distribution. Refer to [Creating a Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.html).

1. Configure static and dynamic origins. Refer to [Using various origins with CloudFront distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html).

1. Specify your distribution’s behavior. Refer to [Values that you specify when you create or update a distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html).
**Note**
If you choose `CloudFront` as your endpoint, you must create your WAFV2 resources in the US East (N. Virginia) Region.

## Configure an ALB
<a name="configure-an-alb"></a>

To configure an ALB to distribute incoming traffic to your web application, refer to [Create an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html) in the *User Guide for Application Load Balancers*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
