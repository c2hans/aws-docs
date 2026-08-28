---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PrivateIpAddressSpecification.html
---

# PrivateIpAddressSpecification
<a name="API_PrivateIpAddressSpecification"></a>

Describes a secondary private IPv4 address for a network interface.

## Contents
<a name="API_PrivateIpAddressSpecification_Contents"></a>

 ** Primary ** (request), ** primary ** (response)
Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.
Type: Boolean
Required: No

 ** PrivateIpAddress ** (request), ** privateIpAddress ** (response)
The private IPv4 address.
Type: String
Required: No

## See Also
<a name="API_PrivateIpAddressSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PrivateIpAddressSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PrivateIpAddressSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PrivateIpAddressSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
