---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLoadBalancerListenerDescription.html
---

# AwsElbLoadBalancerListenerDescription
<a name="API_AwsElbLoadBalancerListenerDescription"></a>

Lists the policies that are enabled for a load balancer listener.

## Contents
<a name="API_AwsElbLoadBalancerListenerDescription_Contents"></a>

 ** Listener **   <a name="securityhub-Type-AwsElbLoadBalancerListenerDescription-Listener"></a>
Information about the listener.
Type: [AwsElbLoadBalancerListener](API_AwsElbLoadBalancerListener.md) object
Required: No

 ** PolicyNames **   <a name="securityhub-Type-AwsElbLoadBalancerListenerDescription-PolicyNames"></a>
The policies enabled for the listener.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElbLoadBalancerListenerDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLoadBalancerListenerDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLoadBalancerListenerDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLoadBalancerListenerDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
