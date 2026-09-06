---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-13.html
---

# WKLD.13 Require HTTPS for public web endpoints
<a name="wkld-13"></a>

Require HTTPS so that your endpoints can use certificates to prove their identity and so that traffic between your endpoint and clients is encrypted. For public websites, HTTPS also improves search engine ranking.

Many AWS services provide public web endpoints for your resources, such as AWS Elastic Beanstalk, Amazon CloudFront, Amazon API Gateway, Elastic Load Balancing, and AWS Amplify. For instructions about how to require HTTPS for each of these services, see the following:
+ [Configuring HTTPS for your Elastic Beanstalk environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html) in the AWS Elastic Beanstalk documentation
+ [Requiring HTTPS for communication between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) in the Amazon CloudFront documentation
+ [How can I use an Application Load Balancer to redirect HTTP requests to HTTPS?](https://repost.aws/knowledge-center/elb-redirect-http-to-https-using-alb) on AWS re:Post
+ [How do I redirect HTTP requests to HTTPS on a Classic Load Balancer?](https://repost.aws/knowledge-center/redirect-http-https-elb) on AWS re:Post
**Note**
Classic Load Balancer is a legacy option. For new deployments, we recommend using an Application Load Balancer.
+ [Connecting a custom domain](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html) in the AWS Amplify documentation

Static websites hosted on Amazon S3 do not support HTTPS. To require HTTPS for these websites, you can use CloudFront. When you use CloudFront to serve content from an Amazon S3 bucket, you don't need to enable public access on the bucket. Use an origin access control (OAC) to allow CloudFront to access the private bucket.

For instructions on setting up CloudFront to serve a static website hosted on Amazon S3, see [How do I use CloudFront to serve a static website hosted on Amazon S3?](https://repost.aws/knowledge-center/cloudfront-serve-static-website) on AWS re:Post.

**To configure HTTPS for a static website hosted on Amazon S3**

1. If you are configuring access to a public Amazon S3 bucket, require HTTPS between viewers and CloudFront. For more information, see [Require HTTPS for communication between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html) in the Amazon CloudFront documentation.

1. If you are configuring access to a private Amazon S3 bucket, restrict access to Amazon S3 content by using an origin access control (OAC). For more information, see [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the Amazon CloudFront documentation.

Configure HTTPS endpoints to require modern Transport Layer Security (TLS) protocols and ciphers, unless compatibility with older protocols is needed. For example, use the** **`ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09` policy or the most recent policy available for Application Load Balancer HTTPS listeners. The most current policies support **TLS 1.2 and TLS 1.3**, forward secrecy, and strong ciphers that are compatible with modern web browsers.

For more information about the available security policies for HTTPS public endpoints, see the following:
+ [Predefined SSL security policies for Classic Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html) in the Elastic Load Balancing documentation
+ [Security policies for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies) in the Elastic Load Balancing documentation
+ [Supported protocols and ciphers between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html) in the Amazon CloudFront documentation
