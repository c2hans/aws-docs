---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AwsEc2NetworkInterfaceViolation.html
---

# AwsEc2NetworkInterfaceViolation
<a name="API_AwsEc2NetworkInterfaceViolation"></a>

Violation detail for network interfaces associated with an EC2 instance.

## Contents
<a name="API_AwsEc2NetworkInterfaceViolation_Contents"></a>

 ** ViolatingSecurityGroups **   <a name="fms-Type-AwsEc2NetworkInterfaceViolation-ViolatingSecurityGroups"></a>
List of security groups that violate the rules specified in the primary security group of the AWS Firewall Manager policy.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolationTarget **   <a name="fms-Type-AwsEc2NetworkInterfaceViolation-ViolationTarget"></a>
The resource ID of the network interface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_AwsEc2NetworkInterfaceViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AwsEc2NetworkInterfaceViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AwsEc2NetworkInterfaceViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AwsEc2NetworkInterfaceViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
