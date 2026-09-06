---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_MonitorLocalResource.html
---

# MonitorLocalResource
<a name="API_MonitorLocalResource"></a>

A local resource is the host where the agent is installed. Local resources can be a a subnet, a VPC, an Availability Zone, an EKS cluster or an AWS Region.

## Contents
<a name="API_MonitorLocalResource_Contents"></a>

 ** identifier **   <a name="networkflowmonitor-Type-MonitorLocalResource-identifier"></a>
The identifier of the local resource. The values you can specify are the following:
+ For a VPC, subnet or EKS cluster, this identifier is the VPC Amazon Resource Name (ARN), subnet ARN or cluster ARN.
+ For an Availability Zone, this identifier is the AZ name, for example, us-west-2b.
+ For a Region, this identifier is the Region name, for example, us-west-2.
Type: String
Required: Yes

 ** type **   <a name="networkflowmonitor-Type-MonitorLocalResource-type"></a>
The type of the local resource. Valid values are `AWS::EC2::VPC` `AWS::AvailabilityZone`, `AWS::EC2::Subnet`, `AWS::EKS::Cluster`, or `AWS::Region`.
Type: String
Valid Values: `AWS::EC2::VPC | AWS::AvailabilityZone | AWS::EC2::Subnet | AWS::Region`
Required: Yes

## See Also
<a name="API_MonitorLocalResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/MonitorLocalResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/MonitorLocalResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/MonitorLocalResource)
