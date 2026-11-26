---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/security-cloudtrail.html
---

# Logging ELB for Envoy API calls using AWS CloudTrail

ELB for Envoy is integrated with AWS CloudTrail (CloudTrail), a service that provides a record of actions taken by a user, role, or an AWS service in ELB for Envoy. CloudTrail captures API calls for ELB for Envoy as events, including calls from the ELB for Envoy console and code calls to the ELB for Envoy API operations.

The CloudTrail event source for ELB for Envoy is `elb-proxy.amazonaws.com`. CloudTrail records the ELB for Envoy API operations, for example:
+ `CreateProxy`
+ `GetProxy`
+ `ListProxies`
+ `DeleteProxy`
+ `UpdateProxyConfiguration`
+ `UpdateProxyNetworkConfiguration`
+ `UpdateProxyAttributes`
+ `AssociateCertificate`
+ `DisassociateCertificate`
+ `TagResource`

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for ELB for Envoy. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to ELB for Envoy, the IP address from which the request was made, who made the request, when it was made, and additional details.

All ELB for Envoy actions are logged by CloudTrail and are documented in the [Elastic Load Balancing for Envoy API Reference](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/).

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).
