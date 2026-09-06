---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_network_encryption_offload.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP04 Leverage load-balancing and encryption offloading
<a name="perf_select_network_encryption_offload"></a>

Use load balancers to achieve optimal performance efficiency of your target resources and improve the responsiveness of your system.

 **Desired outcome:** Reduce the number of computing resources to serve your traffic. Avoid resource consumption imbalance in your targets. Offload compute-intensive tasks to the Load Balancer. Leverage cloud elasticity and flexibility to improve performance and optimize your architecture.

 **Common anti-patterns:**
+ You don’t consider your workload requirements when choosing the load balancer type.
+ You don’t leverage the load balancer features for performance optimization.
+  The workload is exposed directly to the Internet without a load balancer.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Load balancers act as the entry point for your workload and from there they distribute the traffic to your back-end targets, such as compute instances or containers. Choosing the right load balancer type is the first step to optimize your architecture.

 Start by listing your workload characteristics, such as protocol (like TCP, HTTP, TLS, or WebSockets), target type (like instances, containers, or serverless), application requirements (like long running connections, user authentication, or stickiness), and placement (like Region, Local Zone, Outpost, or zonal isolation).

 After choosing the right load balancer, you can start leveraging its features to reduce the amount of effort your back-end has to do to serve the traffic.

 For example, using both Application Load Balancer (ALB) and Network Load Balancer (NLB), you can perform SSL/TLS encryption offloading, which is an opportunity to avoid the CPU-intensive TLS handshake from being completed by your targets and also to improve certificate management.

 When you configure SSL/TLS offloading in your load balancer, it becomes responsible for the encryption of the traffic from and to clients while delivering the traffic unencrypted to your back-ends, freeing up your back-end resources and improving the response time for the clients.

 Application Load Balancer can also serve HTTP2 traffic without needing to support it on your targets. This simple decision can improve your application response time, as HTTP2 uses TCP connections more efficiently.

 Load balancers can also be used to make your architecture more flexible by distributing traffic across different back-end types such as containers and serverless. For example, Application Load Balancer can be configured with [listener rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html) that forward traffic to different target groups based on the request parameters such as header, method or pattern.

 Your workload latency requirements should also be considered when defining the architecture. As an example, if you have a latency-sensitive application, you may decide to use Network Load Balancer, which offers extremely low latencies. Alternatively, you may decide to bring your workload closer to your customers by leveraging Application Load Balancer in [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) or even [AWS Outposts](https://aws.amazon.com/outposts/rack/).

 Another consideration for latency-sensitive workloads is cross-zone load balancing. With cross-zone load balancing, each load balancer node distributes traffic across the registered targets in all allowed Availability Zones. This improves availability, although it can add a single digit millisecond to the roundtrip latency.

 Lastly, both ALB and NLB offer monitoring resources such as logs and metrics. Properly setting up monitoring can help with gathering performance insights of your application. For example, you can use ALB access logs to find which requests are taking longer to be answered or which back-end targets are causing performance issues.

 **Implementation steps**

1.  Choose the right load balancer for your workload.

   1.  Use Application Load Balancer for HTTP/HTTPS workloads.

   1.  Use Network Load Balancer for non-HTTP workloads that run on TCP or UDP.

   1.  Use a combination of both ([ALB as a target of NLB](https://aws.amazon.com/blogs/networking-and-content-delivery/application-load-balancer-type-target-group-for-network-load-balancer/)) if you want to leverage features of both products. For example, you can do this if you want to use the static IPs of NLB together with HTTP header based routing from ALB, or if you want to expose your HTTP workload to an [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html).

   1.  For a full comparison of load balancers, see [ELB product comparison](https://aws.amazon.com/elasticloadbalancing/features/).

1.  Use SSL/TLS offloading.

   1.  Configure HTTPS/TLS listeners with both [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html) integrated with [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/).

   1.  Note that some workloads may require end-to-end encryption for compliance reasons. In this case, it is a requirement to allow encryption at the targets.

   1.  For security best practices, see [SEC09-BP02 Enforce encryption in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html).

1.  Select the right routing algorithm.

   1.  The routing algorithm can make a difference in how well-used your back-end targets are and therefore how they impact performance. For example, ALB provides [two options for routing algorithms](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#modify-routing-algorithm):

   1.  **Least outstanding requests:** Use to achieve a better load distribution to your back-end targets for cases when the requests for your application vary in complexity or your targets vary in processing capability.

   1.  **Round robin:** Use when the requests and targets are similar, or if you need to distribute requests equally among targets.

1.  Consider cross-zone or zonal isolation.

   1.  Use cross-zone turned off (zonal isolation) for latency improvements and zonal failure domains. It is turned off by default in NLB and in [ALB you can turn it off per target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/disable-cross-zone.html).

   1.  Use cross-zone turned on for increased availability and flexibility. By default, cross-zone is turned on for ALB and in [NLB you can turn it on per target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-cross-zone.html).

1.  Turn on HTTP keep-alives for your HTTP workloads.

   1.  For HTTP workloads, turn on HTTP keep-alive in the web server settings for your back-end targets. With this feature, the load balancer can reuse backend connections until the keep-alive timeout expires, improving your HTTP request and response time and also reducing resource utilization on your back-end targets. For detail on how to do this for Apache and Nginx, see [What are the optimal settings for using Apache or NGINX as a backend server for ELB?](https://aws.amazon.com/premiumsupport/knowledge-center/apache-backend-elb/)

1.  Use Elastic Load Balancing integrations for better orchestration of compute resources.

   1.  Use Auto Scaling integrated with your load balancer. One of the key aspects of a performance efficient system has to do with right-sizing your back-end resources. To do this, you can leverage load balancer integrations for back-end target resources. Using the load balancer integration with Auto Scaling groups, targets will be added or removed from the load balancer as required in response to incoming traffic.

   1.  Load balancers can also integrate with Amazon ECS and Amazon EKS for containerised workloads.
      + [ Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)
      + [ Amazon ECS - Service load balancing ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html)
      + [ Application load balancing on Amazon EKS ](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html)
      + [ Network load balancing on Amazon EKS ](https://docs.aws.amazon.com/eks/latest/userguide/network-load-balancing.html)

1.  Monitor your load balancer to find performance bottlenecks.

   1.  Turn on access logs for your [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html).

   1.  The main fields to consider for ALB are `request_processing_time`, `request_processing_time`, and `response_processing_time`.

   1.  The main fields to consider for NLB are `connection_time` and `tls_handshake_time`.

   1.  Be ready to query the logs when you need them. You can use Amazon Athena to query both [ALB logs](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html) and [NLB Logs](https://docs.aws.amazon.com/athena/latest/ug/networkloadbalancer-classic-logs.html).

   1.  Create alarms for performance related metrics such as [`TargetResponseTime` for ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html).

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [SEC09-BP02 Enforce encryption in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html)

 **Related documents:**
+ [ ELB product comparison ](https://aws.amazon.com/elasticloadbalancing/features/)
+ [AWS Global Infrastructure ](https://aws.amazon.com/about-aws/global-infrastructure/)
+ [ Improving Performance and Reducing Cost Using Availability Zone Affinity ](https://aws.amazon.com/blogs/architecture/improving-performance-and-reducing-cost-using-availability-zone-affinity/)
+ [ Step by step for Log Analysis with Amazon Athena ](https://github.com/aws/elastic-load-balancing-tools/tree/master/amazon-athena-for-elb)
+ [ Querying Application Load Balancer logs ](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html)
+ [ Monitor your Application Load Balancers ](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html)
+ [ Monitor your Network Load Balancers ](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-monitoring.html)

 **Related videos:**
+ [AWS re:Invent 2018: [REPEAT 1] Elastic Load Balancing: Deep Dive and Best Practices (NET404-R1) ](https://www.youtube.com/watch?v=VIgAT7vjol8)
+ [AWS re:Invent 2021 - How to choose the right load balancer for your AWS workloads ](https://www.youtube.com/watch?v=p0YZBF03r5A)
+ [AWS re:Inforce 2022 - How to use Elastic Load Balancing to enhance your security posture at scale (NIS203) ](https://www.youtube.com/watch?v=YhNc5VSzOGQ)
+ [AWS re:Invent 2019: Get the most from Elastic Load Balancing for different workloads (NET407-R2) ](https://www.youtube.com/watch?v=HKh54BkaOK0)

 **Related examples:**
+ [ CDK and CloudFormation samples for Log Analysis with Amazon Athena ](https://github.com/aws/elastic-load-balancing-tools/tree/master/log-analysis-elb-cdk-cf-template)
