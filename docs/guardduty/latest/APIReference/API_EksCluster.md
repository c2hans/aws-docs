---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EksCluster.html
---

# EksCluster
<a name="API_EksCluster"></a>

Contains information about the Amazon EKS cluster involved in a GuardDuty finding, including cluster identification, status, and network configuration.

## Contents
<a name="API_EksCluster_Contents"></a>

 ** arn **   <a name="guardduty-Type-EksCluster-arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the Amazon EKS cluster involved in the finding.
Type: String
Required: No

 ** createdAt **   <a name="guardduty-Type-EksCluster-createdAt"></a>
The timestamp indicating when the Amazon EKS cluster was created, in UTC format.
Type: Timestamp
Required: No

 ** ec2InstanceUids **   <a name="guardduty-Type-EksCluster-ec2InstanceUids"></a>
A list of unique identifiers for the Amazon EC2 instances that serve as worker nodes in the Amazon EKS cluster.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** status **   <a name="guardduty-Type-EksCluster-status"></a>
The current status of the Amazon EKS cluster.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING | PENDING`
Required: No

 ** vpcId **   <a name="guardduty-Type-EksCluster-vpcId"></a>
The ID of the Amazon Virtual Private Cloud (Amazon VPC) associated with the Amazon EKS cluster.
Type: String
Required: No

## See Also
<a name="API_EksCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EksCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EksCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EksCluster)
