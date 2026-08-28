---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EksClusterDetails.html
---

# EksClusterDetails
<a name="API_EksClusterDetails"></a>

Details about the EKS cluster involved in a Kubernetes finding.

## Contents
<a name="API_EksClusterDetails_Contents"></a>

 ** arn **   <a name="guardduty-Type-EksClusterDetails-arn"></a>
EKS cluster ARN.
Type: String
Required: No

 ** createdAt **   <a name="guardduty-Type-EksClusterDetails-createdAt"></a>
The timestamp when the EKS cluster was created.
Type: Timestamp
Required: No

 ** name **   <a name="guardduty-Type-EksClusterDetails-name"></a>
EKS cluster name.
Type: String
Required: No

 ** status **   <a name="guardduty-Type-EksClusterDetails-status"></a>
The EKS cluster status.
Type: String
Required: No

 ** tags **   <a name="guardduty-Type-EksClusterDetails-tags"></a>
The EKS cluster tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **   <a name="guardduty-Type-EksClusterDetails-vpcId"></a>
The VPC ID to which the EKS cluster is attached.
Type: String
Required: No

## See Also
<a name="API_EksClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EksClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EksClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EksClusterDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
