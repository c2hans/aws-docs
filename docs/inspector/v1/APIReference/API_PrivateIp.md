---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_PrivateIp.html
---

# PrivateIp
<a name="API_PrivateIp"></a>

Contains information about a private IP address associated with a network interface. This data type is used as a response element in the [DescribeFindings](API_DescribeFindings.md) action.

## Contents
<a name="API_PrivateIp_Contents"></a>

 ** privateDnsName **   <a name="Inspector-Type-PrivateIp-privateDnsName"></a>
The DNS name of the private IP address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

 ** privateIpAddress **   <a name="Inspector-Type-PrivateIp-privateIpAddress"></a>
The full IP address of the network inteface.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

## See Also
<a name="API_PrivateIp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/PrivateIp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/PrivateIp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/PrivateIp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
