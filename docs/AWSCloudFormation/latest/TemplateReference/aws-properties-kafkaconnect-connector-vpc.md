---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-vpc.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector Vpc
<a name="aws-properties-kafkaconnect-connector-vpc"></a>

Information about the VPC in which the connector resides.

## Syntax
<a name="aws-properties-kafkaconnect-connector-vpc-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-vpc-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-kafkaconnect-connector-vpc-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-kafkaconnect-connector-vpc-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-vpc-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-kafkaconnect-connector-vpc-securitygroups): {{
    - String}}
  [Subnets](#cfn-kafkaconnect-connector-vpc-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-vpc-properties"></a>

`SecurityGroups`  <a name="cfn-kafkaconnect-connector-vpc-securitygroups"></a>
The security group IDs for the connector.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-kafkaconnect-connector-vpc-subnets"></a>
The subnets for the connector.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
