---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamDiscoveryFailureReason.html
---

# IpamDiscoveryFailureReason
<a name="API_IpamDiscoveryFailureReason"></a>

The discovery failure reason.

## Contents
<a name="API_IpamDiscoveryFailureReason_Contents"></a>

 ** code **
The discovery failure code.
+  `assume-role-failure` - IPAM could not assume the AWS IAM service-linked role. This could be because of any of the following:
  + SLR has not been created yet and IPAM is still creating it.
  + You have opted-out of the IPAM home Region.
  + Account you are using as your IPAM account has been suspended.
+  `throttling-failure` - IPAM account is already using the allotted transactions per second and IPAM is receiving a throttling error when assuming the AWS IAM SLR.
+  `unauthorized-failure` - AWS account making the request is not authorized. For more information, see [AuthFailure](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html) in the *Amazon Elastic Compute Cloud API Reference*.
Type: String
Valid Values: `assume-role-failure | throttling-failure | unauthorized-failure`
Required: No

 ** message **
The discovery failure message.
Type: String
Required: No

## See Also
<a name="API_IpamDiscoveryFailureReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamDiscoveryFailureReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamDiscoveryFailureReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamDiscoveryFailureReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
