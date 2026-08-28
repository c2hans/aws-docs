---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEksClusterResourcesVpcConfigDetails.html
---

# AwsEksClusterResourcesVpcConfigDetails
<a name="API_AwsEksClusterResourcesVpcConfigDetails"></a>

Information about the VPC configuration used by the cluster control plane.

## Contents
<a name="API_AwsEksClusterResourcesVpcConfigDetails_Contents"></a>

 ** EndpointPublicAccess **   <a name="securityhub-Type-AwsEksClusterResourcesVpcConfigDetails-EndpointPublicAccess"></a>
 Indicates whether the Amazon EKS public API server endpoint is turned on. If the Amazon EKS public API server endpoint is turned off, your cluster's Kubernetes API server can only receive requests that originate from within the cluster VPC.
Type: Boolean
Required: No

 ** SecurityGroupIds **   <a name="securityhub-Type-AwsEksClusterResourcesVpcConfigDetails-SecurityGroupIds"></a>
The security groups that are associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Amazon EKS control plane.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SubnetIds **   <a name="securityhub-Type-AwsEksClusterResourcesVpcConfigDetails-SubnetIds"></a>
The subnets that are associated with the cluster.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEksClusterResourcesVpcConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEksClusterResourcesVpcConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEksClusterResourcesVpcConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEksClusterResourcesVpcConfigDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
