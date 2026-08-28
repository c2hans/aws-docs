---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-kafkaclusterclientvpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator KafkaClusterClientVpcConfig
<a name="aws-properties-msk-replicator-kafkaclusterclientvpcconfig"></a>

Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

## Syntax
<a name="aws-properties-msk-replicator-kafkaclusterclientvpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-kafkaclusterclientvpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-msk-replicator-kafkaclusterclientvpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-msk-replicator-kafkaclusterclientvpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-msk-replicator-kafkaclusterclientvpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-msk-replicator-kafkaclusterclientvpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-msk-replicator-kafkaclusterclientvpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-msk-replicator-kafkaclusterclientvpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-msk-replicator-kafkaclusterclientvpcconfig-securitygroupids"></a>
The security groups to attach to the ENIs for the broker nodes.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-msk-replicator-kafkaclusterclientvpcconfig-subnetids"></a>
The list of subnets in the client VPC to connect to.
*Required*: Yes
*Type*: Array of String
*Minimum*: `2`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
