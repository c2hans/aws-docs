---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/amazon-cloudfront-aws-waf-and-alb.html
---

# Amazon CloudFront, AWS WAF, and ALB
<a name="amazon-cloudfront-aws-waf-and-alb"></a>

CloudFront is used as the entry point into the solution where the bid requests are received. CloudFront speeds up distribution of content through a worldwide network of data centers called edge locations. CloudFront ensures that end-user requests are served by the closest edge location. To prevent requests from bypassing the CDN and accessing the origin (ALB) directly, the solution uses [CloudFront custom headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.html).

AWS WAF is a web application firewall that helps protect the application from common web exploits that could affect application availability, compromise security, or consume excessive resources. It is preconfigured with a set of standard [AWS managed rules](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html). AWS WAF is tightly integrated with CloudFront at the edge. Traffic can be received here as HTTP or HTTPS.

**Note**
If you want to opt out of using CloudFront and AWS WAF and directly send requests to the ALB, see [How to opt out](configure-the-solution.md#how-to-opt-out).
