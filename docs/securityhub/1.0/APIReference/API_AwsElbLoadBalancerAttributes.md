---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLoadBalancerAttributes.html
---

# AwsElbLoadBalancerAttributes
<a name="API_AwsElbLoadBalancerAttributes"></a>

Contains attributes for the load balancer.

## Contents
<a name="API_AwsElbLoadBalancerAttributes_Contents"></a>

 ** AccessLog **   <a name="securityhub-Type-AwsElbLoadBalancerAttributes-AccessLog"></a>
Information about the access log configuration for the load balancer.
If the access log is enabled, the load balancer captures detailed information about all requests. It delivers the information to a specified S3 bucket.
Type: [AwsElbLoadBalancerAccessLog](API_AwsElbLoadBalancerAccessLog.md) object
Required: No

 ** AdditionalAttributes **   <a name="securityhub-Type-AwsElbLoadBalancerAttributes-AdditionalAttributes"></a>
Any additional attributes for a load balancer.
Type: Array of [AwsElbLoadBalancerAdditionalAttribute](API_AwsElbLoadBalancerAdditionalAttribute.md) objects
Required: No

 ** ConnectionDraining **   <a name="securityhub-Type-AwsElbLoadBalancerAttributes-ConnectionDraining"></a>
Information about the connection draining configuration for the load balancer.
If connection draining is enabled, the load balancer allows existing requests to complete before it shifts traffic away from a deregistered or unhealthy instance.
Type: [AwsElbLoadBalancerConnectionDraining](API_AwsElbLoadBalancerConnectionDraining.md) object
Required: No

 ** ConnectionSettings **   <a name="securityhub-Type-AwsElbLoadBalancerAttributes-ConnectionSettings"></a>
Connection settings for the load balancer.
If an idle timeout is configured, the load balancer allows connections to remain idle for the specified duration. When a connection is idle, no data is sent over the connection.
Type: [AwsElbLoadBalancerConnectionSettings](API_AwsElbLoadBalancerConnectionSettings.md) object
Required: No

 ** CrossZoneLoadBalancing **   <a name="securityhub-Type-AwsElbLoadBalancerAttributes-CrossZoneLoadBalancing"></a>
Cross-zone load balancing settings for the load balancer.
If cross-zone load balancing is enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
Type: [AwsElbLoadBalancerCrossZoneLoadBalancing](API_AwsElbLoadBalancerCrossZoneLoadBalancing.md) object
Required: No

## See Also
<a name="API_AwsElbLoadBalancerAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLoadBalancerAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLoadBalancerAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLoadBalancerAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
