---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_IpAddressMember.html
---

# IpAddressMember
<a name="API_IpAddressMember"></a>

Provides information of the IP address.

## Contents
<a name="API_IpAddressMember_Contents"></a>

 ** AllocationType **   <a name="ssmsap-Type-IpAddressMember-AllocationType"></a>
The type of allocation for the IP address.
Type: String
Valid Values: `VPC_SUBNET | ELASTIC_IP | OVERLAY | UNKNOWN`
Required: No

 ** IpAddress **   <a name="ssmsap-Type-IpAddressMember-IpAddress"></a>
The IP address.
Type: String
Required: No

 ** Primary **   <a name="ssmsap-Type-IpAddressMember-Primary"></a>
The primary IP address.
Type: Boolean
Required: No

## See Also
<a name="API_IpAddressMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/IpAddressMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/IpAddressMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/IpAddressMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
