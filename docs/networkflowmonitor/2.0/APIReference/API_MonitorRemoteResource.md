---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_MonitorRemoteResource.html
---

# MonitorRemoteResource
<a name="API_MonitorRemoteResource"></a>

A remote resource is the other endpoint in a network flow. That is, one endpoint is the local resource and the other is the remote resource. The values you can specify are the following:
+ For a VPC or subnet, this identifier is the VPC Amazon Resource Name (ARN) or subnet ARN.
+ For a service, this identifier is one of the following strings: `S3` or `DynamoDB`.
+ For an Availability Zone, this identifier is the AZ name, for example, us-west-2b.
+ For a Region, this identifier is the Region name, for example, us-west-2.

When a remote resource is an AWS Region, Network Flow Monitor provides network performance measurements up to the edge of the Region that you specify.

## Contents
<a name="API_MonitorRemoteResource_Contents"></a>

 ** identifier **   <a name="networkflowmonitor-Type-MonitorRemoteResource-identifier"></a>
The identifier of the remote resource. For a VPC or subnet, this identifier is the VPC Amazon Resource Name (ARN) or subnet ARN. For an Availability Zone, this identifier is the AZ name, for example, us-west-2b. For an AWS Region , this identifier is the Region name, for example, us-west-2.
Type: String
Required: Yes

 ** type **   <a name="networkflowmonitor-Type-MonitorRemoteResource-type"></a>
The type of the remote resource. Valid values are `AWS::EC2::VPC` `AWS::AvailabilityZone`, `AWS::EC2::Subnet`, `AWS::AWSService`, or `AWS::Region`.
Type: String
Valid Values: `AWS::EC2::VPC | AWS::AvailabilityZone | AWS::EC2::Subnet | AWS::AWSService | AWS::Region`
Required: Yes

## See Also
<a name="API_MonitorRemoteResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/MonitorRemoteResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/MonitorRemoteResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/MonitorRemoteResource)
