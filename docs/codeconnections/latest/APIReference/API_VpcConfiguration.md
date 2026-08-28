---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_VpcConfiguration.html
---

# VpcConfiguration
<a name="API_VpcConfiguration"></a>

The VPC configuration provisioned for the host.

## Contents
<a name="API_VpcConfiguration_Contents"></a>

 ** SecurityGroupIds **   <a name="codeconnections-Type-VpcConfiguration-SecurityGroupIds"></a>
The ID of the security group or security groups associated with the Amazon VPC connected to the infrastructure where your provider type is installed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `sg-\w{8}(\w{9})?`
Required: Yes

 ** SubnetIds **   <a name="codeconnections-Type-VpcConfiguration-SubnetIds"></a>
The ID of the subnet or subnets associated with the Amazon VPC connected to the infrastructure where your provider type is installed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-\w{8}(\w{9})?`
Required: Yes

 ** VpcId **   <a name="codeconnections-Type-VpcConfiguration-VpcId"></a>
The ID of the Amazon VPC connected to the infrastructure where your provider type is installed.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-\w{8}(\w{9})?`
Required: Yes

 ** TlsCertificate **   <a name="codeconnections-Type-VpcConfiguration-TlsCertificate"></a>
The value of the Transport Layer Security (TLS) certificate associated with the infrastructure where your provider type is installed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/VpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/VpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/VpcConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
