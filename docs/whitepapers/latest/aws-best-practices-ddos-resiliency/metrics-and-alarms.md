---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/metrics-and-alarms.html
---

# Metrics and alarms
<a name="metrics-and-alarms"></a>

As a best practice you should be using infrastructure and application monitoring tools to check the availability of your application to help detect whether your application is being impacted by a DDoS event, as an option you can configure application and infrastructure Route 53 [health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html) for the resources to help improve the detection of DDoS events. For more information about health checks, see [AWS WAF, Firewall Manager and Shield Advanced Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/health-checks-examples.html).

For organizations operating across multiple AWS accounts, AWS recommends implementing CloudWatch [cross-account](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Cross-Account-Methods.html) observability to establish unified monitoring of DDoS-related metrics and alarms. This feature enables a central security or operations team to monitor DDoS events, analyze attack patterns, and respond to incidents across your entire organization from a single monitoring account. For more information, see [Monitor across accounts and Regions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

When a key operational metric deviates substantially from the expected value, an attacker might be attempting to target your application's availability. Familiarity with the normal behavior of your application means you can act more quickly when you detect an anomaly. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) can help by monitoring applications that you run on AWS. For example, you can collect and track metrics, collect and monitor log files, set alarms, and automatically respond to changes in your AWS resources.

If you follow the DDoS-resilient reference architecture when architecting your application, common infrastructure layer attacks will be blocked before reaching your application. If you're subscribed to [AWS Shield Advanced](https://aws.amazon.com/shield/), you have access to a number of CloudWatch metrics that can indicate that your application is being targeted.

For example, you can configure alarms to notify you when there's a DDoS attack in progress, so you can check your application's health and decide whether to engage AWS SRT. You can configure the `DDoSDetected` metric to tell you if an attack has been detected. If you want to be alerted based on the attack volume, you can also use the `DDoSAttackBitsPerSecond`, `DDoSAttackPacketsPerSecond`, or `DDoSAttackRequestsPerSecond` metrics. You can monitor these metrics by integrating CloudWatch with your own tools or by using tools provided by third parties, such as Slack or PagerDuty.

An application layer attack can elevate many [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics. If you're using [AWS WAF](https://aws.amazon.com/waf/), you can use CloudWatch to monitor and activate alarms on increases in requests that you've set in AWS WAF to be allowed, counted, or blocked. This allows you to receive a notification if the level of traffic exceeds what your application can handle. You can also use [Amazon CloudFront](https://aws.amazon.com/cloudfront/), [Amazon Route 53](https://aws.amazon.com/route53/), Application Load Balancer, [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/), Amazon EC2, and Auto Scaling metrics that are tracked in CloudWatch to detect changes that can indicate a DDoS attack.

The following table lists descriptions of CloudWatch metrics that are commonly used to detect and react to DDoS attacks.

 *Table 4 – Recommended Amazon CloudWatch metrics*

| AWS service | Metric | Description |
| --- | --- | --- |
| AWS Shield Advanced | DDoSDetected | Indicates a DDoS event for a specific Amazon Resource Name (ARN). |
| AWS Shield Advanced | DDoSAttackBitsPerSecond | The number of bytes observed during a DDoS event for a specific ARN. This metric is only available for layer 3 or 4 DDoS events. |
| AWS Shield Advanced | DDoSAttackPacketsPerSecond | The number of packets observed during a DDoS event for a specific ARN. This metric is only available for layer 3 or 4 DDoS events. |
| AWS Shield Advanced | DDoSAttackRequestsPerSecond | The number of requests observed during a DDoS event for a specific ARN. This metric is only available for layer 7 DDoS events and is only reported for the most significant layer 7 events. |
| AWS WAF | AllowedRequests | The number of allowed web requests. |
| AWS WAF | BlockedRequests | The number of blocked web requests. |
| AWS WAF | CountedRequests | The number of counted web requests. |
| AWS WAF | PassedRequests | The number of passed requests. This is only used for requests that go through a rule group evaluation without matching any of the rule group rules. |
| Amazon CloudFront | Requests | The number of HTTP/S requests. |
| Amazon CloudFront | TotalErrorRate | The percentage of all requests for which the HTTP status code is 4xx or 5xx. |
| Amazon Route 53 | HealthCheckStatus | The status of the health check endpoint. |
| Application Load Balancer | ActiveConnectionCount | The total number of concurrent TCP connections that are active from clients to the load balancer, and from the load balancer to targets. |
| Application Load Balancer | ConsumedLCUs | The number of load balancer capacity units (LCU) used by your load balancer. |
| Application Load Balancer | HTTPCode\_ELB\_4XX\_Count HTTPCode\_ELB\_5XX\_Count | The number of HTTP 4xx or 5xx client error codes generated by the load balancer. |
| Application Load Balancer | NewConnectionCount | The total number of new TCP connections established from clients to the load balancer, and from the load balancer to targets. |
| Application Load Balancer | ProcessedBytes | The total number of bytes processed by the load balancer. |
| Application Load Balancer | RejectedConnectionCount | The number of connections that were rejected because the load balancer had reached its maximum number of connections. |
| Application Load Balancer | RequestCount | The number of requests that were processed. |
| Application Load Balancer | TargetConnectionErrorCount | The number of connections that were not successfully established between the load balancer and the target. |
| Application Load Balancer | TargetResponseTime | The time elapsed, in seconds, after the request left the load balancer until a response from the target is received. |
| Application Load Balancer | UnHealthyHostCount | The number of targets that are considered unhealthy. |
| Network Load Balancer | ActiveFlowCount | The total number of concurrent TCP flows (or connections) from clients to targets. |
| Network Load Balancer | ConsumedLCUs | The number of load balancer capacity units (LCU) used by your load balancer. |
| Network Load Balancer | NewFlowCount | The total number of new TCP flows (or connections) established from clients to targets in the time period. |
| Network Load Balancer | ProcessedBytes | The total number of bytes processed by the load balancer, including TCP/IP headers. |
| Global Accelerator | NewFlowCount | The total number of new TCP and UDP flows (or connections) established from clients to endpoints in the time period. |
| Global Accelerator | ProcessedBytesIn | The total number of incoming bytes processed by the accelerator, including TCP/IP headers. |
| Auto Scaling | GroupMaxSize | The maximum size of the Auto Scaling group. |
| Amazon EC2 | CPUUtilization | The percentage of allocated EC2 compute units that are currently in use. |
| Amazon EC2 | NetworkIn | The number of bytes received by the instance on all network interfaces. |

For more information about using Amazon CloudWatch to detect DDoS attacks on your application, refer to [Getting Started with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html).

AWS includes several additional metrics and alarms to notify you about an attack and to help you monitor your application's resources. The [AWS Shield](https://aws.amazon.com/shield/) console or API provide a per-account event summary and details about attacks that have been detected.

![Global activity detected by AWS Shield](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/global-activity-detected.png)

In addition, the global threat environment dashboard provides summary information about all DDoS attacks that have been detected by AWS. This information can be useful to better understand DDoS threats across a larger population of applications in addition to attack trends, and comparing with attacks that you might have observed.

If you're subscribed to AWS Shield Advanced, the service dashboard displays additional detection and mitigation metrics and network traffic details for events detected on protected resources. AWS Shield evaluates traffic to your protected resource along multiple dimensions. When an anomaly is detected, AWS Shield creates an event and reports the traffic dimension where the anomaly was observed. With a placed mitigation this protects your resource from receiving excess traffic and traffic that matches a known DDoS event signature.

Detection metrics are based on sampled network flows or AWS WAF logs when a web ACL is associated with the protected resource. Mitigation metrics are based on traffic that's observed by [AWS Shield](https://aws.amazon.com/shield/)'s DDoS mitigation systems. Mitigation metrics are a more precise measurement of the traffic into your resource.

The *network top contributors* metric provides insight into where traffic is coming from during a detected event. You can view the highest volume contributors and sort by aspects such as protocol, source port, and TCP flags. The top contributors metric includes metrics for all traffic observed on the resource along various dimensions. It provides additional metric dimensions you can use to understand network traffic that's sent to your resource during an event. Keep in mind that for non-reflection layer 3 or 4 attacks, the source IP addresses could have been spoofed and can't be relied on.

The service dashboard also includes details about the actions automatically taken to mitigate DDoS attacks. This information makes it easier to investigate anomalies, explore dimensions of the traffic, and better understand the actions taken by Shield Advanced to protect your availability.
