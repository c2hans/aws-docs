---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-enasrdudpspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance EnaSrdUdpSpecification
<a name="aws-properties-ec2-instance-enasrdudpspecification"></a>

ENA Express is compatible with both TCP and UDP transport protocols. When it's enabled, TCP traffic automatically uses it. However, some UDP-based applications are designed to handle network packets that are out of order, without a need for retransmission, such as live video broadcasting or other near-real-time applications. For UDP traffic, you can specify whether to use ENA Express, based on your application environment needs.

## Syntax
<a name="aws-properties-ec2-instance-enasrdudpspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-enasrdudpspecification-syntax.json"></a>

```
{
  "[EnaSrdUdpEnabled](#cfn-ec2-instance-enasrdudpspecification-enasrdudpenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-instance-enasrdudpspecification-syntax.yaml"></a>

```
  [EnaSrdUdpEnabled](#cfn-ec2-instance-enasrdudpspecification-enasrdudpenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-instance-enasrdudpspecification-properties"></a>

`EnaSrdUdpEnabled`  <a name="cfn-ec2-instance-enasrdudpspecification-enasrdudpenabled"></a>
Indicates whether UDP traffic to and from the instance uses ENA Express. To specify this setting, you must first enable ENA Express.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
