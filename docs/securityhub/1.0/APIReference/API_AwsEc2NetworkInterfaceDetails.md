---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2NetworkInterfaceDetails.html
---

# AwsEc2NetworkInterfaceDetails
<a name="API_AwsEc2NetworkInterfaceDetails"></a>

Details about the network interface

## Contents
<a name="API_AwsEc2NetworkInterfaceDetails_Contents"></a>

 ** Attachment **   <a name="securityhub-Type-AwsEc2NetworkInterfaceDetails-Attachment"></a>
The network interface attachment.
Type: [AwsEc2NetworkInterfaceAttachment](API_AwsEc2NetworkInterfaceAttachment.md) object
Required: No

 ** IpV6Addresses **   <a name="securityhub-Type-AwsEc2NetworkInterfaceDetails-IpV6Addresses"></a>
The IPv6 addresses associated with the network interface.
Type: Array of [AwsEc2NetworkInterfaceIpV6AddressDetail](API_AwsEc2NetworkInterfaceIpV6AddressDetail.md) objects
Required: No

 ** NetworkInterfaceId **   <a name="securityhub-Type-AwsEc2NetworkInterfaceDetails-NetworkInterfaceId"></a>
The ID of the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrivateIpAddresses **   <a name="securityhub-Type-AwsEc2NetworkInterfaceDetails-PrivateIpAddresses"></a>
The private IPv4 addresses associated with the network interface.
Type: Array of [AwsEc2NetworkInterfacePrivateIpAddressDetail](API_AwsEc2NetworkInterfacePrivateIpAddressDetail.md) objects
Required: No

 ** PublicDnsName **   <a name="securityhub-Type-AwsEc2NetworkInterfaceDetails-PublicDnsName"></a>
The public DNS name of the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PublicIp **   <a name="securityhub-Type-AwsEc2NetworkInterfaceDetails-PublicIp"></a>
The address of the Elastic IP address bound to the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecurityGroups **   <a name="securityhub-Type-AwsEc2NetworkInterfaceDetails-SecurityGroups"></a>
Security groups for the network interface.
Type: Array of [AwsEc2NetworkInterfaceSecurityGroup](API_AwsEc2NetworkInterfaceSecurityGroup.md) objects
Required: No

 ** SourceDestCheck **   <a name="securityhub-Type-AwsEc2NetworkInterfaceDetails-SourceDestCheck"></a>
Indicates whether traffic to or from the instance is validated.
Type: Boolean
Required: No

## See Also
<a name="API_AwsEc2NetworkInterfaceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2NetworkInterfaceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2NetworkInterfaceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2NetworkInterfaceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
