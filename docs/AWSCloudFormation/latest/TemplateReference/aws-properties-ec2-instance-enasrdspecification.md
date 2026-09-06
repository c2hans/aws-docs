---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-enasrdspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance EnaSrdSpecification
<a name="aws-properties-ec2-instance-enasrdspecification"></a>

ENA Express uses AWS Scalable Reliable Datagram (SRD) technology to increase the maximum bandwidth used per stream and minimize tail latency of network traffic between EC2 instances. With ENA Express, you can communicate between two EC2 instances in the same subnet within the same account, or in different accounts. Both sending and receiving instances must have ENA Express enabled.

To improve the reliability of network packet delivery, ENA Express reorders network packets on the receiving end by default. However, some UDP-based applications are designed to handle network packets that are out of order to reduce the overhead for packet delivery at the network layer. When ENA Express is enabled, you can specify whether UDP network traffic uses it.

## Syntax
<a name="aws-properties-ec2-instance-enasrdspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-enasrdspecification-syntax.json"></a>

```
{
  "[EnaSrdEnabled](#cfn-ec2-instance-enasrdspecification-enasrdenabled)" : {{Boolean}},
  "[EnaSrdUdpSpecification](#cfn-ec2-instance-enasrdspecification-enasrdudpspecification)" : {{EnaSrdUdpSpecification}}
}
```

### YAML
<a name="aws-properties-ec2-instance-enasrdspecification-syntax.yaml"></a>

```
  [EnaSrdEnabled](#cfn-ec2-instance-enasrdspecification-enasrdenabled): {{Boolean}}
  [EnaSrdUdpSpecification](#cfn-ec2-instance-enasrdspecification-enasrdudpspecification): {{
    EnaSrdUdpSpecification}}
```

## Properties
<a name="aws-properties-ec2-instance-enasrdspecification-properties"></a>

`EnaSrdEnabled`  <a name="cfn-ec2-instance-enasrdspecification-enasrdenabled"></a>
Indicates whether ENA Express is enabled for the network interface.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnaSrdUdpSpecification`  <a name="cfn-ec2-instance-enasrdspecification-enasrdudpspecification"></a>
Configures ENA Express for UDP network traffic.
*Required*: No
*Type*: [EnaSrdUdpSpecification](aws-properties-ec2-instance-enasrdudpspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
