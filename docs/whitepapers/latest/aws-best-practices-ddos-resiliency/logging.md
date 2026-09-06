---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/logging.html
---

# Logging
<a name="logging"></a>

Enable useful logging on all services according to our [Logging and monitoring guide for application owners](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/introduction.html) to maximize visibility and assist with troubleshooting. This includes, but isn't limited to:
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
+ [AWS WAF Logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)
+ [CloudFront access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html)
+ [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) (see [Log and View Network Traffic Flows](https://aws.amazon.com/blogs/aws/vpc-flow-logs-log-and-view-network-traffic-flows/)) – include `tcp-flags` field in the included fields to maximize visibility
+ ELB access logs ([ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html), [NLB](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html))
+ [API Gateway](https://aws.amazon.com/api-gateway/) logs
+ Web server HTTP access logs
+ Operating system security logging
+ [Application logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
