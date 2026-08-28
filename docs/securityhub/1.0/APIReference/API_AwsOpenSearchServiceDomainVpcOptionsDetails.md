---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsOpenSearchServiceDomainVpcOptionsDetails.html
---

# AwsOpenSearchServiceDomainVpcOptionsDetails
<a name="API_AwsOpenSearchServiceDomainVpcOptionsDetails"></a>

Contains information that OpenSearch Service derives based on the `VPCOptions` for the domain.

## Contents
<a name="API_AwsOpenSearchServiceDomainVpcOptionsDetails_Contents"></a>

 ** SecurityGroupIds **   <a name="securityhub-Type-AwsOpenSearchServiceDomainVpcOptionsDetails-SecurityGroupIds"></a>
The list of security group IDs that are associated with the VPC endpoints for the domain.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SubnetIds **   <a name="securityhub-Type-AwsOpenSearchServiceDomainVpcOptionsDetails-SubnetIds"></a>
A list of subnet IDs that are associated with the VPC endpoints for the domain.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsOpenSearchServiceDomainVpcOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsOpenSearchServiceDomainVpcOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsOpenSearchServiceDomainVpcOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsOpenSearchServiceDomainVpcOptionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
