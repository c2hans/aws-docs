---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-14.html
---

# WKLD.14 Use edge-protection services for public endpoints
<a name="wkld-14"></a>

Rather than serve traffic directly from compute services such as Amazon EC2 instances or containers, use an edge protection service. An edge protection service sits between internet traffic and your backend resources, filtering unwanted requests, enforcing encryption, and applying rules such as load balancing before traffic reaches your workloads.

AWS services that can provide public endpoint protection include AWS WAF, Amazon CloudFront, Elastic Load Balancing, Amazon API Gateway, and AWS Amplify Hosting. Deploy VPC-based services, such as Elastic Load Balancing, in a public subnet to receive internet traffic and forward it to your workloads running in a private subnet.

Amazon CloudFront, Amazon API Gateway, and Amazon Route 53 provide protection from Layer 3 and 4 distributed denial of service (DDoS) attacks at no additional charge. AWS WAF provides protection against Layer 7 attacks and incurs additional charges.

For instructions on getting started with each of these services, see the following:
+ [Getting started with AWS WAF](https://aws.amazon.com/waf/getting-started/)
+ [Getting started with Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html)
+ [Getting started with Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-getting-started.html)
+ [Getting started with Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html)
+ [Getting started with AWS Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started.html)
