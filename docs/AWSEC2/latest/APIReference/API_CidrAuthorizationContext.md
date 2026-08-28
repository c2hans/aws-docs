---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CidrAuthorizationContext.html
---

# CidrAuthorizationContext
<a name="API_CidrAuthorizationContext"></a>

Provides authorization for Amazon to bring a specific IP address range to a specific AWS account using bring your own IP addresses (BYOIP). For more information, see [Configuring your BYOIP address range](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#prepare-for-byoip) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_CidrAuthorizationContext_Contents"></a>

 ** Message **
The plain-text authorization message for the prefix and account.
Type: String
Required: Yes

 ** Signature **
The signed authorization message for the prefix and account.
Type: String
Required: Yes

## See Also
<a name="API_CidrAuthorizationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CidrAuthorizationContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CidrAuthorizationContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CidrAuthorizationContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
