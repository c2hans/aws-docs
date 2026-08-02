---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/appendix-b---edge-network-global-service-guidance.html
---

# Appendix B - Edge network global service guidance
<a name="appendix-b---edge-network-global-service-guidance"></a>

 For edge network global services, you should implement static stability in order to maintain resilience of your workload during an AWS service control plane impairment.

## Route 53
<a name="route-53"></a>

 The Route 53 control plane consists of all public Route 53 APIs covering functionality for hosted zones, records, health checks, DNS query logs, reusable delegation sets, traffic policies, and cost allocation tags. It is hosted in us-east-1. The data plane is the authoritative DNS service, which runs across over 200 PoP locations as well as in each AWS Region, answering DNS queries based on your hosted zones and health check data. Additionally, Route 53 has a data plane for health checks which is also a globally-distributed service across multiple AWS Regions. This data plane performs health checks, aggregates the results, and delivers them to the data planes of Route 53 public and private DNS and AGA. During a control plane impairment, CRUDL-type operations for Route 53 may not work, but DNS resolution and health checks, and updates to routing resulting from changes in health checks, will continue to work.

 What this means is that when you are planning for dependencies on Route 53, you should not rely on the Route 53 control plane in your recovery path. For example, a statically-stable design would be to use the status of health checks to perform failovers between Regions or to evacuate an Availability Zone. You can use [Route 53 Application Recovery Controller (ARC) routing controls](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html) to manually change the status of health checks and alter the responses to DNS queries. There are similar patterns to what ARC provides that you can implement based on your requirements. Some of these patterns are outlined in [Creating Disaster Recovery Mechanisms using Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/) and in the [Advanced Multi-AZ Resilience Patterns health check circuit breaker section](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/pattern-1-health-check-circuit-breaker.html). If you have elected to use a Multi-Region DR plan, pre-provision resources that require DNS records to be created, like ELBs and RDS instances. A non-statically-stable design would be to update the value of a Route 53 resource record via the `ChangeResourceRecordSets` API, change the weight of a weighted record, or create new records to perform failover. These approaches depend on the Route 53 control plane.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

 The Amazon CloudFront control plane consists of all public CloudFront APIs for managing distributions, and is hosted in us-east-1. The data plane is the distribution itself served from the PoPs in the edge network. It performs the request handling, routing, and caching of your origin content. During a control plane impairment, CRUDL-type operations for CloudFront (including invalidation requests) may not work, but your content will continue to be cached and served, and [origin failovers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html) will continue to work.

 What this means is that when you are planning for dependencies on CloudFront, you should not rely on the CloudFront control plane in your recovery path. For example, a statically-stable design would be to use automated origin failovers to mitigate the impact from an impairment to one of your origins. You might also choose to build origin load balancing or failover using Lamda@Edge, refer to [Three advanced design patterns for high available applications using Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/three-advanced-design-patterns-for-high-available-applications-using-amazon-cloudfront/) and [Using Amazon CloudFront and Amazon S3 to build multi-Region active-active geo proximity applications](https://aws.amazon.com/blogs/networking-and-content-delivery/using-amazon-cloudfront-and-amazon-s3-to-build-multi-region-active-active-geo-proximity-applications/) for more details on that pattern. A non-statically-stable design would be to manually update the configuration of your distribution in response to an origin failure. This approach would depend on the CloudFront control plane.

### Amazon Certificate Manager
<a name="amazon-certificate-manager"></a>

 If you are using custom certificates with your CloudFront distribution, you also have a dependency on ACM. Using custom certificates with your CloudFront distribution relies on the ACM control plane in the us-east-1 Region. During a control plane impairment, your existing certificates configured in your distribution will continue to work as well as automatic certificate renewals. Do not rely on changing the distribution’s configuration or creating new certificates as part of your recovery path.

### AWS Web Application Firewall (WAF) and WAF Classic
<a name="aws-web-application-firewall-waf-and-waf-classic"></a>

 If you are using AWS WAF with your CloudFront distribution, you have a dependency on the WAF control plane, which is also hosted in the us-east-1 Region. During a control plane impairment, the configured web access control lists (ACLs) and their associated rules continue to function. Do not rely on updating your WAF web ACLs as part of your recovery path.

## AWS Global Accelerator
<a name="aws-global-accelerator"></a>

 The AGA control plane consists of all public AGA APIs and is hosted in us-west-2. The data plane is the network routing of the anycast IP addresses provided by AGA to your registered endpoints. AGA also utilizes Route 53 health checks to determine the health of your AGA endpoints, which is part of the Route 53 data plane. During a control plane impairment, CRUDL-type operations for AGA may not work. Routing to your existing endpoints, as well as existing health checks, traffic dials, and endpoint weight configurations used to route or shift traffic to other endpoints and endpoint groups, will continue to work.

 What this means is that when you are planning for dependencies on AGA, you should not rely on the AGA control plane in your recovery path. For example, a statically-stable design would be to use the status of the configured health checks to fail away from unhealthy endpoints. Refer to [Deploying multi-region applications in AWS using AWS Global Accelerator](https://aws.amazon.com/blogs/networking-and-content-delivery/deploying-multi-region-applications-in-aws-using-aws-global-accelerator/) for examples of this configuration. A non-statically-stable design would be to modify the AGA traffic dial percentages, edit endpoint groups, or remove an endpoint from an endpoint group during an impairment. These approaches would depend on the AGA control plane.

## Amazon Shield Advanced
<a name="amazon-shield-advanced"></a>

 The Amazon Shield Advanced control plane consists of all public Shield Advanced APIs, and is hosted in us-east-1. This includes functionality like `CreateProtection`, `CreateProtectionGroup`, `AssociateHealthCheck`, `DesribeDRTAccess`, and `ListProtections`. The data plane is the DDoS protection provided by Shield Advanced as well as the creation of Shield Advanced metrics. Shield Advanced also utilizes Route 53 health checks (which are part of the Route 53 data plane), if you have configured them. During a control plane impairment, CRUDL-type operations for Shield Advanced may not work, but the DDoS protection configured for your resources, as well as responses to changes in health checks, will continue to function.

 What this means is that you should not rely on the Shield Advanced control plane in your recovery path. Although the Shield Advanced control plane doesn’t provide direct functionality that you would typically use in a recovery situation, there may be times when you would. For example, a statically-stable design would be to have your DR resources already configured to be part of a protection group and have health checks associated with them as opposed to configuring that protection after the failure occurs. This prevents depending on the Shield Advanced control plane for recovery.
