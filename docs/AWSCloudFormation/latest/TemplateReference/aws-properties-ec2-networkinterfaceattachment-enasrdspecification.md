---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinterfaceattachment-enasrdspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInterfaceAttachment EnaSrdSpecification
<a name="aws-properties-ec2-networkinterfaceattachment-enasrdspecification"></a>

ENA Express uses AWS Scalable Reliable Datagram (SRD) technology to increase the maximum bandwidth used per stream and minimize tail latency of network traffic between EC2 instances. With ENA Express, you can communicate between two EC2 instances in the same subnet within the same account, or in different accounts. Both sending and receiving instances must have ENA Express enabled.

To improve the reliability of network packet delivery, ENA Express reorders network packets on the receiving end by default. However, some UDP-based applications are designed to handle network packets that are out of order to reduce the overhead for packet delivery at the network layer. When ENA Express is enabled, you can specify whether UDP network traffic uses it.

## Syntax
<a name="aws-properties-ec2-networkinterfaceattachment-enasrdspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinterfaceattachment-enasrdspecification-syntax.json"></a>

```
{
  "[EnaSrdEnabled](#cfn-ec2-networkinterfaceattachment-enasrdspecification-enasrdenabled)" : {{Boolean}},
  "[EnaSrdUdpSpecification](#cfn-ec2-networkinterfaceattachment-enasrdspecification-enasrdudpspecification)" : {{EnaSrdUdpSpecification}}
}
```

### YAML
<a name="aws-properties-ec2-networkinterfaceattachment-enasrdspecification-syntax.yaml"></a>

```
  [EnaSrdEnabled](#cfn-ec2-networkinterfaceattachment-enasrdspecification-enasrdenabled): {{Boolean}}
  [EnaSrdUdpSpecification](#cfn-ec2-networkinterfaceattachment-enasrdspecification-enasrdudpspecification): {{
    EnaSrdUdpSpecification}}
```

## Properties
<a name="aws-properties-ec2-networkinterfaceattachment-enasrdspecification-properties"></a>

`EnaSrdEnabled`  <a name="cfn-ec2-networkinterfaceattachment-enasrdspecification-enasrdenabled"></a>
Indicates whether ENA Express is enabled for the network interface.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnaSrdUdpSpecification`  <a name="cfn-ec2-networkinterfaceattachment-enasrdspecification-enasrdudpspecification"></a>
Configures ENA Express for UDP network traffic.
*Required*: No
*Type*: [EnaSrdUdpSpecification](aws-properties-ec2-networkinterfaceattachment-enasrdudpspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
