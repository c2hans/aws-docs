---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_VpcInformation.html
---

# VpcInformation
<a name="API_VpcInformation"></a>

Information about your VPC and security groups used with the connector.

## Contents
<a name="API_VpcInformation_Contents"></a>

 ** SecurityGroupIds **   <a name="PcaConnectorAd-Type-VpcInformation-SecurityGroupIds"></a>
The security groups used with the connector. You can use a maximum of 4 security groups with a connector.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `(?:sg-[0-9a-f]{8}|sg-[0-9a-f]{17})`
Required: Yes

 ** IpAddressType **   <a name="PcaConnectorAd-Type-VpcInformation-IpAddressType"></a>
The VPC IP address type.
Type: String
Valid Values: `IPV4 | DUALSTACK`
Required: No

## See Also
<a name="API_VpcInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/VpcInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/VpcInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/VpcInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
