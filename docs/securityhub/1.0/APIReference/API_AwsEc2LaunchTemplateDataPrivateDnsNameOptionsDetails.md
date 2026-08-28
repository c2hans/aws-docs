---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails.html
---

# AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails
<a name="API_AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails"></a>

 Describes the options for Amazon EC2 instance hostnames.

## Contents
<a name="API_AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails_Contents"></a>

 ** EnableResourceNameDnsAAAARecord **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails-EnableResourceNameDnsAAAARecord"></a>
 Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
Type: Boolean
Required: No

 ** EnableResourceNameDnsARecord **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails-EnableResourceNameDnsARecord"></a>
 Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
Type: Boolean
Required: No

 ** HostnameType **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails-HostnameType"></a>
 The type of hostname for EC2 instances.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
