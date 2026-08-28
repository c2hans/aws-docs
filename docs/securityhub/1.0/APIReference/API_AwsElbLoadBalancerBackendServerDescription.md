---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLoadBalancerBackendServerDescription.html
---

# AwsElbLoadBalancerBackendServerDescription
<a name="API_AwsElbLoadBalancerBackendServerDescription"></a>

Provides information about the configuration of an EC2 instance for the load balancer.

## Contents
<a name="API_AwsElbLoadBalancerBackendServerDescription_Contents"></a>

 ** InstancePort **   <a name="securityhub-Type-AwsElbLoadBalancerBackendServerDescription-InstancePort"></a>
The port on which the EC2 instance is listening.
Type: Integer
Required: No

 ** PolicyNames **   <a name="securityhub-Type-AwsElbLoadBalancerBackendServerDescription-PolicyNames"></a>
The names of the policies that are enabled for the EC2 instance.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElbLoadBalancerBackendServerDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLoadBalancerBackendServerDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLoadBalancerBackendServerDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLoadBalancerBackendServerDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
