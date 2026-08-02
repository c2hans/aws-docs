---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-brokernodegroupinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster BrokerNodeGroupInfo
<a name="aws-properties-msk-cluster-brokernodegroupinfo"></a>

Describes the setup to be used for the broker nodes in the cluster.

## Syntax
<a name="aws-properties-msk-cluster-brokernodegroupinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-brokernodegroupinfo-syntax.json"></a>

```
{
  "[BrokerAZDistribution](#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution)" : {{String}},
  "[ClientSubnets](#cfn-msk-cluster-brokernodegroupinfo-clientsubnets)" : {{[ String, ... ]}},
  "[ConnectivityInfo](#cfn-msk-cluster-brokernodegroupinfo-connectivityinfo)" : {{ConnectivityInfo}},
  "[InstanceType](#cfn-msk-cluster-brokernodegroupinfo-instancetype)" : {{String}},
  "[SecurityGroups](#cfn-msk-cluster-brokernodegroupinfo-securitygroups)" : {{[ String, ... ]}},
  "[StorageInfo](#cfn-msk-cluster-brokernodegroupinfo-storageinfo)" : {{StorageInfo}}
}
```

### YAML
<a name="aws-properties-msk-cluster-brokernodegroupinfo-syntax.yaml"></a>

```
  [BrokerAZDistribution](#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution): {{String}}
  [ClientSubnets](#cfn-msk-cluster-brokernodegroupinfo-clientsubnets): {{
    - String}}
  [ConnectivityInfo](#cfn-msk-cluster-brokernodegroupinfo-connectivityinfo): {{
    ConnectivityInfo}}
  [InstanceType](#cfn-msk-cluster-brokernodegroupinfo-instancetype): {{String}}
  [SecurityGroups](#cfn-msk-cluster-brokernodegroupinfo-securitygroups): {{
    - String}}
  [StorageInfo](#cfn-msk-cluster-brokernodegroupinfo-storageinfo): {{
    StorageInfo}}
```

## Properties
<a name="aws-properties-msk-cluster-brokernodegroupinfo-properties"></a>

`BrokerAZDistribution`  <a name="cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution"></a>
This parameter is currently not in use.
*Required*: No
*Type*: String
*Minimum*: `6`
*Maximum*: `9`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientSubnets`  <a name="cfn-msk-cluster-brokernodegroupinfo-clientsubnets"></a>
The list of subnets to connect to in the client virtual private cloud (VPC). Amazon creates elastic network interfaces (ENIs) inside these subnets. Client applications use ENIs to produce and consume data.
If you use the US West (N. California) Region, specify exactly two subnets. For other Regions where Amazon MSK is available, you can specify either two or three subnets. The subnets that you specify must be in distinct Availability Zones. When you create a cluster, Amazon MSK distributes the broker nodes evenly across the subnets that you specify.
Client subnets can't occupy the Availability Zone with ID `use1-az3`.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectivityInfo`  <a name="cfn-msk-cluster-brokernodegroupinfo-connectivityinfo"></a>
Information about the cluster's connectivity setting.
*Required*: No
*Type*: [ConnectivityInfo](aws-properties-msk-cluster-connectivityinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-msk-cluster-brokernodegroupinfo-instancetype"></a>
The type of Amazon EC2 instances to use for brokers. Depending on the [broker type](https://docs.aws.amazon.com/msk/latest/developerguide/broker-instance-types.html), Amazon MSK supports the following broker sizes:
 **Standard broker sizes**
+ kafka.t3.small
**Note**
You can't select the kafka.t3.small instance type when the metadata mode is KRaft.
+ kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.8xlarge, kafka.m5.12xlarge, kafka.m5.16xlarge, kafka.m5.24xlarge
+ kafka.m7g.large, kafka.m7g.xlarge, kafka.m7g.2xlarge, kafka.m7g.4xlarge, kafka.m7g.8xlarge, kafka.m7g.12xlarge, kafka.m7g.16xlarge
 **Express broker sizes**
+ express.m7g.large, express.m7g.xlarge, express.m7g.2xlarge, express.m7g.4xlarge, express.m7g.8xlarge, express.m7g.12xlarge, express.m7g.16xlarge
Some broker sizes might not be available in certian AWS Regions. See the updated [Pricing tools](https://aws.amazon.com/msk/pricing/) section on the Amazon MSK pricing page for the latest list of available instances by Region.
*Required*: Yes
*Type*: String
*Minimum*: `5`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroups`  <a name="cfn-msk-cluster-brokernodegroupinfo-securitygroups"></a>
The security groups to associate with the ENIs in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don't specify a security group, Amazon MSK uses the default security group associated with the VPC. If you specify security groups that were shared with you, you must ensure that you have permissions to them. Specifically, you need the `ec2:DescribeSecurityGroups` permission.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageInfo`  <a name="cfn-msk-cluster-brokernodegroupinfo-storageinfo"></a>
Contains information about storage volumes attached to Amazon MSK broker nodes.
*Required*: No
*Type*: [StorageInfo](aws-properties-msk-cluster-storageinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
