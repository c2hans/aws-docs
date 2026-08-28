---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_InstanceState.html
---

# InstanceState
<a name="API_InstanceState"></a>

Information about the state of an EC2 instance.

## Contents
<a name="API_InstanceState_Contents"></a>

 ** Description **
A description of the instance state. This string can contain one or more of the following messages.
+  `N/A`
+  `A transient error occurred. Please try again later.`
+  `Instance has failed at least the UnhealthyThreshold number of health checks consecutively.`
+  `Instance has not passed the configured HealthyThreshold number of health checks consecutively.`
+  `Instance registration is still in progress.`
+  `Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to.`
+  `Instance is not currently registered with the LoadBalancer.`
+  `Instance deregistration currently in progress.`
+  `Disable Availability Zone is currently in progress.`
+  `Instance is in pending state.`
+  `Instance is in stopped state.`
+  `Instance is in terminated state.`
Type: String
Required: No

 ** InstanceId **
The ID of the instance.
Type: String
Required: No

 ** ReasonCode **
Information about the cause of `OutOfService` instances. Specifically, whether the cause is Elastic Load Balancing or the instance.
Valid values: `ELB` \| `Instance` \| `N/A`
Type: String
Required: No

 ** State **
The current state of the instance.
Valid values: `InService` \| `OutOfService` \| `Unknown`
Type: String
Required: No

## See Also
<a name="API_InstanceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/InstanceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/InstanceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/InstanceState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
