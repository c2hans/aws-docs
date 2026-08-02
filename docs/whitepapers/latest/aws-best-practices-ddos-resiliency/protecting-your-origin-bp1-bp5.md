---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/protecting-your-origin-bp1-bp5.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Protecting your origin (BP1, BP5)
<a name="protecting-your-origin-bp1-bp5"></a>

 If you are using Amazon CloudFront with an origin that is inside of your VPC, you may want to ensure that only your CloudFront distribution can forward requests to your origin. With Edge-to-Origin Request Headers, you can add or override the value of existing request headers when CloudFront forwards requests to your origin. You can use the *Origin Custom Headers*, for example, the `X-Shared-Secret` header, to help validate that the requests made to your origin were sent from CloudFront.

 For more information about protecting your origin with an *Origin Custom Headers*, refer to [Adding](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.html) [custom headers to origin requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.html) and [Restricting access to Application Load Balancers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html).

 For a guide on implementing a sample solution to automatically rotate the value of *Origin Custom Headers* for the origin access restriction, refer to [How to enhance Amazon CloudFront origin security with AWS WAF and Secrets Manager](https://aws.amazon.com/blogs/security/how-to-enhance-amazon-cloudfront-origin-security-with-aws-waf-and-aws-secrets-manager/).

 Alternatively, you can use an [AWS Lambda](https://aws.amazon.com/lambda/) function to automatically update your security group rules to allow only CloudFront traffic. This improves your origin’s security by helping to ensure that malicious users cannot bypass CloudFront and AWS WAF when accessing your web application.

 For more information about how to protect your origin by automatically updating your security groups, and the `X-Shared-Secret` header, refer to [How to Automatically Update Your Security Groups for Amazon CloudFront and AWS WAF by Using AWS Lambda](https://aws.amazon.com/blogs/security/how-to-automatically-update-your-security-groups-for-amazon-cloudfront-and-aws-waf-by-using-aws-lambda/).

 However, the solution involves additional configuration and the cost of running Lambda functions. To simplify this, we have now introduced an [AWS-managed prefix list for CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html#managed-prefix-list) to limit the inbound HTTP/HTTPS traffic to your origins from only the CloudFront origin-facing IP addresses. AWS-managed prefix lists are created and maintained by AWS and are available to use at no additional cost. You can reference the managed prefix list for CloudFront in your (Amazon VPC) security group rules, subnet route tables, common security group rules with AWS Firewall Manager, and any other AWS resources that can use a [managed prefix list](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html).

 For more information about using AWS-managed prefix list for Amazon CloudFront, refer to [Limit access to your origins using the AWS-managed prefix list for Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/limit-access-to-your-origins-using-the-aws-managed-prefix-list-for-amazon-cloudfront/).

**Note**
 As discussed in other sections of this document, relying on security groups to protect your origin can add [security-group connection tracking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html) as a potential bottle-neck during a request flood. Unless you are able to filter malicious requests at CloudFront using a caching policy that enables caching, it may be better to rely on the *Origin Custom Headers*, discussed previously, to help validate that the requests made to your origin were sent from CloudFront, rather than use security groups. Using a custom request header with an Application Load Balancer listener rule prevents throttling due to tracking limits that may affect establishing new connections to a load balancer, thus allowing Application Load Balancer to scale based on the increase in traffic in an event of an DDoS attack.
