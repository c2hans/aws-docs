---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroup SecurityDetails
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails"></a>

 Information about IAM roles, subnets, and security groups needed for this DataflowEndpointGroup.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails-syntax.json"></a>

```
{
  "[RoleArn](#cfn-groundstation-dataflowendpointgroup-securitydetails-rolearn)" : {{String}},
  "[SecurityGroupIds](#cfn-groundstation-dataflowendpointgroup-securitydetails-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-groundstation-dataflowendpointgroup-securitydetails-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails-syntax.yaml"></a>

```
  [RoleArn](#cfn-groundstation-dataflowendpointgroup-securitydetails-rolearn): {{String}}
  [SecurityGroupIds](#cfn-groundstation-dataflowendpointgroup-securitydetails-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-groundstation-dataflowendpointgroup-securitydetails-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails-properties"></a>

`RoleArn`  <a name="cfn-groundstation-dataflowendpointgroup-securitydetails-rolearn"></a>
The ARN of a role which Ground Station has permission to assume, such as `arn:aws:iam::012345678910:role/DataDeliveryServiceRole`.
 Ground Station will assume this role and create an ENI in your VPC on the specified subnet upon creation of a dataflow endpoint group. This ENI is used as the ingress/egress point for data streamed during a satellite contact.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-groundstation-dataflowendpointgroup-securitydetails-securitygroupids"></a>
The security group Ids of the security role, such as `sg-1234567890abcdef0`.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-groundstation-dataflowendpointgroup-securitydetails-subnetids"></a>
The subnet Ids of the security details, such as `subnet-12345678`.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails--examples"></a>

### Create SecurityDetails
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails--examples--Create_SecurityDetails"></a>

The following example creates Ground Station `SecurityDetails`

#### JSON
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails--examples--Create_SecurityDetails--json"></a>

```
{
  "SecurityDetails": {
    "SubnetIds": [
      "subnet-6782e71e"
    ],
    "SecurityGroupIds": [
      "sg-6979fe18"
    ],
    "RoleArn": "arn:aws:iam::012345678910:role/groundstation-service-role-AWSServiceRoleForAmazonGroundStation-EXAMPLEBQ4PI"
  }
}
```

#### YAML
<a name="aws-properties-groundstation-dataflowendpointgroup-securitydetails--examples--Create_SecurityDetails--yaml"></a>

```
SecurityDetails:
  SubnetIds:
    - subnet-12345678
  SecurityGroupIds:
    - sg-87654321
  RoleArn: arn:aws:iam::012345678910:role/groundstation-service-role-AWSServiceRoleForAmazonGroundStation-EXAMPLEABCDE
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
